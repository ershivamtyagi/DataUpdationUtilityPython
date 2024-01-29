import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import font
import mysql.connector
def create_connection():
    # Create and return a connection object
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="database_for_ds_questions"
    )

def insert_data():
    question = entry_question.get()
    description = text_description.get("1.0", tk.END)

   # Connect to your MySQL database
    conn = create_connection()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Define your SQL query to insert data
    query = "INSERT INTO daily_questions (question, description) VALUES (%s, %s)"
    data = (question, description)

    # Execute the query
    cursor.execute(query, data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Clear the entry fields after inserting data
    #entry_question.delete(0, tk.END)
    #text_description.delete("1.0", tk.END)

def display_data():
   # Connect to your MySQL database
    conn = create_connection()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Define your SQL query to retrieve data
    query = "SELECT * FROM daily_questions"

    # Execute the query
    cursor.execute(query)

    # Fetch all rows from the result set
    rows = cursor.fetchall()

    # Display the data in a separate window or console
    for row in rows:
        print(row)

    # Close the connection
    conn.close()

def update_data():
    # Connect to your MySQL database
    conn = create_connection()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Get values from entry fields
    day_id = entry_day_id.get()
    new_description = text_new_description.get("1.0", tk.END)
    intuition = entry_intuition.get()
    new_brute_force = text_new_brute_force.get("1.0", tk.END)
    new_complexitybf = text_new_complexitybf.get("1.0", tk.END)
    new_better1 = text_new_better1.get("1.0", tk.END)
    new_complexity_b = text_new_better1_bf.get("1.0", tk.END)
    new_optimal = text_new_optimal.get("1.0", tk.END)
    new_complexity_o = text_new_optimal_bf.get()
    
    # Define your SQL query to update data
    query = "UPDATE daily_questions SET description = %s, intuition = %s, brute_force = %s, complexitybf = %s, better1 = %s, complexity_b = %s, optimal = %s, complexity_o = %s  WHERE day_id = %s"
    data = (new_description, intuition, new_brute_force, new_complexitybf, new_better1, new_complexity_b, new_optimal, new_complexity_o, day_id)

    # Execute the query
    cursor.execute(query, data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Clear the entry fields after updating data
    entry_day_id.delete(0, tk.END)
    text_new_description.delete("1.0", tk.END)

def delete_data():
    # Connect to your MySQL database
    conn = create_connection()

    # Create a cursor object to execute SQL queries
    cursor = conn.cursor()

    # Get value from entry field
    day_id = entry_day_id_delete.get()

    # Define your SQL query to delete data
    query = "DELETE FROM daily_questions WHERE day_id = %s"
    data = (day_id,)

    # Execute the query
    cursor.execute(query, data)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Clear the entry field after deleting data
    entry_day_id_delete.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("MySQL Data Entry App")
# Create a vertical scrollbar
scrollbar = ttk.Scrollbar(root, orient="vertical")
# Create a canvas to hold the widgets
canvas = tk.Canvas(root, yscrollcommand=scrollbar.set)
# Create a frame inside the canvas to hold the widgets
frame = ttk.Frame(canvas)

# Add the frame to the canvas window
canvas.create_window((0, 0), window=frame, anchor="nw")

#canvas.grid(side="left", fill="both", expand=True)

# Configure the scrollbar to work with the canvas
scrollbar.config(command=canvas.yview)

# Create a frame inside the canvas to hold the widgets
frame = ttk.Frame(canvas)

# Add the frame to the canvas window
canvas.create_window((0, 0), window=frame, anchor="nw")


# Create labels and entry fields for insert operation
# label_question = ttk.Label(root, text="Question:")
#label_question.grid(row=0, column=0, padx=10, pady=5)
#entry_question = ttk.Entry(root)
#entry_question.grid(row=0, column=1, padx=10, pady=5)

#label_description = ttk.Label(root, text="Description:")
#label_description.grid(row=1, column=0, padx=10, pady=5)
#text_description = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
#text_description.grid(row=1, column=1, padx=10, pady=5)

#insert_button = ttk.Button(root, text="Insert Data", command=insert_data)
#insert_button.grid(row=2, column=0, columnspan=2, pady=5)

# Create labels and entry fields for display operation
#display_button = ttk.Button(root, text="Display Data", command=display_data)
#display_button.grid(row=3, column=0, columnspan=2, pady=5)

# Create labels and entry fields for update operation
label_day_id = ttk.Label(root, text="Day ID:")
label_day_id.grid(row=4, column=0, padx=10, pady=5)
entry_day_id = ttk.Entry(root)
entry_day_id.grid(row=4, column=1, padx=10, pady=5)

# Tags
label_intuition = ttk.Label(root, text="New Tags:")
label_intuition.grid(row=4, column=2, padx=10, pady=5)
entry_intuition = ttk.Entry(root)
entry_intuition.grid(row=4, column=3, padx=10, pady=5)


label_new_description = ttk.Label(root, text="New Description:")
label_new_description.grid(row=5, column=0, padx=10, pady=5)
text_new_description = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_new_description.grid(row=5, column=1, padx=10, pady=5)



# Brute Force Solution text_new_brute_force
label_text_new_brute_force = ttk.Label(root, text="New Brute Force Solution:")
label_text_new_brute_force.grid(row=5, column=2, padx=10, pady=5)
text_new_brute_force = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_new_brute_force.grid(row=5, column=3, padx=10, pady=5)

# Brute Force complexity text_new_complexitybf
label_text_new_complexitybf = ttk.Label(root, text="New Brute Force Solution Complexity:")
label_text_new_complexitybf.grid(row=6, column=0, padx=10, pady=5)
text_new_complexitybf = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_new_complexitybf.grid(row=6, column=1, padx=10, pady=5)

# text_new_better1
label_text_new_better1 = ttk.Label(root, text="New Better Solution :")
label_text_new_better1.grid(row=6, column=2, padx=10, pady=5)
text_new_better1 = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_new_better1.grid(row=6, column=3, padx=10, pady=5)

# text_new_better1 complexity
label_text_new_better1_bf = ttk.Label(root, text="New Better Solution :")
label_text_new_better1_bf.grid(row=7, column=0, padx=10, pady=5)
text_new_better1_bf = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_new_better1_bf.grid(row=7, column=1, padx=10, pady=5)

# text_new_optimal
label_text_new_optimal = ttk.Label(root, text="New Better Solution :")
label_text_new_optimal.grid(row=7, column=2, padx=10, pady=5)
text_new_optimal = scrolledtext.ScrolledText(root, width=50, height=10, wrap=tk.WORD)
text_new_optimal.grid(row=7, column=3, padx=10, pady=5)

# text_new_optimal
label_text_new_optimal_bf = ttk.Label(root, text="New Better Solution bf :")
label_text_new_optimal_bf.grid(row=8, column=0, padx=10, pady=5)
text_new_optimal_bf = ttk.Entry(root)
text_new_optimal_bf.grid(row=8, column=1, padx=10, pady=5)

# update button
update_button = ttk.Button(root, text="Update Data", command=update_data)
update_button.grid(row=9, column=0, columnspan=2, pady=5)

# Create labels and entry fields for delete operation
label_day_id_delete = ttk.Label(root, text="Day ID:")
label_day_id_delete.grid(row=10, column=0, padx=10, pady=5)
entry_day_id_delete = ttk.Entry(root)
entry_day_id_delete.grid(row=10, column=1, padx=10, pady=5)

delete_button = ttk.Button(root, text="Delete Data", command=delete_data)
delete_button.grid(row=11, column=0, columnspan=2, pady=5)

# Add a dummy widget to determine the frame's size
dummy_label = ttk.Label(frame, text="")
dummy_label.grid(row=100, column=0, pady=10)

# Bind the event to adjust the canvas scrolling region
frame.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Start the Tkinter event loop
root.mainloop()
