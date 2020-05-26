from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3 as pp
from win32 import win32api
#import imp,sys, os



'''engine = pp.init("dummy")

voices=engine.getProperty("voices")
print(voices)

engine.setProperty("voice",voices[0].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()'''

bot = ChatBot("My_Bot")


convo = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "That is good to hear",
    "Thank you.",
    "You're welcome."
]

trainer=ListTrainer(bot)
trainer.train(convo)

'''#answer=bot.get_response("How are you doing?")
#print(answer)

print("Talk to Bot")
while(True):
    querry=input()
    if(querry=="exit"):
        break
    answer=bot.get_response(querry)
    print(answer)'''

root=Tk()
root.geometry("500x650")
root.title("CHAT BOT")
img=PhotoImage(file= "F:\ChatBot\\08e7ec0f84233b37ac26e920bc60ec57.gif")
photoL=Label(root,image=img)
photoL.pack(pady=5)


def ask_from_bot():
    querry=textF.get()
    answer_from_bot=bot.get_response(querry)
    msgs.insert(END,"you : " + querry)
    msgs.insert(END,"bot : " + str(answer_from_bot))
    #speak(answer_from_bot)
    textF.delete(0,END)
    msgs.yview(END)

frame=Frame(root)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()
textF=Entry(root,font=("Verdana",20))
textF.pack(fill=X,pady=10)
btn=Button(root,text="Ask From Bot",font=("Verdana",20),command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

root.bind('<Return>',enter_function)    

root.mainloop()
