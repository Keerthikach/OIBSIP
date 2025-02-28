import secrets 
import string 

def rand(length=8,upr=True,sym=True,num=True):
    accepted=string.ascii_lowercase
    if upr:
        accepted+=string.ascii_uppercase
    if sym:
        accepted+="@#$*&_-~" 
    if num:
        accepted+=string.digits 
    password=''.join(secrets.choice(accepted) for i in range(length))     
    return  password        
print(rand()) 

