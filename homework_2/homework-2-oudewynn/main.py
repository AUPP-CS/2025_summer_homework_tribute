from bmi_calc import bmi_check
Loop = True

print("Welcome to the BMI Calculator!")

print("╔════════════════════════════════════════════════╗")
print("║           🧮 BMI CALCULATOR 3000 🧮            ║")
print("║      Calculate your Body Mass Index (BMI)      ║")
print("║    Find out if you're underweight, normal,     ║")
print("║       overweight, obese, or extremely obese    ║")
print("╚════════════════════════════════════════════════╝\n")
import time
time.sleep(1)  # Adds a cool pause effect


# Call the bmi_calc function and add in a user interface for the bmi calculator (ex. welcome message, instructions, etc.)
while Loop:
# Add your code here
    try:
        name = input("👤 Please put in your name:\n ")
        weight = float(input("⚖️  Please input your weight as kg:\n "))
        height = float(input("📏  Please input your height as meters:\n "))
        BMI_calc = bmi_check(weight, height)
        word, num = BMI_calc

        
    except ValueError as Error:
        print ("❌ Invalid input please try again\n Perhap maybe misclick some information?\n ")
        continue

    except KeyboardInterrupt:
        print("⚠️ Keyboard Interrupt detected!")
        continue #this is for when the info input is wrong from instruction it will skip the rest and go backk to the top learn it from AI

    print ("🕒 The program is loading please wait for a momment...!")
    import time
    time.sleep(2)
    
    input("Press enter to continue:\n ")
    
    # print(f"Hello {name}, You are {word} and your BMI result is {num}\n")
    print(f"🎉 Awesome, {name}! Based on your input:")
    print(f"📊 Your BMI is **{round(num, 1)}**, which means you are **{word.upper()}**.")
    print("💡 Remember, this is just a tool — always consult a health professional for full guidance!")
    print("🏃‍♂️ Stay active, eat well, and keep crushing it! 💪\n\n")

    continue_yes_no = input("Do you wish to continue? \n Press Yes to continue, Press No to stop \n Yes/No:\n")

    if continue_yes_no.lower() != "yes":
        if "No":   
            import time

            print("\n✨ Wrapping things up... please wait...\n")
            time.sleep(1.5)

            print("╔══════════════════════════════════════════════════╗")
            print("║                                                  ║")
            print("║     ✅ THANK YOU FOR USING BMI CALCULATOR 3000!  ║")
            print("║                                                  ║")
            print("║  Stay healthy, stay strong, and stay awesome! 💪 ║")
            print("║     Remember: Your health is your true wealth! 💎║")
            print("║                                                  ║")
            print("╚══════════════════════════════════════════════════╝")
            time.sleep(1)

            print("\n📅 Come back anytime to check your BMI again!\n")
            time.sleep(1)

            print("👋 Logging off...")
            time.sleep(0.5)
            print("💤 Shutting down BMI CALCULATOR 3000...")
            time.sleep(1)
            print("🖥️  System offline. Goodbye, legend.\n")
            break


    
