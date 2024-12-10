from ticket_prices import ADULT, CHILD, SENIOR, WRISTBAND

import os
from datetime import datetime

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def generate_ticket(ticket_info, date):
    total_tickets = ticket_info['num_adult'] + ticket_info['num_child'] + ticket_info['num_senior']
    surname_field_len = 18 + len(ticket_info['booker_surname'])
    ticket_field_len = 21 + len(str(total_tickets))
    wristband_field_len = 24 + len(str(ticket_info['num_wristbands']))
    date_field_len = 8 + len(date)
    parking_pass_field_len = 16 + len(str("Yes" if ticket_info['parking_pass'] == True else "No"))

    longest_line_len = max(surname_field_len, ticket_field_len, wristband_field_len, date_field_len, parking_pass_field_len)

    longest_line_len += 5

    # Calculate padding for each field
    surname_padding = " " * (longest_line_len - surname_field_len)
    ticket_padding = " " * (longest_line_len - ticket_field_len)
    wristband_padding = " " * (longest_line_len - wristband_field_len)
    date_padding = " " * (longest_line_len - date_field_len)
    parking_pass_padding = " " * (longest_line_len - parking_pass_field_len)

    ticket = f"""
{'-' * (longest_line_len+1)}
| Booker Surname: {ticket_info['booker_surname']}{surname_padding}|
| Tickets Purchased: {total_tickets}{ticket_padding}|
| Wristbands Purchased: {ticket_info['num_wristbands']}{wristband_padding}|
| Date: {date}{date_padding}|
| Parking Pass: {"Yes" if ticket_info['parking_pass'] == True else "No"}{parking_pass_padding}|
{'-' * (longest_line_len+1)}
"""
    return ticket

def get_ticket_info() -> list:
    booker_surname = num_adult = num_child = num_senior = num_wristbands = parking_pass = None

    done = False

    while not done:
        try:
            if booker_surname is None:
                booker_surname_input = input("What is the booker's surname?\nBooker surname: ")
                if all(c.isalpha() or c.isspace() for c in booker_surname_input):
                    booker_surname = booker_surname_input
                else:
                    print("Please input only letters (A-Z)")
            elif num_adult is None:
                num_adult_input = int(input("How many adult tickets?\nNumber of adults: "))
                if num_adult_input >= 0:
                    num_adult = num_adult_input
                else:
                    raise ValueError
            elif num_child is None:
                num_child_input = int(input("How many child tickets?\nNumber of children: "))
                if num_child_input >= 0:
                    num_child = num_child_input
                else:
                    raise ValueError
            elif num_senior is None:
                num_senior_input = int(input("How many senior tickets?\nNumber of seniors: "))
                if num_senior_input >= 0:
                    num_senior = num_senior_input
                else:
                    raise ValueError
            elif num_wristbands is None:
                total_tickets = (num_adult + num_child + num_senior)
                num_wristbands_input = int(input(f"How many wristbands are needed?\nAllowed range: 1-{total_tickets}\nNumber of wristbands: "))
                if num_wristbands_input > 0:
                    if num_wristbands_input <= total_tickets:
                        num_wristbands = num_wristbands_input
                    else:
                        print(f"Please input a number in the range 1-{total_tickets}")
                else:
                    raise ValueError
            elif parking_pass is None:
                parking_pass_input = input("Do you require a parking pass?\nParking pass (Y/N): ")
                parking_pass_input = parking_pass_input.lower()
                valid_yes = ["y", "yes", "true"]
                valid_no = ["n", "no", "false", "none"]
                if parking_pass_input in valid_yes:
                    parking_pass = True
                elif parking_pass_input in valid_no:
                    parking_pass = False
                else:
                    print("Please type 'Y' for a parking pass, or 'N' for no parking pass")
            else:
                done = True
        except ValueError:
            print("Please input either zero or a positive integer")
        except (KeyboardInterrupt, EOFError):
            print("Please don't do that...")

    ticket_info = {
        "booker_surname": booker_surname,
        "num_adult": num_adult,
        "num_child": num_child,
        "num_senior": num_senior,
        "num_wristbands": num_wristbands,
        "parking_pass": parking_pass
    }

    clear()
    return ticket_info

def get_payment(total_cost):
    payment_total = 0

    paid = False

    print("Please input either £10 or £20 notes to pay")

    while not paid:
        try:
            if payment_total < total_cost:
                note_input = int(float(input("Enter £10 or £20 note: £")))
                assert note_input in (10, 20), "Invalid input. Please input either a £10 or £20 note"
                payment_total += note_input
                print(f"You have paid £{payment_total:.2f} of £{total_cost:.2f}")
            else:
                paid = True
        except ValueError:
            print("Invalid input. Please enter a £10 or £20 note")
        except AssertionError as e:
            print(e)
    
    change = (payment_total - total_cost) if (payment_total > total_cost) else 0

    clear()

    print(f"""
Subtotal: £{total_cost:.2f}
Total Payment: £{payment_total:.2f}
Amount Due: £0.00
Change Due: £{change:.2f}
""")

if __name__ == "__main__":
    print(f"""
Welcome to the Copington Adventure Theme Park!

TICKET PRICES:
Adult: £{ADULT:.2f}
Child: £{CHILD:.2f}
Senior: £{SENIOR:.2f}""")
    ticket_info = get_ticket_info()

    adult_total = ticket_info["num_adult"] * ADULT
    child_total = ticket_info["num_child"] * CHILD
    senior_total = ticket_info["num_senior"] * SENIOR
    wristband_total = ticket_info["num_wristbands"] * WRISTBAND

    total_cost = (adult_total + child_total + senior_total + wristband_total)

    print(f"""
Ticket Information:
Number of adults: {ticket_info['num_adult']} (£{adult_total:.2f})
Number of children: {ticket_info['num_child']} (£{child_total:.2f})
Number of seniors: {ticket_info['num_senior']} (£{senior_total:.2f})
Number of wristbands: {ticket_info['num_wristbands']} (£{wristband_total:.2f})

Total Cost: £{total_cost:.2f}
""")
    
    get_payment(total_cost)

    print(generate_ticket(ticket_info, date=datetime.now().strftime("%d/%m/%Y")))

    print("Thank you for your purchase. Enjoy your visit!")