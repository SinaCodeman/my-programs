import requests
from tkinter import PhotoImage
from tkinter import messagebox
import tkinter as tc
def data_by_character():
    anime_character=Enter2.get()
    anime_jyson=requests.get(f'https://animechan.xyz/api/random/character?name={anime_character}')
    info1=anime_jyson.json()['quote']
    info2=anime_jyson.json()['anime']
    info3=anime_jyson.json()['character']
    Label3.config(text=info1, bg='yellow')
    Label4.config(text=info2, bg='blueviolet')
    Label5.config(text=info3, bg='springgreen')
def data_by_anime():
    anime_name=Enter1.get()
    anime_jyson=requests.get(f'https://animechan.xyz/api/random/anime?title={anime_name}')
    info1=anime_jyson.json()['quote']
    info2=anime_jyson.json()['anime']
    info3=anime_jyson.json()['character']
    Label3.config(text=info1,bg='yellow')
    Label4.config(text=info2,bg='blueviolet')
    Label5.config(text=info3,bg='springgreen')
def exit():
    if messagebox.askyesno('Exit','do you want to Exit?'):
        Anime.destroy()
#Def
Anime=tc.Tk()
image_patch=r"C:\Users\USER\Pictures\anime.png"
image_bg=PhotoImage(file=image_patch)
set_image_bg=tc.Label(Anime,image=image_bg)
set_image_bg.pack()
Anime.title('Anime character quotes program')
Anime.geometry('673x550')
Label1=tc.Label(Anime,text='pleas enter anime name to get random quote:',font='Verdana 11 bold',bg='orange')
Label1.place(x=0,y=0)
Label2=tc.Label(Anime,text='pleas enter anime character to get quotes:',font='Verdana 11 bold',bg='orange')
Label2.place(x=0,y=20)
Label3=tc.Label(Anime,text='quote:',font='Helvetica',bg='yellow')
Label3.place(x=0,y=80)
Label4=tc.Label(Anime,text='anime name:',font='Helvetica',bg='blueviolet')
Label4.place(x=0,y=110)
Label5=tc.Label(Anime,text='character name:',font='Helvetica',bg='springgreen')
Label5.place(x=0,y=140)
#Label
Enter1=tc.Entry(Anime)
Enter1.place(x=390,y=0)
Enter2=tc.Entry(Anime)
Enter2.place(x=370,y=24)
#Entery
Button1=tc.Button(Anime,text='click for quote by anime name',command=data_by_anime,bg='cyan')
Button1.place(x=220,y=180)
Button2=tc.Button(Anime,text='click for quote by character name',command=data_by_character,bg='cyan')
Button2.place(x=320,y=205)
Button3=tc.Button(Anime,text='click for Exit',command=exit,bg='red')
Button3.place(x=600,y=0)
#Button
Anime.mainloop()