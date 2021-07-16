from tkinter import *
import random
import timeit
from timeit import default_timer
import difflib
import time


from datetime import datetime
from datetime import date

root = Tk()
##window=Tk()
root.title('Python Typing Speed test')
root.geometry("1350x400")
root.resizable('false','false')
root.configure(bg="sandybrown")



entered = StringVar()

greet = Label(root, font=('arial', 30, 'bold'),bg="sandybrown", text="Typing Test")
greet.place(relx=0.5,rely=0.1,anchor=CENTER)

words = ['Let"s type type type.... and type to increase speed.','This time I will use &peci@l ch@rac@ter$ .','Let us try with numbers . There are 9 apples 4 person and 2 plate','Let us try number + speci@l ch@ra@cters all in 1 , @are you re@dy :\n 5+3 i& 8 and 8-3 i$ 5 while 8*3 iS 24 and 24/8 IS 3','We are developing PytHon prOject 0X00', 'This is WindoWs Os', 'We are Hiring so show us your skiLLs', 'Lets Play a game',
         'Python is a programming language', 'We love Coding', 'This is an amazing Article', 'I am an Intern',
         'Lets check the Output', 'we are Compiling this program']

word="Are You Ready??"


def check():
    global entered
    global word
    global start

    string = f"{entered.get()}"
    today2=datetime.now()
    end=today2.strftime("%H:%M:%S")
    
    ##end = timeit.default_timer()
    FMT = "%H:%M:%S"
    s_time = datetime.strptime(end,FMT) - datetime.strptime(start , FMT)
    
    s_time=str(s_time)
    dif=[]
    s_time=s_time.split(":")
    for s in s_time:
        dif.append(int(s))
    time=dif[0]*3600+dif[1]*60+dif[2]

    try:
        speed = round(len(string.split()) * 60 / time, 2)
    except:
        speed=0

    if string == word:
        Msg1 = "Time= " + str(time) + ' seconds'
        Msg2 = " Accuracy= 100% "
        Msg3 = " Speed= " + str(speed) + 'wpm'

    else:
        accuracy = difflib.SequenceMatcher(None, word, string).ratio()
        accuracy = str(round(accuracy * 100, 2))
        Msg1 = "Time= " + str(time) + ' seconds'
        Msg2 = " Accuracy= " + accuracy + '%'
        Msg3 = " Speed= " + str(speed) + ' wpm'  # words per minute

    label = Label(root, font=('arial', 15, 'bold'), text=Msg1)
    label.grid(row=7, columnspan=3)

    label = Label(root, font=('arial', 15, 'bold'), text=Msg2)
    label.grid(row=8, columnspan=3)

    label = Label(root, font=('arial', 15, 'bold'), text=Msg3)
    label.grid(row=9, columnspan=3)
    

def play():
    global word
    
    global entered

    today= datetime.now()
    global start
    start=today.strftime("%H:%M:%S")
    
    word = random.choice(words)
    label.config(text=word)
    label1 = Label(root, font=('arial', 15), text="Type here")
    label1.place(relx=0.1,rely=0.6,anchor=CENTER)

    entered = StringVar()
    enter = Entry(root, textvariable=entered, font=('arial', 15), width=80)
    enter.place(relx=0.85,rely=0.6,anchor=E)

    btn = Button(root, text="Check", command=check, bg="DodgerBlue2", fg="white", font=('arial', 10))
    btn.grid(row=6, columnspan=6)


label = Label(root, font=('arial', 20, 'bold'), text=word)
label.place(relx=0.5,rely=0.4,anchor=CENTER)


s_typing = Button(root, text=" Start typing", command=play, bg="DodgerBlue2", fg="white", font=('arial', 10))
s_typing.place(relx=0.5,rely=0.23,anchor=CENTER)


mainloop()






###############################################################################################################################
##
##today= datetime.now()
##c_time=today.strftime("%H:%M:%S")
##print(today)
##print(c_time)
##print("\n\n")
##time.sleep(1)
##today2=datetime.now()
##c_time2=today2.strftime("%H:%M:%S")
##print(today2)
##print(c_time2)
##
##
##FMT = "%H:%M:%S"
##tdelta = datetime.strptime(c_time2,FMT) - datetime.strptime(c_time , FMT)
##tdelta=str(tdelta)
##dif=[]
##tdelta=tdelta.split(":")
##for t in tdelta:
##    dif.append(int(t))
##diff=dif[0]*24+dif[1]*60+dif[2]
##print(diff)




