API_key1='b0487221ef54a092700f682bdc754376'
API_key2='d5df80fac38a0886af4dfe0de43178d2'
API_key3='b539194fdedea0df26fc43aec2ddb73b'
from tkinter import messagebox
import requests
import tkinter as tc
from tkinter import ttk
from tkinter import PhotoImage
def Current_Weather():
    e1=Entery1.get()
    e2=Entery2.get()
    weather=requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={e1}&appid={e2}')
    if e2==API_key1 or e2==API_key2 or e2==API_key3:
        lat_and_lon=weather.json()['coord']
        temp=weather.json()['main']['temp']
        pressure=weather.json()['main']['pressure']
        humidity=weather.json()['main']['humidity']
        wind=weather.json()['wind']
        country=weather.json()['sys']['country']
        sun_set=weather.json()['sys']['sunset']
        sky=weather.json()['weather'][0]['description']
        label59.config(text=sky)
        label19.config(text=country)
        label17.config(text=wind)
        label18.config(text=sun_set)
        label16.config(text=humidity)
        label15.config(text=pressure)
        label14.config(text=temp)
        label8.config(text=lat_and_lon)
        messagebox.showinfo('The operation was successful!','API successfully taken')
    else:
        messagebox.showerror('opps!','The API key is wrong')
def Air_Pollution():
    e1=Entery2.get()
    e2=Entery3.get()
    e3=Entery4.get()
    air=requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution?lat={e3}&lon={e2}&appid={e1}')
    if e1==API_key1 or e1==API_key2 or e1==API_key3:
        lat_and_lon=air.json()['coord']
        co=air.json()['list'][0]['components']['co']
        no=air.json()['list'][0]['components']['no']
        no2=air.json()['list'][0]['components']['no2']
        o3=air.json()['list'][0]['components']['o3']
        so2=air.json()['list'][0]['components']['so2']
        nh3=air.json()['list'][0]['components']['nh3']
        label20.config(text=lat_and_lon)
        label21.config(text=no)
        label22.config(text=co)
        label23.config(text=no2)
        label24.config(text=o3)
        label25.config(text=so2)
        label26.config(text=nh3)
        messagebox.showinfo('The operation was successful!', 'API successfully taken')
    else:
        messagebox.showerror('opps!', 'The API key is wrong')
def weather_forecast():
    e1=Entery1.get()
    e2=Entery2.get()
    five_day_weather=requests.get(f'http://api.openweathermap.org/data/2.5/forecast?q={e1}&appid={e2}')
    if e2==API_key1 or e2==API_key2 or e2==API_key3:
        forecast1=five_day_weather.json()['list'][5]['main']['temp']
        forecast2=five_day_weather.json()['list'][7]['main']['temp']
        forecast3=five_day_weather.json()['list'][9]['main']['temp']
        forecast4=five_day_weather.json()['list'][11]['main']['temp']
        forecast5=five_day_weather.json()['list'][5]['main']['pressure']
        forecast6=five_day_weather.json()['list'][7]['main']['pressure']
        forecast7=five_day_weather.json()['list'][9]['main']['pressure']
        forecast8=five_day_weather.json()['list'][11]['main']['pressure']
        forecast9=five_day_weather.json()['list'][5]['main']['humidity']
        forecast10=five_day_weather.json()['list'][7]['main']['humidity']
        forecast11=five_day_weather.json()['list'][9]['main']['humidity']
        forecast12=five_day_weather.json()['list'][11]['main']['humidity']
        forecast13=five_day_weather.json()['list'][5]['wind']['speed']
        forecast14=five_day_weather.json()['list'][7]['wind']['speed']
        forecast15=five_day_weather.json()['list'][9]['wind']['speed']
        forecast16=five_day_weather.json()['list'][11]['wind']['speed']
        label27.config(text=forecast1)
        label28.config(text=forecast2)
        label29.config(text=forecast3)
        label30.config(text=forecast4)
        label31.config(text=forecast5)
        label32.config(text=forecast6)
        label33.config(text=forecast7)
        label34.config(text=forecast8)
        label35.config(text=forecast9)
        label36.config(text=forecast10)
        label37.config(text=forecast11)
        label38.config(text=forecast12)
        label39.config(text=forecast13)
        label40.config(text=forecast14)
        label41.config(text=forecast15)
        label42.config(text=forecast16)
        messagebox.showinfo('The operation was successful!', 'API successfully taken')
    else:
        messagebox.showerror('opps!', 'The API key is wrong')
