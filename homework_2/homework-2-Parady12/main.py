from bmi_calc import bmi_check

# Call the bmi_calc function and add in a user interface for the bmi calculator (ex. welcome message, instructions, etc.)

# Add your code here

condition = True

print("\n" + "="*50)
print("                  BMI CONVERTER")
print("="*50)

while True:
    print("\nChoose your measurement system:")
    print(" [1] BMI in kg/m^2 (Kilograms, Meters)")
    print(" [0] Exit")
    print("-"*50)

    try:
      choice = input("Enter your choice (0-1): ")
      print("-"*50)

      if choice == "1":
          user_weight = input("Enter your weight in kilograms (kg): ")
          user_height = input("Enter your height in meters (m): ")

          result, bmi = bmi_check(user_weight, user_height) # type: ignore

          print("\n" + "="*50)
          print("                  BMI RESULT")
          print("="*50)

          if result != "invalid input" and result != "unrealistic information":
              print(f" Your result is: {result}")
              print(f" Your BMI is: {bmi}")
              condition = True
          elif result == "unrealistic information":
              print(f"Unrealistic information is captured! Weight should be <= 635 kg. Height should be <= 2.75 m")
              condition = False
          else:
              print("Unexpected value is inputed. Systems cannot calculate the BMI!")
              condition = False

      elif choice == "0":
          condition = False
          print("\nThank you for using the BMI Converter!")
          print("Goodbye!")
          print("="*50)
          break
      else:
          condition = False
          print("\nInvalid choice. Please enter 0, 1, or 2.")

      # Check if the calculation is succeeded
      if condition is True:
        print("\nCongratulation! You got your BMI.")
      else:
        print("\nSorry for your unsuccessful calculation. You can try again :)")

      # Ask user to retry
      retry = input("Do you want to try again? (Y/N): ")
      if retry.lower() == "n":
        print("\nThank you for using our BMI Converter!")
        break

    except KeyboardInterrupt:
        print("\nExiting the program...")
        break
  
