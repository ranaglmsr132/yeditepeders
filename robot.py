#Robot Barista
print("Hello Welcome to ZoeBanana Coffee Shop!!")
#Ask your customer what their name is
name = input("What's your name?\n")

if name == "Ben":
    print("You're note welcome here Ben!!Get out here!!")
    exit()
else:
    print("Hello " + name + ", thank you so much for coming in today.\n\n\n")
  
#Coffee menu
menu = "Black Coffe, Espresso, Latte, Cappucino, Frappuccino"
#Ask customer what they would like from menu
print(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")
order= input() 

#Set the price for coffee
if order== "Frappuccino":
    price= 13
elif order== "Black Coffe":
    price= 3
elif order== "Espresso":
    price= 5
elif order== "Latte":
    answer=input("Do you want whipped cream? ")
    if answer == "yes":
        price= 11
    else:
        price= 9
elif order== "Cappucino":
    price= 10
else:
    print("Sorry, we dont have that here.")
    price= 0

#Ask customer how many would they like
quantity= input("How many coffees would you like?\n")

#Calculate the customer's total
total= price * int(quantity)

print("Thank you. Your total is: $ " + str(total))

print("Sounds good " + name + " , we'll have your " + quantity + " " + order + " ready for you in a moment.\n\n\n")