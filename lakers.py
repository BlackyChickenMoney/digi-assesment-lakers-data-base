# Import the libraries to connect to the database and present the information in tables
import sqlite3
from tabulate import tabulate

# This is the filename of the database to be used
DB_NAME = 'lakers.db'

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
    menu_choice = input('Welcome to the lakers database\n\n' 
                        'Type the letter for the information you want:\n' 
                        'A: Alex stats\n' 
                        'B: Austin stats\n' 
                        'C: Bronny stats\n' 
                        'D: Christian stats\n' 
                        'E: Dalton stats\n' 
                        'F: Dorian stats\n' 
                        'G: Gabe stats\n' 
                        'H: Jarred stats\n' 
                        'I: Jaxson stats\n' 
                        'J: Jordan stats\n' 
                        'K: Lebron stats\n' 
                        'L: Luka stats\n' 
                        'M: Markieff stats\n' 
                        'N: Maxi stats\n' 
                        'O: Rui stats\n' 
                        'P: Shake stats\n' 
                        'Q: Trey stats\n'
                        'R: most apg career\n' 
                        'S: most apg season\n' 
                        'T: most ppg career\n'  
                        'U: most ppg season\n' 
                        'V: most rpg career\n' 
                        'W: most rpg season\n' 
                        'X: player position\n' 
                        'Y: tallest players in the lakers\n'  
                        'Z: Exit\n\n'
                        'Type option here: ') 
    menu_choice = menu_choice.upper()
    if menu_choice == 'A':
        print_query('Alex stats')
    elif menu_choice == 'B':
         print_query('Austin stats')
    elif menu_choice == 'C':
         print_query('Bronny stats')
    elif menu_choice == 'D':
         print_query('Christian stats')     
    elif menu_choice == 'E':
         print_query('Dalton stats')    
    elif menu_choice == 'F':
         print_query('Dorian stats')      
    elif menu_choice == 'G':
         print_query('Gabe stats') 
    elif menu_choice == 'H':
         print_query('Jarred stats') 
    elif menu_choice == 'I':
         print_query('Jaxson stats') 
    elif menu_choice == 'J':
         print_query('Jordan stats')   
    elif menu_choice == 'K':
         print_query('Lebron stats')  
    elif menu_choice == 'L':
         print_query('Luka stats')     
    elif menu_choice == 'M':
         print_query('Markieff stats')    
    elif menu_choice == 'N':
         print_query('Maxi stats')    
    elif menu_choice == 'O':
         print_query('Rui stats') 
    elif menu_choice == 'P':
         print_query('Shake stats')        
    elif menu_choice == 'Q':
         print_query('Trey stats') 
    elif menu_choice == 'R':
         print_query('most apg career') 
    elif menu_choice == 'S':
         print_query('most apg season') 
    elif menu_choice == 'T':
         print_query('most ppg career') 
    elif menu_choice == 'U':
         print_query('most ppg season')   
    elif menu_choice == 'V':
         print_query('most rpg career')  
    elif menu_choice == 'W':
         print_query('most rpg season')  
    elif menu_choice == 'X':
         print_query('player position')       
    elif menu_choice == 'Y':
         print_query('tallest players in the lakers')               
    elif menu_choice == 'Z':
         print('Goodbye Lads')
