import subprocess
import tempfile
import os
import re
import tkinter as t
from tkinter import PhotoImage
import time
import threading

found=''
url=''
em=''
pw=''
ck=''
root = t.Tk()
root.title("Course Jumper")
root.geometry("800x600")
image = PhotoImage(file="Logo.png")
logo = t.Label(root,image = image)
logo.pack()
credit = t.Label(text = "Created by ayushshukla8920",fg='Yellow', font=("Helvetica", 20,"bold"))
credit.pack()
heading = t.Label(text = "Skip Coursera Videos : The Easy Way", font=("Helvetica", 30,"bold"))
heading.pack(pady=8)
link_label = t.Label(text = "Enter Course URL : ", font=("Helvetica", 20,"bold"))
link_label.pack(pady = 5)
course_url=t.Entry(root,width=60,font=("Helvetica", 20))
course_url.pack(pady=5)
email_label = t.Label(text = "Coursera Email Address : ", font=("Helvetica", 15,"bold"))
email_label.pack(pady = 2)
email=t.Entry(root,width=20,font=("Helvetica", 20))
email.pack()
password_label = t.Label(text = "Password : ", font=("Helvetica", 15,"bold"))
password_label.pack(pady = 2)
password=t.Entry(root,width=20,font=("Helvetica", 20))
password.pack()
cookie_label = t.Label(text = "Browser Cookie : ", font=("Helvetica", 15,"bold"))
cookie_label.pack(pady = 2)
cookie=t.Entry(root,width=70,font=("Helvetica", 14))
cookie.pack()


def url_button():
    global url
    global em
    global pw
    global ck
    button_pressed = t.StringVar()
    button = t.Button(root, text="Start", command=lambda: button_pressed.set("button pressed"),height=1,width=10,font=("Helvetica", 25,'bold'))
    button.pack(pady=10)
    button.wait_variable(button_pressed)
    url=course_url.get()
    em=email.get()
    pw=password.get()
    ck=cookie.get()
    print(url)
    print(em)
    print(pw)
    print(ck)
    f = open("headers.ct", "r")
    x=f.read()
    em="EMAIL = '"+em+"'"
    pw="PASSWORD = '"+pw+"'"
    ck="COOKIES = "+ck[10:]
    config=x+'\n'+em+'\n'+pw+'\n'+ck
    f.close()
    cf=open("config.py","w")
    cf.write(config)
    cf.close()
    button.destroy()
url_button()



def displaystatus(text,typ):
    global url
    if typ=='url-error':
        url_error = t.Label(text = text, font=("Helvetica", 20,"bold"))
        url_error.pack(pady = 20)
        root.after(1000,url_error.destroy)
        url_button()
        url_extract()
    if typ=='success':
        global success
        success = t.Label(text = text, font=("Helvetica", 20,"bold"))
        success.pack(pady = 20)
        text=text+'.'
        root.after(200,success.config(text=text))
        text=text+'.'
        root.after(200,success.config(text=text))
        text=text+'.'
        root.after(200,success.config(text=text))
        text=text+'.'
        root.after(200,success.config(text=text))



def url_extract():
    global url
    global slug
    global success
    m=re.search('/learn/(.+?)/home',url)
    if m:
        found=m.group(1)
    try:
        print(found)
        slug=found
        displaystatus("URL Validated !!\nProcessing Course Skip",'success')
        start_check_in_bg()
    except:
        print("Invalid URL found during Extraction of Slug")
        displaystatus("Invalid URL! \nPlease Enter Correct Course URL",'url-error')


def check():
    global slug
    global success
    print(found)
    os.system("pip3 install requests")
    os.system("pip3 install loguru")


    try:
        with tempfile.TemporaryFile() as tempf:
            proc = subprocess.Popen(['python3', 'Backend.py' , slug], stdout=tempf)
            proc.wait()
            tempf.seek(0)
            print(tempf.read())

    except:
        print("Invalid URL")
        displaystatus("Invalid URL! \nPlease Enter Correct Course URL",'url-error')
    success.destroy()
    link_label.destroy()
    course_url.destroy()
    email_label.destroy()
    email.destroy()
    password_label.destroy()
    password.destroy()
    cookie_label.destroy()
    cookie.destroy()
    os.system("rm config.py")
    complete = t.Label(text = "Completed", font=("Helvetica", 50,"bold"),fg="green")
    complete.pack(pady = 20)

    
trd = threading.Thread(target=check)
def start_check_in_bg():
    trd.start()

url_extract()


root.mainloop()