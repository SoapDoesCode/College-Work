import datetime # I'm not quite sure why this is imported but it was there before I got here so it has to be important... right?
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Task_4A.csv') # read the csv file as df


def mainmenu():
    print("""\t\t****Welcome to the Dashboard****
1) Return all current data
2) Return data for a specific region
3) Return data for a specific region, property type, and room count
4) Exits the program
""") # displays the main menu
    while True: # loops until a valid menu option is chosen
        try:
            return int(input("Option: ")) # if valid input, return it
        except ValueError: # catches invalid inputs
            print("Please input a valid option.") # warns the user that the input is not valid

def get_all_data() -> pd.DataFrame:
    return df # returns all data

def validate_input(user_input: str): # this validates and formats the user's input to make their life easier
    validation_output = "" # default value

    if user_input.lower() in ("semi-detached", "semi detached"): # checks if the user has attempted to write Semi-Detached without perfect formatting
        validation_output = "Semi-Detached" # makes sure Semi-Detached is always formatted perfectly
    else: # if its any other input, format it accordingly
        validation_output = user_input.capitalize() # capitalizes the first letter and lowercases everything else

    return validation_output # returns the validated input

def region_check(region=None, property_type=None, room_count=None, start_date=None, end_date=None): # region, start_date, end_date
    df1 = df.loc[:, start_date:end_date]
    df2 = df.loc[:, 'Region Code':'Rooms']

    if (property_type == None) and (room_count == None): # filters by region only (option 2 of main menu)
        result = pd.concat([df2, df1], axis=1, join='inner').where(df2['Region'] == region) # sets result to the data filtered by region
    else: # filters by region, property type, and room count (opiton 3 of main menu)
        result = pd.concat([df2, df1], axis=1, join='inner').where(df2['Region'] == region).where(df2['Property Type'] == property_type).where(df2['Rooms'] == room_count) # sets result to the data filtered by region, property type, and room count

    result = pd.DataFrame(result) # converts the data into a DataFrame object (more usable)
    result.dropna(inplace=True) # removes any missing values
    print(result) # show the user the result in text
    average = df1.mean() # calculate the average
    graph = average.plot() # plot the average on the graph
    graph.set_title("Average Percentage Increase") # set the title
    graph.set_xlabel("Date (Month-Year)") # set the X-axis label
    graph.set_ylabel("Property Value") # set the Y-axis label
    plt.show() # show the user the graph
    return result

def get_region() -> str:
    valid_region = False # sets default value so loop continues until the input is valid

    while not valid_region: # loops until the user inputs a valid region
        print(f"Valid regions: {", ".join(df['Region'].unique())}") # show the user the valid regions
        region = input("Please enter the name of the region you would like to check:\nRegion: ")
        region = validate_input(region) # validate and format the user input
        if region in df['Region'].values:
            valid_region = True
            return region # return the selected region
        else:
            print(f"ERROR: Region not found: {region}\nPlease check your spelling") # inform the user they've input an invalid value

def get_property_type() -> str:
    valid_type = False # sets default value so loop continues until the input is valid

    while not valid_type: # loops until the user inputs a valid property type
        print(f"Valid property types: {", ".join(df['Property Type'].unique())}") # show the user the valid property types
        property_type = input("Please enter the type of property you would like to check\nProperty Type: ")
        property_type = validate_input(property_type) # validate and format the user input
        if property_type in df['Property Type'].values:
            valid_type = True
            return property_type # return the selected property type
        else:
            print(f"ERROR: Invalid property type: {property_type}\nPlease check your spelling") # inform the user they've input an invalid value

def get_room_count() -> int:
    valid_room_count = False # sets default value so loop continues until the input is valid

    while not valid_room_count: # loops until the user inputs a valid room count
        print(f"Valid room count: {", ".join(str(count) for count in df['Rooms'].unique())}")
        try:
            room_count = input("Please enter the number of rooms you're looking for\nRoom Count: ") # ask the user for the number of rooms
            room_count = int(room_count) # convert the input to an integer
            if room_count in df['Rooms'].values:
                valid_room_count = True
                return room_count # return the selected room count
            else:
                raise ValueError
        except ValueError:
            print(f"ERROR: No property found with {room_count} rooms") # inform the user they've input an invalid value

def get_start_date() -> str:
    valid_start = False # sets default value so loop continues until the input is valid

    while not valid_start: # loops until the user inputs a valid start date
        start_date = input("Please enter a start date in the format MONTH-YEAR e.g. Jan-20\nStart Date: ")
        start_date = validate_input(start_date) # validate and format the user input
        if start_date in df.columns:
            valid_start = True
            return start_date # return the selected start date
        else:
            print(f"ERROR: Start date not found: {start_date}") # inform the user they've input an invalid value

def get_end_date() -> str:
    valid_end = False # sets default value so loop continues until the input is valid

    while not valid_end: # loops until the user inputs a valid end date
        end_date = input("Please enter an end date in the format MONTH-YEAR e.g. Jan-20\nEnd Date: ")
        end_date = validate_input(end_date) # validate and format the user input
        if end_date in df.columns:
            valid_end = True
            return end_date # return the selected end date
        else:
            print(f"ERROR: End date not found: {end_date}") # inform the user they've input an invalid value

while True:
    option = mainmenu() # brings up the main menu

    match option:
        case 1: # Return all current data
            all_data = get_all_data() # gets all data and stores it
            print(all_data) # shows all of the data to the user
        case 2: # Return data for a specific region
            print() # adds extra newline for formatting
            region = get_region() # runs the function to ask for region
            start_date = get_start_date() # asks for the start date
            end_date = get_end_date() # asks for the end date
            region_check(region, start_date=start_date, end_date=end_date)
        case 3: # Return data for a specific region, property type, and size
            print() # adds extra newline for formatting
            region = get_region() # runs the function to ask for region
            property_type = get_property_type() # asks for the property type
            room_count = get_room_count() # asks for the room count
            start_date = get_start_date() # asks for the start date
            end_date = get_end_date() # asks for the end date
            region_check(region, property_type, room_count, start_date, end_date)
        case _: # the user has chosen to exit
            print("Exitting program...") # tells the user the program is stopping
            exit(0) # exits the program without errors