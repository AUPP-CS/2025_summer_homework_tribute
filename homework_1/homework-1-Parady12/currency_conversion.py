def currency_conversion(currency, amount):
  usd_format = "usd"
  yuan_format = "yuan"
  baht_format = "baht"

  # Check if amount is str, if so, convert to int or float
  if type(amount) == str:
    if amount.isdigit(): # Chech if amount consists all digit (int)
      amount = int(amount)
    else:
      if (amount.find(".") != -1): # Check if there is "." (float)
        amount = float(amount)
      else: # Otherwise, there is letter (str)
        return "invalid amount"
  
  # Check if it is negative
  if amount >= 0:
    # Check currency and calculate
    if currency.lower() == usd_format:
      return (amount * 4075)
    elif currency.lower() == yuan_format:
      return (amount * 575)
    elif currency.lower() == baht_format:
      return (amount * 115)
    else:
      return "not found"
  else:
    return "invalid amount"