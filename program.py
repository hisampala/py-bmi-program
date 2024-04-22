import math

def calculate_bmi(weight:float,height:float):
    return (weight/(math.pow(height / 100,2)))

def display_result(bmi:float):
    display:str
    if bmi > 40:
        display  = 'อ้วนขั้นสูงสุด' 
    elif bmi >= 35: 
        display  = 'อ้วนขั้นที่ 2'
    elif bmi >= 28.5:
        display  = 'อ้วนขั้นที่ 1'
    elif bmi >= 23.5:
        display  = 'น้ำหนักเกิน'
    elif bmi >= 18.5:
        display  = 'อยู่ในเกณฑ์ปกติ'
    else:
        display  = 'น้ำหนักต่ำกว่าเกณฑ์'
    return display

weight = float(input("น้ำหนัก(กิโลกรัม) :"))
height = float(input("ส่วนสูง(เซนติเมตร) :"))
bmi:float = calculate_bmi(weight,height)

print("ค่า BMI คือ:%s" % format(bmi , '.2f'))
print("ลักษณะรูปร่างคือ:%s" % display_result(bmi))