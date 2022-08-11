from tkinter import *
from tkinter import messagebox
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
import random


def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = []

    pass_list_1 = [random.choice(letters) for char in range(nr_letters)]

    pass_list_2 = [random.choice(symbols) for c in range(nr_symbols)]

    pass_list_3 = [random.choice(numbers) for ch in range(nr_numbers)]

    password_list = pass_list_1 + pass_list_2 + pass_list_3

    random.shuffle(password_list)

    password = ""
    for char in password_list:
        password += char

    pass_entry.insert(0, password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showwarning(title=website_entry.get(), message=f"Please don't "
                                                                  f"leave any empty fields")
    else:
        try:
            with open("data.json", "r") as file:
                # Read old data
                data = json.load(file)
                # Update old data with new data
                data.update(new_data)
        except:
            with open("data.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            with open("data.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            website_entry.delete(0, "end")
            email_entry.delete(0, "end")
            pass_entry.delete(0, "end")

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title=website_entry.get(), message="No Data File Found")
    else:
        if website in data:
            password = data[website]["password"]
            email = data[website]["email"]
            messagebox.showinfo(title=website_entry.get(), message=f"Email: {email} \n"
                                                                   f"Password: {password}")
        else:
            messagebox.showinfo(title="Error", message=f"No details for {website} exists.")




# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_image)
canvas.grid(row=0, column=0, columnspan=3)

website_text = Label(text='Website:', padx=20)
website_text.grid(row=1, column=0, sticky="E")

email_text = Label(text='Email/Username:', padx=20)
email_text.grid(row=2, column=0, sticky="E")

password_text = Label(text='Password:', padx=20)
password_text.grid(row=3, column=0, sticky="E")

website_entry = Entry(width=21)
website_entry.grid(row=1, column=1, columnspan=2, sticky="W")
website_entry.focus()

email_entry = Entry(width=42)
email_entry.grid(row=2, column=1, columnspan=2, sticky="W")
email_entry.insert(0, "sekhukhune056@gmail.com")

pass_entry = Entry(width=21)
pass_entry.grid(row=3, column=1, sticky='W')

search_button = Button(text="Search", width=16, command=find_password)
search_button.grid(row=1, column=2, sticky='W')

gen_pass_button = Button(text='Generate Password', width=16, command=generate_password)
gen_pass_button.grid(row=3, column=2, sticky='W')

add_button = Button(text='Add', width=35, command=save)
add_button.grid(row=4, column=1, columnspan=2, sticky="W")

window.mainloop()
