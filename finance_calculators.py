#  =========  Capstone Project =========
# Author: Gayathri
# Created Date: 20/03/2023
# References: W3 schools to use while and functions
# This is a python program and the purose is to calculate - simple interest, compound interest and bond 
# by getting inputs from user
# Added a function for validation, repeated operations.
# Tried to reuse the code using function- get_confirmation and thankyou_message.
#  ======================================

import math

# Function to validate the inputs from user is not null or empty and accept only numeric value
# It get 2 argument values. 1st is the value that user enters and 2nd is the variable type for which validation is done.
# Returns the validated value.
def validate(variable_to_validate, message):
    variable_empty_message = "The {} can only be a number. Please enter the correct value:"
    while(True):
        try:   
            if(message == "interest rate"):
                variable_to_validate = variable_to_validate.strip("%")                      
            variable_to_validate = float(variable_to_validate)
            if(variable_to_validate == 0.0): 
                variable_to_validate = input(f"The {message} cannot be 0.0. Please enter a value:")
            else:
                return variable_to_validate
        except ValueError:
            variable_to_validate = input(variable_empty_message.format(message))
    
            
# Function to validate the confirmation message of the user
def get_confirmation(is_yes):
    is_yes = is_yes.lower()
    if(is_yes == "yes"):
        return True
    else:
        print("You have not entered \'yes\'. ", end=' ')
        thankyou_message()
        return False

# Function to resue the thank you message
def thankyou_message():
    print("Thank you for using financial calculator!")    
    print("---------------------------------------------------------------------------------------------------------------------")   

print("\n-----------------------------------------------------------------")
print("--------------------Finance Calculator---------------------------")


is_not_exit = True
#Using this message variable repeatadly.
empty_message = "\nYou have not provided any values from the options! If you wish to calculate again, then Please enter \'yes\': " 
incorrect_value_message = "\nYou have provided incorrect values from the options! If you want to calculate again, then enter \'yes\': "
calculate_again_message = "\nDo you want to calculate anything else from the option? then please say \'yes\': "

#Using Loop for giving user an option to calculate again.
while(is_not_exit):  
    print("-----------------------------------------------------------------")
    print("\nPlease enter your selection from the below option:\n")    
    print("Investment - to calculate the amount of interest you'll earn on your investment")
    print("Bond - to calculate the amount youu'll have to pay to your house loan")
    
    type_of_calculation = input("\nEnter either \'Investment\' or \'Bond\' from the options above to calculate: ") 
    type_of_calculation = type_of_calculation.lower()

    if(type_of_calculation == "investment"):     

        principle_amount = input("\nPlease enter the amount of money that you are depositing: ")
        #Using validate method to check principle amount
        principle_amount = validate(principle_amount, "principle amount")

        interest_rate = input("Please enter the interest rate: ")
        interest_rate = validate(interest_rate, "interest rate")
        interest_rate = (interest_rate/100)

        no_of_year = input("Please enter the number of years, you plan to invest: ")
        no_of_year = validate(no_of_year, "number of years")      
        
        type_of_interest = input("\nPlease enter the type of interest ie either \'simple interest\' or \'compound interest\': ")
        type_of_interest = type_of_interest.lower() 
        
        #Validation to check type_of_interest is entered or not
        if(type_of_interest == ""):  
            is_yes = input(empty_message)
            #Using get_confirmation function to validate whether user entered yes or not
            is_not_exit = get_confirmation(is_yes)
        elif(type_of_interest != "compound interest" and type_of_interest != "compound" and         
             type_of_interest != "simple interest" and type_of_interest != "simple"): 
                    #validation to check whther type_of_interest has correct value
                    is_yes = input(incorrect_value_message)
                    #Using get_confirmation function to validate whether user entered yes or not
                    is_not_exit = get_confirmation(is_yes)
        else:
            if(type_of_interest == "simple interest" or type_of_interest == "simple"):
                total_amount = principle_amount *(1 + interest_rate * no_of_year)
                print(f"\nThe amount of Simple interest that you will earn is {total_amount}")
                #Ask user if they want to calculate anything else
                is_yes = input(calculate_again_message)
                is_not_exit = get_confirmation(is_yes)          
            elif(type_of_interest == "compound interest" or type_of_interest == "compound"): 
                total_amount = principle_amount * math.pow((1 + interest_rate), no_of_year)
                print(f"\nThe amount of Compound interest that you will earn is {total_amount}")
                #Ask user if they want to calculate anything else
                is_yes = input(calculate_again_message)
                is_not_exit = get_confirmation(is_yes)                         
    elif(type_of_calculation == "bond"):
            #Validating all inputs
            value_of_house = input("\nPlease enter the current value of the house: ")
            value_of_house = validate(value_of_house, "value of house")

            interest_rate = input("Please enter the interest rate: ")
            interest_rate = validate(interest_rate, "interest rate")
            interest_rate = (interest_rate/100)/12

            no_of_months = input("Please enter the number of months, you plan to repay: ")
            no_of_months = validate(no_of_months, "number of months")
                
            repayment_amount = (interest_rate * value_of_house)/(1 - (1 + interest_rate)**(-no_of_months))
            print(f"\nThe amount that you have to repay each month for the house:{repayment_amount}")
            #Ask user if they want to calculate anything else
            is_yes = input(calculate_again_message)
            is_not_exit = get_confirmation(is_yes)
    elif(type_of_calculation == ""):
        is_yes = input(empty_message)  
        #Using get_confirmation function to validate whether user entered yes or not                
        is_not_exit = get_confirmation(is_yes)
    else:
        is_yes = input(incorrect_value_message)
        #Using get_confirmation function to validate whether user entered yes or not                  
        is_not_exit = get_confirmation(is_yes)
         
                                               

            
                           
                  