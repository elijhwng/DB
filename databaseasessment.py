# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'phones.db'

def print_query(view_name:str):
    ''' Prints the specified view from the database in a table '''
    # Set up the connection to the database
    db = sqlite3.connect(DB_NAME)
    cursor = db.cursor()
    # Get the results from the view
    sql = "SELECT * FROM '" + view_name + "'"
    cursor.execute(sql)
    results = cursor.fetchall()
    # Get the field names to use as headings
    field_names = "SELECT name from pragma_table_info('" + view_name + "') AS tblInfo"
    cursor.execute(field_names)
    headings = list(sum(cursor.fetchall(),()))
    # Print the results in a table with the headings
    print(tabulate(results,headings))
    db.close()

menu_choice =''
while menu_choice != 'Z':
    menu_choice = input('Welcome to the Phones database\n\n'
                        'Type the letter for the information you want:\n'
                        'A: All phones and informations\n'
                        'B: Phones made by Apple\n'
                        'C: The brand and model for all phones\n'
                        'D: The least expensive phones\n'
                        'E: The phones with amount bought over 400000 and excluding xiaomi\n'
                        'F: The phones with amount bought less than 400000 and the price of less than 1200\n'
                        'G: Phones that are from China and South Korea\n'
                        'H: Phones that are not Apple\n'
                        'Z: Exit\n\nType option here: ')
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('all phones')
    elif menu_choice == 'B':
        print_query('only apple')
    elif menu_choice == 'C':
        print_query('brand and model')
    elif menu_choice == 'D':
        print_query('least expensive')
    elif menu_choice == 'E':
        print_query('amount bought over 400000 excluding xiaomi')
    elif menu_choice == 'F':
        print_query('amount bought less than 400000 and price of less than 1200')
    elif menu_choice == 'G':
        print_query('south korea and china')
    elif menu_choice == 'H':
        print_query('excluding apple')
print('Thank you for using me!🙂')