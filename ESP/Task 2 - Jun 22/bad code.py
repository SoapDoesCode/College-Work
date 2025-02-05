
houses = [['LONDON','Terraced', 3 735000], ['CARDIFF', 'Semi-Detached' 2, 100000], ['LEEDS','Terraced' 3,245000],['LONDON','Semi-Detatched' 1, 240000]]
sales = []
ourregions = ['LONDON', 'LEEDS', 'CARDIFF', 'BRISTOL']    
property_types =  ['TERRACED', 'SEMI-DETATCHED','DETATCHED']

def return_stock():
    print("CURRENT HOUSES FOR SALE \n\n REGION - HOUSE TYPE - BEDROOMS - COST")
    for i in houses:
        print (i)

def unique_regions():
    unique_list = []
    existing_regions = [item[0] for item in houses]
    for x in existing_regions:
        if x in unique_list:       
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



def show_sales():
    if len(sold) > 0:    
        print("Forename  Surname Property cost  Total")
        for i in sales:
            print(i)
    else:
        print('no sales')


def house_sale():
    sale = []
    customer_forename = input('Please enter customer forename:')
    customer_surname = input('Please enter customer surname:')
    for i, item in enumerate(houses, 1):
        print(i, item)

    sel_check = False
    while not sel_check:
        try:
            select = input('Please select a purchase'))   
            if select > 0 and select < len(houses):
                sel_check = True

        except:
            print('ERROR PLEASE ENTER A VALID PROPERTY')

    sub_total = houses[select-1][3]
    print(sub_total)
    total_fees = 0


    if sub_total > 100000:
        total_fees += 3000+(sub_total-100000) * 0.2
    else:
        total_fees += sub_total *0.3

    

    final_total = sub_total+total_fees
    sale.append(customer_forename)
    sale.append(customer_surname)
    sale.append(sub_total)
    sale.append(final_total)
    sales.append(sale)

    print('Customer Receipt\n\n  FORENAME:{}  SURNAME: {}  PROPERTY COST:  {}  WITH STAMP DUTY:   {}'.format(*sales[-1]))
    print('\nTRANSACTION COMPLETE - PROPERTY REMOVED FROM SALES DATABASE\n')
    print (houses[select])
    del houses[select] 


while True:
    menuselection = int(input(" WELCOME TO THE NEWHAVEN DASHBOARD \n\n Please select from the following menu options \n\n"
                              " 1: View current houses on market \n 2: Search for available houses in a region \n 3: Record"
                              " a sale \n 4: Add a new property for sale \n 5:Show Sales \n 6: Exit"))


    if menuselection == 1:
        return_stock
    if menuselection == 2:
        region_search
    if menuselection ==3:
        house_sale
    if menuselection==4:
        show_sales

         