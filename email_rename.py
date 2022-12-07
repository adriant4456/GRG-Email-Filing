import win32com.client as win32
import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter import messagebox
from pathlib import PureWindowsPath
import extract_msg
from datetime import datetime
from PIL import ImageTk, Image
import sys
from tkinterdnd2 import DND_FILES, TkinterDnD
import re
import pathlib
import win32api


def get_emails(emails, sender, window, option_selected, filter_prog):
    """Takes list of emails as file paths and returns list of formatted file names"""
    #progress bar increment
    if filter_prog:
        increment = 45/len(emails)
    else:
        increment = 90/len(emails)
    email_list = {}
    #Loop through specified emails rename according to sender and date
    for i in emails:
        try:
            #extract email details
            with extract_msg.Message(i) as msg:
                msg_sender = msg.sender
                msg_recip = msg.recipients[0].name
                msg_date = msg.date
        except NotImplementedError or TypeError:
            window.updateprogress(increment,\
                                "Getting email senders/receivers...")
            continue
        except IndexError:
            window.updateprogress(increment,\
                                "Getting email senders/receivers...")
            continue
        #check if emails to be formatted to sender
        if sender:
            name = strip_name(msg_sender)
        else:
            name = strip_name(msg_recip)
        if not name:
            window.updateprogress(increment,\
                            "Getting email senders/receivers...")
            continue
        time_received = datetime.strptime(msg_date, '%a, %d %b %Y %H:%M:%S %z')
        date = time_received.strftime('%y%m%d')
        #check if email is already formatted
        base_name = os.path.basename(i)
        if name in i.name:
            window.updateprogress(increment,\
                                "Getting email senders/receivers...")
            base_name = base_name.replace(F"{name} ", "")
            base_name = base_name.replace(F"{date} ", "")
        if option_selected == "Name":
            email_list[i] = f"{name} {date} {base_name}"
        elif option_selected == "Date":
            email_list[i] = f"{date} {name} {base_name}"
        #print(f"old name is {i}")
        #print(f"new name is {os.path.dirname(i)}/{name} {date} {os.path.basename(i)}")
        window.updateprogress(increment,\
                                "Getting email senders/receivers...")   
    return email_list

def strip_name(name):
    """Takes name from extract_msg object as string and returns formatted name or False if failed"""
    name_list = []
    delimiters = [' ',',', '.']
    #check if extracted name is an email address
    if name.count('@') == 1 and len(name.split()) == 1:
        name = name.split('@')[0]
    elif len(name.split()) > 1 and '@' in name:
        name = ' '.join(e for e in name.split() if '@' not in e)
    #remove weird characters and spaces
    name = ''.join(e for e in name if e.isalnum() or e in delimiters).strip()
    #check for delimiter characters
    if ',' in name:
        name =  name.split(',')
        name_list.append(name[1].strip().title())
        name_list.append(name[0].strip().title())
    elif '.' in name:
        name =  name.split('.')
        name_list.append(name[0].title())
        name_list.append(name[1].title())
    elif ' ' in name:
        name =  name.split(' ')
        name_list.append(name[0].title())
        name_list.append(name[-1].title())
    else:
        name_list.append(name.title())
    if name_list[0]:
        if len(name_list) == 2:
            formatted_name = name_list[1] + name_list[0][0]
        else:
            formatted_name = name_list[0]
        return formatted_name
    else:
        return False
        

