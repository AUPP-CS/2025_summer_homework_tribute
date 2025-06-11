
# currency = input("please put in the types of currency: ")
# amount = float (input("please put in the amount "))

 
def currency_conversion(currency, amount):
    

    Exchanges_from_USD_to_RIEL_rate = 4075
    Exchanges_from_YUAN_to_RIEL_rate = 575
    Exchanges_from_BAHT_to_RIEL_rate = 115

    if not isinstance(amount, (float, int)):
        return "invalid amount"
    
    # Add your code here
    # Reminders: 
    # - currency is a string that tells us what currency to change to. It can be 'usd', 'yuan', or 'baht'.
    # - amount is a number that tells us how much money to change into riel.
    
    # 1. add a check to ensure that 'amount' is a number.
    # 2. convert the 'amount' to the right 'currency'.
    
    if currency.upper() == "USD":
        amount_from_usd_to_riel = Exchanges_from_USD_to_RIEL_rate * amount
        # print (f"{amount_from_usd_to_riel}")
        return amount_from_usd_to_riel
    elif currency.upper() == "YUAN":
        amount_from_yuan_to_riel = Exchanges_from_YUAN_to_RIEL_rate * amount
        # print (f"{amount_from_yuan_to_riel}")
        return amount_from_yuan_to_riel
    elif currency.upper() == "BAHT":
        amount_from_baht_to_riel = Exchanges_from_BAHT_to_RIEL_rate * amount
        # print (f"{amount_from_baht_to_riel}")
        return amount_from_baht_to_riel
    else:
        return "not found"
         

# currency_conversion(currency, amount)







    

    


