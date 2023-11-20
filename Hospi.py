from tkinter import *
from tkinter import ttk
import random
import time
import datetime
import tkinter as tk
import tkinter.messagebox
import mysql.connector

class Hospital:
    def __init__(self, root):
        self.root = root
        self.root.title("Hospital Management System")
        self.root.geometry("1920x1080")

        self.nameoftablet=StringVar()
        self.ref=StringVar()
        self.Dose=StringVar()
        self.numberoftables=StringVar()
        self.lot=StringVar()
        self.nameoftablet=StringVar()
        self.issuedate=StringVar()
        self.expdate=StringVar()
        self.dailydose=StringVar()
        self.sideeffect=StringVar()
        self.furtherinfo=StringVar()
        self.storageadvice=StringVar()
        self.drivingusingmachine=StringVar()
        self.howtousemedication=StringVar()
        self.patientid=StringVar()
        self.nhsnumber=StringVar()
        self.patientname=StringVar()
        self.dateofbirth=StringVar()
        self.patientaddress=StringVar()

        lbltitle = Label(self.root, bd=20, relief=RIDGE, text="HOSPITAL MANAGEMENT SYSTEM", fg="red", bg="white", font=("times new roman", 50, "bold"))
        lbltitle.pack(side=TOP, fill=X)

        # ------------------------------------------ Dataframe ------------------------------------------------------------------------------------------------------
        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=130, width=1530, height=400)

        DataframeLeft = LabelFrame(Dataframe, bd=10, relief=RIDGE, font=("ariel", 12, "bold"), text="Patient Information")
        DataframeLeft.place(x=0, y=5, width=980, height=350)
        DataframeRight = LabelFrame(Dataframe, bd=10, relief=RIDGE, padx=10, font=("times new roman", 12, "bold"), text="Prescription")
        DataframeRight.place(x=990, y=5, width=460, height=350)

        # ------------------------------ Buttom frame -------------------------------------------------------------------------------
        Buttonframe = Frame(self.root, bd=20, relief=RIDGE)
        Buttonframe.place(x=0, y=530, width=1530, height=70)

        # ------------------------------ Details frame ----------------------------------------------------------------------------------------

        Dataframe = Frame(self.root, bd=20, relief=RIDGE)
        Dataframe.place(x=0, y=600, width=1530, height=190)

        # --------------------------------- data frame ---------------------------------
        lblNameTablet = Label(DataframeLeft, text="Names of tablets", font=("times new roman", 12, "bold"), padx=2, pady=6)
        lblNameTablet.grid(row=0, column=0)



        comNametablet = ttk.Combobox(DataframeLeft, textvariable=self.nameoftablet, font=("arial", 12, "bold"), width=33)
        comNametablet["values"] = ("nice", "corona", "corona vaccine", "Acetamination", "Addrenll", "Amlodipine", "Ativan")
        comNametablet.grid(row=0, column=1)


        lblref = Label(DataframeLeft, text="Reference no:", font=("arial", 12, "bold"), padx=2)
        lblref.grid(row=1, column=0, sticky=W)
        txtref = Entry(DataframeLeft, textvariable=self.ref, font=("arial", 13, "bold"), width=35)
        txtref.grid(row=1, column=1)

        lblDose = Label(DataframeLeft,font=("arial", 12, "bold"), text="Dose", padx=2, pady=4)
        lblDose.grid(row=2, column=0, sticky=W)
        txtDose = Entry(DataframeLeft,textvariable=self.Dose , font=("arial", 13, "bold"), width=35)
        txtDose.grid(row=2, column=1)

        lblNoOfTablet = Label(DataframeLeft, font=("arial", 12, "bold"), text="No of Tablets :", padx=2, pady=6)
        lblNoOfTablet.grid(row=3, column=0, sticky=W)
        txtNoOfTablet = Entry(DataframeLeft,textvariable=self.numberoftables, font=("arial", 13, "bold"), width=35)
        txtNoOfTablet.grid(row=3, column=1)

        lbllot = Label(DataframeLeft, font=("arial", 12, "bold"), text="Lot:", padx=2, pady=6)
        lbllot.grid(row=4, column=0, sticky=W)
        txtlot = Entry(DataframeLeft,  textvariable=self.lot,font=("arial", 13, "bold"), width=35)
        txtlot.grid(row=4, column=1)

        lblissuedate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Issue Date:", padx=2, pady=6)
        lblissuedate.grid(row=5, column=0, sticky=W)
        txtissuedate = Entry(DataframeLeft, textvariable=self.issuedate, font=("arial", 13, "bold"), width=35)
        txtissuedate.grid(row=5, column=1)

        lblexpdate = Label(DataframeLeft, font=("arial", 12, "bold"), text="Exp Date:", padx=2, pady=6)
        lblexpdate.grid(row=6, column=0, sticky=W)
        txtexpdate = Entry(DataframeLeft,textvariable=self.expdate, font=("arial", 13, "bold"), width=35)
        txtexpdate.grid(row=6, column=1)

        lbldailydose = Label(DataframeLeft, font=("arial", 12, "bold"), text="Daily Dose:", padx=2, pady=6)
        lbldailydose.grid(row=7, column=0, sticky=W)
        txtdailydose = Entry(DataframeLeft,  textvariable=self.dailydose,font=("arial", 13, "bold"), width=35)
        txtdailydose.grid(row=7, column=1)

        lblsideeffect = Label(DataframeLeft, font=("arial", 12, "bold"), text="Side Effect:", padx=2, pady=6)
        lblsideeffect.grid(row=8, column=0, sticky=W)
        txtsideeffect = Entry(DataframeLeft,  textvariable=self.sideeffect,font=("arial", 13, "bold"), width=35)
        txtsideeffect.grid(row=8, column=1)

        lblfurthrinfo = Label(DataframeLeft,  font=("arial", 12, "bold"), text="Further Information:", padx=2)
        lblfurthrinfo.grid(row=0, column=2, sticky=W)
        txtfurthrinfo = Entry(DataframeLeft,textvariable=self.furtherinfo, font=("arial", 13, "bold"), width=35)
        txtfurthrinfo.grid(row=0, column=3)

        lblBloodPressure = Label(DataframeLeft,font=("arial", 12, "bold"), text="Blood Pressure:", padx=2, pady=6)
        lblBloodPressure.grid(row=1, column=2, sticky=W)
        txtBloodPressure = Entry(DataframeLeft,textvariable=self.drivingusingmachine , font=("arial", 13, "bold"), width=35)
        txtBloodPressure.grid(row=1, column=3)

        lblStorage = Label(DataframeLeft, font=("arial", 12, "bold"), text="Storage Advice:", padx=2, pady=6)
        lblStorage.grid(row=2, column=2, sticky=W)
        txtStorage = Entry(DataframeLeft,textvariable=self.storageadvice, font=("arial", 13, "bold"), width=35)
        txtStorage.grid(row=2, column=3)

        lblmedicine = Label(DataframeLeft, font=("arial", 12, "bold"), text="Medication:", padx=2, pady=6)
        lblmedicine.grid(row=3, column=2, sticky=W)
        txtmedicine = Entry(DataframeLeft, textvariable=self.howtousemedication,font=("arial", 13, "bold"), width=35)
        txtmedicine.grid(row=3, column=3, sticky=W)

        lblpatientId = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient ID:", padx=2, pady=6)
        lblpatientId.grid(row=4, column=2, sticky=W)
        txtpatientId = Entry(DataframeLeft,textvariable=self.patientid , font=("arial", 13, "bold"), width=35)
        txtpatientId.grid(row=4, column=3)

        lblnhsnumber = Label(DataframeLeft, font=("arial", 12, "bold"), text="NHS Number:", padx=2, pady=6)
        lblnhsnumber.grid(row=5, column=2, sticky=W)
        txtnhsnumber = Entry(DataframeLeft, textvariable=self.nhsnumber,  font=("arial", 13, "bold"), width=35)
        txtnhsnumber.grid(row=5, column=3)

        lblpname = Label(DataframeLeft,font=("arial", 12, "bold"), text="Patient Name:", padx=2, pady=6)
        lblpname.grid(row=6, column=2, sticky=W)
        txtpname = Entry(DataframeLeft, textvariable=self.patientname,  font=("arial", 13, "bold"), width=35)
        txtpname.grid(row=6, column=3)

        lblDOB = Label(DataframeLeft, font=("arial", 12, "bold"), text="Date of Birth:", padx=2, pady=6)
        lblDOB.grid(row=7, column=2, sticky=W)
        txtDOB = Entry(DataframeLeft,textvariable=self.dateofbirth, font=("arial", 13, "bold"), width=35)
        txtDOB.grid(row=7, column=3)

        lbladdress = Label(DataframeLeft, font=("arial", 12, "bold"), text="Patient Address:", padx=2, pady=6)
        lbladdress.grid(row=8, column=2, sticky=W)
        txtaddress = Entry(DataframeLeft, textvariable=self.patientaddress, font=("arial", 13, "bold"), width=35)
        txtaddress.grid(row=8, column=3)

        # --------------------------- Dataframe Right ------------------------------------------------------------------------
        self.txtPrescription = Text(DataframeRight, font=("arial", 12, "bold"), width=26, height=16, padx=2, pady=6)
        self.txtPrescription.grid(row=0, column=0)

        # ----------------------------- Buttons -------------------------------------------------------------------------

        btnprescription = Button(Buttonframe, text="Prescription", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=16, padx=2, pady=6,
                                     command=self.iprescription)
        btnprescription.grid(row=0, column=0)

        btnprescriptionData = Button(Buttonframe, text="Prescription Data", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=16, padx=2, pady=6,
                                     command=self.iPrescriptionTableData)
        btnprescriptionData.grid(row=0, column=1)

        btnupdate = Button(Buttonframe, text="Update", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=16, padx=2, pady=6,
                           command=self.update)
        btnupdate.grid(row=0, column=2)

        btnDelete = Button(Buttonframe, text="Delete", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=16, padx=2, pady=6,
                           command=self.idelete)
        btnDelete.grid(row=0, column=3)

        btnclear = Button(Buttonframe, text="Clear", bg="green", fg="white", font=("arial", 12, "bold"), width=20, height=16, padx=2, pady=6,
                          command=self.clear)
        btnclear.grid(row=0, column=4)

        btnexit = Button(Buttonframe, text="Exit", bg="green", fg="white", font=("arial", 12, "bold"), width=18, height=16, padx=2, pady=6,
                         command=self.exit)
        btnexit.grid(row=0, column=5)