#filters out emails with redundant content
def filter_email_list(filenames, window):
    body_list = []
    filtered_list = []
    delete_list = []
    duplicate_list = []
    increment = 45/2/len(filenames)
    for email in filenames:
        try:
            with extract_msg.Message(email) as msg:
                attachment_list = extract_attachments(msg)
                body = extract_body(msg)
                body_list.append((email, (body, attachment_list)))
                window.updateprogress(increment,
                                        "Extracting email contents...")
        except NotImplementedError:
            window.updateprogress(increment,
                                "Extracting email contents...")
            continue
    increment = 45/2/len(body_list)
    for count1, item1 in enumerate(body_list):
        delete_condition = False
        for count2, item2 in enumerate(body_list):
            #skip if comparing the same email in the list
            if count1 == count2:
                continue
            result = compare_email(item1[1], item2[1])
            if result == True:
                print(F"Found {convert_path(item1[0]).name} in"
                      F" {convert_path(item2[0]).name}")
                print(F"Deleted {convert_path(item1[0]).name}")
                delete_list.append(item1[0])
                delete_condition = True
                window.updateprogress(increment,
                                      "Checking for non-unique emails...")
                break
            elif result == "duplicate":
                if item1[0] not in duplicate_list and\
                   item2[0] not in duplicate_list:
                    duplicate_list.append(item1[0])
                    delete_condition = True
                    window.updateprogress(increment,
                                      "Checking for non-unique emails...")
                    print(F"Found duplicate {convert_path(item1[0]).name} in"
                          F" {convert_path(item2[0]).name}")
                    print(F"Deleted {convert_path(item1[0]).name}")
                    break
        if not delete_condition:
            window.updateprogress(increment,
                                  "Checking for non-unique emails...")
            filtered_list.append(item1[0])
    #add items from duplicate list to delete list
    delete_list += duplicate_list 
    return filtered_list, delete_list

def extract_attachments(msg):
    '''Takes extract_msg message, returns list of attachment names'''
    attachment_list = []
    #ignore image attachments (signatures, pasted images)
    ignore_list = []
    for a in msg.attachments:
        #catch .msg file attachments which have no long filenames (??)
        if a.type == 'msg':
            attachment_list.append(F"{a.shortFilename}.msg")
            continue
        if not any(i in a.longFilename for i in ignore_list):
            attachment_list.append(a.longFilename)
    return attachment_list


def extract_body(msg):
    '''Takes extract_msg message, returns formatted email body'''
    raw_body = msg.body.split('\r\n')
    processed_body = []
    remove = ['\t','<','>']
    for i in raw_body:
        if not any(j in i.strip() for j in remove) and i.strip() != '':
            processed_body.append(i)
    return processed_body

#returns True if msg 1 in msg 2
def compare_email(msg1, msg2):
    tolerance = 0.999
    #if message 1 is longer email -  exit
    if len(msg1[0]) > len(msg2[0]):
        return False
    #check for duplicate emails
    elif msg1[0] == msg2[0] and msg1[1] == msg2[1]:
        return "duplicate"
    long_email = msg2[0]
    short_email = msg1[0]
    match_count = 0
    #iterate through email contents
    for line in short_email:
        if line in long_email:
            match_count += 1
    #check for unique attachments - if found return False
    if not set(msg1[1]).issubset(set(msg2[1])):
        return False
    #return True if empty email with no unique attachments
    if len(short_email) == 0:
        return True
    if match_count/len(short_email) > tolerance:
        print(F"{match_count/len(short_email)*100}% of content found.")
        return True
    else:
        return False

    

def rename_emails(email_list):

    #loop through and rename
    error_list = []
    for i in email_list:
        try:
            i.rename(i.parent.joinpath(email_list[i]))
        except PermissionError:
            error_list.append(os.path.basename(i))
            continue
    return error_list


def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)

#handles long paths and converts to pathlib path
def convert_path(path):
    if type(path) == pathlib.WindowsPath:
        path = path.as_posix()
    if '?' not in path[0:10]:
        new_path = os.fspath(pathlib.WindowsPath(path))
        if 'GRGSVRDATA' in new_path:
            new_path = u'\\\\?\\UNC\\' + new_path[2:]
        else:
            new_path = u'\\\\?\\' + new_path
        new_path = pathlib.WindowsPath(new_path)
    else:
        new_path = pathlib.WindowsPath(path)
    return new_path


#GUI


