#!/usr/bin/env python 
from selenium import webdriver
import sys
import time
import os

    # django v3.0

def arrtotext(arr):
    string=''
    for b in arr:
        string += b
    return string
def openwrite(nameoffile,textinput):
        try:
            f = open(nameoffile,'w+')
            f.write(textinput)
        # perform file operations
        except :
            print('could not open.'+nameoffile+'\n open file returned this error stream. Raise OSError')
        finally:
            f.close()
def namingerror():
    print('There seems to be an error in your syntax.\ndid you follow the easydjango syntax :\n\n \t easydjango create [name of project] [name of app] [otional: port number]\n')
    print('Or did you follow the naming rules: ')
    print('\n\tModules should have short, all-lowercase names. \n\tUnderscores can be used in the module name if it improves readability. \n\tPython packages should also have short, all-lowercase names, although the use of underscores is discouraged.')
    print('\nopen this link to learn more about naming modules: https://www.python.org/dev/peps/pep-0008/')
    print(' \n\trun easydjango --h or -help. \nOr open an issue at https://github.com/easydjango/issues')
def create():
    # length should be less than five and more than four. print out an error for naming
    if len(sys.argv)>5 or len(sys.argv)<4:
        namingerror()
        quit()
    else:
        if len(sys.argv)>4:
            #this means the user has entered the port number hence;
            try:
                create.portnumber=int(arrtotext(sys.argv[4]))
            except:
                print('the last item should be a port number')
                namingerror()
                quit()
        else:
            # if user has not entered port number declare it as empty
            create.portnumber=''
        print('easydjango is creating your app....')
        #get the name of the project
        create.projectname=arrtotext(sys.argv[2])
        #create django project
        try:
            os.system('django-admin startproject '+create.projectname)
            #get the name of the app
            create.appname=arrtotext(sys.argv[3])
            # navigate to the folder and create the  app
            time.sleep(3)
            os.chdir(create.projectname)
            time.sleep(3)
            os.system('python3 manage.py startapp '+create.appname)
            #navigate to the app folder and open the views.py folder
            time.sleep(3)
            os.chdir(create.appname)
            
            #open views.py and paste the following code
            openwrite('views.py',"from django.shortcuts import render\n\ndef index(request):\n\treturn render(request, '"+create.appname+"/index.html', {}) ")
            openwrite('urls.py',"from django.urls import path\nfrom . import views\n\nurlpatterns = [\n\tpath('', views.index, name='index'),\n]")
            # create html template now
            os.makedirs('templates/'+create.appname)
            os.chdir('templates/'+create.appname)

            welcomemessage="""<html>
                <body style='width:100%;position:absolute;height:100%;text-align:center;display: table-cell;vertical-align: middle;'>
                    <span  style='font-size:100px;'>U+1F916</span>
                    <h1  style='font-weight:bold;'>Hello Human!</h1>
                    <h3  style='font-weight:normal;'>I am easydjango.<br>Glad to be of service.<br>Here's your neat django website.<br>Hope to see you again soon<h3>
                </body>
            </html>
            """
            openwrite('index.html',welcomemessage)
            # change directory to the [project name folder]
            os.chdir('..')
            os.chdir('..')
            os.chdir('..')
            os.chdir(create.projectname)
            # write onto urls.py inside there
            openwrite('urls.py',"from django.contrib import admin\nfrom django.urls import include, path\nurlpatterns = [\n\tpath('',include('"+create.appname+".urls')),\n path('admin/', admin.site.urls),\n]")
            edsettings = open("settings.py", "r")
            lines = edsettings.readlines()
            lines[39] = "\t'"+create.appname+".apps."+create.appname.capitalize()+"Config',\n]\n"

            edsettings = open("settings.py", "w")
            edsettings.writelines(lines)
            edsettings.close()
            # make migrations
            os.chdir('..')
            os.system('python3 manage.py migrate')
            print('\n\n'+u"\U0001F389"+u"\U0001F389"+'congrats your project has been created '+u"\U0001F389"+u"\U0001F389"+'\n\n')
            openbrowser()

        except:
            print('sorry, that project already exists.')
           

def openbrowser():
            # run server
            
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument("--test-type")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument('--window-size=1420,1080')
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        options.binary_location = "/usr/bin/google-chrome"
    
        driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
        if create.portnumber=='':
            
            driver.get('http://127.0.0.1:8000/')
            os.system('python3 manage.py runserver '+str(create.portnumber))
            
        else:
            driver.get('http://127.0.0.1:'+str(create.portnumber)+'/')
            os.system('python3 manage.py runserver '+str(create.portnumber))



def helpme():
    print('Hi. I\'m easydjango. I make creating django projects easy (obviously, as my name suggests .)\n')
    print('using me is pretty easy, just follow the instructions below')
    print('command syntax:\n\n\tcreating a project: \teasydjango create [project_name] [app_name] [optional:port_number]\n\nhelp:\teasydjango -help or easydjango --h')
    print('Also make suree to follow the following naming rules when naming your projects and apps: ')
    print('\n\tModules should have short, all-lowercase names. \n\tUnderscores can be used in the module name if it improves readability. \n\tPython packages should also have short, all-lowercase names, although the use of underscores is discouraged.')
    print('\nopen this link to learn more about naming modules: https://www.python.org/dev/peps/pep-0008/')
    print('and remember; we are  all adults, you can do as you wish')
    print('I was created and I am maintained by leonkoech. You can find him here https://github.com/leonkoech')
def main():
    userselection= arrtotext(sys.argv[1])
    if userselection=='--h' or userselection=='-help':
        helpme()
    elif userselection=='create':
        create()
    else:
        print('wrong input. please run: easydjango --h or help to get help')
if __name__=='__main__':
    main()