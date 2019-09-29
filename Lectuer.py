from gtts import gTTS
import os
from tkinter import *

def click():
    text = entry_1.get()

    language = 'pl'

    audio = gTTS(text=text, lang=language, slow=False)

    audio.save("note.mp3")

    os.system("start note.mp3")

window = Tk()
window.title("Lectuer")
window.configure(background='black')

photo = PhotoImage(file="gif.gif")
Label (window,image=photo,bg='black').grid(row=0,column=0)
Label(window,text="Wpisz zawartość notatki:", bg='black',fg='white',font = 'non 12 bold').grid(row=1,column=0,sticky=N)
entry_1 = Entry(window, width = 100,)
entry_1.grid(row=2,column=0,sticky=N)
Label(window,text="",bg='black').grid(row=3,column=0,sticky=N)
Button(window,text='Start',width=10,fg='red',command=click).grid(row=4,column=0,sticky=N)
Label(window,text="",bg='black').grid(row=5,column=0,sticky=N)
Label(window,text="",bg='black').grid(row=5,column=0,sticky=N)




window.mainloop()