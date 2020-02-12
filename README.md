Project "control" by Wikwoj0512 
Technology used:
Python 3.7.2
Flask, Flask-Socketio, Pillow, Requests, Json

Tested on Windows 7 Professional

Project was made to remotly control a pc via a website. On the website you can find a screenshot of the computer you want to control and a input box for commands. 

/website is the code designated for the server. All PIP requirements are to be found in "requirements" file.
Setup is done by changing the values in /website/config.py file to ip and port of the server. 
The password part doesn't work for now, i will try to debug in in later commits

/computer is the code designated for the computer you want to controll. All PIP requirements are to be found in "requirements" file.
Setup is done by changing the values in /computer/config.py file to point to your web server.
All you need to do is to run "mainapp.py" file. 
I will add full list of commands, for now you can try to take them from custom library "keystrs".

Be careful and have fun 
