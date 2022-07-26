from tkinter import * 
import random, string
from turtle import color

passwordtext = ''
passwordtext1= ''

def copy_to_clipboard():
    window.clipboard_clear()  
    window.clipboard_append(str(passwordtext1[:int(scaleofnum.get())]))

def gen():
    global passwordtext, outputpass, passwordtext1
    passwordtext1 = ''
    passwordtext = ''
    if (va1.get() == 0 and va2.get()==0 and va3.get()==0):
        if (scaleofnum.get() == 0):
            for i in range(8):
                passwordtext = passwordtext + random.choice(string.ascii_letters)
            for i in range(4):
                    passwordtext = passwordtext + str(random.choice(string.punctuation))
            for i in range(3):
                    passwordtext= passwordtext + str(random.randint(0,10))
            passwordtext = list(passwordtext)
            random.shuffle(passwordtext)
            passwordtext1="".join(passwordtext)
            outputpass.config(text=passwordtext1)
            window.update()
        else:
            for i in range(20):
                passwordtext = passwordtext + random.choice(string.ascii_letters)
            for i in range(20):
                passwordtext = passwordtext + str(random.choice(string.punctuation))
            for i in range(20):
                passwordtext= passwordtext + str(random.randint(0,10))
            passwordtext = list(passwordtext)
            random.shuffle(passwordtext)
            passwordtext1="".join(passwordtext)
            outputpass.config(text=str(passwordtext1[:int(scaleofnum.get())]))
            window.update()
    else:
        if (scaleofnum.get() == 0):
            if (va3.get() == 1):
                for i in range(20):
                    passwordtext = passwordtext + random.choice(string.ascii_letters)
            if (va2.get() == 1):
                for i in range(20):
                    passwordtext = passwordtext + str(random.choice(string.punctuation))
            if (va1.get() == 1):
                for i in range(20):
                    passwordtext= passwordtext + str(random.randint(0,10))
            passwordtext = list(passwordtext)
            random.shuffle(passwordtext)
            passwordtext1="".join(passwordtext)
            outputpass.config(text=str(passwordtext1[:int(scaleofnum.get())]))
            window.update()
        else:
            if (va3.get() == 1):
                for i in range(20):
                    passwordtext = passwordtext + random.choice(string.ascii_letters)
            if (va2.get() == 1):
                for i in range(20):
                    passwordtext = passwordtext + str(random.choice(string.punctuation))
            if (va1.get() == 1):
                for i in range(20):
                    passwordtext= passwordtext + str(random.randint(0,10))
            passwordtext = list(passwordtext)
            random.shuffle(passwordtext)
            passwordtext1="".join(passwordtext)
            outputpass.config(text=str(passwordtext1[:int(scaleofnum.get())]))
            window.update()

    
window = Tk()

va1 = IntVar()
va2 = IntVar()
va3 = IntVar()

window.title('Password generator')
window.config(background='black')
window.geometry('190x250')

outputpass = Label(window, width=20,borderwidth = 3, relief="sunken", background='black' )
outputpass.pack()
generatebutton = Button(window, text="generate new password", command=gen, width=20, background='black')
generatebutton.pack()
copybutton = Button(window, text='copy', width=20, command=copy_to_clipboard, compound='left')
copybutton.pack()
Label2 = Label(window, text='длинна пароля:', background='black', foreground='white')
Label2.pack(fill=BOTH)
scaleofnum = Scale(window, from_= 0, to=20, orient=HORIZONTAL, tickinterval=5, background='black')
scaleofnum.pack(fill=BOTH)

Label3 = Label(window, text='символы:', background='black', foreground='white')
Label3.pack(fill=BOTH)

c3 = Checkbutton(window, text='words', variable=va3 , onvalue=1, offvalue=0, background='black')
c3.pack(side=TOP)
c1 = Checkbutton(window, text='digits', variable=va1 , onvalue=1, offvalue=0, background='black')
c1.pack(side=TOP)
c2 = Checkbutton(window, text='special symbols', variable=va2 , onvalue=1, offvalue=0, background='black')
c2.pack(side=TOP)

window.mainloop()
 



