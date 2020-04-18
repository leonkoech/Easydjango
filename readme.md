# Easy Django

![chromedriver:80.0.3987.106](https://img.shields.io/badge/chromedriver-80.0.3987.106-blue)
![python:3.7.3](https://img.shields.io/badge/python-3.7.3-blue)
![build:passing](https://img.shields.io/badge/build-passing-green)
![selenium:3.141.0](https://img.shields.io/badge/selenium-3.141.0-black)
![coverage:76%](https://img.shields.io/badge/coverage-76%25-yellowgreen)
![version:1.0.0](https://img.shields.io/badge/version-1.0.0-black)

**easydjango is an automation software for creating django webapps with one command.**

I created the project to help me easily create a django project and save lots of time, it also automatically runs the server and opens the browser with selenium after it has created the webapp

``easydjango create [project_name] [app_name] [optional:port_number]``


## Requirements

easydjango requires you to have django already installed on your system

```pip install django```

verify with

```django-admin --version```


easydjango requires the following to open a browser window once it is done creating the web app.


*selenium 3.141.0 [documentation](https://selenium-python.readthedocs.io/api.html#selenium.webdriver.remote.webdriver.WebDriver.current_url)[download](https://pypi.org/project/selenium/)

*chrome version 80 [download](https://www.google.com/chrome/?brand=CHBD&gclid=CjwKCAjwpqv0BRABEiwA-TySwcmdG9S6AfkK0EmkAgCUchDrG_NLrQmbyZ5PcTMYACxK2po4Tsq5nhoCZh0QAvD_BwE&gclsrc=aw.ds)

*chromedriver 80.0.3987.106[download](https://chromedriver.chromium.org/downloads)
python 3.7.3+ [download](https://www.python.org/downloads/)

## Setup

If you are going to use the chrome driver make sure chrome driver and the chrome binary are set to the right directory in the easydjango.py file

```
        options.binary_location = "/usr/bin/google-chrome"
        driver = webdriver.Chrome(options=options, executable_path='/usr/local/bin/chromedriver')
```

if you do not wish to use the selenium webdriver (boo!) you can remove this line from your easydjango.py file

```def create:

        #remove this line
        openbrowser()
```

## Installation

This is the fun part. Making easydjango acessible through the terminal.
Also a disclaimer of sorts, this installation is for linux systems. Please look on how to make a python script executable for your operating system.

1. clone easydjango project to a directory of your choice and open the easydjango folder. 

    ``easydjango/easydjango``

2. run the following command in a terminal

    ``chmod +x easydjango.py``

3. edit the shebang - *the* **!/usr/bin/env python3** *at the top to match the location of your python environment. Though this shebang should work on both mac and linux systems for python 3*

4. drop the .py extension by running the following command

    ``mv easydjango.py easydjango``

5. Now add easydjango to your path. Start by creating bin directory if you don't already have it. It's in home/bin
        create bin
    ``mkdir -p ~/bin``
        or  continue if bin already exists

6. copy script to bin

    ``cp easydjango ~/bin``

7. finally add it to your path. You can either add it temporarily or permanently.
        to add it temporarily run the folowing command(so that you can test it out)
    ``export PATH=$PATH"=$HOME/bin"``
        to add it permanently 
    ``echo 'export PATH=$PATH":$HOME/bin"' >> .profile``
        refresh terminal with the following commannd OR just open a new terminal
    ``source .profile``
    


## Demo

A short demo of ``easydjango`` at work.

![demo2](https://user-images.githubusercontent.com/39020723/79636059-b709f680-817d-11ea-8fcf-93d5868b7dc4.gif)


## Contribution

If you would like to contribute to the project you can reach me via [email](mailto:leonkipkip@gmail.com)
Read the [contribution guide](https://github.com/leonkoech/easydjango/blob/master/contributions.md)

## License

This project is under the [MIT license](https://github.com/leonkoech/easydjango/blob/master/LICENSE)


