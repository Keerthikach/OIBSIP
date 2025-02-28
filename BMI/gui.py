from calculate_bmi import cal_bmi 
import tkinter as tk 
from db import add_recs
from plot import bmi_graph 

def check_bmi():
    name=name_entry.get()
    try:
        weight=float(weight_entry.get()) 
        height=float(height_entry.get())
        bmi,category=cal_bmi(weight,height)
        result_label.config(text=f" Your BMI is : {round(bmi,2)}\n You fall under the category of {category}") 
    except ValueError:
        result_label.config(text="Please Enter valid numbers")   

    add_recs(name,weight,height,bmi)    

#GUI Setup 
root=tk.Tk()    #creating window 
root.title("BMI Calculator") 
root.geometry("300x250")   

#name entry 
tk.Label(root,text="Enter your name ").pack() 
name_entry=tk.Entry(root) 
name_entry.pack() 

#weight entry
tk.Label(root,text="Enter your weight in kgs: ").pack()
weight_entry=tk.Entry(root) 
weight_entry.pack() 

#height entry
tk.Label(root,text="Enter height in m's: ").pack()
height_entry=tk.Entry(root)
height_entry.pack() 

#calculate button 
tk.Button(root,text="Calculate BMI",command=check_bmi).pack()  
tk.Button(root, text="Show Trends", command=lambda: bmi_graph(name_entry.get())).pack()


#result label
result_label=tk.Label(root,text="Your BMI is: ")
result_label.pack() 

#run application
root.mainloop()  




