from currency_conversion import currency_conversion

space_decoration = " " * 5
dash_decoration = "-" * 47
thousand_float = "{:,.3f}"
thousand = "{:,}"

# Title Decoration
print("\n" + dash_decoration)
print(f"|{space_decoration}AUPP Currency Conversion to RIEL 💸{space_decoration}|")
print(dash_decoration)

# Welcome Message
input("\nWelcome to AUPP Currency Conversion to RIEL app. \nThis is where you can exchange your money \n(USD, YUAN, BAHT) to Khmer Riel. \n\nSee instruction below: ")

# Instruction
print("1/. Enter currency you want to convert from. (usd, yuan, baht)")
print("2/. Enter amount you want to convert.")
print("3/. The amount will be converted to RIEL (៛).")

# Take input
input("\nPlease read the instruction before continue...✨")
user_currency = input("\nEnter the currency: ")
user_amount = input("Enter amount: ")

# Convert to Khmer Riel
converted = currency_conversion(user_currency, user_amount)

# Display result
print("\n-------------------------------------------------------")

if converted != "invalid amount" and converted != "not found":
  print(f"  Currency conversion from {user_currency.lower()} to riel")
  if user_amount.isdecimal():
    print(f"  {thousand.format(int(user_amount))} {user_currency} = {thousand.format(converted)} riel")
  else:
    print(f"  {thousand_float.format(float(user_amount))} {user_currency} = {thousand_float.format(converted)} riel")
else:
  print("  Sorry! The system cannot detect and convert your money.")

print("-------------------------------------------------------")

print("\nThank you for using our app. Come again when you travel to another country (❁´◡`❁)")

