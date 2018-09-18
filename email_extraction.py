import imapclient
imapObj = imapclient.IMAPClient('imap.gmail.com', ssl=True)
imapObj.login('somefreaky@gmail.com ', 'secretkey')
imapObj.select_folder('INBOX',readonly=True)
import imaplib
imaplib._MAXLINE = 10000000
UIDs = imapObj.gmail_search('ALL')


filename = "mail1.csv"
f = open(filename,"w", encoding='utf-8')
header = "subject,from,email\n"
f.write(header)

import pyzmail
for i in range(len(UIDs)):
    rawMessages = imapObj.fetch(UIDs[i], ['BODY[]'])
    #import pprint
    #pprint.pprint(rawMessages)
    message = pyzmail.PyzMessage.factory(rawMessages[UIDs[i]][b'BODY[]'])
    sub=message.get_subject()
    print(message.get_subject())
    from1= message.get_addresses('from')
    f1=from1[0]
    f10=f1[0]
    f11=f1[1]
    print(from1)
    print(f1[0])
    print(f1[1])
    print(sub)
    f.write(sub.replace(',','|')+","+f10.replace(',','|')+","+ f11.replace(',','|')+"\n")
f.close()
imapObj.logout()


