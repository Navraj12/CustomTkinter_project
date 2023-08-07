from customtkinter import * # Importing customtkinter library for custom Tkinter widgets
from PIL import ImageTk, Image, ImageFilter # Importing necessary classes from PIL library
from tkinter import ttk # Importing ttk module from Tkinter for themed widgets
import mysql.connector # Importing MySQL Connector/Python module for database connectivity


set_appearance_mode("dark") # Set the appearance mode to dark theme for customtkinter
set_default_color_theme("green") # Set the default color theme to green for customtkinter

root= CTk() # Create the root/main window using customtkinter CTk class
root.geometry("600x400") # Set the size of the root window to 600x400

# Load image icons and create CTkImage objects with the specified size
img1= CTkImage(Image.open("edit.png"), size=(20,20))
img2= CTkImage(Image.open("delete.png"), size=(20,20))
img3= CTkImage(Image.open("add.png"), size=(20,20))
img4= CTkImage(Image.open("view.png"), size=(20,20))
img5 = CTkImage(Image.open("back.png"), size=(20,20))

count=1
fram= None
fram2 = None
lc=CTkLabel(master=fram)
# Create a label for the title "XYZ company Database"
l1 = CTkLabel(master=root, text="XYZ company Database", font=("Bell MT", 19)).pack(padx=10, pady=20, side =TOP)

# Configure the Treeview widget style for custom appearance
style = ttk.Style()
style.configure("Treeview", background="#242424", foreground="white", fieldbackground="white")
style.map("Treeview", background=[('selected', 'blue')])

# Create a Treeview widget for displaying data
tree = ttk.Treeview()

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host='localhost',
    user='root',
    password='nraraja123@',
    database='project_sample'
)
# Create a cursor to execute SQL queries
cursor = db_connection.cursor()


# This function is called when the program starts or when returning from other views
def front():
    # Use the global keyword to modify the global variable 'fra'
    global fra
    
    # Create a frame named 'fra' with a specified foreground color
    fra = CTkFrame(master=root, fg_color="#242424")
    fra.pack(pady=20, fill=BOTH)
    
    # Create a label 'l1' with the text "Welcome" and a specified font
    l1 = CTkLabel(master=fra, text="Welcome", font=("Bell MT", 19))
    l1.pack(padx=20, pady=10)
    
    # This function 'a_login()' is called when the "Admin" button is clicked
    def a_login():
        # Hide the current frame 'fra'
        fra.pack_forget()
        
        # Use the global keyword to modify the global variable 'fram'
        global fram
        
        # Create a new frame named 'fram' with a specified foreground color
        fram = CTkFrame(master=root, fg_color="#242424")
        fram.pack(pady=20, fill=BOTH)
        
        # Create a new frame 'g' inside 'fram' to hold the back button (bt1)
        g = CTkFrame(master=fram, fg_color="#242424")
        g.pack(pady=1, anchor=E)
        
        # Create a back button 'bt1' with a specified image, font, and command
        bt1 = CTkButton(master=g, image=img5, text="", font=("Bell MT", 19), width=1, command=back_P)
        bt1.pack(side=RIGHT, padx=1)
        
        # Create a label 'l' inside 'fram' with the text "Admin Login:" and a specified font
        l = CTkLabel(master=fram, text="Admin Login:", font=("Bell MT", 19))
        l.pack(padx=20, pady=10)
        
        # Create an entry field 'u' inside 'fram' for the username with a specified font
        u = CTkEntry(master=fram, placeholder_text="Username", font=("Bell MT", 19))
        u.pack(padx=20, pady=20)
        
        # Create an entry field 'p1' inside 'fram' for the password with a specified font
        # Store 'p1' as a property of the 'front' function to access it later
        front.p1 = CTkEntry(master=fram, placeholder_text="Password", font=("Bell MT", 19))
        front.p1.pack(padx=20, pady=20)
        front.p1.configure(show="*")  # Show password characters as asterisks
        
        # Create a button 'b2' inside 'fram' with the text "Submit", a specified font, and a command 'normal'
        b2 = CTkButton(master=fram, text="Submit", font=("Bell MT", 19), command=normal)
        b2.pack(padx=20, pady=20)
        
        # Bind events to focus-in on the entry fields to modify the label 'l' text
        u.bind("<FocusIn>", lambda s: l.configure(text="Username:"))
        u.bind("<Return>", lambda s: front.p1.focus())  # Pressing Return moves focus to the password entry
        front.p1.bind("<FocusIn>", lambda s: l.configure(text="Password:"))
        front.p1.bind("<Return>", lambda s: conf(u, front.p1))  # Pressing Return calls 'conf' function with entries 'u' and 'p1'
    
    # Create an "Admin" button 'b1' inside 'fra' with a specified font and a command 'a_login'
    b1 = CTkButton(master=fra, text="Admin", font=("Bell MT", 19), command=a_login)
    b1.pack(padx=20, pady=20)
    
    # Create a "Login As Customer" button 'b' inside 'fra' with a specified font and a command 'normal'
    b = CTkButton(master=fra, text="Login As Customer", font=("Bell MT", 19), command=normal)
    b.pack(padx=20, pady=20)


