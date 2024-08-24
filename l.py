from tkinter import *
from tkinter import messagebox
from tkinter import ttk
import pymysql
db_connection=pymysql.connect(
    host='localhost',
    user='root',
    password='saranya',
    database='lead'
)
my_database=db_connection.cursor()
print("Connected successfully")

admin_list = []
lead_list = []
root = Tk()
root.title('CRM')
root.geometry("1200x800")
root.configure(background='#1A5276')
def admin_signin():
    def save_admin():
        name = name_entry.get()
        mobile = mobile_entry.get()
        password = password_entry.get()
        if not name or not mobile or not password:
            messagebox.showerror("Error",
                                 "Please fill out all fields")
            return
        else:
            sql_statement="INSERT INTO admin_register (name,mobile,password) values(%s,%s,%s)"
            values=(name,mobile,password)
            my_database.execute(sql_statement,values)
            db_connection.commit()
            
            admin_list.append({'name': name,
                           'mobile': mobile, 'password': password})
            messagebox.showinfo("Success",
                            "Admin registered successfully")
        signin_frame.destroy()
    signin_frame = Frame(root, bg='#1A5276',width=500,height=700)
    signin_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(signin_frame, text="Admin Sign-in",
          font=('century gothic', 25, 'bold'), fg="white")

    Label(signin_frame, text="Name",
          font=('century gothic', 15, 'bold'),
          fg="white", bg='#1A5276').pack(pady=5)
    name_entry = Entry(signin_frame,
                       font=('century gothic', 15))
    name_entry.pack(pady=5)

    Label(signin_frame, text="Mobile No",
          font=('century gothic', 15, 'bold'),
          fg="white", bg='#1A5276').pack(pady=5)
    mobile_entry = Entry(signin_frame,
                         font=('century gothic', 15))
    mobile_entry.pack(pady=5)

    Label(signin_frame, text="Password",
         font=('century gothic', 15, 'bold'),
          fg="white", bg='#1A5276').pack(pady=5)
    password_entry = Entry(signin_frame,
                           font=('century gothic', 15), show='*')
    password_entry.pack(pady=5)

    Button(signin_frame, text="Register",
           command=save_admin,
           font=('century gothic', 15, 'bold'),
           bg="#EE8309", fg="white").pack(pady=20)

