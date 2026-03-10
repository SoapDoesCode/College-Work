import tkinter as tk
import re

def read_card():
    # Simulated Read of card with UTF-8 encoding
    with open("card.txt", "r", encoding="utf-8") as f:
        card = f.read()

        # Extract card owner
        card_owner_match = re.search(r"name:(\w+\s\w+)", card)
        card_owner = card_owner_match.group(1) if card_owner_match else "Unknown"

        # Extract balance
        card_bal_match = re.search(r"bal:£(\d+\.\d{2})", card)
        card_bal = float(card_bal_match.group(1)) if card_bal_match else 0.0

        # Extract PIN
        card_pin_match = re.search(r"pin:(\d+)", card)
        card_pin = card_pin_match.group(1) if card_pin_match else "0000"

    return card_owner, card_bal, card_pin

def write_card(ops: str = "", amount: float = 0):
    # Simulated Read of card with UTF-8 encoding
    with open("card.txt", "r", encoding="utf-8") as f:
        card = f.read()

        # Extract card details (owner, balance, pin)
        card_owner_match = re.search(r"name:(\w+\s\w+)", card)
        card_owner = card_owner_match.group(1) if card_owner_match else "Unknown"

        card_bal_match = re.search(r"bal:£(\d+\.\d{2})", card)
        card_bal = float(card_bal_match.group(1)) if card_bal_match else 0.0

        card_pin_match = re.search(r"pin:(\d+)", card)
        card_pin = card_pin_match.group(1) if card_pin_match else "0000"

        # Modify balance based on the operation
        if ops == "-bal":
            card_bal -= float(amount)
        elif ops == "+bal":
            card_bal += float(amount)
        elif ops == "pin":
            card_pin = amount

        # Create updated card content
        updated_card = f"name:{card_owner} bal:£{card_bal:.2f} pin:{card_pin}"

    # Write the updated card details back to the file
    with open("card.txt", "w", encoding="utf-8") as f:
        f.write(updated_card)

    return card_owner, card_bal, card_pin

def center_window(window):
    """Center the window on the screen."""
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry(f"{width}x{height}+{x}+{y}")

# Create the main application window
root = tk.Tk()
root.title("Ride Kiosk")
root.geometry("750x500")  # Set initial window size to 750x500 pixels

# Create a centered label widget with text and background color
label = tk.Label(root, text="Welcome to the Ride Kiosk", bg="lightblue", font=("Helvetica", 24))
label.place(relx=0.5, rely=0.4, anchor="center")  # Center the label

rides = {
    "Boneshaker": 3.00,
    "Carousel": 2.50,
    "Coaster": 4.00,
    "Wild West": 5.00
}

def show_frame(frame):
    """Bring a frame to the front."""
    frame.tkraise()
    center_window(root)  # Center window when frame is shown

def update_balance_label():
    """Updates the balance label with the current balance."""
    name, balance, _ = read_card()  # Read card details and balance
    balance_label.config(text=f"Hi {name}\nBalance: £{balance:.2f}")

def show_loading_frame(message, next_frame):
    """Shows an intermediary loading frame with a message."""
    loading_label.config(text=message)
    show_frame(loading_frame)
    root.after(2000, lambda: show_frame(next_frame))  # Simulate 2-second loading delay

def complete_action_frame(message, next_frame):
    """Shows a completed action frame with a message."""
    complete_label.config(text=message)
    show_frame(complete_frame)
    root.after(2000, lambda: show_frame(next_frame))  # Show completed action frame for 2 seconds

def pay_for_ride(ride_name, ride_cost):
    """Process ride payment and update balance."""
    _, balance, _ = read_card()
    verify = bool(check_pin())
    if balance >= ride_cost and verify:
        write_card("-bal", ride_cost)  # Deduct ride cost
        update_balance_label()
        complete_action_frame(f"£{ride_cost:.2f} deducted for {ride_name}.", main_menu_frame)
    elif not verify:
        complete_action_frame("Incorrect Pin.", main_menu_frame)
    else:
        complete_action_frame("Insufficient balance!", main_menu_frame)

def top_up_card():
    """Top up card and update balance. (PLACEHOLDER)"""
    try:
        top_up_amount = float(top_up_entry.get())  # Get the top-up amount
        _, bal, _ = read_card()
        if top_up_amount>100:
            top_up_entry.delete(0, tk.END)  # Clear the entry box after submission
            complete_action_frame(f"You can only add £100\nat a time", main_menu_frame)
        elif float(top_up_amount)<0:
            top_up_entry.delete(0, tk.END)  # Clear the entry box after submission
            complete_action_frame(f"You cannot input\nnegative values", main_menu_frame)
        elif float(bal+top_up_amount)<=999.99:
            write_card("+bal", top_up_amount)  # Top up the card
            update_balance_label()
            top_up_entry.delete(0, tk.END)  # Clear the entry box after submission
            complete_action_frame(f"£{top_up_amount:.2f} added to your card.", main_menu_frame)
        else:
            top_up_entry.delete(0, tk.END)  # Clear the entry box after submission
            complete_action_frame(f"You cannot have more than\n£999.99 on your card.", main_menu_frame)
    except ValueError:
        complete_action_frame("Please enter a valid amount.", main_menu_frame)

