from currency_conversion import currency_conversion



# Print a welcome message and list of valid currencies

print("===========================================")
print("           🏦 AUPP Currency Converter       ")
print("===========================================\n")

print("Welcome")

print("Available currencies to convert TO 🇰🇭 RIEL:")
print("   💵 USD")
print("   🐉 YUAN")
print("   🛕 BAHT\n")

# Ask the user for the currency they want to convert from
currency = input("Please enter the currency type:\n ")

# Ask the user for the amount they want to convert
amount = float (input("Please enter the amount:\n "))
print("\nConverting money... 💵➡️៛")
print("Please kindly press enter on your keyboard to continue\n")
input("")
# Call the currency_conversion function with the user's currency and amount
result = currency_conversion(currency, amount)
print(f"✅ Success! You will receive: {result}៛")