# This function is called when the user logs in as an admin
def admin():
    # Hide the current frame 'fram'
    fram.pack_forget()
    
    # Use the global keyword to modify the global variable 'fram2'
    global fram2
    
    # Create a new frame named 'fram2' with a specified foreground color
    fram2 = CTkFrame(master=root, fg_color="#242424")
    fram2.pack(fill=BOTH)
    
    # Create a new frame 'g' inside 'fram2' to hold the back button (bt1)
    g = CTkFrame(master=fram2, fg_color="#242424")
    g.pack(pady=1, anchor=E)
    
    # Create a label 'l1' inside 'fram2' with the text "Welcome Admin" and a specified font
    l1 = CTkLabel(master=fram2, text="Welcome Admin", font=("Bell MT", 19))
    l1.pack(padx=60, anchor=N)
    
    # Create a back button 'bt1' with a specified image, font, and command 'back'
    bt1 = CTkButton(master=g, image=img5, text="", font=("Bell MT", 19), width=1, command=back)
    bt1.pack(side=RIGHT, padx=1)
    
    # Create a new frame 'fr' inside 'fram2' with a specified height, width, and foreground color
    fr = CTkFrame(master=fram2, height=10, width=1, fg_color="#242424")
    fr.pack(padx=60, pady=20, anchor=N)
    
    # Create a label 'l2' inside 'fr' with the text "Musician" and a specified font, then pack it to the left
    l2 = CTkLabel(master=fr, text="Musician", font=("Bell MT", 19)).pack(side=LEFT, padx=10)
    
    # Create buttons 'b1', 'b2', 'b3', 'b4' inside 'fr' with specified images, widths, and commands
    # The lambda functions are used to pass different arguments to the 'edit', 'delete', 'add', and 'view' functions
    b1 = CTkButton(master=fr, image=img1, text="", width=1, command=lambda: edit("M")).pack(side=RIGHT, padx=1)
    b2 = CTkButton(master=fr, image=img2, text="", width=1, command=lambda: delete("M")).pack(side=RIGHT, padx=1)
    b3 = CTkButton(master=fr, image=img3, text="", width=1, command=lambda: add("M")).pack(side=RIGHT, padx=1)
    b4 = CTkButton(master=fr, image=img4, text="", width=1, command=lambda: view("M", "A")).pack(side=RIGHT, padx=1)
    
    # Create a new frame 'fra' inside 'fram2' with a specified height, width, and foreground color
    fra = CTkFrame(master=fram2, height=10, width=1, fg_color="#242424")
    fra.pack(padx=60, pady=20, anchor=N)
    
    # Create a label 'l3' inside 'fra' with the text "Song" and a specified font, then pack it to the left
    l3 = CTkLabel(master=fra, text="Song", font=("Bell MT", 19)).pack(side=LEFT, padx=10)
    
    # Create buttons 'c1', 'c2', 'c3', 'c4' inside 'fra' with specified images, widths, and commands
    # The lambda functions are used to pass different arguments to the 'edit', 'delete', 'add', and 'view' functions
    c1 = CTkButton(master=fra, image=img1, text="", width=1, command=lambda: edit("S")).pack(side=RIGHT, padx=1)
    c2 = CTkButton(master=fra, image=img2, text="", width=1, command=lambda: delete("S")).pack(side=RIGHT, padx=1)
    c3 = CTkButton(master=fra, image=img3, text="", width=1, command=lambda: add("S")).pack(side=RIGHT, padx=1)
    c4 = CTkButton(master=fra, image=img4, text="", width=1, command=lambda: view("S", "A")).pack(side=RIGHT, padx=1)
    
    # Create a new frame 'f' inside 'fram2' with a specified height, width, and foreground color
    f = CTkFrame(master=fram2, height=10, width=1, fg_color="#242424")
    f.pack(padx=60, pady=20, anchor=N)
    
    # Create a label 'l4' inside 'f' with the text "Instrument" and a specified font, then pack it to the left
    l4 = CTkLabel(master=f, text="Instrument", font=("Bell MT", 19)).pack(side=LEFT, padx=10)
    
    # Create buttons 'd1', 'd2', 'd3', 'd4' inside 'f' with specified images, widths, and commands
    # The lambda functions are used to pass different arguments to the 'edit', 'delete', 'add', and 'view' functions
    d1 = CTkButton(master=f, image=img1, text="", width=1, command=lambda: edit("I")).pack(side=RIGHT, padx=1)
    d2 = CTkButton(master=f, image=img2, text="", width=1, command=lambda: delete("I")).pack(side=RIGHT, padx=1)
    d3 = CTkButton(master=f, image=img3, text="", width=1, command=lambda: add("I")).pack(side=RIGHT, padx=1)
    d4 = CTkButton(master=f, image=img4, text="", width=1, command=lambda: view("I", "A")).pack(side=RIGHT, padx=1)
    
    # Create a new frame 'fa' inside 'fram2' with a specified height, width, and foreground color
    fa = CTkFrame(master=fram2, height=10, width=1, fg_color="#242424")
    fa.pack(padx=60, pady=20, anchor=N)
    
    # Create a label 'l5' inside 'fa' with the text "Album" and a specified font, then pack it to the left
    l5 = CTkLabel(master=fa, text="Album", font=("Bell MT", 19)).pack(side=LEFT, padx=10)
    
    # Create buttons 'e1', 'e2', 'e3', 'e4' inside 'fa' with specified images, widths, and commands
    # The lambda functions are used to pass different arguments to the 'edit', 'delete', 'add', and 'view' functions
    e1 = CTkButton(master=fa, image=img1, text="", width=1, command=lambda: edit("A")).pack(side=RIGHT, padx=1)
    e2 = CTkButton(master=fa, image=img2, text="", width=1, command=lambda: delete("A")).pack(side=RIGHT, padx=1)
    e3 = CTkButton(master=fa, image=img3, text="", width=1, command=lambda: add("A")).pack(side=RIGHT, padx=1)
    e4 = CTkButton(master=fa, image=img4, text="", width=1, command=lambda: view("A", "A")).pack(side=RIGHT, padx=1)


