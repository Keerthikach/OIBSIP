def cal_bmi(weight,height):
    if weight<=0 or height<=0:
        return "invalid","invalid"
    
    bmi=weight/(height**2)

    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 24.9:
        category = "Normal weight"
    elif 25 <= bmi < 29.9:
        category = "Overweight"
    else:
        category = "Obese"

    return bmi,category           




