import requests as rq
import tkinter as tk 
from tkinter import messagebox 

my_api="eb311e26340c3f3fceb02995d9be23e1"

def get_weather():
    city=city_entry.get()

    if not city:
        messagebox.showerror("Error","Please enter your city") 
        return 
    
    url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={my_api}&units=metric"
    response=rq.get(url) 

    
    if response.status_code==200:
        text_data=response.text 

        #extract temperature 
        temp_index=text_data.find('"temp":')
        temp_str=text_data[temp_index+7:text_data.find(',',temp_index)]

        #weather description 
        desc_index=text_data.find('"description":') 
        desc_str=text_data[desc_index+14:text_data.find(',',desc_index)]  

        #weather_label 
        weather_label.config(text=f"City:{city} \n temperature:{temp_str} \n description:{desc_str}") 
    else:
        messagebox.showerror("Error","City not found!")     
        

#create window 
root=tk.Tk() 
root.title("Today's Weather") 
root.geometry("400x400") 

#entry part 
tk.Label(root,text="Enter your city name").pack()
city_entry=tk.Entry(root,width=20)
city_entry.pack()

#button 
search=tk.Button(root,text="Get weather",command=get_weather)
search.pack() 

#weather label
weather_label=tk.Label(root,text="",font=("Helvetika",12)) 
weather_label.pack()

root.mainloop() 





