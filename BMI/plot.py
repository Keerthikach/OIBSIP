import matplotlib.pyplot as plt 
from db import display_recs 

def bmi_graph(username):
    history=display_recs(username)
    if not  history:
        return 
    #extracting dates and bmi_values from the db
    dates=[rec[5] for rec in history] 
    bmi_val=[rec[4] for rec in history]

    plt.figure(figsize=(8,4))
    plt.plot(dates,bmi_val,marker='o',linestyle="-",color="b",label="BMI GRAPH") 
    plt.xlabel("Date")
    plt.ylabel("BMI")
    plt.title("BMI over TIME")
    plt.show() 
  



