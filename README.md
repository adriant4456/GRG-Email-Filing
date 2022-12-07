# GRG-Email-Filing

Simple program to rename exported .msg files for filing and QA purposes, created for GRG Consulting Engineers.


## Functionality
This program allows the user to select exported .msg file and renames files according to selected options for QA and filing purposes. The following renaming options are allowed:

- "Email In" option renames the file with the name of the sender
- "Email Out" option renames the file with the name of the first recipient
- "Name First" option renames the file with the format (Last Name)(First Letter of First Name) (YYMMDD) (Email Name)
- "Name First" option renames the file with the format  (YYMMDD) (Last Name)(First Letter of First Name) (Email Name)
- "Delete Non-Unique Emails" option searches email content to find redundant emails (ie. emails with replies already in another email and no unique attachments)


## Features

- Tkinter GUI
- Build file for PyInstaller to export to .exe file
