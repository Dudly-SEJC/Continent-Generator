# This Program asks for a user's country of origin and the output will generate their continent through a message box

# This program is a combination of codes from ('Module 5 - Assignment 1, Version 3.5 ChatGPT recommendations, & a guide-
# -to a calculator program from https://www.simplifiedpython.net/python-calculator/

import tkinter as tk
from tkinter import messagebox

# Sets a list of countries that will provide an output of continents
def get_continent(country):
    # Dictionary of countries along with their designated continents
    # Countries are on the left of the ':' and continents on the right
    # I added more options from the original list of a library countries to continents created by ChatGPT
    continent_mapping = {
        'United States': 'North America',
        'U.S.': 'North America',
        'Canada': 'North America',
        'Phillipines': 'Asia',
        'India': 'Asia',
        'Japan': 'Asia',
        'Brazil': 'South America',
        'Egypt': 'Africa',
        'United Kingdom': 'Europe',
        'Zimbabwe': 'Africa',
        'South Africa': 'Africa',
        'New Zealand': 'Australia',
        'Papua New Guinea': 'Australia',
        'Argentina': 'South America',
        'Bolivia': 'South America',
        'France': 'Europe',
        'Italy': 'Europe'
        # Can add more countries and continental origins
    }

    # Checks if the provided country is in the dictionary, Uses If, Else functions
    # Continent_mapping is set as a variable
    if country in continent_mapping:
        return continent_mapping[country]
    else:
        return 'Continent or Country Not found'

# The output of the continent is presented in this message box, with country and continents set from the library above
def show_continent():
    country = entry.get()
    continent = get_continent(country)
    messagebox.showinfo('Continent', f'{country} is a country located in {continent}')

# Creates the main window
# I changed the size of the window to make GUI more presentable
#referenced from Module 5 - Assignment 1
root = tk.Tk()
root.title('Continent Finder')
root.geometry('300x200')
root.configure(background='powder blue')

# A label that says 'Enter Your Country'
# I edited the font, size, & color to make GUI more presentable
label = tk.Label(root, text='Enter Your Country:', background='papaya whip', font=('ds-digital', 15))
label.pack(pady=10)

# Asks for Country Input
# I edited the font, size, & color to make GUI more presentable
# entry referenced from link provided
entry = tk.Entry(root, background='light green', font=('Arial Italic', 12))
entry.pack(pady=10)

# Label for finding continent output
# I edited the font, size, & color to make GUI more presentable
# widget referenced from link provided
button = tk.Button(root, text='Find Continent', command=show_continent, background='papaya whip', font=('Arial Bold', 15))
button.pack(pady=20)

# Start the main loop
root.mainloop()