def change_pin():
    """Change card PIN."""
    show_frame(pin_frame)
    new_pin = change_pin_entry.get()
    if new_pin.isdigit() and len(new_pin) > 3:
        write_card("pin", new_pin)  # Update the card's PIN
        complete_action_frame("PIN successfully changed!", main_menu_frame)
    else:
        complete_action_frame("Invalid PIN! Must be longer than 3 digits.", main_menu_frame)

def check_pin() -> bool:
    """Check card PIN."""
    usr_pin = pin_entry.get()
    _, _, pin = read_card()
    print(pin, "+", usr_pin)
    try:
        if int(usr_pin) == int(pin):
            return True
        else:
            return False
    except ValueError:
        return False

# Define a container for frames
container = tk.Frame(root)
container.pack(fill="both", expand=True)

# Create frames (Main Menu, Top-Up, Ride Selection, Loading, Completed Action, PIN Change)
main_menu_frame = tk.Frame(container)
top_up_frame = tk.Frame(container)
ride_selection_frame = tk.Frame(container)
loading_frame = tk.Frame(container)
complete_frame = tk.Frame(container)
pin_frame = tk.Frame(container)
change_pin_frame = tk.Frame(container)

for frame in (main_menu_frame, top_up_frame, ride_selection_frame, loading_frame, complete_frame, pin_frame, change_pin_frame):
    frame.grid(row=0, column=0, sticky="nsew")

# --- Main Menu Frame ---
name, balance, _ = read_card()
balance_label = tk.Label(main_menu_frame, text=f"Hi {name}\nBalance: £{balance:.2f}", font=("Helvetica", 24))
balance_label.pack(padx=(100, 10), pady=20, side="right")

pay_button = tk.Button(main_menu_frame, text="Pay for Ride", command=lambda: show_frame(ride_selection_frame), width=30, height=2)
pay_button.pack(padx=(10, 10), pady=(100, 10))

top_up_button = tk.Button(main_menu_frame, text="Top Up Card", command=lambda: show_frame(top_up_frame), width=30, height=2)
top_up_button.pack(padx=(10, 10), pady=10)

change_pin_button = tk.Button(main_menu_frame, text="Change PIN", command=lambda: show_frame(pin_frame), width=30, height=2)
change_pin_button.pack(padx=(10, 10), pady=(10, 100))

# --- Top-Up Frame ---
top_up_label = tk.Label(top_up_frame, text="Enter top-up amount:", font=("Helvetica", 18))
top_up_label.pack(pady=5)

top_up_entry = tk.Entry(top_up_frame, font=("Helvetica", 18))
top_up_entry.pack(pady=5)

submit_top_up_button = tk.Button(top_up_frame, text="Submit Top-Up", command=top_up_card, width=20)
submit_top_up_button.pack(pady=10)

back_to_menu_button = tk.Button(top_up_frame, text="Back to Main Menu", command=lambda: show_frame(main_menu_frame), width=20)
back_to_menu_button.pack(pady=10)

# --- Ride Selection Frame ---
ride_label = tk.Label(ride_selection_frame, text="Select a Ride:", font=("Helvetica", 24))
ride_label.pack(pady=20)

for ride_name, ride_cost in rides.items():
    ride_button = tk.Button(ride_selection_frame, text=f"{ride_name} (£{ride_cost:.2f})", 
                            command=lambda r=ride_name, c=ride_cost: pay_for_ride(r, c), width=30, height=2)
    ride_button.pack(pady=5)

pin_label = tk.Label(ride_selection_frame, text="Enter new PIN:", font=("Helvetica", 18))
pin_label.pack(pady=10)

pin_entry = tk.Entry(ride_selection_frame, font=("Helvetica", 18), show="*")
pin_entry.pack(pady=10)

back_to_menu_button = tk.Button(ride_selection_frame, text="Back to Main Menu", command=lambda: show_frame(main_menu_frame), width=20)
back_to_menu_button.pack(pady=10)

# --- Loading Frame ---
loading_label = tk.Label(loading_frame, text="Loading...", font=("Helvetica", 24))
loading_label.pack(pady=20)

# --- Completed Action Frame ---
complete_label = tk.Label(complete_frame, text="Action Completed!", font=("Helvetica", 24))
complete_label.pack(pady=20)

# --- PIN Change Frame ---
pin_label = tk.Label(change_pin_frame, text="Enter new PIN:", font=("Helvetica", 18))
pin_label.pack(pady=10)

change_pin_entry = tk.Entry(change_pin_frame, font=("Helvetica", 18), show="*")
change_pin_entry.pack(pady=10)

submit_pin_button = tk.Button(change_pin_frame, text="Submit PIN", command=change_pin, width=20)
submit_pin_button.pack(pady=10)

back_to_menu_button = tk.Button(change_pin_frame, text="Back to Main Menu", command=lambda: show_frame(main_menu_frame), width=20)
back_to_menu_button.pack(pady=10)

# Show the main menu initially
show_frame(main_menu_frame)

# Start the GUI event loop
root.mainloop()