#----------------------------------------- Table ---------------------------------------------------------------------------------------------------------
#-------------------------- Scrollbar ------------------------------------
        scroll_x = ttk.Scrollbar(Dataframe, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Dataframe, orient=VERTICAL)

        self.hospital_table = ttk.Treeview(Dataframe, column=("nameoftablets", "reference", "dose", "nooftables", "lot", "issuedate",
                                                       "expdate", "dailydose", "storage", "nhsnumber", "pname", "dob", "address"),
        xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        

        scroll_x.config(command=self.hospital_table.xview)
        scroll_y.config(command=self.hospital_table.yview)

        self.hospital_table.heading("nameoftablets", text="Name of Tablets")
        self.hospital_table.heading("reference", text="Reference No. ")
        self.hospital_table.heading("dose", text="Dose")
        self.hospital_table.heading("nooftables", text="No of Tablets")
        self.hospital_table.heading("lot", text="Lot")
        self.hospital_table.heading("issuedate", text="Issue Date")
        self.hospital_table.heading("expdate", text="Exp Date")
        self.hospital_table.heading("dailydose", text="Daily Date")
        self.hospital_table.heading("storage", text="Storage")
        self.hospital_table.heading("nhsnumber", text="NHS Number")
        self.hospital_table.heading("pname", text="Patient Name")
        self.hospital_table.heading("dob", text="DOB")
        self.hospital_table.heading("address", text="Address")

        self.hospital_table["show"] = "headings"

        self.hospital_table.column("nameoftablets", width=5)
        self.hospital_table.column("reference", width=5)
        self.hospital_table.column("dose", width=5)
        self.hospital_table.column("nooftables", width=5)
        self.hospital_table.column("lot", width=5)
        self.hospital_table.column("issuedate", width=5)
        self.hospital_table.column("expdate", width=5)
        self.hospital_table.column("dailydose", width=5)
        self.hospital_table.column("storage", width=5)
        self.hospital_table.column("nhsnumber", width=5)
        self.hospital_table.column("pname", width=5)
        self.hospital_table.column("dob", width=5)
        self.hospital_table.column("address", width=5)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        self.hospital_table.pack(fill=BOTH, expand=1)
        self.hospital_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fatch_data()



#------------------------------ functionality ----------------------------------------      

    def iPrescriptionTableData(self):
        if self.nameoftablet.get() == "" or self.ref.get() == "":
            tkinter.messagebox.showerror("Error", "Please enter the required fields: Nameoftablets, ref")
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Akash@2001", database="Hospital")
            my_cursor = conn.cursor()
            my_cursor.execute("INSERT INTO hospital VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                self.nameoftablet.get(),
                self.ref.get(),
                self.Dose.get(),
                self.numberoftables.get(),
                self.lot.get(),
                self.issuedate.get(),
                self.expdate.get(),
                self.dailydose.get(),
                self.storageadvice.get(),
                self.nhsnumber.get(),
                self.patientname.get(),
                self.dateofbirth.get(),
                self.patientaddress.get(),
            ))
            conn.commit()
            self.fatch_data()
            conn.close()
            tkinter.messagebox.showinfo("success","recored has been added sussesfully")
            # Refresh the table after inserting data
            self.show_data_in_table()
    def update(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Akash@2001", database="Hospital")
            my_cursor = conn.cursor()

            update_query = """
                UPDATE hospital
                SET nameoftablets=%s, dose=%s, numberoftablets=%s, lot=%s, issuedate=%s, expdate=%s, dailydose=%s,
                    storage=%s, nhsnumber=%s, patientname=%s, dob=%s, patientaddress=%s
                WHERE Reference_no=%s
                """

            my_cursor.execute(update_query, (
                self.nameoftablet.get(),
                self.Dose.get(),
                self.numberoftables.get(),
                self.lot.get(),
                self.issuedate.get(),
                self.expdate.get(),
                self.dailydose.get(),
                self.storageadvice.get(),
                self.nhsnumber.get(),
                self.patientname.get(),
                self.dateofbirth.get(),
                self.patientaddress.get(),
                self.ref.get(),
                ))

            conn.commit()
            tkinter.messagebox.showinfo("Success", "Data updated successfully")
        except Exception as e:
            tkinter.messagebox.showerror("Error", f"Error updating data: {str(e)}")
        finally:
            conn.close()

        # Refresh the table after updating data
        self.fatch_data()

        


        
    def fatch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Akash@2001", database="Hospital")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from hospital")
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.hospital_table.delete(*self.hospital_table.get_children())
            for i in rows:
                self.hospital_table.insert("",END,values=i)
            conn.close()
    def get_cursor(self,event=""):
        cursor_row=self.hospital_table.focus()
        content=self.hospital_table.item(cursor_row)
        row=content["values"]
        self.nameoftablet.set(row[0])
        self.ref.set(row[1])
        self.Dose.set(row[2])
        self.numberoftables.set(row[3])
        self.lot.set(row[4])
        self.issuedate.set(row[5])
        self.expdate.set(row[6])
        self.dailydose.set(row[7])
        self.storageadvice.set(row[8])
        self.nhsnumber.set(row[9])
        self.patientname.set(row[10])
        self.dateofbirth.set(row[11])
        self.patientaddress.set(row[12])

    def iprescription(self):
        prescription_text = (
                "Name of Tablets: \t" + self.nameoftablet.get() + "\n" +
                "Reference No.: \t" + self.ref.get() + "\n" +
                "Dose: \t" + self.Dose.get() + "\n" +
                "No of Tablets: \t" + self.numberoftables.get() + "\n" +
                "Lot: \t" + self.lot.get() + "\n" +
                "Issue Date: \t" + self.issuedate.get() + "\n" +
                "Exp Date: \t" + self.expdate.get() + "\n" +
                "Daily Dose: \t" + self.dailydose.get() + "\n" +
                "Storage Advice: \t" + self.storageadvice.get() + "\n" +
                "NHS Number: \t" + self.nhsnumber.get() + "\n" +
                "Patient Name: \t" + self.patientname.get() + "\n" +
                "Date of Birth: \t" + self.dateofbirth.get() + "\n" +
                "Patient Address: \t" + self.patientaddress.get() + "\n"
                 )
        self.txtPrescription.insert(END, prescription_text)


    def idelete(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Akash@2001", database="Hospital")
        my_cursor = conn.cursor()
        query="delete from hospital where Reference_no=%s"
        value=(self.ref.get(),)
        my_cursor.execute(query,value)

        conn.commit()
        conn.close()
        self.fatch_data()
        tkinter.messagebox.showinfo("Delete","patient has deleted succesfully")

    def clear(self):
        self.nameoftablet.set("")
        self.ref.set("")
        self.Dose.set("")
        self.numberoftables.set("")
        self.lot.set("")
        self.issuedate.set("")
        self.expdate.set("")
        self.dailydose.set("")
        self.sideeffect.set("")
        self.furtherinfo.set("")
        self.storageadvice.set("")
        self.drivingusingmachine.set("")
        self.howtousemedication.set("")
        self.patientid.set("")
        self.nhsnumber.set("")
        self.patientname.set("")
        self.dateofbirth.set("")
        self.patientaddress.set("")
    
        self.txtPrescription.delete(1.0, END)
    
    def exit(self):
        iexit=tkinter.messagebox.askyesno("hospital management system","confirm you want to exit")
        if iexit>0:
            root.destroy()
            return


if __name__ == "__main__":
    root = tk.Tk()
    app = Hospital(root)
    root.mainloop()
