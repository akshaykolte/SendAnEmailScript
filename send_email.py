import smtplib
import getpass
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.mime.text import MIMEText
from email.utils import formatdate
from email import Encoders

def send_email(recipients, subject_text, mail_text,
            email_id,
            password ):
    
    COMMASPACE = ', '

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject_text
    me = email_id

    msg['From'] = me
    msg['Date'] = formatdate(localtime=True)
    msg.attach( MIMEText(mail_text, 'html') )

    msg['To'] = COMMASPACE.join(recipients)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(email_id, password)
    server.sendmail(me, recipients, msg.as_string())
    server.quit()






def getEmailId():
    print 'Enter your email address: '
    email_id = raw_input()
    return email_id

def getRecipients():
    print 'Enter recepient email address: (-1 to stop) '
    recipients = []
    while(1):
        email = raw_input()
        if email == "-1":
            break
        recipients.append(email)
    
    return recipients

def getSubjectText():
    print 'Enter subject: '
    subject = raw_input()
    return subject

def getMailText():
    print 'Enter mail text: '
    mail_text = raw_input()
    return mail_text

def getPasswordText():
    print 'Enter your password: '
    pw = getpass.getpass()
    return pw

def main():
    email_id = getEmailId()
    recipients = getRecipients()
    subject_text = getSubjectText()
    mail_text = getMailText()
    password = getPasswordText()

    send_email(recipients, subject_text = subject_text, mail_text = mail_text,
            email_id = email_id,
            password = password)
if __name__ == '__main__':
    main()
