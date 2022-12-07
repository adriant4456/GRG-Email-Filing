mock_long_matching_email = (['Thanks Gary, Jay,',
                 'Just noting that the instruction has been sent to me, so I’ll raise an order to you this morning.',
                 '@Jay, let me know when you’d like to book a meeting. We can do by Teams or at either office, as you prefer.',
                 'Regards,', 'Simon',
                 'Sent: Wednesday, 15 September 2021 6:13 PM',
                 'Subject: RE: 21-3250 - Herrenknecht, Shield Turner',
                 'This is an external e-mail. Do not click links or open attachments unless you recognize the sender and know the content is safe.',
                 'Thanks Simon, great news, much appreciated!', 'Regards',
                 '| Gary Gibson | Director ',
                 '| MEng | BEng | ADMechEng | FIEAust CPEng | RPEQ (Mech & Struct) | RBP Vic (Mech & Civil)',
                 '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 419 674 065',
                 '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo',
                 'Over 20 Years of engineering excellence', 'Sent: 15 September 2021 4:48 PM',
                 'Subject: RE: 21-3250 - Herrenknecht, Shield Turner', 'Hi Jay,',
                 'I got a call today from CRR indicating they’d like to proceed with the shield turning frame design.',
                 'I will let you know as soon as I receive the formal instruction, at which time I’ll get a PO issued from my side.',
                 'Following this I think it makes sense to have a kickoff meeting.', 'Looking forward to working with you on this topic.',
                 'Best regards,', 'Simon', 'Sent: Monday, 13 September 2021 5:16 PM',
                 'Subject: 21-3250 - Herrenknecht, Shield Turner',
                 'This is an external e-mail. Do not click links or open attachments unless you recognize the sender and know the content is safe.',
                 'Good Afternoon Simon,', 'Please allow $11,220 + GST to complete the following design and certification:',
                 'Fabrication Drawings can be provided, allow $4640 + GST',
                 'Site Visit/Inspection by Engineering representative, allow $1016 + GST (includes 2x site visits, including travel)',
                 'Exclusions', '- Design Check of crane/crane structure', '- Design Check of shield segments ',
                 '- Analysis for lifting or erection', '- Risk assessment or Safety in Design', 'Information Required',
                 '- Provide 3D model of structure', '- Load/weights and CoG of shield configurations', '- Clamping loads for clamp collar',
                 'The lead time for the completion of this analysis and certification would be 2-3 weeks based on current work load.',
                 'Kind Regards', '| Jay Lu | Design & Drafting Manager', '| BEng | RPEQ | MIEAust CPEng, NER', '| GRG Consulting Engineers',
                 '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 448 245 458', '| 31/139 Commercial Road | Newstead | QLD 4006',
                 '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo'], ['image001.jpg', 'image002.png', 'image003.png'])


mock_short_matching_email = (['Hi Jay,', 'I got a call today from CRR indicating they’d like to proceed with the shield turning frame design.', 'I will let you know as soon as I receive the formal instruction, at which time I’ll get a PO issued from my side.', 'Following this I think it makes sense to have a kickoff meeting.', 'Looking forward to working with you on this topic.', 'Best regards,', 'Simon', 'Sent: Monday, 13 September 2021 5:16 PM', 'Subject: 21-3250 - Herrenknecht, Shield Turner', 'This is an external e-mail. Do not click links or open attachments unless you recognize the sender and know the content is safe.', 'Good Afternoon Simon,', 'Please allow $11,220 + GST to complete the following design and certification:', 'Fabrication Drawings can be provided, allow $4640 + GST', 'Site Visit/Inspection by Engineering representative, allow $1016 + GST (includes 2x site visits, including travel)', 'Exclusions', '- Design Check of crane/crane structure', '- Design Check of shield segments ', '- Analysis for lifting or erection', '- Risk assessment or Safety in Design', 'Information Required', '- Provide 3D model of structure', '- Load/weights and CoG of shield configurations', '- Clamping loads for clamp collar', 'The lead time for the completion of this analysis and certification would be 2-3 weeks based on current work load.', 'Kind Regards', '| Jay Lu | Design & Drafting Manager', '| BEng | RPEQ | MIEAust CPEng, NER', '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 448 245 458', '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo'], ['image001.jpg', 'image002.png'])

