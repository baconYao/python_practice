import smtplib
import os
import sys

mailserver = smtplib.SMTP('mail.yourisp.com')
mail_files = os.listdir('mail_queue')

# Read in mail files
for eachfile in mail_files:
    file_name = 'mail_queue' + os.path.sep + eachfile
    file = open(file_name, 'r')
    me = file.readline()
    them = file.readline()
    mail_body = ''.join(file.readlines())
    file.close()
    # Try to send mail, then delete it
    try:  
        mailserver.sendmail(me, them, mail_body)
    except smtplib.SMTPAuthenticationError, error:      # Normal exception handler
        print "Bad username or password:", error
    except (smtplib.SMTPConnectError, smtplib.SMTPHeloError), error:        # Multiple exception handlers
        print "The server is not responding!", error
    except Exception, error:        # Generic exception handler
        print "An unexpected exception: ", error
    else:           # Ran successfully
        os.remove(file_name)


mailserver.quit()