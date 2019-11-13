#Short discription about this program

PRICE1 = 5.25
PRICE2 = 5.75
PRICE3 = 5.95
PRICE4 = 5.95
PRICE5 = 5.95
TAX = 0.09


def main():
    '''
    Put this function docstring here(short description about this function)
    '''
    displayMenu()
    number_of_burger1 , number_of_burger2 , number_of_burger3 , number_of_burger4 , number_of_burger5 , student_staff, count, tax = get_input()

    if count!=0:
        price_before_tax, price_after_tax = compute_bill(number_of_burger1 , number_of_burger2 , number_of_burger3 , number_of_burger4 , number_of_burger5, student_staff)
        show_bill(number_of_burger1 , number_of_burger2 , number_of_burger3 , number_of_burger4 , number_of_burger5 , price_before_tax, price_after_tax, tax)
    else:
        print("\nHope to see you next time!")
        
def displayMenu():
    '''
    Put this function docstring here(short description about this function)
    '''
    print("1. DA Burger $5.25")
    # your code here...
    # print the menu 
    print("5. Don Cali Burger $5.95")
    print("6. Exit")

def get_input ():
    '''
    Put this function docstring here(short description about this function)
    '''
    number_of_burger1 = number_of_burger2 = number_of_burger3 = number_of_burger4 = number_of_burger5 = 0
    count = 0
    flag0 = True
    while flag0:
        flag1 = True
        while flag1:
            try:
                 # your code here...
                 # Enter what type of burger you would like to have
                 #Show an error if user enters a negative number or a string or any other numbers except 1,2,3,4,5,6 
                 #
                 #
            except:
                print("Please enter an integer number between 1 and 6!")


        flag2 = True
        while flag2 and type_burger != 6:
            try:
                 # your code here...
                 # How many burgers would you like to have:
                 # Show an error if user enters a negative number or a string
                 # count should be increased here
                 #
            except:
                print("Please enter a positive integer number!")


                
        if type_burger == 1:
            number_of_burger1 = number_of_burger
         # your code here...
         #
         #
         #
            number_of_burger5 = number_of_burger
        elif type_burger == 6:
            print("Thank you for being intresteted in our service!")
            flag0 = False

        

    flag3 = True
    while flag3 and count !=0:
            # your code here...
            #Enter 1 if you are student or 2 if you are staff:
            #
            #
            # Show an error if user enters any numbers except 1 or 2!
            
    return number_of_burger1 , number_of_burger2 , number_of_burger3 , number_of_burger4 , number_of_burger5 , student_staff, count , tax
            

def compute_bill(number_of_burger1 , number_of_burger2 , number_of_burger3 , number_of_burger4 , number_of_burger5, student_staff):
    '''
    Put this function docstring here(short description about this function)
    '''
     # your code here...
     #
     #
    return price_before_tax, price_after_tax

def show_bill(number_of_burger1 , number_of_burger2 , number_of_burger3 , number_of_burger4 , number_of_burger5 , price_before_tax, price_after_tax, tax):
    '''
    Put this function docstring here(short description about this function)
    '''
     # your code here...
     #print the bill with showing the all ordered items

main()

"""
Sample result:

1. DA Burger $5.25
2. Bacon Cheese $5.75
3. Mushroom Swiss $5.95
4. Western Burger $5.95
5. Don Cali Burger $5.95
6. Exit

Enter what type of burger you would like to have:hello
Please enter an integer number between 1 and 6!

Enter what type of burger you would like to have:-5
Please enter an integer number between 1 and 6!

Enter what type of burger you would like to have:7
Please enter an integer number between 1 and 6!

Enter what type of burger you would like to have:0
Please enter an integer number between 1 and 6!

Enter what type of burger you would like to have:5

How many burgers would you like to have:something
Please enter a positive integer number!

How many burgers would you like to have:-9
Please enter a positive integer number!

How many burgers would you like to have:52

Enter what type of burger you would like to have:1

How many burgers would you like to have:23

Enter what type of burger you would like to have:4

How many burgers would you like to have:52

Enter what type of burger you would like to have:3

How many burgers would you like to have:74

Enter what type of burger you would like to have:6
Thank you for being intresteted in our service!

Enter 1 if you are student or 2 if you are staff:hello
Please enter an integer number 1 or 2!

Enter 1 if you are student or 2 if you are staff:-1
Please enter an integer number 1 or 2!

Enter 1 if you are student or 2 if you are staff:2

**************************************************

Your Receipt:
DA Burger $5.25 x  23  =  120.75
Mushroom Swiss $5.95 x  74  =  440.3
Western Burger $5.95 x  52  =  309.4
--------------------------------------------------
Price Before Tax:  870.45
Tax:  78.34
Price After Tax:  948.79

"""
    
          
