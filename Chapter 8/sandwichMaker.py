import pyinputplus as pyip

priceList = {'bread': {'wheat': 3,
                       'white': 2,
                       'sourdough': 5},
             'protein': {'chicken':5,
                         'turkey': 5,
                         'ham': 5,
                         'tofu': 3},
             'cheese' : {'cheddar': 4,
                         'Swiss': 5,
                         'mozzarella': 4}
             }

total_price = 0
while True:
    buy_again = 'yes'
    print("Enter 'q' to quit anytime")
    bread = pyip.inputMenu(['wheat', 'white', 'sourdough'], prompt='Select a bread: \n', numbered=True, allowRegexes=[r'q'])
    if bread =='q':
        break
    protein = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], prompt='Select a protein: \n', lettered=True, allowRegexes=[r'q'])
    if protein =='q':
        break
    put_cheese = pyip.inputYesNo("Do you want cheese? ", allowRegexes=[r'q'])
    if put_cheese == 'yes':
        cheese = pyip.inputMenu(['cheddar', 'Swiss', 'mozzarella'], prompt='What cheese would you like?\n', numbered=True, allowRegexes=[r'q'])
    elif put_cheese == 'q':
        break
    mayo = pyip.inputYesNo("Do you want mayo? ", allowRegexes=[r'q'])
    if mayo == 'q':
        break
    mustard = pyip.inputYesNo("Do you want mustard? ", allowRegexes=[r'q'])
    if mustard =='q':
        break
    lettuce = pyip.inputYesNo("Do you want lettuce? ", allowRegexes=[r'q'])
    if lettuce =='q':
        break
    tomato = pyip.inputYesNo("Do you want tomato? ", allowRegexes=[r'q'])
    if tomato =='q':
        break
    no = pyip.inputInt("How many of this sandwich do you want? Enter 'c' to cancel this order ", min=1, allowRegexes=[r'q|c'])
    if no == 'q':
        break
    elif no == 'c':
        continue
    if put_cheese=='yes':
        total_price += (priceList['bread'][bread] + priceList['protein'][protein] + priceList['cheese'][cheese]) * no
    else:
        total_price += (priceList['bread'][bread] + priceList['protein'][protein]) * no

    buy_again = pyip.inputYesNo("Do you still wish to purchase more? ", allowRegexes=[r'q'])
    if buy_again=='no' or buy_again=='q':
        break

if buy_again == 'no':
    print('The total price is: $' + str(total_price))

