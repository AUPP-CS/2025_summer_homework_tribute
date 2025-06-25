from bmi_calc import bmi_check

# Call the bmi_calc function and add in a user interface for the bmi calculator (ex. welcome message, instructions, etc.)

# Add your code here
print("\nWelcome to BMI Calculater 🧮")
print("Instructions:")
print("- Enter your name (in 1 word).")
print("- Enter your weight in kilograms (e.g., 70.5).")
print("- Enter your height in meters (e.g., 1.75).")
enter = input("Press enter for continue....")

while True:
    print("\n-----------------------------------------")
    
    try: 
        name = input("Please input your name: ")
        # check the name is a letter
        if not name.isalpha():
            print("Are you serious?, Name should only contain letters! 🤦")
            continue
            
        weight = input("Please enter your weight in kg: ")
        # chech the weight is a number
        try:
            weight = float(weight)
        except ValueError:
            print("Your weight should be a number in kg! 👍")
            continue
        
        height = input("Please input your height in meters: ")
        # chech the height is a number
        try:
            height = float(height)
        except ValueError:
            print("Your height should be a number in meter! 👍")
            continue
            
        print("-----------------------------------------")
        output = bmi_check(weight, height)
        # check the result
        try:
            result, bmi = output
            print(f"\nHello {name}")
            print(f"Your BMI is {bmi}.")
            print(f"You are {result}.")
        except (TypeError, ValueError):
            print(f"Error: {output}")
        print("-----------------------------------------")
    # finally:
    #     print("\nThank you for using our service!😊")
    
    # ask user to continue or not
        try:
            while True:
                option = input("\nDo you want to continue? (y/n): ").lower()
                print("-----------------------------------------")
                if option == 'y':
                    print("\nGreat! Let's continue... 🚀")
                    option = True
                    break
                elif option == 'n':
                    print("Alright, goodbye! 👋")
                    exit()
                else:
                    print(" Just enter Y or N. 🤦")
                print("-----------------------------------------")
        except KeyboardInterrupt:
            print("\nAlright, goodbye! 👋")
            print("-----------------------------------------")
            exit()   
        finally:
            print("\nThank you for using the BMI Calculator! 👋")   
    except KeyboardInterrupt:
        print(f'\n\nProgram terminated by user. {KeyboardInterrupt}')
        exit()
