import tkinter as tk
from tkinter import *

import requests
URL="https://api.openweathermap.org/data/2.5/weather?"

pencere=Tk()
pencere.geometry('800x500')
pencere.title("Hava Durumu Uygulaması")
pencere.config(bg="white")

sonuc1=Label(pencere,text="",bg="white",)
sonuc1.place(x=100,y=200)

sonuc2=Label(pencere,text="",bg="white",)
sonuc2.place(x=520,y=200)
Antalya=0
Istanbulsıcaklık2=0

def Antalya():
     global Antalya
     getWeather=requests.get(URL+f"q=Antalya&appid=0579d17c54ac1c305ac37e953cbd4e79&lang=tr&units=metric")
     data=getWeather.json()
     Antalya=data.get("main").get("temp")

     hissedilen=data.get("main").get("feels_like")
     havanasil2=data["weather"][0]["description"]
     sonuc1.config(text=f"Hava Antalya :{Antalya}C \nHissedilen :{hissedilen} \n Hava nasıl? {havanasil2}")



def Ist():
    global Istanbulsıcaklık2
    getWeather=requests.get(URL+f"q=Istanbul&appid=0579d17c54ac1c305ac37e953cbd4e79&lang=tr&units=metric")
    data=getWeather.json()
    Istanbulsıcaklık2=data.get("main").get("temp")

    hissedilen2=data.get("main").get("feels_like")
    havanasil=data["weather"][0]["description"]

    sonuc2.config(text=f"Hava İstanbulda :{Istanbulsıcaklık2}C \n Hissedilen :{hissedilen2}\n Hava nasıl?{havanasil}")
    karsilastir()
def karsilastir():
    if Istanbulsıcaklık2 > Antalya:
        yaz = Label(pencere, text="İstanbul Antalyadan sıcak")
        yaz.place(x=300, y=300, width=200, height=100)

    else:
        yaz2 = Label(pencere, text="Antalya İstanbuldan sıcak")
        yaz2.place(x=300, y=300, width=200, height=100)


Istanbulsıcaklıkb=Button(pencere,text="İstanbulun Sıcaklığı",command=Ist,fg="Red",font="Times 15 bold")

Istanbulsıcaklıkb.place(x=450,y=40,width=300,height=100)
cikis=Button(text="Çıkış",command=pencere.destroy)
cikis.place(width=50,height=50,x=380,y=400)

Antalyab=Button(pencere,text="Antalya sıcaklıgı",command=Antalya,fg="Red",font="times 15 bold")
Antalyab.place(x=40,y=40,width=300,height=100)


pencere.mainloop()