def Forecast_air_pollution_data():
    e1=Entery4.get()
    e2=Entery3.get()
    e3=Entery2.get()
    forecast_air=requests.get(f'http://api.openweathermap.org/data/2.5/air_pollution/forecast?lat={e1}&lon={e2}&appid={e3}')
    if e3==API_key1 or e3==API_key2 or e3==API_key3:
        Co_forecast1=forecast_air.json()['list'][10]['components']['co']
        Co_forecast2=forecast_air.json()['list'][16]['components']['co']
        Co_forecast3=forecast_air.json()['list'][22]['components']['co']
        Co_forecast4=forecast_air.json()['list'][28]['components']['co']
        No_forecast1=forecast_air.json()['list'][10]['components']['no']
        No_forecast2=forecast_air.json()['list'][16]['components']['no']
        No_forecast3=forecast_air.json()['list'][22]['components']['no']
        No_forecast4=forecast_air.json()['list'][28]['components']['no']
        O3_forecast1=forecast_air.json()['list'][10]['components']['o3']
        O3_forecast2=forecast_air.json()['list'][16]['components']['o3']
        O3_forecast3=forecast_air.json()['list'][22]['components']['o3']
        O3_forecast4=forecast_air.json()['list'][28]['components']['o3']
        So2_forecast1=forecast_air.json()['list'][10]['components']['so2']
        So2_forecast2=forecast_air.json()['list'][16]['components']['so2']
        So2_forecast3=forecast_air.json()['list'][22]['components']['so2']
        So2_forecast4=forecast_air.json()['list'][28]['components']['so2']
        label43.config(text=Co_forecast1)
        label44.config(text=Co_forecast2)
        label45.config(text=Co_forecast3)
        label46.config(text=Co_forecast4)
        label47.config(text=No_forecast1)
        label48.config(text=No_forecast2)
        label49.config(text=No_forecast3)
        label50.config(text=No_forecast4)
        label51.config(text=O3_forecast1)
        label52.config(text=O3_forecast2)
        label53.config(text=O3_forecast3)
        label54.config(text=O3_forecast4)
        label55.config(text=So2_forecast1)
        label56.config(text=So2_forecast2)
        label57.config(text=So2_forecast3)
        label58.config(text=So2_forecast4)
        messagebox.showinfo('The operation was successful!','API successfully taken')
    else:
        messagebox.showerror('opps!', 'The API key is wrong')
def Exit():
    if messagebox.askyesno('Exit','Do you want to Exit?'):
        root.destroy()
