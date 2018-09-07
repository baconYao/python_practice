 #!/usr/bin/python
 # -*- coding: utf-8 -*-

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import tempfile
import os

def mail_report(to, ticker_name):
    """
        This structure has two containers. The outside one contains the message part and any number of attachments,
        and the inside container has the two versions of your email. 
        If you need extra attachments, attach them to the outside container.
    """

    # Create external container
    outer = MIMEMultipart()
    outer['Subject'] = "Stock report for " + ticker_name
    outer['From'] = "type your email's account@gmail.com"
    outer['To'] = to

    # Internal text container, create body of email
    """
        Normally an email program will display the last part of this container as the body, 
        and fall back on the others if it can’t handle it, so you put the HTML last.
    """
    inner = MIMEMultipart('alternative')
    text = "Here is the stock report for" + ticker_name
    html = """\
    <html>
        <head></head>
        <body>
            <p>Here is the stock report for
                <b>""" + ticker_name + """</b>
            </p>
        </body>
    </html>
    """

    # Attach body to external container, create MIMEText objects to hold the email body
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')
    inner.attach(part1)
    inner.attach(part2)
    outer.attach(inner)

    # Create CSV part and attach it
    filename = 'stocktracker-%s.csv' % ticker_name
    csv_text = ''.join(file(filename).readlines())
    csv_part = MIMEText(csv_text, 'csv')
    # Add a Content-Disposition header to say that it’s an attachment, and give it a file name
    csv_part.add_header('Content-Disposition', 'attachment', filename=filename)
    outer.attach(csv_part)
    
    return outer

def send_message(message):
    try:
        # Create SMTP sender
        s = smtplib.SMTP("smtp.googlemail.com")         #In this program, I use google as SMTP server
        s.ehlo()
        s.starttls()
        s.ehlo()

        # Type your email account and password here
        """
            Hint: If you use 2-factor authentication, you can follow this solution:
            https://stackoverflow.com/questions/28421887/django-email-with-smtp-gmail-smtpauthenticationerror-534-application-specific-pa
        """
        username = "type your email's account"
        password = "type your email's password"
        
        s.login(username, password)
        # Use sender to send an email
        s.sendmail(
            message['From'],
            message['To'],
            message.as_string()
        )
        print "Ok the email has sent"
        s.quit()
    except Exception, error:
        print 'can\'t send the Email'
        print
        print error

def queue_mail(message):
    # Create mail queue directory
    if os.access('mail_queue', os.F_OK) != 1:
        os.mkdir('mail_queue')
    # Make temporary file 
    handle, file_name = tempfile.mkstemp(
        prefix='mail',
        dir='mail_queue',
        text='True'
    )
    mail_file = open(file_name, 'w')
    # Write mail info to mail file
    mail_file.write(message['From'] + '\n')
    mail_file.write(message['To'] + '\n')
    mail_file.write(message.as_string() + "\n")

if __name__ == "__main__":
    email = mail_report("peiyaochang@qnap.com,bacon735392@yahoo.com.tw", "GOOG")
    # print email.as_string()     # print out the email
    send_message(email)