mock_non_matching_email = (['Jay,', 'You could put this below on it', 'Civils Area Manager – Northern, Mayne & Clapham', '271 Gilchrist Avenue, Herston, QLD 4006, Australia', 'PO Box 1227, Milton, QLD 4064', 'Greg Ryan', 'Managing Director, Soilwicks Australia', 'IMPORTANT: The contents of this email and any attachments are confidential. They are intended for the named recipient(s) only. If you have received this email by mistake, please notify the sender immediately and do not disclose the contents to anyone or make copies thereof.', '\u200c', 'Sent: Tuesday, 11 January 2022 2:42 PM', 'Subject: RE: U7 Report', 'Hi Greg,', 'Just writing up the certificate, is there a site address you have for CRR?', 'Kind Regards', '| Jay Lu | Design & Drafting Manager', '| BEng | RPEQ | MIEAust CPEng, NER', '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 448 245 458', '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo', 'Sent: 11 January 2022 11:11 AM', 'Subject: RE: U7 Report', 'Greg Ryan', 'Managing Director, Soilwicks Australia', 'IMPORTANT: The contents of this email and any attachments are confidential. They are intended for the named recipient(s) only. If you have received this email by mistake, please notify the sender immediately and do not disclose the contents to anyone or make copies thereof.', '\u200c', 'Sent: Tuesday, 11 January 2022 11:59 AM', 'Subject: RE: U7 Report', 'Hi Greg,', 'Do you have a photo of the unit with the counterweights attached? We are trying to understand where the load is applied. I am assuming they attach to the underside of the vehicle, as shown below. Can you confirm this?', 'Regards,', '| Ben Barry | Mechanical Engineer', '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 421 965 190', '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo', 'Sent: 11 January 2022 10:37 AM', 'Subject: RE: U7 Report', 'Jay,', 'We built them as per option 2 - 1200mm x 1910mm made out of our Mandrel Steel which is 120mm x 60mm x 10mm  ', 'Greg Ryan', 'Managing Director, Soilwicks Australia', 'IMPORTANT: The contents of this email and any attachments are confidential. They are intended for the named recipient(s) only. If you have received this email by mistake, please notify the sender immediately and do not disclose the contents to anyone or make copies thereof.', '\u200c', 'Sent: Tuesday, 11 January 2022 10:46 AM', 'Subject: RE: U7 Report', 'Hi Greg,', 'I didn’t think it was that unreasonable to be honest. On one of our previous analysis for Rib 8 that Andy Hartley did, he required 7.5t of counterweight.', 'Since we have the limit on the counterweight, we will do some checks to see if the effects of 3.7t counterweight and bog mats will get us over the line. Do you have any drawings of the bog mats or advise what RHS sections you make them from?', 'Kind Regards', '| Jay Lu | Design & Drafting Manager', '| BEng | RPEQ | MIEAust CPEng, NER', '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 448 245 458', '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo', 'Sent: 11 January 2022 8:56 AM', 'Subject: RE: U7 Report', 'Geez that doesn’t seem right !! – I can see the rear digging into the pad while in the working position with that much weight over the back.', 'We can fit 3.7t which includes the frame – you will have to combine it with the Bog Mats as attached. The front of the tracks sit up 240mm so that’s a lot of weight transferred to the rear.  ', 'Greg Ryan', 'Managing Director, Soilwicks Australia', 'IMPORTANT: The contents of this email and any attachments are confidential. They are intended for the named recipient(s) only. If you have received this email by mistake, please notify the sender immediately and do not disclose the contents to anyone or make copies thereof.', '\u200c', 'Sent: Tuesday, 11 January 2022 8:40 AM', 'Subject: RE: U7 Report', 'Hi Greg,', 'Our calculations suggest we need at least 5t of counterweight. 600kg for the frame plus 4x 1.1t plates, totalling 5tonne. Would you have access to this much counterweight (an additional 2x plates on top of what you currently have). If so, we can finalise the report and draft up the certificate.', 'Kind Regards', '| Jay Lu | Design & Drafting Manager', '| BEng | RPEQ | MIEAust CPEng, NER', '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 448 245 458', '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo', 'Sent: 7 January 2022 12:56 PM', 'Subject: RE: U7 Report', 'Ben,', 'My mistake I used Unit 8 Brown section for the weight – it has counterweights attached on each side. ', 'This is the correct weight of this Mast U7', 'Regards', 'Greg Ryan', 'Managing Director, Soilwicks Australia', 'IMPORTANT: The contents of this email and any attachments are confidential. They are intended for the named recipient(s) only. If you have received this email by mistake, please notify the sender immediately and do not disclose the contents to anyone or make copies thereof.', '\u200c', 'Sent: Friday, 7 January 2022 1:29 PM', 'Subject: RE: U7 Report', 'Hi Greg,', 'We have been reviewing the overturning stability of the unit and have encountered some issues with achieving the required safety factors. Below is a list of issues which we may need to fix to increase the accuracy:', 'I will continue with the analyses of the boom and stick cylinder attachments based on the information we have.', 'Regards,', '| Ben Barry | Mechanical Engineer', '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 421 965 190', '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo', 'Sent: 7 January 2022 11:43 AM', 'Subject: U7 Report', 'Hi Ben,', 'How are you going with this ?', 'Cheers', 'Greg Ryan', 'Managing Director, Soilwicks Australia', 'IMPORTANT: The contents of this email and any attachments are confidential. They are intended for the named recipient(s) only. If you have received this email by mistake, please notify the sender immediately and do not disclose the contents to anyone or make copies thereof.', '\u200c'], ['image016.jpg', 'image029.png', 'image030.png', 'image031.png', 'image032.png', 'image033.png', 'image034.png', 'image035.png', 'image036.png', 'image037.png', 'image038.png', 'image039.png', 'image040.png', 'image041.jpg', 'image042.png', 'image043.png', 'image044.png', 'image045.png', 'image046.png', 'image047.png', 'image048.png', 'image049.png', 'image050.png', 'image051.png', 'image052.png', 'image053.png', 'image054.png', 'image055.png'])

