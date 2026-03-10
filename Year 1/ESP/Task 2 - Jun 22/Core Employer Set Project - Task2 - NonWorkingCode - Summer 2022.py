houses = [['LONDON', 'Terraced', 3, 735000], ['CARDIFF', 'Semi-Detached', 2, 100000], ['LEEDS','Terraced', 3, 245000],['LONDON','Semi-Detatched', 1, 240000]]
# added comma after 3, 'Semi-Detatched', and 'Terraced'

sales = []
ourregions = ['LONDON', 'LEEDS', 'CARDIFF', 'BRISTOL']    
property_types =  ['TERRACED', 'SEMI-DETATCHED','DETATCHED']

def return_stock():
    print("""CURRENT HOUSES FOR SALE:

REGION - HOUSE TYPE - BEDROOMS - COST""") # changed to multi-line string for readability
    for i in houses:
        print(i) # removed space for formatting

def unique_regions():
    unique_list = []
    existing_regions = [item[0] for item in houses]
    for x in existing_regions:
        if not x in unique_list: # added 'not' to the if-statement
            unique_list.append(x)
    print(unique_list)


def region_search():
    print("Available Regions")
    unique_regions()
    r_check = False

    while not r_check:
        region_select= input("Please enter region: ").capitalize()

        for x in houses:
            if region_select.upper() == x[0].upper():
                r_check = True
                if x[0] == region_select.upper():
                    print(x)

        if r_check == False:
            print("Entered region is not valid")

def add_new_property():
    property = [None, None, None, None] # initial state

    index = 0 # current index, used for which input should be taken
    while not all(property): # keeps running until all values are filled
        match index:
            case 0:
                region = input("Please input the property region: ").upper() # asks for region
                if region in ourregions: # checks that the region is valid
                    property[0] = region # appends the data to the property
                    index += 1 # moves onto the next piece of data
                else:
                    print(f"Please input a valid region. Allowed regions:\n{ourregions}")
            case 1:
                property_type = input("Please input the type of property: ").upper() # asks for property type
                if property_type in property_types: # checks that the property type is valid
                    property[1] = property_type # appends the data to the property
                    index += 1 # moves onto the next piece of data
                else:
                    print(f"Please input a valid property type. Allowed types:\n{property_types}")
            case 2:
                try:
                    bedrooms = int(input("Please input the number of bedrooms: ")) # asks for number of bedrooms
                    if bedrooms < 1: # makes sure it isn't less than 1
                        raise ValueError
                    property[2] = bedrooms # appends the data to the property
                    index += 1 # moves onto the next piece of data
                except ValueError: # handles invalid input
                    print("Please input a positive integer for number of bedrooms!")
            case 3:
                try:
                    price = int(input("Please input the price of the property: ")) # asks for the price
                    if price < 1: # makes sure it isn't less than 1
                        raise ValueError
                    property[3] = price # appends the data to the property
                except ValueError: # handles invalid input
                    print("Please input a positive integer for the price!")
    houses.append(property)
    print(f"""Final property information:

Region: {property[0]}
Property type: {property[1]}
Bedrooms: {property[2]}
Price: £{property[3]}

Property successfully added to the database!""")

def show_sales(sold: list): # added sold as an argument to fix variable not defined error
    if len(sold) > 0:    
        print("Forename  Surname Property cost  Total")
        for i in sales:
            print(i)
    else:
        print('no sales')

def house_sale():
    sale = []
    customer_forename = input('Please enter customer forename: ') # added space after : for formatting
    customer_surname = input('Please enter customer surname: ') # added space after : for formatting
    for i, item in enumerate(houses, 1):
        print(i, item)

    sel_check = False
    while not sel_check:
        try:
            select = int(input('Please select a purchase: ')) # added int conversion
            select = select-1
            if select > 0 and select < len(houses):
                sel_check = True
        except ValueError: # catching Value Errors
            print('ERROR PLEASE ENTER A VALID PROPERTY')

    sub_total = houses[select][3]
    # removed unnecessary print statement
    total_fees = 0

    if sub_total > 100000:
        total_fees += 3000+(sub_total-100000) * 0.2
    else:
        total_fees += sub_total *0.3

    total = round(sub_total + total_fees, 2) # corrected calculation and added rounding to 2dp

    final_total = sub_total+total_fees
    sale.append(customer_forename)
    sale.append(customer_surname)
    sale.append(sub_total)
    sale.append(final_total)
    sales.append(sale)

    print(f"""Customer Receipt
FORENAME: {customer_forename}
SURNAME: {customer_surname}
PROPERTY COST: {sub_total}
WITH STAMP DUTY: {total}

TRANSACTION COMPLETE - PROPERTY REMOVED FROM SALES DATABASE
""")
    # removed unnecessary print statements
    del houses[select] # changed to select-1


while True:
    try: # added try-except to catch Value Errors
        menuselection = int(input("""WELCOME TO THE NEWHAVEN DASHBOARD
Please select from the following menu options:

1: View current houses on market
2: Search for available houses in a region
3: Record a sale
4: Add a new property for sale
5: Show Sales
6: Exit

Selection: """))
        # changed input to multi-line string for formatting


        if menuselection == 1:
            return_stock() # added brackets to return_stock()
        elif menuselection == 2: # changed to elif
            region_search() # added brackets to region_search()
        elif menuselection == 3: # changed to elif
            house_sale() # added brackets to house_sale()
        elif menuselection == 4:
            add_new_property()
        elif menuselection == 5: # added menuselection of 5 for sales
            show_sales(sales) # added brackets and input parameter to show_sales(sales)
        elif menuselection == 6:
            print("Exitting the program...")
            exit(0) # added menu select option 6 to safely exit the program
        else: # catches numbers < 1 and > 6 and informs the user
            print("Please input an integer 1-6")
        input("Press enter to continue...")
    except ValueError: # catches ValueError and informs the user of their mistake
        print("Please input an integer 1-6")
        input("Press enter to continue...")