root=tc.Tk()
image_patch=r"C:\Users\USER\Pictures\18312178_web1_Mainly-sunny.png"
image_bg=PhotoImage(file=image_patch)
set_image_bg=tc.Label(root,image=image_bg)
set_image_bg.pack()
root.geometry('850x700')
root.title('Weather information')
root.config(cursor='target')
new_window=ttk.Notebook(root)
tab1=tc.Frame(root,width=600,height=120)
tab2=tc.Frame(root,width=600,height=120)
tab3=tc.Frame(root,width=600,height=120)
tab4=tc.Frame(root,width=600,height=120)
new_window.add(tab1,text='Current Weather Data')
new_window.add(tab2,text='Air Pollution Data')
new_window.add(tab3,text='Weather forecast')
new_window.add(tab4,text='Air Pollution forecast')
tab1.config(bg='deepskyblue')
tab2.config(bg='fuchsia')
tab3.config(bg='tan')
tab4.config(bg='darkorange')
new_window.place(x=200,y=399)
label1=tc.Label(root,text='Welcome to the weather information app',font='Helvetica',bg='cyan')
label1.place(x=200,y=1)
label2=tc.Label(root,text='Enter The City Name,API key,Lon and Lat to get Data',font='Verdana 11 bold',bg='light yellow',fg='green')
label2.place(x=160,y=30)
label3=tc.Label(root,text='City Name:',bg='red')
label3.place(x=255,y=55)
label4=tc.Label(root,text='API key:',bg='red')
label4.place(x=270,y=78)
label5=tc.Label(root,text='Longitude:',bg='red')
label5.place(x=259,y=100)
label6=tc.Label(root,text='Latitude:',bg='red')
label6.place(x=267,y=123)
label7=tc.Label(root,text='If you dont know how to get latitude and longitude, go to this site: https://www.maps.ie/coordinates.html',font='Helvetica',fg='blue',bg='tomato')
label7.place(x=1,y=350)
label8=tc.Label(tab1,text='lat & lon:')
label8.place(x=-30,y=-30)
label13=tc.Label(root,text='If you dont know how to get start and end data,go to this site: https://www.unixtimestamp.com',font='Helvetica',bg='tomato',fg='blue')
label13.place(y=320,x=1)
label14=tc.Label(tab1,text='temp:')
label14.place(x=-3,y=0)
label15=tc.Label(tab1,text='pressure:')
label15.place(x=-3,y=23)
label16=tc.Label(tab1,text='humidity:')
label16.place(x=-3,y=45)
label17=tc.Label(tab1,text='wind:')
label17.place(x=-3,y=67)
label18=tc.Label(tab1,text='sunset:')
label18.place(x=-3,y=89)
label19=tc.Label(tab1,text='country:')
label19.place(x=70,y=0)
label20=tc.Label(tab2,text='lat & lon:')
label20.place(x=-3,y=0)
label21=tc.Label(tab2,text='nobelium (No):')
label21.place(x=-3,y=23)
label22=tc.Label(tab2,text='Cobalt (Co):')
label22.place(x=-3,y=45)
label23=tc.Label(tab2,text='Nitrogen dioxide (No2):')
label23.place(x=-3,y=67)
label24=tc.Label(tab2,text='Ozone (O3):')
label24.place(x=-3,y=89)
label25=tc.Label(tab2,text='Sulfur dioxide (So2):')
label25.place(x=150,y=0)
label26=tc.Label(tab2,text='nitrogen and hydrogen (Nh3):')
label26.place(x=110,y=23)
label27=tc.Label(tab3,text='Tomorrow Temp at 00:00:00:')
label27.place(x=-3,y=0)
label28=tc.Label(tab3,text='Tomorrow Temp at 06:00:00:')
label28.place(x=-3,y=23)
label29=tc.Label(tab3,text='Tomorrow Temp at 12:00:00:')
label29.place(x=-3,y=45)
label30=tc.Label(tab3,text='Tomorrow Temp at 18:00:00:')
label30.place(x=-3,y=67)
label31=tc.Label(tab3,text='Tomorrow Pressure at 00:00:00:')
label31.place(x=-3,y=89)
label32=tc.Label(tab3,text='Tomorrow Pressure at 06:00:00:')
label32.place(x=150,y=0)
label33=tc.Label(tab3,text='Tomorrow Pressure at 12:00:00:')
label33.place(x=150,y=23)
label34=tc.Label(tab3,text='Tomorrow Pressure at 18:00:00:')
label34.place(x=150,y=45)
label35=tc.Label(tab3,text='Tomorrow Humidity at 00:00:00:')
label35.place(x=150,y=67)
label36=tc.Label(tab3,text='Tomorrow Humidity at 06:00:00:')
label36.place(x=167,y=89)
label37=tc.Label(tab3,text='Tomorrow Humidity at 12:00:00:')
label37.place(x=320,y=0)
label38=tc.Label(tab3,text='Tomorrow Humidity at 18:00:00:')
label38.place(x=320,y=23)
label39=tc.Label(tab3,text='Tomorrow Wind Speed at 00:00:00:')
label39.place(x=320,y=45)
label40=tc.Label(tab3,text='Tomorrow Wind Speed at 06:00:00:')
label40.place(x=326,y=67)
label41=tc.Label(tab3,text='Tomorrow Wind Speed at 12:00:00:')
label41.place(x=343,y=89)
label42=tc.Label(tab3,text='Tomorrow Wind Speed at 18:00:00:')
label42.place(x=496,y=0)
label43=tc.Label(tab4,text='Tomorrow Co at 00:00:00:')
label43.place(x=-3,y=0)
label44=tc.Label(tab4,text='Tomorrow Co at 06:00:00:')
label44.place(x=-3,y=20)
label45=tc.Label(tab4,text='Tomorrow Co at 12:00:00:')
label45.place(x=-3,y=40)
label46=tc.Label(tab4,text='Tomorrow Co at 18:00:00:')
label46.place(x=-3,y=60)
label47=tc.Label(tab4,text='Tomorrow No at 00:00:00:')
label47.place(x=-3,y=80)
label48=tc.Label(tab4,text='Tomorrow No at 06:00:00:')
label48.place(x=-3,y=100)
label49=tc.Label(tab4,text='Tomorrow No at 12:00:00:')
label49.place(x=140,y=0)
label50=tc.Label(tab4,text='Tomorrow No at 18:00:00:')
label50.place(x=140,y=20)
label51=tc.Label(tab4,text='Tomorrow O3 at 00:00:00:')
label51.place(x=140,y=40)
label52=tc.Label(tab4,text='Tomorrow O3 at 06:00:00:')
label52.place(x=140,y=60)
label53=tc.Label(tab4,text='Tomorrow O3 at 12:00:00:')
label53.place(x=140,y=80)
label54=tc.Label(tab4,text='Tomorrow O3 at 18:00:00:')
label54.place(x=140,y=100)
label55=tc.Label(tab4,text='Tomorrow So2 at 00:00:00:')
label55.place(x=285,y=0)
label56=tc.Label(tab4,text='Tomorrow So2 at 06:00:00:')
label56.place(x=285,y=20)
label57=tc.Label(tab4,text='Tomorrow So2 at 12:00:00:')
label57.place(x=285,y=40)
label58=tc.Label(tab4,text='Tomorrow So2 at 18:00:00:')
label58.place(x=285,y=60)
label59=tc.Label(tab1,text='The state of the sky:')
label59.place(x=70,y=23)
#labels
Entery1=tc.Entry(root)
Entery1.place(x=320,y=55)
Entery2=tc.Entry(root)
Entery2.place(x=320,y=78)
Entery3=tc.Entry(root)
Entery3.place(x=320,y=100)
Entery4=tc.Entry(root)
Entery4.place(x=320,y=123)
#enterys
Button1=tc.Button(root,text='pls enter city name and API key for Current Weather',command=Current_Weather,bg='yellow')
Button1.place(x=230,y=180)
Button2=tc.Button(root,text='pls enter API key,lat,lon for Current air Pollution',command=Air_Pollution,bg='light blue')
Button2.place(x=400,y=210)
Button3=tc.Button(root,text='pls enter city name and API key for Tomorrow weather forecast',command=weather_forecast,bg='mediumslateblue')
Button3.place(x=50,y=210)
Button4=tc.Button(root,text='pls enter lat,lon and APIkey for Tomorrow air Pollution',command=Forecast_air_pollution_data,bg='violet')
Button4.place(x=240,y=237)
Button5=tc.Button(root,text='click for exit',command=Exit,bg='crimson')
Button5.place(x=0,y=380)
#buttons
root.mainloop()