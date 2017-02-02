"""
File alert  script for Louis Dillon by Lloyd Browman
2017-02-02
"""
import os, time, ast, sys
from email.MIMEMultipart import MIMEMultipart
import ConfigParser, yagmail

CONFIG = ConfigParser.RawConfigParser() #initilizes the config parser
CONFIG.read("app.cfg")

MAIL = yagmail.SMTP({'pyfilechecker@gmail.com': 'PythonFileChecker - Lloyd Browman'},
                    'YmTthNbM*<F4-,,e') #mail client used

def sendmail(minutes):
    """Sends mail"""
    recipient = ast.literal_eval(CONFIG.get('email', 'recipient')) #gets mail recipients
    msg = MIMEMultipart('alternative')
    msg['subject'] = str(ast.literal_eval(CONFIG.get('email', 'subject'))).format(
        ast.literal_eval(CONFIG.get('email', 'computer'))) # gets subject paramters
    #fills body of message
    msg['body'] = "Your target directory has not been updaed in {} mins.".format(minutes)
    MAIL.send(recipient, msg['subject'], msg['body'])

def gettimepassed(targeted_directory, filename):
    """Gets the time passed since file was modified"""
    return (time.time()-os.path.getmtime(os.path.join(targeted_directory, filename)))/60

try:
    while 1:
        DIRECTORIES = ast.literal_eval(CONFIG.get('dir', 'dir')) #gets directory from config file
        #gets time interval to check for
        MINUTES = ast.literal_eval(CONFIG.get('timeinterval', 'minutes'))
        for directory in DIRECTORIES:
            if os.path.exists(directory): #check if directory exists
                files = os.listdir(directory)
                newest_file = max(files, key=os.path.getctime) #gets last modified file
                if gettimepassed(directory, newest_file) > MINUTES:
                    sendmail(MINUTES)
                    time.sleep((MINUTES*60))
                else:
                    time.sleep(60)
            else:
                print "Directory Does not Exist"
                time.sleep(15)
                sys.exit()
except Exception as identifier:
    with open("error.log", "a+") as log:
        log.write("Error: {}".format(identifier.msg))




