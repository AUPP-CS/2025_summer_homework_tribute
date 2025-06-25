'''
This function should return 2 values: 
- the BMI category (ex. "underweight") 
- the actual BMI value (ex. 22.86)

Reminders: 
- calculate bmi before returning outputs 
- add error checking for invalid input and unrealistic information
'''
def bmi_check(weight, height):
    try:
        weight = float(weight)
        height = float(height)

        bmi = round(float(weight) / float(height)**2, 1)

        if weight > 0 and height > 0:
            # Check if unrealistic info
            if weight > 635 or height > 2.72:
                return 'unrealistic information'

            # If realistic, calculate BMI
            if bmi < 18.5:
                return "underweight", bmi
            elif bmi >= 18.5 and bmi <= 24.9:
                return "normal", bmi
            elif bmi >=25 and bmi <= 29.9:
                return "overweight", bmi
            elif bmi >=30 and bmi <= 39.9:
                return "obese", bmi
            elif bmi > 40:
                return "extremely obese", bmi
            
        else: # If negative weight or height
            return 'invalid input'
        
    except: # If inputs are string
        return 'invalid input' 
    