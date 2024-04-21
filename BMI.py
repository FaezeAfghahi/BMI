
"""
BMI
Body Mass Index (BMI)
The formula for BMI is weight in kilograms divided by height in meters squared. 

"""

W = int(input("pleaseenter your weight(kg)="))
L = float(input("pleaseenter your length(m)="))
BMI = W/L**2
print ("your BMI is ", BMI)
if BMI <= 18.5:
    w_normal_1 = 18.5 * (L**2)
    Add = w_normal_1 - W
    print("you are underweight, you must add ",Add,"(kg)")
elif 18.5 <= BMI <= 25:
    print("you are normal")
elif 25 <= BMI <= 30:
    w_normal_2 = 25 * (L**2)
    lose = W - w_normal_2
    print("you are overweight,you must lose ",lose,"(kg)")
elif  BMI >= 30:
    w_normal_2 = 25 * (L**2)
    lose = W - w_normal_2
    print("you are obese,you must lose ",lose,"(kg)")
