'''
This function should return 2 values: 
- the BMI category (ex. "underweight") 
- the actual BMI value (ex. 22.86)

Reminders: 
- calculate bmi before returning outputs 
- add error checking for invalid input and unrealistic information
'''
def bmi_check(weight, height):
    # Add your code here
    # if not isinstance(weight, (float, int)):
    #     return ("invalid input")
    # elif (weight) <= 0:
    #     return ("invalid input")

    # if not isinstance(height, (float, int)):
    #     return ("invalid input")
    # elif (height) <= 0:
    #     return ("invalid input")
    if not isinstance(weight, (float, int)) or not isinstance(height, (float, int)):
        return "invalid input"
    if weight <= 0 or height <= 0:
        return "invalid input"

# BMI = weight in kg/(height in m)^2
    BMI = (weight) /((height)*(height))
    if (BMI < 10) or (BMI > 60):
        return "unrealistic information"
    elif BMI < 18.5:
        return "underweight", round(BMI, 1)
    
    elif (BMI >= 18.5) and (BMI < 25):
        return ("normal", round(BMI, 1))
    
    elif (BMI >= 25) and (BMI < 30):
        return ("overweight", round(BMI, 1))
    
    elif (BMI >= 30) and (BMI < 40):
        return ("obese", round(BMI, 1))
    elif (BMI >= 40):
        return ("extremely obese", round(BMI, 1))
    








    