def manage_leads():
    lead_frame = Frame(root, bg='#1A5276')
    lead_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

    Label(lead_frame, text="Lead Details",
          font=('century gothic', 25, 'bold'),
          fg="white", bg='#1A5276').pack(pady=20)

    columns = ("Name", "Email", "Mobile",
               "LeadSource", "LeadOwner", "Status",
               "FollowupDate", "NextFollowupDate")
    tree = ttk.Treeview(lead_frame, columns=columns,
                        show='headings')
    
    for col in columns:
        tree.heading(col, text=col)
    tree.pack(pady=20)

    for lead in lead_list:
        tree.insert("", END, values=(lead['name'],
                                     lead['email'], lead['mobile'],
                                  lead['lead_source'], lead['lead_owner'], lead['status'], lead['followup_date'], lead['next_followup_date']))
    sql="SELECT name, email, mobile, leadsource, leadowner, statuss, followup_dates, nextfollowup_date from leadd"
    my_database.execute(sql)
    res=my_database.fetchall()
    for lead in res:
        add_lead(*lead) 
    def add_lead():
        def save_lead():
            name = name_entry.get()
            email = email_entry.get()
            mobile = mobile_entry.get()
            lead_source = lead_source_combobox.get()
            lead_owner = lead_owner_combobox.get()
            status = status_combobox.get()
            followup_date = followup_date_entry.get()
            next_followup_date = next_followup_date_entry.get()
            if not (name and email and mobile and
                    lead_source and lead_owner and status
                    and followup_date and next_followup_date):
                messagebox.showerror("Error",
                                     "Please fill out all fields")
                return
            elif (name and email and mobile and lead_source_combobox and lead_owner_combobox and status_combobox and followup_date_entry and next_followup_date_entry):
                op = messagebox.askyesno("Save", "Do you really want to save?")
                if op > 0:
                    sql_statement="INSERT INTO leadd (name,email,mobile,leadsource, leadowner,statuss,followup_dates,nextfollowup_date) values(%s,%s,%s,%s,%s,%s,%s,%s)"
                    values=(name,email,mobile,lead_source_combobox,lead_owner_combobox,status_combobox, followup_date_entry,next_followup_date_entry)
                    my_database.execute(sql_statement,values)
                    db_connection.commit()
                    messagebox.showinfo("DONE", "Stored Successfully")
                    lead_list.append({
                       'name': name, 'email': email, 'mobile': mobile,
                         'lead_source': lead_source, 
                         'lead_owner': lead_owner, 'status': status,
                           'followup_date': followup_date, 
                         'next_followup_date': next_followup_date })
            tree.insert("", END, values=(name, email, mobile,
                                         lead_source, lead_owner, status,
                                         followup_date, next_followup_date))
            messagebox.showinfo("Success",
                                "Lead added successfully")
            add_lead_frame.destroy()
        add_lead_frame = Frame(root, bg='#1A5276')
        add_lead_frame.place(relx=0.5, rely=0.5,
                             anchor=CENTER)
        Label(add_lead_frame, text="Add Lead Details",
              font=('century gothic', 25, 'bold'), fg="white",
              bg='#1A5276').pack(pady=20)
        Label(add_lead_frame, text="Name",
              font=('century gothic', 15, 'bold'), fg="white",
              bg='#1A5276').pack(pady=5)
        name_entry = Entry(add_lead_frame,
                           font=('century gothic', 15))
        name_entry.pack(pady=5)

        Label(add_lead_frame, text="Email",
              font=('century gothic', 15, 'bold'),
              fg="white", bg='#1A5276').pack(pady=5)
        email_entry = Entry(add_lead_frame,
                            font=('century gothic', 15))
        email_entry.pack(pady=5)

        Label(add_lead_frame, text="Mobile",
              font=('century gothic', 15, 'bold'), fg="white",
              bg='#1A5276').pack(pady=5)
        mobile_entry = Entry(add_lead_frame,
                             font=('century gothic', 15))
        mobile_entry.pack(pady=5)
        Label(add_lead_frame, text="Lead Source",
              font=('century gothic', 15, 'bold'),
              fg="white", bg='#1A5276').pack(pady=5)
        lead_source_combobox =ttk.Combobox(add_lead_frame, values=["Website",
                                             "Social Media", "Reference"],
                     font=('century gothic', 15))
        lead_source_combobox.pack(pady=5)
        Label(add_lead_frame, text="Lead Owner"
              , font=('century gothic', 15, 'bold'), fg="white",
              bg='#1A5276').pack(pady=5)
        lead_owner_combobox = ttk.Combobox(add_lead_frame, values=["Admin1",
                                             "Admin2", "Admin3"],
                     font=('century gothic', 15))
        lead_owner_combobox.pack(pady=5)
        Label(add_lead_frame, text="Status",
              font=('century gothic', 15, 'bold'),
              fg="white", bg='#1A5276').pack(pady=5)
        status_combobox = ttk.Combobox(add_lead_frame,
                                       values=["Registered", "Follow Up",
                                               "Not Interested"],
                                       font=('century gothic', 15))
        status_combobox.pack(pady=5)

        Label(add_lead_frame, text="Follow Up Date",
              font=('century gothic', 15, 'bold'), fg="white",
              bg='#1A5276').pack(pady=5)
        followup_date_entry = Entry(add_lead_frame,
                                    font=('century gothic', 15))
        followup_date_entry.pack(pady=5)

        Label(add_lead_frame, text="Next Follow Up Date",
              font=('century gothic', 15, 'bold'), fg="white",
              bg='#1A5276').pack(pady=5)
        next_followup_date_entry = Entry(add_lead_frame,
                                         font=('century gothic', 15))
        next_followup_date_entry.pack(pady=5)

        Button(add_lead_frame, text="Save Lead",
               command=save_lead, font=('century gothic', 15,
                                        'bold'), bg="#EE8309",
               fg="white").pack(pady=20)

    Button(lead_frame, text="Add Lead", command=add_lead, font=('century gothic', 15, 'bold'), bg="#EE8309", fg="white").pack(pady=20)
    Button(lead_frame, text="Back", command=lead_frame.destroy, font=('century gothic', 15, 'bold'), bg="white", fg="#1A5276").pack(pady=10)

# Main Interface
main_frame = Frame(root, bg='#1A5276')
main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

Label(main_frame, text="CRM",
      font=('century gothic', 50, 'bold'), fg="white",
      bg='#1A5276').pack(pady=50)

Button(main_frame, text="Admin Signin",
       command=admin_signin,
       font=('century gothic', 20, 'bold'),
       bg="#EE8309", fg="white").pack(pady=20)
Button(main_frame, text="Manage Leads",
       command=manage_leads, font=('century gothic',
                                   20, 'bold'), bg="#EE8309", fg="white").pack(pady=40)

# Run the main loop
root.mainloop()
