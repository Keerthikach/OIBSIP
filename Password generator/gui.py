import tkinter as tk
import generator as gn 

def gen_pass():
    w1=length_entry.get()
    try:
        a=gn.rand(int(w1),u1.get(),s1.get(),n1.get()) 
        result_label.config(text=f"Your password is: {a}") 
    except ValueError:
        result_label.config(text="Invalid literal") 

#creating window
root=tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400") 

#length entry 
tk.Label(root,text="Required length").pack()
length_entry=tk.Entry(root)
length_entry.pack() 

#checkbox for constraints 
u1=tk.IntVar()
n1=tk.IntVar()
s1=tk.IntVar()

tk.Checkbutton(root,text="Uppercase",variable=u1).pack()
tk.Checkbutton(root,text="Number",variable=n1).pack()
tk.Checkbutton(root,text="Symbol",variable=s1).pack() 

#button 

tk.Button(root,text="Generate Password",command=gen_pass).pack() 
result_label=tk.Label(root,text="Your password is:")
result_label.pack()
 

root.mainloop() 



