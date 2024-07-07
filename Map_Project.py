import tkintermapview as tm
import customtkinter as ct
import tkinter as tk
from tkinter import messagebox
import requests
import sqlite3
marker_list=[]
class map:
    def __init__(self, window):
        self.window = window
        self.window.title('Map_Program')
        self.window.geometry('700x700')
        image_patch1 =r"C:\Users\USER\Desktop\پروژه\map.png"
        image_bg1 = tk.PhotoImage(file=image_patch1)
        Label1 = ct.CTkLabel(self.window, image=image_bg1)
        Label1.pack()
        Label2 = ct.CTkLabel(self.window, text='welcome to map program/made by sina', font=('Helvetica', 20),
                             text_color='#51d6a1', bg_color='black')
        Label2.place(x=150, y=0)
        Label4 = ct.CTkLabel(self.window, text='please enter Latitude:', text_color='#51e0ba')
        Label4.place(x=0, y=130)
        Label5 = ct.CTkLabel(self.window, text='please enter Longitude:', text_color='#51e0ba')
        Label5.place(x=0, y=160)
        global Label7
        Label7=ct.CTkLabel(self.window,text='result of Longitude:',text_color='#ff3d51', font=('Georgia', 20),bg_color='#141e52')
        Label7.place(x=0,y=340)
        global Label9
        Label9=ct.CTkLabel(self.window,text='result of Latitude:',text_color='#ff3d51', font=('Georgia', 20),bg_color='#141e52')
        Label9.place(x=0,y=370)
        Label10 = ct.CTkLabel(self.window, text='if you have lat&lon and need city name enter them',
                              font=('Times New Roman', 18), bg_color='black', text_color='#db2531')
        Label10.place(x=0, y=100)
        global Label11
        Label11 = ct.CTkLabel(self.window, text='result of city name:', text_color='#ff3d51', font=('Georgia', 20),
                              bg_color='#141e52')
        Label11.place(x=0, y=310)
        Label12 = ct.CTkLabel(self.window,
                              text='Please enter the latitude and longitude of the origin and destination of the route',
                              font=('Helvetica', 14), text_color='#43d938', bg_color='#010363')
        Label12.place(x=0, y=75)
        Label13 = ct.CTkLabel(self.window, text='Please enter lat and lon of origin:', text_color='#1fe0e0')
        Label13.place(x=244, y=190)
        Label14 = ct.CTkLabel(self.window, text='Please enter lat and lon of destination:', text_color='#1fe0e0')
        Label14.place(x=210, y=220)
        Label15=ct.CTkLabel(self.window,text='If you want to find the latitude and longitude of a place, enter the address',text_color='#b722e0',bg_color='black')
        Label15.place(x=400,y=100)
        global Label16
        Label16=ct.CTkLabel(self.window,text='result of Distance from origin to destination:',text_color='#3de346',bg_color='#141e52')
        Label16.place(x=400,y=300)
        global Label17
        Label17=ct.CTkLabel(self.window,text='result of The duration of the distance:',text_color='#3de346',bg_color='#141e52')
        Label17.place(x=400,y=330)
        global Label18
        Label18=ct.CTkLabel(self.window,text='Summary from origin to destination',text_color='#3de346',bg_color='#141e52')
        Label18.place(x=400,y=360)
        Button3 = ct.CTkButton(self.window, text='click here to find city name',
                               command=self.Convert_location_toaddress, text_color='#fc7323')
        Button3.place(x=30, y=580)
        Button4 = ct.CTkButton(self.window, text='click here to work with map', command=self.showing_Map,
                               text_color='#fc7323')
        Button4.place(x=200, y=580)
        Button5 = ct.CTkButton(self.window, text='click here for exit', command=self.close_page, text_color='#fc7323')
        Button5.place(x=370, y=580)
        Button6 = ct.CTkButton(self.window, text='click here for routing', command=self.Routing_Car_Motorcycle,
                               text_color='#fc7323')
        Button6.place(x=510, y=580)
        Button7=ct.CTkButton(self.window,text='click here to find lat and lon',command=self.Convert_address_tolocation,text_color='#fc7323')
        Button7.place(x=350,y=550)
        Button8=ct.CTkButton(self.window,text='click here to Draw an arc between origin and destination',command=self.map_image,text_color='#fc7323')
        Button8.place(x=0,y=550)
        global Entery1, Entery2, Entery3, Entery4, Entery5
        Entery1=ct.CTkEntry(self.window)
        Entery1.place(x=500,y=140)
        Entery2 = ct.CTkEntry(self.window)
        Entery2.place(x=160, y=130)
        Entery3 = ct.CTkEntry(self.window)
        Entery3.place(x=160, y=160)
        Entery4 = ct.CTkEntry(self.window)
        Entery4.place(x=430, y=190)
        Entery5 = ct.CTkEntry(self.window)
        Entery5.place(x=430, y=220)
    def search_api(self):
        title=Entery1.get()
        lat=Entery5.get()
        lon=Entery6.get()
        headers = {'Api-Key': 'service.ffeec211c7284553873970b5350b1aa7'}
        api=f'https://api.neshan.org/v1/search?term={title}&lat={lat}&lng={lon}'
        data=requests.get(api,headers=headers)
        global result3
        result3=data.json()
        title1=result3['items'][0]['title']
        address1=result3['items'][0]['address']
        job1=result3['items'][0]['type']
        title2=result3['items'][1]['title']
        address2=result3['items'][1]['address']
        job2=result3['items'][1]['type']
        title3=result3['items'][2]['title']
        address3=result3['items'][2]['address']
        job3=result3['items'][2]['type']
        Label14.configure(text=title1)
        Label15.configure(text=address1)
        Label16.configure(text=job1)
        Label17.configure(text=title2)
        Label18.configure(text=address2)
        Label19.configure(text=job2)
        Label20.configure(text=title3)
        Label21.configure(text=address3)
        Label22.configure(text=job3)
    def Convert_address_tolocation(self):
        headers = {'Api-Key': 'service.ffeec211c7284553873970b5350b1aa7'}
        add = Entery1.get()
        api = f'https://api.neshan.org/v4/geocoding?address={add}'
        data=requests.get(api,headers=headers)
        global result2
        result2=data.json()
        x_data = result2['location']['x']
        y_data = result2['location']['y']
        Label7.configure(text=x_data)
        Label9.configure(text=y_data)
    def Routing_Car_Motorcycle(self):
        headers = {'Api-Key': 'service.ffeec211c7284553873970b5350b1aa7'}
        start=Entery4.get()
        end=Entery5.get()
        api=f'https://api.neshan.org/v4/direction?parameters&origin={start}&destination={end}'
        data=requests.get(api,headers=headers)
        result=data.json()
        summary = result['routes'][0]['legs'][0]['summary']
        distance=result['routes'][0]['legs'][0]['distance']['text']
        duration=result['routes'][0]['legs'][0]['duration']['text']
        Label16.configure(text=distance)
        Label17.configure(text=duration)
        Label18.configure(text=summary)
    def Convert_location_toaddress(self):
        lat=Entery2.get()
        lon=Entery3.get()
        headers = {'Api-Key': 'service.ffeec211c7284553873970b5350b1aa7'}
        api=f'https://api.neshan.org/v5/reverse?lat={lat}&lng={lon}'
        data=requests.get(api,headers=headers)
        global result1
        result1=data.json()
        city_name=result1['city']
        Label11.configure(text=city_name)
    def showing_Map(self):
        global Top_Level
        self.Top_Level = tk.Toplevel(self.window)
        global Map
        Map = tm.TkinterMapView(self.Top_Level, width=700, height=700)
        self.Top_Level.geometry('900x900')
        self.Top_Level.title('Map')
        self.Top_Level.configure(bg='black')
        Map.set_zoom(12)
        Map.set_position(35.6892523,51.3896004)
        frame=ct.CTkFrame(self.Top_Level,width=200,height=200)
        frame.pack(side='left',fill='y')
        Label3=ct.CTkLabel(self.Top_Level,text='If you want To search street names, old names, places enter city name&lat&lon',font=('Georgia',17),text_color='#93f514',bg_color='black')
        Label3.pack(side='top')
        Label6=ct.CTkLabel(self.Top_Level,text='please enter city name:',text_color='#1aebd2')
        Label6.place(x=0,y=0)
        Label12=ct.CTkLabel(self.Top_Level,text='please enter Latitude:',text_color='#1aebd2')
        Label12.place(x=0,y=60)
        Label13=ct.CTkLabel(self.Top_Level,text='please enter Longitude:',text_color='#1aebd2')
        Label13.place(x=0,y=120)
        global Label14
        Label14=ct.CTkLabel(self.Top_Level,text='result of place name1:',font=('Comic Sans',16),text_color='#7a2feb')
        Label14.place(x=0,y=180)
        global Label15
        Label15=ct.CTkLabel(self.Top_Level,text='result of place address1:',font=('Comic Sans',16),text_color='#7a2feb')
        Label15.place(x=0,y=210)
        global Label16
        Label16=ct.CTkLabel(self.Top_Level,text='result of place job1:',font=('Comic Sans',16),text_color='#7a2feb')
        Label16.place(x=0,y=240)
        global Label17
        Label17=ct.CTkLabel(self.Top_Level,text='result of place name2:',font=('Comic Sans',16),text_color='#d7de1d')
        Label17.place(x=0,y=270)
        global Label18
        Label18=ct.CTkLabel(self.Top_Level,text='result of place address2:',font=('Comic Sans',16),text_color='#d7de1d')
        Label18.place(x=0,y=300)
        global Label19
        Label19=ct.CTkLabel(self.Top_Level,text='result of place job2:',font=('Comic Sans',16),text_color='#d7de1d')
        Label19.place(x=0,y=330)
        global Label20
        Label20=ct.CTkLabel(self.Top_Level,text='result of place name3:',font=('Comic Sans',16),text_color='#21c91e')
        Label20.place(x=0,y=360)
        global Label21
        Label21=ct.CTkLabel(self.Top_Level,text='result of place address3:',font=('Comic Sans',16),text_color='#21c91e')
        Label21.place(x=0,y=390)
        global Label22
        Label22=ct.CTkLabel(self.Top_Level,text='result of place job3:',font=('Comic Sans',16),text_color='#21c91e')
        Label22.place(x=0,y=420)
        Label23=ct.CTkLabel(self.Top_Level,text='If you looking for any place in the world,\nenter the address and we show you!',font=('Comic Sans',14),text_color='#02f7ef')
        Label23.place(x=0,y=560)
        global Entery1
        Entery1=ct.CTkEntry(self.Top_Level)
        Entery1.place(x=50,y=30)
        global Entery5
        Entery5=ct.CTkEntry(self.Top_Level)
        Entery5.place(x=50,y=90)
        global Entery6
        Entery6=ct.CTkEntry(self.Top_Level)
        Entery6.place(x=50,y=150)
        global Entery7
        Entery7 = ct.CTkEntry(self.Top_Level)
        Entery7.place(x=50, y=600)
        Button1=ct.CTkButton(self.Top_Level,text='click here to search places',text_color='#f53131',command=self.search_api)
        Button1.place(x=0,y=650)
        Button2=ct.CTkButton(self.Top_Level,text='Enter the address you are looking for',command=self.search_Map,text_color='#f53131')
        Button2.place(x=0,y=690)
        Button3=ct.CTkButton(self.Top_Level,text='click to add two marker',command=self.add_marker,text_color='#f53131')
        Button3.place(x=0,y=530)
        Button4=ct.CTkButton(self.Top_Level,text='click here to destroy all markers',command=self.clear_marker,text_color='#f53131')
        Button4.place(x=0,y=500)
        Map.pack()
    def search_Map(self):
        Map.set_address(Entery7.get())
    def add_marker(self):
        get_position=Map.get_position()
        marker_list.append(Map.set_marker(get_position[0],get_position[1]))
    def clear_marker(self):
        for marke in marker_list:
            marke.delete()
        messagebox.showinfo('Done.','Markers Successfully Deleted')
    def close_page(self):
        if messagebox.askyesno('Exit.','are you sure you want close the window?'):
            self.window.destroy()
    def map_image(self):
        global Top_level
        self.Top_level=tk.Toplevel(self.window)
        self.Top_level.geometry('500x500')
        self.Top_level.configure(bg='black')
        global Entery6,Entery7,Entery8,Entery9,Entery10,Entery11
        Entery6 = ct.CTkEntry(self.Top_level)
        Entery6.pack()
        Entery7 = ct.CTkEntry(self.Top_level)
        Entery7.pack()
        Entery8 = ct.CTkEntry(self.Top_level)
        Entery8.pack()
        Entery9 = ct.CTkEntry(self.Top_level)
        Entery9.pack()
        Entery10 = ct.CTkEntry(self.Top_level)
        Entery10.pack()
        Label1=ct.CTkLabel(self.Top_level,text='please enter the model of bg image',text_color='lime')
        Label2=ct.CTkLabel(self.Top_level,text='enter the origin lat and lon',text_color='lime')
        Label3=ct.CTkLabel(self.Top_level,text='enter the destination lat and lon',text_color='lime')
        Label4=ct.CTkLabel(self.Top_level,text='enter the width size',text_color='lime')
        Label5=ct.CTkLabel(self.Top_level,text='enter the height size',text_color='lime')
        Label1.place(x=0,y=0)
        Label2.place(x=0,y=30)
        Label3.place(x=0,y=60)
        Label4.place(x=0,y=90)
        Label5.place(x=0,y=120)
        Button=ct.CTkButton(self.Top_level,command=self.get_image,text='click here to creat')
        Button.pack(side='bottom')
    def get_image(self):
        bg = Entery6.get()
        start = Entery7.get()
        end = Entery8.get()
        wi = Entery9.get()
        he = Entery10.get()
        url = f'https://api.neshan.org/v4/static/arc?key=service.ffeec211c7284553873970b5350b1aa7&type={bg}&from={start}&to={end}&width={wi}&height={he}&dashed=true&color=%23FF0AA5&marker1Token=181511.p07dDfSD&marker2Token=461510.QTb8T17o'
        response = requests.get(url)
        if response.status_code == 200:
            with open("map_image.png", "wb") as file:
                file.write(response.content)
            print("Map image has been saved as map_image.png")
        else:
            print(f"Failed to retrieve data: {response.status_code}")
    def save_sql(self,city_name,lat,lon):
        self.connect=sqlite3.connect('Map_data.db')
        self.cursor=self.connect.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS Map(city_name TEXT PRIMARY KEY ,longitude REAL,latitude REAL)')
        try:
            self.cursor.execute("INSERT INTO Map (city_name, longitude, latitude) VALUES (?, ?, ?)",
                                (city_name, lon, lat))
            self.connect.commit()
            self.connect.close()
        except sqlite3.IntegrityError:
            messagebox.showwarning("Warning", f"{city_name} already exists in the database.")
if __name__=="__main__":
    window = ct.CTk()
    obj = map(window)
    window.mainloop()