# This function is called when the user logs in as a normal customer
def normal():
    # Hide the current frame 'fra'
    fra.pack_forget()
    
    # Use the global keyword to modify the global variable 'framn'
    global framn
    
    # Create a new frame named 'framn' with a specified foreground color
    framn = CTkFrame(master=root, fg_color="#242424")
    framn.pack(fill=BOTH)
    
    # Create a new frame 'g' inside 'framn' to hold the back button (bt1)
    g = CTkFrame(master=framn, fg_color="#242424")
    g.pack(pady=1, anchor=E)
    
    # Create a label 'l1' inside 'framn' with the text "Welcome Customer" and a specified font
    l1 = CTkLabel(master=framn, text="Welcome Customer", font=("Bell MT", 19))
    l1.pack(padx=60, anchor=N)
    
    # Create a back button 'bt1' with a specified image, font, and command 'back_N'
    bt1 = CTkButton(master=g, image=img5, text="", font=("Bell MT", 19), width=1, command=back_N)
    bt1.pack(side=RIGHT, padx=1)
    
    # Create buttons 'bt2', 'bt3', 'bt4', 'bt5' inside 'framn' with specified texts and commands
    # The lambda functions are used to pass different arguments to the 'view' function for different data types
    bt2 = CTkButton(master=framn, text="Musician", font=("Bell MT", 19), command=lambda: view("M", "N")).pack(padx=20, pady=20)
    bt3 = CTkButton(master=framn, text="Album", font=("Bell MT", 19), command=lambda: view("A", "N")).pack(padx=20, pady=20)
    bt4 = CTkButton(master=framn, text="Song", font=("Bell MT", 19), command=lambda: view("S", "N")).pack(padx=20, pady=20)
    bt5 = CTkButton(master=framn, text="Instrument", font=("Bell MT", 19), command=lambda: view("I", "N")).pack(padx=20, pady=20)

