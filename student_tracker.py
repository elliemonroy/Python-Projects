
from tkinter import * #  importing module for creating GUI
import sqlite3 # importing module for performing SQL operations


window = Tk()
window.title("Student Tracking")
window.geometry('800x600+0+0')
header = Label(window, text="Student Tracking", font=("arial",30,"bold"), fg="steelblue").pack()


conn = sqlite3.connect('student_tracking.db')
with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE if not exists students( \
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
                    First_Name TEXT, \
                    Last_Name TEXT, \
                    Phone_Number TEXT, \
                    Email_Address TEXT, \
                    Current_Course TEXT \
                    )")
    conn.commit()
conn.close()
    


L1 = Label(window, text = "First Name:", font=("arial",18)).place(x=10,y=150)
L2 = Label(window, text = "Last Name:", font=("arial",18)).place(x=10,y=200)
L3 = Label(window, text = "Phone Number:", font=("arial",18)).place(x=10,y=250)
L4 = Label(window, text = "Email Address:", font=("arial",18)).place(x=10,y=300)
L5 = Label(window, text = "Current Course:", font=("arial",18)).place(x=10,y=350)



fn = StringVar(window)
ln = StringVar(window)
pn = StringVar(window)
ea = StringVar(window)
cc = StringVar(window)


# entry for 'input' in GUI
fnE = Entry(window)
fnE.place(x=220,y=155)

lnE = Entry(window)
lnE.place(x=220,y=205)

pnE = Entry(window)
pnE.place(x=220,y=255)

eaE = Entry(window)
eaE.place(x=220,y=305)

ccE = Entry(window)
ccE.place(x=220,y=355)



def get():

    firName = fnE.get()
    LasName = lnE.get()
    PhoNum = pnE.get()
    EmaAdd = eaE.get()
    CurCo = ccE.get()
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cur = conn.cursor()
        cur.execute("INSERT INTO students (First_Name,Last_Name,Phone_Number,Email_Address,Current_Course)VALUES (?,?,?,?,?)",(firName,LasName,PhoNum,EmaAdd,CurCo))

        data = cur.fetchall() # Gets the data from the table
        
        
        Lb.insert(0,firName) # Inserts record row by row in list box

        L6 = Label(window, text = "List of Students..", 
                   font=("arial", 16)).place(x=400,y=350)

        conn.commit()
    conn.close()


def delete():
    conn = sqlite3.connect('student_tracking.db')
    new = Lb.get(Lb.curselection())
    with conn:
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE First_Name=?", (new,))
        conn.commit()
    conn.close()


def onSelect(event):
    # Calling the event is the self.1stList1 widget
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student_tracking.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT First_Name,Last_Name,Phone_Number,Email_Address,Current_Course FROM students WHERE First_Name = (?)""", [value])
        varBody = cursor.fetchall()
        # This returns a tuple and we can slice it into 4 parts using data[] during the iteration
        for data in varBody:
            fnE.delete(0,END)
            fnE.insert(0,data[0])
            lnE.delete(0,END)
            lnE.insert(0,data[1])
            pnE.delete(0,END)
            pnE.insert(0,data[2])
            eaE.delete(0,END)
            eaE.insert(0,data[3])
            ccE.delete(0,END)
            ccE.insert(0,data[4])

    
    

button_1 = Button(window, text="Submit",command=get)
button_1.place(x=100,y=400)

button_2 = Button(window,text= "Delete",command=delete)
button_2.place(x=10,y=400)


frame = Frame(window)
frame.place(x=400, y =150)

                  
Lb = Listbox(frame, height = 8, width = 25,font=("arial",12))
Lb.pack(side = LEFT, fill = Y)

scroll = Scrollbar(frame, orient = VERTICAL) # Set scrollbar to list box for when entries exceed size of list box
scroll.config(command = Lb.yview)
scroll.pack(side = RIGHT, fill =Y)
Lb.config(yscrollcommand = scroll.set)
Lb.bind('<<ListboxSelect>>',lambda event:onSelect(event))


if __name__ == "__main__":
    window.mainloop() #mainloop() make sure that window stays open







 





