class igui:

    def __init__(self, master):
        self.master = master            #master = root = tk()
        self.master.title("Email Format")   #master.title = root.title = tk().title
        
        #initializing tkk frame to hold widgets, sets size to expand and padding
        self.mainframe = ttk.Frame(master, padding = '20 12 20 12')
        self.mainframe.grid(column = 0, row = 0, sticky = (N,S,E,W))
        self.mainframe.columnconfigure(0, weight = 1)
        self.mainframe.rowconfigure(0, weight = 1)

        #style options
     

        #labels and buttons
        '''
        self.NewButton = ttk.Button(self.mainframe, text = 'Rename \"Email In\"', width=40, command = lambda: self.select_folder(True))
        self.NewButton.grid(column = 1, row = 2, sticky = E)
        self.NewButton = ttk.Button(self.mainframe, text = 'Rename \"Email Out\"', width=40, command = lambda: self.select_folder(False))
        self.NewButton.grid(column =1 , row = 3, sticky = E)
        '''
        self.HelpButton = ttk.Button(self.mainframe, width=5, text='?', command = self.help)
        self.HelpButton.grid(column = 4, row = 1, sticky = (E))
        


        #GRG logo image
        path = resource_path("GRG.png")
        img = ImageTk.PhotoImage(Image.open(path))
        self.image = img
        self.Logo = ttk.Label(self.mainframe, image = img,)
        self.Logo.grid(column = 2, row = 1, sticky = N, columnspan = 3)

        #radio buttons, rename options

        self.LF3 = ttk.LabelFrame(self.mainframe, borderwidth = 5,
                                  relief = GROOVE, text= "Rename Options")
        self.LF3.grid(column = 1, row = 2, sticky = E, rowspan = 4)

        self.LF2 = ttk.LabelFrame(self.LF3)
        self.emailoption = StringVar()
        
        self.OptionSelect3 = ttk.Radiobutton(self.LF2, text = 'Email In', value = 'In', variable = self.emailoption)
        self.OptionSelect4 = ttk.Radiobutton(self.LF2, text = 'Email Out', value = 'Out', variable = self.emailoption)
        self.OptionSelect3.grid(row = 1, sticky = (W))
        self.OptionSelect4.grid(row = 2, sticky = (W))
        
        self.LF1 = ttk.LabelFrame(self.LF3)
        self.datenameoption = StringVar()
        
        self.OptionSelect1 = ttk.Radiobutton(self.LF1, text = 'Name First', value = 'Name', variable = self.datenameoption)
        self.OptionSelect2 = ttk.Radiobutton(self.LF1, text = 'Date First', value = 'Date', variable = self.datenameoption)
        self.OptionSelect1.grid(row = 2, sticky = (W))
        self.OptionSelect2.grid(row = 1, sticky = (W))

        #checkbox for delete redundant
        self.delete_dupe = IntVar()
        self.Delete = ttk.Checkbutton(self.LF3, text = "Delete Non-unique Emails",
                                      variable = self.delete_dupe,
                                      padding = '7 7 7 7')

        #radio buttons, email options



        #listbox
        self.ListBox = Listbox(self.mainframe, width = 100, height = 15)
        self.ListBox.grid(column = 2, row = 2, sticky = W, columnspan = 3, rowspan = 4)
        self.dnd_message = 'Drag and drop .msg files here...'
        self.ListBox.insert(END, self.dnd_message)

        #Listbox drag and drop
        self.ListBox.drop_target_register(DND_FILES)
        self.ListBox.dnd_bind('<<Drop>>', self.lbox_dnd)

        self.NewButton = ttk.Button(self.mainframe, text = 'Rename Emails', width=40, command = self.rename_emails)
        self.NewButton.grid(column = 3, row = 7, sticky = N)

        self.LF_list = [self.mainframe, self.LF1, self.LF2, self.LF3]
        for i in self.LF_list:
            for child in i.winfo_children():
                child.grid_configure(padx=5, pady=5)
       
        self.OptionSelect2.invoke()
        self.OptionSelect3.invoke()
        self.Delete.invoke()
        self.master.update()

    def lbox_dnd(self, e):
        path_list = []
        for i in re.split('[{}]', e.data):
            if convert_path(i).exists():
                i = convert_path(win32api.GetLongPathNameW(i))
                if i.suffix.lower() == ".msg":
                    path_list.append(i)
                else:
                    continue
            else:
                resplit = i.split()
                for k in resplit:
                    k = convert_path(win32api.GetLongPathNameW(k))
                    if k.exists():
                        if k.suffix == ".msg":
                            path_list.append(k)
        if path_list:
            if self.ListBox.size() == 1 and self.ListBox.get(0) == self.dnd_message:
                self.ListBox.delete(0, END)
            for j in path_list:
                if str(j) not in self.ListBox.get(0, END): #check file not already in
                    self.ListBox.insert(END, j)

    def rename_emails(self):
        if self.ListBox.get(0, 1)[0] != self.dnd_message:
            filenames = list(convert_path(i) for i in self.ListBox.get(0, self.ListBox.size()))
            #create loading window, pass to loading window class
            self.mwindow = Toplevel(self.master)
            self.mwindow.transient()
            self.app = loadwindow(self.mwindow)
            #set window position on top of other window
            self.mwindow.geometry("+%d+%d" % (self.master.winfo_x() + 150, self.master.winfo_y() + 100))
            self.mwindow.grab_set()
            self.mwindow.update()
            print(self.delete_dupe.get())
            if self.delete_dupe.get() == 1:
                filtered = filter_email_list(filenames, self.app)
                filenames, delete_list = filtered[0], filtered[1]
                filter_prog = True
            else:
                filter_prog = False
                delete_list = []
            if self.emailoption.get() == "In":
                email_list = get_emails(filenames, True,
                                        self.app, self.datenameoption.get(),
                                        filter_prog)
            else:
                email_list = get_emails(filenames, False, self.app,
                                        self.datenameoption.get(),
                                        filter_prog)
            if delete_list:
                increment = 10/len(delete_list)
                print(delete_list)
                for i in delete_list:
                    self.app.updateprogress(increment, \
                                "Deleting non-unique emails...")
                    os.remove(i)
            error_list = rename_emails(email_list)
            if error_list:
                messagebox.showinfo(message = f'Could not rename some files as they are in use. Please close the following files in Outlook: "{error_list}"')
            else:
                self.app.doneprogress(len(filenames), len(delete_list))
            self.ListBox.delete(0, END)
            self.ListBox.insert(END, self.dnd_message)   
            os.startfile(os.path.dirname(filenames[0]))
            
        


    def help(self):
        self.helpmessage = messagebox.showinfo(message = """This app assists in filing emails by renaming email .msg files:
        \n - "Email In" option renames the file with the name of the sender
        \n - "Email Out" option renames the file with the name of the first recipient
        \n - "Name First" option renames the file with the format (Last Name)(First Letter of First Name) (YYMMDD) (Email Name)
        \n - "Name First" option renames the file with the format  (YYMMDD) (Last Name)(First Letter of First Name) (Email Name)
        \n - "Delete Non-Unique Emails" option searches email content to find redundant emails (ie. emails with replies already in another email and no unique attachments)""")
        