# This function is used to display different data views (Musician, Song, Album, Instrument)
def view(val, x):
    # Check the value of 'x' to determine which frame to forget (either 'fram2' or 'framn')
    if x == "A":
        fram2.pack_forget()
    elif x == "N":
        framn.pack_forget()
    else:
        print("Error")
    
    # Use the global keyword to modify the global variable 'fram3'
    global fram3
    
    # Create a new frame named 'fram3' with a specified height and foreground color
    fram3 = CTkFrame(master=root, height=400, fg_color="#242424")
    fram3.pack(fill=BOTH, expand=True)
    
    # Create a new frame 'f3' inside 'fram3' to hold the back button (bt1)
    f3 = CTkFrame(master=fram3, fg_color="#242424")
    f3.pack(anchor=E)
    
    # Create a back button 'bt1' with a specified image, font, and command 'back_2(x)'
    bt1 = CTkButton(master=f3, image=img5, text="", font=("Bell MT", 19), width=1, command=lambda: back_2(x))
    bt1.pack(side=RIGHT, padx=1)
    
    # Create a frame 'frag' inside 'fram3' to hold labels and the data table
    frag = CTkFrame(master=fram3, fg_color="#242424", height=100, width=400)
    frag.pack(fill=BOTH, padx=20, pady=20, anchor=N)
    
    # Create a new frame 'fra' inside 'fram3' to hold the data table
    fra = CTkFrame(master=fram3, fg_color="#242424")
    fra.pack(fill=BOTH, padx=20)

    # Create a label 'lb' inside 'frag' with an empty text (to be updated later) and a specified font
    lb = CTkLabel(master=frag, text="", font=("Bell MT", 19))
    lb.pack(fill=X, pady=20, padx=20)

    # Based on the value of 'val', update the label 'lb' text and create specific table headers and corresponding data
    if val == "M":
        lb.configure(text="Musician's data")
        h1 = CTkLabel(master=frag, text="SSN", font=("Bell MT", 19)).pack(pady=5, padx=12, side=LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Name", font=("Bell MT", 19)).pack(pady=5, padx=12, side=LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Address", font=("Bell MT", 19)).pack(pady=5, padx=12, side=LEFT, expand=True)
        h4 = CTkLabel(master=frag, text="Telephone", font=("Bell MT", 19)).pack(pady=5, padx=12, side=LEFT, expand=True)
        m_tree(fra)
        V_M()

    elif val == "S":
        lb.configure(text="Song's data")
        h1 = CTkLabel(master=frag, text="Song_ID", font=("Bell MT", 19)).pack(pady=5, padx=20, side=LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Title", font=("Bell MT", 19)).pack(pady=5, padx=20, side=LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Author", font=("Bell MT", 19)).pack(pady=5, padx=20, side=LEFT, expand=True)
        s_tree(fra)
        V_S()

    elif val == "A":
        lb.configure(text="Album's data")
        h1 = CTkLabel(master=frag, text="ID", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Title", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="CopyrightDate", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h4 = CTkLabel(master=frag, text="Format", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h5 = CTkLabel(master=frag, text="Album_identifier", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h6 = CTkLabel(master=frag, text="Producer", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        a_tree(fra)
        V_A()

    elif val == "I":
        lb.configure(text="Instrument's data")
        h1 = CTkLabel(master=frag, text="Instrument.ID", font=("Bell MT", 19)).pack(pady=5, padx=12, side=LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Name", font=("Bell MT", 19)).pack(pady=5, padx=12, side=LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Musicial_Key", font=("Bell MT", 19)).pack(pady=5, padx=12, side=LEFT, expand=True)
        i_tree(fra)
        V_I()


def add(val):
    # Hide the previous frames 'fram2' or 'framn'
    fram2.pack_forget()

    # Use the global keyword to modify the global variables
    global fram4, ae1, ae2, ae3, ae4, ae5, ae6

    # Create a new frame named 'fram4' with a specified height and foreground color
    fram4 = CTkFrame(master=root, height=400, fg_color="#242424")
    fram4.pack(fill=BOTH, expand=True)

    # Create a new frame 'f3' inside 'fram4' to hold the back button (bt1)
    f3 = CTkFrame(master=fram4, fg_color="#242424")
    f3.pack(anchor=E)

    # Create a back button 'bt1' with a specified image, font, and command 'back_3'
    bt1 = CTkButton(master=f3, image=img5, text="", font=("Bell MT", 19), width=1, command=back_3)
    bt1.pack(side=RIGHT, padx=1)

    # Create a frame 'frag' inside 'fram4' to hold labels and the form elements
    frag = CTkFrame(master=fram4, fg_color="#242424")
    frag.pack(expand=True, fill=BOTH)

    # Create a new frame 'fra' inside 'fram4' to hold the form elements
    fra = CTkFrame(master=fram4, fg_color="#242424")
    fra.pack(fill=BOTH, padx=20, expand=TRUE)

    # Create a label 'lb' inside 'frag' with an empty text (to be updated later) and a specified font
    lb = CTkLabel(master=frag, text="", font=("Bell MT", 19))
    lb.pack(fill=X, padx=20)

    # Create an 'Add' button 'bt2' with a specified font and command (to be updated later)
    bt2 = CTkButton(master=frag, text="ADD", font=("Bell MT", 19), width=1)
    bt2.pack(side=BOTTOM, padx=1)

    if val == "M":
        # Create entry fields for Musician data and set the label text to "Musician"
        ae1 = CTkEntry(master=frag, placeholder_text="SSN", font=("Bell MT", 19))
        ae1.pack(pady=10, side=LEFT, expand=TRUE)
        ae2 = CTkEntry(master=frag, placeholder_text="Name", font=("Bell MT", 19))
        ae2.pack(pady=10, side=LEFT, expand=TRUE)
        ae3 = CTkEntry(master=frag, placeholder_text="Address", font=("Bell MT", 19))
        ae3.pack(pady=10, side=LEFT, expand=TRUE)
        ae4 = CTkEntry(master=frag, placeholder_text="Telephone", font=("Bell MT", 19))
        ae4.pack(pady=10, side=LEFT, expand=TRUE)
        lb.configure(text="Musician")
        m_tree(fra)
        bt2.configure(command=A_M)
        V_M()

    elif val == "A":
        # Create entry fields for Album data and set the label text to "Album"
        ae1 = CTkEntry(master=frag, placeholder_text="ID", font=("Bell MT", 19), width=60)
        ae1.pack(pady=10, side=LEFT, expand=True)
        ae2 = CTkEntry(master=frag, placeholder_text="Title", font=("Bell MT", 19), width=80)
        ae2.pack(pady=10, side=LEFT, expand=True)
        ae3 = CTkEntry(master=frag, placeholder_text="CopyrightDate", font=("Bell MT", 19), width=105)
        ae3.pack(pady=10, side=LEFT, expand=True)
        ae4 = CTkEntry(master=frag, placeholder_text="Format", font=("Bell MT", 19), width=50)
        ae4.pack(pady=10, side=LEFT, expand=True)
        ae5 = CTkEntry(master=frag, placeholder_text="Album_identifier", font=("Bell MT", 19))
        ae5.pack(pady=10, side=LEFT, expand=True)
        ae6 = CTkEntry(master=frag, placeholder_text="Producer", font=("Bell MT", 19))
        ae6.pack(pady=10, side=LEFT, expand=True)
        lb.configure(text="Album")
        a_tree(fra)
        bt2.configure(command=A_A)
        V_A()

    elif val == "S":
        # Create entry fields for Song data and set the label text to "Song"
        ae1 = CTkEntry(master=frag, placeholder_text="Song_ID", font=("Bell MT", 19))
        ae1.pack(padx=10, expand=True)
        ae2 = CTkEntry(master=frag, placeholder_text="Title", font=("Bell MT", 19))
        ae2.pack(pady=10, expand=True)
        ae3 = CTkEntry(master=frag, placeholder_text="Author", font=("Bell MT", 19))
        ae3.pack(pady=10, expand=True)
        lb.configure(text="Song")
        s_tree(fra)
        bt2.configure(command=A_S)
        V_S()

    elif val == "I":
        # Create entry fields for Instrument data and set the label text to "Instrument"
        ae1 = CTkEntry(master=frag, placeholder_text="Instrument.ID", font=("Bell MT", 19))
        ae1.pack(pady=10, expand=True)
        ae2 = CTkEntry(master=frag, placeholder_text="Name", font=("Bell MT", 19))
        ae2.pack(pady=10, expand=True)
        ae3 = CTkEntry(master=frag, placeholder_text="Musicial_Key", font=("Bell MT", 19))
        ae3.pack(pady=10, expand=True)
        lb.configure(text="Instrument")
        i_tree(fra)
        bt2.configure(command=A_I)
        V_I()


def edit(val):
    # Hide the previous frame 'fram2'
    fram2.pack_forget()

    # Use the global keyword to modify the global variables
    global fram5, h1, h2, h3, h4, h5

    # Create a new frame named 'fram5' with a specified height and foreground color
    fram5 = CTkFrame(master=root, height=400, fg_color="#242424")
    fram5.pack(fill=BOTH, expand=True)

    # Create a new frame 'f4' inside 'fram5' to hold the back button (bt1)
    f4 = CTkFrame(master=fram5, fg_color="#242424")
    f4.pack(anchor=E)

    # Create a back button 'bt1' with a specified image, font, and command 'back_4'
    bt1 = CTkButton(master=f4, image=img5, text="", font=("Bell MT", 19), width=1, command=back_4)
    bt1.pack(side=RIGHT, padx=1)

    # Create a frame 'frag' inside 'fram5' to hold the label and form elements
    frag = CTkFrame(master=fram5, fg_color="#242424", height=100, width=400)
    frag.pack(fill=BOTH, padx=20, pady=20, anchor=N)

    # Create a label 'lb' inside 'frag' with an empty text (to be updated later) and a specified font
    lb = CTkLabel(master=frag, text="", font=("Bell MT", 19))
    lb.pack(fill=X, pady=20, padx=20)

    # Create a new frame 'fra' inside 'fram5' to hold the form elements
    fra = CTkFrame(master=fram5, fg_color="#242424")
    fra.pack(fill=BOTH, padx=20, expand=TRUE)

    # Create an 'UPDATE' button 'bt2' with a specified font and command (to be updated later)
    bt2 = CTkButton(master=frag, text="UPDATE", font=("Bell MT", 19), width=1)
    bt2.pack(side=BOTTOM, padx=1)

    if val == "M":
        # Create entry fields for Musician data and set the label text to "Select the data to update:"
        lb.configure(text="Select the data to update:")
        h1 = CTkEntry(master=frag, placeholder_text="Name", font=("Bell MT", 19))
        h1.pack(pady=5, padx=12, side=LEFT, expand=True)
        h2 = CTkEntry(master=frag, placeholder_text="Address", font=("Bell MT", 19))
        h2.pack(pady=5, padx=12, side=LEFT, expand=True)
        h3 = CTkEntry(master=frag, placeholder_text="Telephone", font=("Bell MT", 19))
        h3.pack(pady=5, padx=12, side=LEFT, expand=True)
        m_tree(fra)
        bt2.configure(command=U_M)
        V_M()

    elif val == "A":
        # Create entry fields for Album data and set the label text to "Select the data to update:"
        lb.configure(text="Select the data to update:")
        h1 = CTkEntry(master=frag, placeholder_text="Title", font=("Bell MT", 19), width=70)
        h1.pack(pady=5, padx=5, side=LEFT, expand=True)
        h2 = CTkEntry(master=frag, placeholder_text="CopyrightDate", font=("Bell MT", 19), width=100)
        h2.pack(pady=5, padx=5, side=LEFT, expand=True)
        h3 = CTkEntry(master=frag, placeholder_text="Format", font=("Bell MT", 19), width=100)
        h3.pack(pady=5, padx=5, side=LEFT, expand=True)
        h4 = CTkEntry(master=frag, placeholder_text="Album_identifier", font=("Bell MT", 19))
        h4.pack(pady=5, padx=5, side=LEFT, expand=True)
        h5 = CTkEntry(master=frag, placeholder_text="Producer", font=("Bell MT", 19), width=100)
        h5.pack(pady=5, padx=5, side=LEFT, expand=True)
        a_tree(fra)
        bt2.configure(command=U_A)
        V_A()

    elif val == "I":
        # Create entry fields for Instrument data and set the label text to "Select the data to update:"
        lb.configure(text="Select the data to update:")
        h1 = CTkEntry(master=frag, placeholder_text="Name", font=("Bell MT", 19))
        h1.pack(pady=5, padx=12, side=LEFT, expand=True)
        h2 = CTkEntry(master=frag, placeholder_text="Musicial_Key", font=("Bell MT", 19))
        h2.pack(pady=5, padx=12, side=LEFT, expand=True)
        i_tree(fra)
        bt2.configure(command=U_I)
        V_I()

    elif val == "S":
        # Create entry fields for Song data and set the label text to "Select the data to update:"
        lb.configure(text="Select the data to update:")
        h1 = CTkEntry(master=frag, placeholder_text="Title", font=("Bell MT", 19))
        h1.pack(pady=5, padx=20, side=LEFT, expand=True)
        h2 = CTkEntry(master=frag, placeholder_text="Author", font=("Bell MT", 19))
        h2.pack(pady=5, padx=20, side=LEFT, expand=True)
        s_tree(fra)
        bt2.configure(command=U_S)
        V_S()

def delete(val):
    # Hide the previous frame 'fram2'
    fram2.pack_forget()

    # Use the global keyword to modify the global variables
    global fram6

    # Create a new frame named 'fram6' with a specified height and foreground color
    fram6 = CTkFrame(master=root, height=400, fg_color="#242424")
    fram6.pack(fill=BOTH, expand=True)

    # Create a new frame 'f5' inside 'fram6' to hold the back button (bt1)
    f5 = CTkFrame(master=fram6, fg_color="#242424")
    f5.pack(anchor=E)

    # Create a back button 'bt1' with a specified image, font, and command 'back_5'
    bt1 = CTkButton(master=f5, image=img5, text="", font=("Bell MT", 19), width=1, command=back_5)
    bt1.pack(side=RIGHT, padx=1)

    # Create a frame 'frag' inside 'fram6' to hold the label and form elements
    frag = CTkFrame(master=fram6, fg_color="#242424", height=100, width=400)
    frag.pack(fill=BOTH, padx=20, pady=20, anchor=N)

    # Create a new frame 'fra' inside 'fram6' to hold the form elements
    fra = CTkFrame(master=fram6, fg_color="#242424")
    fra.pack(fill=BOTH, padx=20, expand=TRUE)

    # Create a label 'lb' inside 'frag' with an empty text (to be updated later) and a specified font
    lb = CTkLabel(master=frag, text="", font=("Bell MT", 19))
    lb.pack(fill=X, padx=20)

    # Create a 'DELETE' button 'bt2' with a specified font and command (to be updated later)
    bt2 = CTkButton(master=frag, text="DELETE", font=("Bell MT", 19), width=1)
    bt2.pack(padx=1, pady=20)

    if val == "M":
        # Create labels for Musician data and set the label text to "Select the data to delete:"
        lb.configure(text="Select the data to delete:")
        h1 = CTkLabel(master=frag, text="SSN", font=("Bell MT", 19))
        h1.pack(pady=5, padx=12, side=LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Name", font=("Bell MT", 19))
        h2.pack(pady=5, padx=12, side=LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Address", font=("Bell MT", 19))
        h3.pack(pady=5, padx=12, side=LEFT, expand=True)
        h4 = CTkLabel(master=frag, text="Telephone", font=("Bell MT", 19))
        h4.pack(pady=5, padx=12, side=LEFT, expand=True)
        m_tree(fra)
        bt2.configure(command=D_M)
        V_M()

    elif val == "A":
        # Create labels for Album data and set the label text to "Select the data to delete:"
        lb.configure(text="Select the data to delete:")
        h1 = CTkLabel(master=frag, text="ID", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Title", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="CopyrightDate", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h4 = CTkLabel(master=frag, text="Format", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h6 = CTkLabel(master=frag, text="Album_identifier", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        h5 = CTkLabel(master=frag, text="Producer", font=("Bell MT", 19)).pack(pady=5, padx=5, side=LEFT, expand=True)
        a_tree(fra)
        bt2.configure(command=D_A)
        V_A()

    elif val == "I":
        # Create labels for Instrument data and set the label text to "Select the data to delete:"
        lb.configure(text="Select the data to delete:")
        h1 = CTkLabel(master=frag, text="Instrument.ID", font=("Bell MT", 19)).pack(pady=5, padx=0, side=LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Name", font=("Bell MT", 19)).pack(pady=5, padx=10, side=LEFT, expand=True)
        h3 = CTkLabel(master=frag, text="Musicial_Key", font=("Bell MT", 19)).pack(pady=5, padx=12, side=LEFT, expand=True)
        i_tree(fra)
        bt2.configure(command=D_I)
        V_I()

    elif val == "S":
        # Create labels for Song data and set the label text to "Select the data to delete:"
        lb.configure(text="Select the data to delete:")
        h3 = CTkLabel(master=frag, text="Song_ID", font=("Bell MT", 19)).pack(pady=5, padx=20, side=LEFT, expand=True)
        h1 = CTkLabel(master=frag, text="Title", font=("Bell MT", 19)).pack(pady=5, padx=20, side=LEFT, expand=True)
        h2 = CTkLabel(master=frag, text="Author", font=("Bell MT", 19)).pack(pady=5, padx=20, side=LEFT, expand=True)
        s_tree(fra)
        bt2.configure(command=D_S)
        V_S()


# The V_M(), V_A(), V_S(), and V_I() functions query the database and populate the Treeview with data for Musician, Album, Song, and Instrument respectively.
def V_M():
    # Fetch all rows from the 'Musician' table using an SQL query
    cursor.execute("SELECT * FROM Musician")
    data = cursor.fetchall()

    # Iterate over the fetched data and insert each row into the treeview
    for row in data:
        tree.insert("", "end", values=row)

def V_A():
    # Fetch all rows from the 'Album' table using an SQL query
    cursor.execute("SELECT * FROM Album")
    data = cursor.fetchall()

    # Iterate over the fetched data and insert each row into the treeview
    for row in data:
        tree.insert("", "end", values=row)

def V_S():
    # Fetch all rows from the 'Song' table using an SQL query
    cursor.execute("SELECT * FROM Song")
    data = cursor.fetchall()

    # Iterate over the fetched data and insert each row into the treeview
    for row in data:
        tree.insert("", "end", values=row)

def V_I():
    # Fetch all rows from the 'Instrument' table using an SQL query
    cursor.execute("SELECT * FROM Instrument")
    data = cursor.fetchall()

    # Iterate over the fetched data and insert each row into the treeview
    for row in data:
        tree.insert("", "end", values=row)


# The A_M(), A_A(), A_S(), and A_I() functions handle adding new records for Musician, Album, Song, and Instrument respectively.
def A_M():
    # Execute an SQL INSERT query to add a new record into the 'Musician' table
    cursor.execute("INSERT INTO Musician (SSN, Name, Address, PhoneNumber) VALUES (%s, %s, %s, %s)", (ae1.get(), ae2.get(), ae3.get(), ae4.get()))
    
    # Commit the changes to the database
    db_connection.commit()
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    # Update the treeview with the latest data from the 'Musician' table
    V_M()

def A_A():
    # Execute an SQL INSERT query to add a new record into the 'Album' table
    cursor.execute("INSERT INTO Album (Album_ID, Title, CopyrightDate, Format, Album_Identifier, Producer_SSN) VALUES (%s, %s, %s, %s, %s, %s)", (ae1.get(), ae2.get(), ae3.get(), ae4.get(), ae5.get(), ae6.get()))
    
    # Commit the changes to the database
    db_connection.commit()
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    # Update the treeview with the latest data from the 'Album' table
    V_A()

def A_S():
    # Execute an SQL INSERT query to add a new record into the 'Song' table
    cursor.execute("INSERT INTO Song (Song_ID, Title, Author) VALUES (%s, %s, %s)", (ae1.get(), ae2.get(), ae3.get()))
    
    # Commit the changes to the database
    db_connection.commit()
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    # Update the treeview with the latest data from the 'Song' table
    V_S()

def A_I():
    # Execute an SQL INSERT query to add a new record into the 'Instrument' table
    cursor.execute("INSERT INTO Instrument (InstrumentID, Name, Musical_Key) VALUES (%s, %s, %s)", (ae1.get(), ae2.get(), ae3.get()))
    
    # Commit the changes to the database
    db_connection.commit()
    
    # Clear the existing data in the treeview
    tree.delete(*tree.get_children())
    
    # Update the treeview with the latest data from the 'Instrument' table
    V_I()


# The D_M(), D_A(), D_S(), and D_I() functions handle deleting records for Musician, Album, Song, and Instrument respectively.
def D_M():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]  # Assuming SSN is the primary key
        cursor.execute("DELETE FROM Musician WHERE SSN=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        V_M()

def D_A():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]  # Assuming Album_ID is the primary key
        cursor.execute("DELETE FROM Album WHERE Album_ID=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        V_A()

def D_S():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]  # Assuming Song_ID is the primary key
        cursor.execute("DELETE FROM Song WHERE Song_ID=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        V_S()

def D_I():
    selected_item = tree.selection()
    if selected_item:
        item = tree.item(selected_item)
        row_data = item['values']
        primary_key = row_data[0]  # Assuming InstrumentID is the primary key
        cursor.execute("DELETE FROM Instrument WHERE InstrumentID=%s", (primary_key,))
        db_connection.commit()
        tree.delete(selected_item)
        tree.delete(*tree.get_children())
        V_I()


# The U_M(), U_A(), U_S(), and U_I() functions handle updating records for Musician, Album, Song, and Instrument respectively.
def U_M():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    SSN = row_data[0]  # Assuming SSN is the primary key for Musician table
    cursor.execute("UPDATE Musician SET Name=%s, Address=%s, PhoneNumber=%s WHERE SSN=%s", (h1.get(), h2.get(), h3.get(), SSN))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_M()

def U_A():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    Album_ID = row_data[0]  # Assuming Album_ID is the primary key for Album table
    cursor.execute("UPDATE Album SET Title=%s, CopyrightDate=%s, Format=%s, Album_Identifier=%s, Producer_SSN=%s WHERE Album_ID=%s", (h1.get(), h2.get(), h3.get(), h4.get(), h5.get(), Album_ID))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_A()

def U_I():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    InstrumentID = row_data[0]  # Assuming InstrumentID is the primary key for Instrument table
    cursor.execute("UPDATE Instrument SET Name=%s, Musical_key=%s WHERE InstrumentID=%s", (h1.get(), h2.get(), InstrumentID))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_I()

def U_S():
    selected_item = tree.selection()
    item = tree.item(selected_item)
    row_data = item['values']
    Song_ID = row_data[0]  # Assuming Song_ID is the primary key for Song table
    cursor.execute("UPDATE Song SET Title=%s, Author=%s WHERE Song_ID=%s", (h1.get(), h2.get(), Song_ID))
    db_connection.commit()
    tree.delete(*tree.get_children())
    V_S()

def m_tree(val):
    scrollbar = ttk.Scrollbar(master=val, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(val, columns=("SSN", "Name", "Address", "TelePhone"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("SSN", text="SSN")
    tree.heading("Name", text="Name")
    tree.heading("Address", text="Address")
    tree.heading("TelePhone", text="TelePhone")
    tree.column("SSN", width=100)
    tree.pack(fill="both",expand=True)

def a_tree(val):
    scrollbar = ttk.Scrollbar(master=val, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(val, columns=("ID", "Title", "CopyrightDate", "Format", "Album_identifier", "Producer"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("ID", text="ID")
    tree.heading("Title", text="Title")
    tree.heading("CopyrightDate", text="CopyrightDate")
    tree.heading("Format", text="Format")
    tree.heading("Producer", text="Producer")
    tree.heading("Album_identifier", text="Album_identifier")
    tree.column("ID", width=50)
    tree.column("Title", width=80)
    tree.column("CopyrightDate", width=160)
    tree.column("Format", width=110)
    tree.column("Album_identifier", width=120)
    tree.pack(fill="both",expand=True)

def i_tree(val):
    scrollbar = ttk.Scrollbar(master=val, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(val, columns=("Instrument.ID", "Name", "Musicial_Key"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("Instrument.ID", text="Instrument.ID")
    tree.heading("Name", text="Name")
    tree.heading("Musicial_Key", text="Musicial_Key")
    tree.pack(fill="both",expand=True)

def s_tree(val):
    scrollbar = ttk.Scrollbar(master=val, orient="vertical")
    scrollbar.pack(side="right",fill="y")
    global tree
    tree = ttk.Treeview(val, columns=("Song_ID","Title", "Author"), show="headings", yscrollcommand=scrollbar.set)
    tree.heading("Title", text="Title")
    tree.heading("Author", text="Author")
    tree.heading("Song_ID", text="Song_ID")
    tree.pack(fill="both",expand=True)

def conf(x,y):
    global count
    global lc
    if count >1:
        lc.pack_forget()
    count+=1
    if x.get()=="Admin":
        if y.get()=="Admin":
            admin()
        else:
            lc=CTkLabel(master=fram,text="Invalid password", font=("Bell, MT", 19))
            lc.pack(padx=10, pady=20)
    else:
        lc=CTkLabel(master=fram,text="Invalid username", font=("Bell, MT", 19))
        lc.pack(padx=10, pady=20)

def back_N():
    framn.pack_forget()
    front()   
def back_P():
    fram.pack_forget()
    front()
def back():
    fram2.pack_forget()
    front()
def back_2(a):
    fram3.pack_forget()
    if a == "A":
        admin()
    elif a == "N":
        normal()
    else:
        print("Error")
def back_3():
    fram4.pack_forget()
    admin()
def back_4():
    fram5.pack_forget()
    admin()
def back_5():
    fram6.pack_forget()
    admin()

front()
root.mainloop()

# conf(x, y): This function seems to handle login authentication. It checks if the provided username (x) and password (y) match some predefined conditions. If the username and password match, the admin() function is called, which may be responsible for showing the admin interface. If not, it displays an error message.

# back_N(), back_P(), back(), back_2(a), back_3(), back_4(), back_5(): These functions are used for navigation and managing different views. Each function hides or "forgets" the current view and then calls another function to go back to the previous view or move to a different view based on the context.

# front(): This function is not provided, but it's likely intended to be the starting point of the application or the main GUI window.