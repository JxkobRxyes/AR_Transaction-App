#Jakob Reyes
#11/10/20
#019.1

from tkinter import *
from tkinter.ttk import *
import sqlite3

root = Tk()
root.title("A/R Transaction")
root.geometry("320x175")

# Creating database
conn = sqlite3.connect('Records.db')

# cursor to run sql commands
c = conn.cursor()

'''
#Invoice table
c.execute("""CREATE TABLE invoices (
            customer_num integer,
            customer_name text,
            invoice_num integer,
            invoice_date numeric,
            invoice_amount text
            )""")
'''

# Submit button action
def submit():
    conn = sqlite3.connect('Records.db')
    c = conn.cursor()

    # Insert to table
    c.execute("INSERT INTO invoices VALUES (:c_num, :c_name, :i_num, :i_date, :i_amount)",
              {
                 'c_num': c_num.get(),
                  'c_name': c_name.get(),
                  'i_num': i_num.get(),
                  'i_date': i_date.get(),
                  'i_amount': i_amount.get()
                 })
    conn.commit()
    conn.close()

    # deletes input after submit button is clicked
    c_num.delete(0, END)
    c_name.delete(0, END)
    i_num.delete(0, END)
    i_date.delete(0, END)
    i_amount.delete(0, END)

# function that create libraries
def library():
    conn = sqlite3.connect('Records.db')
    c = conn.cursor()

    # query database
    c.execute("SELECT *, oid FROM invoices")
    records = c.fetchall()
    
    print_records = ''

    for item in records:
        print_records += str(item[0]) + '   ' + str(item[1]) + '   ' + str(item[2]) + '   ' + str(item[3]) + '   ' + str(item[4]) + "\n"

    # Database window to show all records
    dew = Toplevel(root)
    dew.title("Data Entry Form")
    dew.geometry("400x400")

    Label(dew, text=print_records).pack() # Edit on label column and row 

    # Exit function for database window
    def exit():
        dew.destroy()
    
    # Exit button for database window
    db_exit_btn = Button(dew, text="Exit", command=exit).pack()
    
    
    conn.commit()
    conn.close()

# exit function for main window
def mainExit():
    conn = sqlite3.connect('Records.db')
    c = conn.cursor()

    root.destroy()

    conn.commit()
    conn.close()
    
# Create text box labels
c_num_label = Label(root, text="Customer Number")
c_name_label = Label(root, text="Customer Name")
i_num_label = Label(root, text="Invoice Number")
i_date_label = Label(root, text="Invoice Date")
i_amount_label = Label(root, text="Invoice Amount")

# Create input
c_num = Entry(root, width=30)
c_name = Entry(root, width=30)
i_num = Entry(root, width=30)
i_date = Entry(root, width=30)
i_amount = Entry(root, width=30)

# Create submit button and layout
submit_btn = Button(root, text="Submit", command=submit)
submit_btn.grid(row=5, column=0)

# Create a view button and layout
view_btn = Button(root, text="View", command=library)
view_btn.grid(row=5, column=1, padx=10, pady=5, sticky=W)

# Exit button for main window
main_exit = Button(root, text="Exit", command=mainExit)
main_exit.grid(row=5, column=1, pady=5, sticky=E)

# labels grid layout
c_num_label.grid(row=0, column=0, sticky=W, pady=(10, 0))
c_name_label.grid(row=1, column=0, sticky=W)
i_num_label.grid(row=2, column=0, sticky=W)
i_date_label.grid(row=3, column=0, sticky=W)
i_amount_label.grid(row=4, column=0, sticky=W)

# Input field layout
c_num.grid(row=0, column=1, padx=(10, 0),pady=(10, 0))
c_name.grid(row=1, column=1, padx=(10, 0))
i_num.grid(row=2, column=1, padx=(10, 0))
i_date.grid(row=3, column=1, padx=(10, 0))
i_amount.grid(row=4, column=1, padx=(10, 0))

# Commits current transaction
conn.commit()

# Closes database
conn.close()

root.mainloop()
        
              