mock_matching_email_unique_attachment = (['Hi Jay,', 'I got a call today from CRR indicating they’d like to proceed with the shield turning frame design.', 'I will let you know as soon as I receive the formal instruction, at which time I’ll get a PO issued from my side.', 'Following this I think it makes sense to have a kickoff meeting.', 'Looking forward to working with you on this topic.', 'Best regards,', 'Simon', 'Sent: Monday, 13 September 2021 5:16 PM', 'Subject: 21-3250 - Herrenknecht, Shield Turner', 'This is an external e-mail. Do not click links or open attachments unless you recognize the sender and know the content is safe.', 'Good Afternoon Simon,', 'Please allow $11,220 + GST to complete the following design and certification:', 'Fabrication Drawings can be provided, allow $4640 + GST', 'Site Visit/Inspection by Engineering representative, allow $1016 + GST (includes 2x site visits, including travel)', 'Exclusions', '- Design Check of crane/crane structure', '- Design Check of shield segments ', '- Analysis for lifting or erection', '- Risk assessment or Safety in Design', 'Information Required', '- Provide 3D model of structure', '- Load/weights and CoG of shield configurations', '- Clamping loads for clamp collar', 'The lead time for the completion of this analysis and certification would be 2-3 weeks based on current work load.', 'Kind Regards', '| Jay Lu | Design & Drafting Manager', '| BEng | RPEQ | MIEAust CPEng, NER', '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 448 245 458', '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo'], ['image001.jpg', 'image002.png', 'unique.gif'])

mock_partial_matching_email = (['Hi Jay,', 'I got a call today from CRR indicating they’d like to proceed with the shield turning frame design.', 'I will let you know as soon as I receive the formal instruction, at which time I’ll get a PO issued from my side.', 'Following this I think it makes sense to have a kickoff meeting.', 'Looking forward to working with you on this topic.', 'Best regards,', 'Simon', 'Sent: Monday, 13 September 2021 5:16 PM', 'Subject: 21-3250 - Herrenknecht, Shield Turner', 'This is an external e-mail. Do not click links or open attachments unless you recognize the sender and know the content is safe.', 'Good Afternoon Simon,', 'Please allow $11,220 + GST to complete the following design and certification:', 'Fabrication Drawings can be provided, allow $4640 + GST', 'Site Visit/Inspection by Engineering representative, allow $1016 + GST (includes 2x site visits, including travel)', 'Exclusions', '- Design Check of crane/crane structure', '- Design Check of shield segments ', '- Analysis for lifting or erection', '- Risk assessment or Safety in Design', 'Information Required', '- Provide 3D model of structure', '- Load/weights and CoG of shield configurations', '- Clamping loads for clamp collar', 'This is some alternate text lalalalalaala', 'Kind Regards', '| Jay Lu | Design & Drafting Manager', '| BEng | RPEQ | MIEAust CPEng, NER', '| GRG Consulting Engineers', '| T +61 7 3085 1000 | F +61 7 3085 1005 | M +61 (0) 448 245 458', '| 31/139 Commercial Road | Newstead | QLD 4006', '| Brisbane | Melbourne | Sydney | Adelaide | Bendigo'], ['image001.jpg', 'image002.png'])