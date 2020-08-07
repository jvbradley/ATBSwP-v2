#! python3
# https://automatetheboringstuff.com/2e/chapter8/
'''
Write a program that asks users for their sandwich preferences.  The program
should use PyInputPlus to ensure that they enter valid input, such as:

- Using inputMenu() for a bread type: wheat, white, or sourdough.
- Using inputMenu() for a protein type: chicken, turkey, ham, or tofu.
- Using inputYesNo() to ask if they want cheese.
- If so, using inputMenu() to ask for a cheese type: cheddar, Swiss, or
mozzarella.
- Using inputYesNo() to ask if they want mayo, mustard, lettuce, or tomato.
- Using inputInt() to ask how many sandwiches they want.  Make sure this number
is 1 or more.
- Come up with prices for each of these options, and have your program display
a total cost after the user enters their selection.
'''
def generateRandomPrices():
    # Generate random prices for the ingredients.
    import random
    return round(random.uniform(0.79, 1.79), 2)

def sandwichMaker():
    from decimal import getcontext
    getcontext().prec = 2
    import pyinputplus as pyip

    # This variable stores the ingredients and costs of your lunch.
    myLunch = {'ingredients': [], 'costs': []}

    # Build a dictionary of your options for what goes on the sandwich.
    sandwichOptions = {}
    sandwichOptions['bread'] = [['wheat', 'white', 'sourdough'], []]
    sandwichOptions['meat'] = [['chicken', 'turkey', 'ham', 'spam'], []]
    sandwichOptions['cheese'] = [['cheddar', 'Swiss', 'mozzarella'], []]
    sandwichOptions['condiments'] = [['mayonaisse', 'mustard', 'lettuce', 'tomato'], []]

    # Iterate through each category and item of ingredient options and get
    # a randomly generated price.
    for itemCategory, itemList in sandwichOptions.items():
        print(' * Setting random prices for \'' + itemCategory  + '\' ...')
        for item in itemList[0]:
            itemList[1].append(generateRandomPrices())

    print('\n\tYe Olde Timey Sandwich Shoppe Menu\n')

    # This builds the sandwich.
    for itemCategory, itemList in sandwichOptions.items():
        if itemCategory == 'bread' or itemCategory == 'meat':
            myLunch['ingredients'].append(pyip.inputMenu(itemList[0], numbered = True))
        else:
            notMeatYN = pyip.inputYesNo('Do you want ' + itemCategory + '? ')
            if notMeatYN == 'no':
                continue
            elif notMeatYN == 'yes':
                if itemCategory == 'cheese':
                    myLunch['ingredients'].append(pyip.inputMenu(itemList[0], numbered = True))
                elif itemCategory == 'condiments':
                    # Would you like some more ... SYRUP?!
                    # https://youtu.be/1R3G_beQccA?t=85
                    for condiment in itemList[0]:
                        thisCondiment = pyip.inputYesNo('Do you want to add ' + condiment + '? ')
                        if thisCondiment == 'no':
                            continue
                        elif thisCondiment == 'yes':
                            myLunch['ingredients'].append(condiment)

    # Ask the user to confirm the selected sandwich.
    print('\nTo confirm, you want this sandwich:')
    for ingredient in myLunch['ingredients']:
        print(' * ' + ingredient)

    sandwichYN = pyip.inputYesNo('\nThis is what you wanted? ')
    if sandwichYN == 'no':
        print(' * My mistake ...')
        exit()
    elif sandwichYN == 'yes':
        # How hungry are you feeling?
        sandwichCount = pyip.inputInt('\nHow many sandwiches do you want? ', min = 1)

        # This variable holds the running costs of the ingredients that you have
        # selected for your lunch.
        totalCost = float()
        print(' * I\'m on it!')
        for ingredient in myLunch['ingredients']:
            for ingredientCategory, ingredientPrice in sandwichOptions.values():
                if ingredient == ingredientCategory[0]:
                    totalCost += ingredientPrice[1]

    print(' * That comes out to $' + str(totalCost) + ' per sandwich.')
    print(' * Your total is $' + str(totalCost * sandwichCount) + ' for this food.')
sandwichMaker()
