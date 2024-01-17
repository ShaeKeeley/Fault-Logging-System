import tkinter as tk
import tkinter.messagebox
# importing connection
import mysql.connector

# defining database class and method
class Database:
    def dbconnect(self):
    #establishing connection
        global conn
        conn = mysql.connector.connect(user='root', password='ITAPA@123', host='localhost', database='mydatabase')

        global cursor
        cursor= conn.cursor()
    #defining insert method
    def insert(self):
        name = firstName.get()
        lstNme = lastName.get()
        gndr = gender.get()
        contactNo = contactNumber.get()
        dateofRep = dateOfReporting.get()
        unitNo = unitNumber.get()
        apartNme = apartmentName.get()
        flt = fault.get()

        insert_statment = ("INSERT INTO data(firstName, lastName, gender, contactNumber, dateOfReporting, unitNumber, apartmentName, fault)"
                            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
        val = (name, lstNme, gndr, contactNo, dateofRep, unitNo, apartNme, flt)

        try:
            #execute the sql
            cursor.execute(insert_statment, val)
            #commit changes
            conn.commit()
        except:
            conn.rollback()

# defining window class and init method
class Window:
    def __init__(self, faultlog_screen):
        self.faultlog_screen = faultlog_screen

        faultlog_screen.title("Fault Logging System")
        faultlog_screen.geometry("500x500")
        faultlog_screen.configure(bg= "light blue")
        global firstName
        global lastName
        global gender
        global contactNumber
        global dateOfReporting
        global unitNumber
        global apartmentName
        global fault

        firstName = tk.StringVar()
        lastName = tk.StringVar()
        gender = tk.StringVar()
        contactNumber = tk.StringVar()
        dateOfReporting = tk.StringVar()
        unitNumber = tk.StringVar()
        apartmentName = tk.StringVar()
        fault = tk.StringVar()

        lf = ListFaults()

        #labels + entries(input from user)
        firstName_lbl = tk.Label(faultlog_screen, text='First Name', font=('arial', 12, 'bold'), bg="light blue").grid(row=0, column=0, padx=10, pady=10, sticky="w")
        firstName_entry = tk.Entry(faultlog_screen, textvariable=firstName, font=('arial', 12, 'normal'), bd=5).grid(row=0, column=1, padx=10, pady=10)

        lastName_lbl = tk.Label(faultlog_screen, text='Last Name', font=('arial', 12, 'bold'), bg="light blue").grid(row=1, column=0, padx=10, pady=10, sticky="w")
        lastName_entry = tk.Entry(faultlog_screen, textvariable=lastName, font=('arial', 12, 'normal'), bd=5).grid(row=1, column=1, padx=10, pady=10)

        gender_lbl = tk.Label(faultlog_screen, text='Gender', font=('arial', 12, 'bold'), bg="light blue").grid(row=2, column=0, padx=10, pady=10, sticky="w")
        gender_entry =tk.Entry(faultlog_screen, textvariable=gender, font=('arial', 12, 'normal'), bd=5).grid(row=2, column=1, padx=10, pady=10)

        contactNumber_lbl = tk.Label(faultlog_screen, text='Contact Number', font=('arial', 12, 'bold'), bg="light blue").grid(row=3, column=0, padx=10, pady=10, sticky="w")
        contactNumber_entry = tk.Entry(faultlog_screen, textvariable=contactNumber, font=('arial', 12, 'normal'), bd=5).grid(row=3, column=1, padx=10, pady=10)

        dateOfReporting_lbl = tk.Label(faultlog_screen, text='Date Of Reporting', font=('arial', 12, 'bold'), bg="light blue").grid(row=4, column=0, padx=10, pady=10, sticky="w")
        dateOfReporting_entry = tk.Entry(faultlog_screen, textvariable=dateOfReporting, font=('arial', 12, 'normal'), bd=5).grid(row=4, column=1, padx=10, pady=10)


        unitNumber_lbl = tk.Label(faultlog_screen, text='Unit Number', font=('arial', 12, 'bold'), bg="light blue").grid(row=5, column=0, padx=10, pady=10, sticky="w")
        unitNumber_entry = tk.Entry(faultlog_screen, textvariable=unitNumber, font=('arial', 12, 'normal'), bd=5).grid(row=5, column=1, padx=10, pady=10)

        apartmentName_lbl = tk.Label(faultlog_screen, text='Apartment Name', font=('arial', 12, 'bold'), bg="light blue").grid(row=6, column=0, padx=10, pady=10, sticky="w")
        apartmentName_entry = tk.Entry(faultlog_screen, textvariable=apartmentName, font=('arial', 12, 'normal'), bd=5).grid(row=6, column=1, padx=10, pady=10)

        fault_lbl = tk.Label(faultlog_screen, text='Fault', font=('arial', 12, 'bold'), bg="light blue").grid(row=7, column=0, padx=10, pady=10, sticky="w")
        fault_entry = tk.Entry(faultlog_screen, textvariable=fault, font=('arial', 12, 'normal'), bd=5).grid(row=7, column=1, padx=10, pady=10)

        sub_btn = tk.Button(faultlog_screen, text='Submit', command=self.submit, font=('arial', 12, 'bold'))
        sub_btn.grid(row=8, column=1)

        sub_btn = tk.Button(faultlog_screen, text='List faults', command=lf.display, font=('arial', 12, 'bold'))
        sub_btn.grid(row=9, column=1)

    # defining submit method
    def submit(self):
        name = firstName.get()
        lstNme = lastName.get()
        gndr = gender.get()
        contactNo = contactNumber.get()
        dateofRep = dateOfReporting.get()
        unitNo = unitNumber.get()
        apartNme = apartmentName.get()
        flt = fault.get()

        print("The First Name is : " + name)
        print("The Last Name is : " + lstNme)
        print("The Gender is : " + gndr)
        print("The Contact No is : " + contactNo)
        print("The Date Of Reporting is : " + dateofRep)
        print("The Unit No is : " + unitNo)
        print("The Apartment Name is : " + apartNme)
        print("The fault is : " + flt)
        tk.messagebox.showinfo("Submitted", "Your info has been submitted")
        db.insert()

# defining list faults class and display method
class ListFaults:
    def display(self):
        select_statement = ("SELECT fault FROM data")
        cursor.execute(select_statement)
        myresult = cursor.fetchall()
        tk.messagebox.showinfo("Faults that have been logged:", myresult)

#initialization
db = Database()
db.dbconnect()
faultlog_screen = tk.Tk()
obj = Window(faultlog_screen)
faultlog_screen.mainloop()