class loadwindow:
    def __init__(self, master):
        self.master = master
        self.master.attributes("-topmost", True)
        self.progress = ttk.Progressbar(self.master, orient = 'horizontal', \
                                        mode = 'determinate', length = 280)
        self.progress.grid_configure(padx = 20, pady = 20)
        self.progress.grid(column = 1, row = 2, sticky = N)
        #progress bar label
        self.text = StringVar()
        self.text.set("Loading")
        self.label = ttk.Label(self.master, textvariable = self.text)
        self.label.grid_configure(padx = 40, pady = 10)
        self.label.grid(column = 1, row = 1, sticky = S)


    def updateprogress(self, percent, text = None):
        self.progress['value'] += percent
        if text:
            self.text.set(text)
        self.master.update()


    def doneprogress(self, renamed, deleted):
        self.progress['value'] = 100
        self.text.set("Done!\n"
                       F"Renamed {renamed} emails\n"
                       F"Deleted {deleted} non-unique emails")
        self.ok_button()
        self.master.update()


    def ok_button(self):
        self.NewButton = ttk.Button(self.master, text = 'OK', width=40, command = self.master.destroy)
        self.NewButton.grid(row = 3, column = 1, sticky = N)
        self.NewButton.grid_configure(padx = 15, pady = 15)


            



root=TkinterDnD.Tk()
#style = ttk.Style()
#style.theme_use('alt')       
app=igui(root)
root.mainloop()
