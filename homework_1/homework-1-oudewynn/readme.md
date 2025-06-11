[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=19683139&assignment_repo_type=AssignmentRepo)
# HW.1 Currency Conversion

You are working as a software developer at a currency exchange company called AUPP Currency.

Your manager has assigned you to create an application that can handle the transactions below:
- Exchanges from USD to RIEL,  USD rate=4075៛.
- Exchanges from YUAN to RIEL, YUAN rate=575៛.
- Exchanges from BAHT to RIEL, BAHT rate=115៛.

<br>

# Technical Requirements:

The application development team requires you to create a function called currency_conversion that takes 2 parameters - **currency** and **amount**.

Make sure that the currency_conversion function returns the following values in different situations:

1. When a invalid currency provided, make sure the function returns **‘Not Found’**

2. If the amount is not a float or integer, make sure the function returns **‘Invalid Amount’**

3. If both parameters are correct, return the converted value from the function example:
   > currency_conversion('USD', 2) # The function should return 8150

<br>

### Task: You will be creating an application that helps the user convert their currency of choice to Riel.

<br>

### Instructions:

> In the main file, ask for user inputs.
>   > Inputs:
>   > - Ask user to pick the desired currency (show the options)
>   > - Ask user to pick the desired amount to convert
> - Do a calculation according to user input by multiplying the input with the desire currency (ex: currency \* amount)
> - Then display result in a creative way.

### Expected Output:

![image](https://github.com/AUPP-CS/homework_1/assets/80062829/3e6e75fe-8513-4b4b-9878-ae153e357952)


### Hint:
> You will be modifying 2 files:
>   1. The first file will be the logic file which contains the currency function.
>   2. The second file stores the UI for displaying the user's input inside the terminal and calls the currency function.

<br><br>

### Reminders:

Tests will be run on your main file, make sure to check that your code meets the technical requirements before submitting.

Also, for next week, there will be a showcase for the three students who are most creative with this project. 

Please do your best on this and try to be creative, especially with how you do the output. Good luck! :)
