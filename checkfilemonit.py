import os, time, ast
from email.MIMEMultipart import MIMEMultipart
import ConfigParser, yagmail

CONFIG = ConfigParser.RawConfigParser() #initilizes the config parser
CONFIG.read("app.cfg")

MAIL = yagmail.SMTP({'pyfilechecker@gmail.com': 'PythonFileChecker - Lloyd Browman'},
                    'YmTthNbM*<F4-,,e') #mail client used

def sendmail(alertfile, passedtime):
    """Sends mail"""
    recipient = ast.literal_eval(CONFIG.get('email', 'email'))
    msg = MIMEMultipart('alternative')
    msg['subject'] = 'A file has not been updated'
    msg['body'] = "{} has not been modified in {} mins.".format(alertfile, passedtime)
    MAIL.send(recipient, msg['subject'], msg['body'])

def gettimepassed(directory, filename):
    """Gets the time passed since file was modified"""
    return (time.time()-os.path.getmtime(os.path.join(directory, filename)))/60

while 1:
    TIME_INTERVAL = CONFIG.get('timeinterval', 'time')
    DIRECTORIES = ast.literal_eval(CONFIG.get('dir', 'dir'))

    for directory in DIRECTORIES:
        files = os.listdir(directory)
        newest_file = max(files, key=os.path.getctime)
        timelastmodified = gettimepassed(directory, newest_file)
        print  newest_file, timelastmodified
        if gettimepassed(directory, newest_file) < 20:
            sendmail(newest_file, timelastmodified)



