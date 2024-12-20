import tkinter as tk
from tkinter import Toplevel, messagebox
import mysql.connector

#  connection 
mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hospital"
        
    )

cur=mydb.cursor()


# Heading
root = tk.Tk()
root.title("Hospital Management System")

# Patient window
def open_patient_window():
    patient_window = Toplevel(root)
    patient_window.title("Patient Management")
    
    # Patient label
    tk.Label(patient_window, text="Patient ID").grid(row=0, column=0)
    patient_id_entry = tk.Entry(patient_window)
    patient_id_entry.grid(row=0, column=1)

    tk.Label(patient_window, text="Medicine ID").grid(row=1, column=0)
    medicine_id_entry_patient = tk.Entry(patient_window)
    medicine_id_entry_patient.grid(row=1, column=1)

    tk.Label(patient_window, text="Entry Date").grid(row=2, column=0)
    entry_date_entry = tk.Entry(patient_window)
    entry_date_entry.grid(row=2, column=1)

    tk.Label(patient_window, text="Exit Date").grid(row=3, column=0)
    exit_date_entry = tk.Entry(patient_window)
    exit_date_entry.grid(row=3, column=1)

    # Patient 
    def add_patient():
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hospital"
        
    )

        
        cur=mydb.cursor()
        try:
            query="INSERT INTO Patients (patient_id, medicine_id, entry_date, exit_date) VALUES (%s, %s, %s, %s)" 

            cur.execute(query,(patient_id_entry.get(),medicine_id_entry_patient.get(),entry_date_entry.get(),exit_date_entry.get()))
            mydb.commit()
            messagebox.showinfo("Success", "Patient added successfully!")
        except mysql.connector.Error  as err:
            messagebox.showerror("Error", f"ERROR: {err}")
        finally:
            mydb.close()      

    def delete_patient():

        patient_id=patient_id_entry.get()
        if patient_id:
             
             try:
                query="DELETE FROM Patients WHERE patient_id = %s"
                cur.execute(query,(patient_id,))     
                mydb.commit()
                messagebox.showinfo("Success", f"Patient with ID {patient_id} deleted.")
            
             except mysql.connector.Error as err:
                 
                  messagebox.showerror("Error", f"Error{err}")
        else:
            messagebox.showerror("Error", "Please enter a Patient ID to delete.")

        patient_id_entry.delete(0, tk.END)
        medicine_id_entry_patient.delete(0, tk.END)
        entry_date_entry.delete(0, tk.END) 
        exit_date_entry.delete(0,tk.END)   
            

    #  Patient Operations
    tk.Button(patient_window, text="Add Patient", command=add_patient).grid(row=4, column=0)
    tk.Button(patient_window, text="Delete Patient", command=delete_patient).grid(row=4, column=1)

#  Medicine window
def open_medicine_window():
    medicine_window = Toplevel(root)
    medicine_window.title("Medicine Management")
    
    # Medicine options
    tk.Label(medicine_window, text="Medicine ID").grid(row=0, column=0)
    medicine_id_entry = tk.Entry(medicine_window)
    medicine_id_entry.grid(row=0, column=1)

    tk.Label(medicine_window, text="Medicine Name").grid(row=1, column=0)
    medicine_name_entry = tk.Entry(medicine_window)
    medicine_name_entry.grid(row=1, column=1)

    tk.Label(medicine_window, text="Quantity").grid(row=2, column=0)
    quantity_entry = tk.Entry(medicine_window)
    quantity_entry.grid(row=2, column=1)

    # Medicine Button operation
    def add_medicine():
        mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hospital"
        
    )

        cur=mydb.cursor()

        try:     
            query="INSERT INTO Medicines (medicine_id, medicine_name, quantity) VALUES (%s, %s, %s)" 
            cur.execute(query,(medicine_id_entry.get(), medicine_name_entry.get(), quantity_entry.get()))
            mydb.commit()
            messagebox.showinfo("Success", "Medicine added successfully!")
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error: {err}")
        finally:
            mydb.close()

    def delete_medicine():

        try:
            
            cur = mydb.cursor()
            cur.execute("DELETE FROM Medicines WHERE medicine_id = %s", (medicine_id_entry.get(),))
            mydb.commit()
            if cur.rowcount == 0:
                messagebox.showinfo("Info", "No medicine found with the given ID.")
            else:
                messagebox.showinfo("Success", "Medicine deleted successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"Failed to delete medicine: {e}")
        finally:
            mydb.close()

    #  Medicine Operations
    tk.Button(medicine_window, text="Add Medicine", command=add_medicine).grid(row=3, column=0)
    tk.Button(medicine_window, text="Delete Medicine", command=delete_medicine).grid(row=3, column=1)

#  display join results
def display_join_results(join_type):

    mydb=mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="Hospital"
        
    )

    cur=mydb.cursor()
    try:
        
        if join_type == "Inner":
            query = """
                SELECT Patients.patient_id, Patients.medicine_id, Patients.entry_date, Patients.exit_date,
                       Medicines.medicine_name, Medicines.quantity
                FROM Patients
                INNER JOIN Medicines ON Patients.medicine_id = Medicines.medicine_id
            """
        elif join_type == "Left":
            query = """
                SELECT Patients.patient_id, Patients.medicine_id, Patients.entry_date, Patients.exit_date,
                       Medicines.medicine_name, Medicines.quantity
                FROM Patients
                LEFT JOIN Medicines ON Patients.medicine_id = Medicines.medicine_id
            """
        elif join_type == "Right":
            query = """
                SELECT Patients.patient_id, Patients.medicine_id, Patients.entry_date, Patients.exit_date,
                       Medicines.medicine_name, Medicines.quantity
                FROM Patients
                RIGHT JOIN Medicines ON Patients.medicine_id = Medicines.medicine_id
            """
        elif join_type == "Full Outer":
            query = """
                SELECT Patients.patient_id, Patients.medicine_id, Patients.entry_date, Patients.exit_date,
                       Medicines.medicine_name, Medicines.quantity
                FROM Patients
                FULL OUTER JOIN Medicines ON Patients.medicine_id = Medicines.medicine_id
            """

        else:
             raise ValueError("Invalid join type specified")

        cur.execute(query)
        results = cur.fetchall()
        
        # Display results in a new pop-up or console
        result_window = Toplevel(root)
        result_window.title(f"{join_type} Join Results")
         



        for idx, row in enumerate(results):
            tk.Label(result_window, text=str(row)).grid(row=idx, column=0)
    except Exception as e:
        messagebox.showerror("Error", f"Error: {e}")
    finally:
        cur.close()
        mydb.close()

# Open Patient and Medicine Windows
tk.Button(root, text="Manage Patients", command=open_patient_window).grid(row=0, column=0)
tk.Button(root, text="Manage Medicines", command=open_medicine_window).grid(row=0, column=1)

#  Joins
tk.Button(root, text="Inner Join", command=lambda: display_join_results("Inner")).grid(row=1, column=0)
tk.Button(root, text="Left Join", command=lambda: display_join_results("Left")).grid(row=1, column=1)
tk.Button(root, text="Right Join", command=lambda: display_join_results("Right")).grid(row=1, column=2)
tk.Button(root, text="Full Outer Join", command=lambda: display_join_results("Full Outer")).grid(row=1, column=3)

root.mainloop()