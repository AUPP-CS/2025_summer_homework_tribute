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
    
    try:
    # input error 
    # weight or height <=0
        if weight <= 0 or height <= 0:
            return 'invalid input'
        if weight > 630 or height > 2.5:
            return 'unrealistic information'
           
    
    # calculate BMI
        BMI = weight /(height ** 2)
        if BMI < 18.5:
            result = 'underweight'
        elif BMI >= 18.5 and BMI <= 24.9:
            result = 'normal'
        elif BMI >= 25 and BMI <= 29.9:
            result = 'overweight'
        elif BMI >= 30 and BMI <= 39.9:
            result = 'obese'
        else:
            result = 'extremely obese'
            
        # 1 dicimal number    
        return result, round(BMI, 1)
    
    except ValueError:
        return 'invalid input'
    # finally:
    #      print("\nThank you for using our service!😊")
    
    
        
            
            

