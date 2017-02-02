# Overview

This is a simple script to  monitor one or more specified directories checking if the last modified file has 
been updated recently. If it has not an email alert is sent.

## Dependencies

This script uses python2.7 and requires the following libraries to be installed:

    1. ast
    2. yagmail
    3. ConfigParser

Follow the link as a guide to pip install [https://github.com/BurntSushi/nfldb/wiki/Python-&-pip-Windows-installation]

## Set up as a Task

1. On windows, open Task Scheduler.

2. Click create Basic Task.

3. Set a name for your Task then  hit next.

4. Select schedule for the  task to run then hit next.

5. Under Action select start a program

6. Place "C:\Python27\python.exe" in Program/script. Place "checkfilemonit.py" as the script you which to start. Finally place th location of the script where you see start in (optional).

7. Press next then Finished.
