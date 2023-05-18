import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as tkst
from PIL import ImageTk, Image
import os


class Manage:
        
    def __init__(self, dashboard_window):

        self.dashboard_window = dashboard_window
        dashboard_window.rowconfigure(0, weight=1)
        dashboard_window.columnconfigure(0, weight=1)
        screen_width = dashboard_window.winfo_screenwidth()
        screen_height = dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # window Icon
        icon = PhotoImage(file='images/pulpaa.png')
        dashboard_window.iconphoto(True, icon)
        dashboard_window.title('Welcome to Pulpa drinks shop')

        # Navigating through windows
        product_page = Frame(dashboard_window)
        purchase_page = Frame(dashboard_window)

        for frame in (product_page, purchase_page):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(product_page)

        #*********************************** DB CONNECTION ***************************************

        with sqlite3.connect("./Database/drinkShop.db") as db:
            cur = db.cursor()

        # ************************************* HOME PAGE *************************************

        product_page.config(background='white')
        
        # ************************************* BAR MENU *************************************

        menuBar_line = Canvas(product_page, width=2600, height=1.5, bg='#f20089', highlightthickness=0)
        menuBar_line.place(x=0, y=90)

        home_bgImg = Image.open('images/pulpaa.png')
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(product_page, image=photo, bg='white')
        home_bg.image = photo
        home_bg.place(x=0, y=0)

         # ************************************* HOME BUTTON **************************************************

        def Home():
            dashboard_window.withdraw()
            os.system("python dashboard.py")
            dashboard_window.destroy()

        home_button = Button(product_page, text='Home', bg='white', font=("", 13, "bold"), bd=0, fg='#000',
                             cursor='hand2', activebackground='white', activeforeground='#f20089', command=Home)
        home_button.place(x=110, y=31)


        # ************************************* MANAGE BUTTON *************************************
        manage_button = Button(product_page, text='Manage', bg='white', font=("", 13, "bold"), bd=0, fg='#f20089',
                               cursor='hand2', activebackground='white', activeforeground='#f20089')
        manage_button.place(x=200, y=31)

        # ************************************* PURCHASE BUTTON *************************************

        def Purchase():
            dashboard_window.withdraw()
            os.system("python purchase.py")
            dashboard_window.destroy()

        manage_button = Button(dashboard_window, text='Purchase', bg='white', font=("", 13, "bold"), bd=0, fg='#000',
                               cursor='hand2', activebackground='white', activeforeground='#f20089', command=Purchase)
        manage_button.place(x=300, y=31)

        #************************************* The logout button *************************************

        def logout():
            dashboard_window.destroy()
            import login

        logout_button = Button(product_page, text='Logout', bg='white', font=("", 13, "bold"), bd=0, fg='black',
                               cursor='hand2', activebackground='#eee', activeforeground='#f20089', command=logout)
        logout_button.place(x=420, y=31)

        def exit2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=dashboard_window)
            if sure == True:
                 dashboard_window.destroy()
                #Manage_window.destroy()

        #************************************* The Exit button *************************************

        self.button6 = Button(product_page)
        self.button6.place(relx=0.920, rely=0.041, width=86, height=25)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#fd6a36")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="#000")
        self.button6.configure(background="#fd6a36")
        self.button6.configure(font=("", 13, "bold"))
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Exit""")
        self.button6.configure(fg='black', bg='white')
        self.button6.configure(command=exit2)
        self.button6.configure(activebackground='#eee', activeforeground='#f20089')

        coverFrame2 = Frame(product_page, bg='#eee')
        coverFrame2.place(x=0, y=92, width=290, height=630)

        # Manage Drink Label
        managedrink = Label(coverFrame2, text='MANAGE Drink', font=("yu gothic ui", 13, "italic"), bg='#eee',
                                     fg='#f20089')
        managedrink.place(x=85, y=19)

        coverFrame3 = LabelFrame(coverFrame2, bg='white', bd='2.4')
        coverFrame3.place(x=20, y=65, width=255, height=580)

        drink = StringVar()
        type = StringVar()
        discount = StringVar()
        in_stock = StringVar()
        price = StringVar()
        drink_id = StringVar()

        #ID 
        idLabel = Label(coverFrame3, text="#", bg='white', fg='#f20089',  font=("yu gothic ui", 13, "bold"))
        idLabel.place(x=5, y=18)
        idName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="white", fg="black",
                                     font=("", 10, 'bold'), textvariable=drink_id)
        idName_entry.place(x=22, y=20, width=40, height=24)
        idName_entry.config(highlightbackground="#6b6a69", highlightcolor="#f20089")

        #Drink NAME 
        drinkLabel = Label(coverFrame3, text="Drink", bg='white', fg='#f20089', font=("yu gothic ui", 12, "italic"))
        drinkLabel.place(x=90, y=17)
        drinkName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#eee", fg="black",
                                         font=("", 10, 'bold'), textvariable=drink)
        drinkName_entry.place(x=10, y=62, width=225, height=34)
        drinkName_entry.config(highlightbackground="#6b6a69", highlightcolor="#f20089")

        #Drink TYPE
        typeLabel = Label(coverFrame3, text="TYPE", bg='white', fg='#f20089', font=("yu gothic ui", 12, "italic"))
        typeLabel.place(x=90, y=99)
        typeName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#eee", fg="black",
                                       font=("", 10, 'bold'), textvariable=type)
        typeName_entry.place(x=10, y=130, width=225, height=34)
        typeName_entry.config(highlightbackground="#6b6a69", highlightcolor="#f20089")

        #Drink DISCOUNT
        discountLabel = Label(coverFrame3, text="DISCOUNT", bg='white', fg='#f20089', font=("yu gothic ui", 12, "italic"))
        discountLabel.place(x=70, y=170)
        discountName_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#eee", fg="#6b6a69",
                                           font=("", 10, 'bold'), textvariable=discount)
        discountName_entry.place(x=10, y=200, width=225, height=34)
        discountName_entry.config(highlightbackground="#6b6a69", highlightcolor="#f20089")

        # IN STOCK 
        inStockLabel = Label(coverFrame3, text="IN STOCK", bg='white', fg='#f20089', font=("yu gothic ui", 12, "italic"))
        inStockLabel.place(x=75, y=240)
        inStock_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#eee", fg="#6b6a69",
                                      font=("", 12, 'bold'), textvariable=in_stock)
        inStock_entry.place(x=10, y=270, width=225, height=34)
        inStock_entry.config(highlightbackground="#6b6a69", highlightcolor="#f20089")

        # PRICE
        priceLabel = Label(coverFrame3, text="PRICE", bg='white', fg='#f20089', font=("yu gothic ui", 12, "italic"))
        priceLabel.place(x=86, y=310)
        price_entry = Entry(coverFrame3, highlightthickness=2, relief=FLAT, bg="#eee", fg="#6b6a69",
                                    font=("", 12, 'bold'), textvariable=price)
        price_entry.place(x=20, y=340, width=160, height=34)
        price_entry.config(highlightbackground="#6b6a69", highlightcolor="#f20089")

        # Currency
        currencyLabel = Label(coverFrame3, text="Dh", bg='white', fg='#f20089',  font=("yu gothic ui", 12, "italic"))
        currencyLabel.place(x=198, y=340)


        #****************************************** Tree View ************************************************

        def show_all():
            conn = sqlite3.connect("./Database/drinkShop.db")
            cur = conn.cursor()
            cur.execute("select * from drink_category")
            rows = cur.fetchall()
            if len(rows) != 0:
                drink_tree.delete(*drink_tree.get_children())
                for row in rows:
                    drink_tree.insert('', END, values=row)
                conn.commit()

            conn.close()

        #FETCHING    

        def drink_info(ev):
            viewInfo = drink_tree.focus()
            coffee_data = drink_tree.item(viewInfo)
            row = coffee_data['values']
            drink_id.set(row[0])
            drink.set(row[1])
            type.set(row[2])
            discount.set(row[3])
            in_stock.set(row[4])
            price.set(row[5])        

        # Define and initialize the price variable
        price = StringVar()
        def add_drink():
            if drink_id.get() == "":
                messagebox.showerror("Failed", "Drink data can't be empty !")
            else:
                conn = sqlite3.connect("./Database/drinkShop.db")
                cur = conn.cursor()
                cur.execute("INSERT INTO drink_category values(?,?,?,?,?,?)",
                                (drink_id.get(), drink.get(), type.get(), discount.get(), in_stock.get(), price.get()))
                conn.commit()
                conn.close()
                show_all()
                messagebox.showinfo("Success", "The drink has been  added Successfully")        

        def delete_records():
            try:
                tree_view_content = drink_tree.focus()
                tree_view_items = drink_tree.item(tree_view_content)
                tree_view_values = tree_view_items['values'][1]
                ask = messagebox.askyesno("Warning", f"Are you sure you want to delete records of {tree_view_values}")
                if ask is True:
                    conn = sqlite3.connect("./Database/drinkShop.db")
                    cur = conn.cursor()
                    cur.execute("DELETE FROM drink_category where drink_id=?", [drink_id.get()])
                    conn.commit()
                    show_all()
                    clear_all()
                    conn.close()
                    messagebox.showinfo("Success", f" {tree_view_values} records has been deleted Successfully")
                else:
                    pass

            except BaseException as msg:
                print(msg)
                messagebox.showerror("Error", "There is an error deleting the data\n Make sure you have Selected the data")

        def update():
            conn = sqlite3.connect("./Database/drinkShop.db")
            cur = conn.cursor()
            cur.execute(
                "UPDATE drink_category set drink_name=?,type=?,discount=?,in_stock=?,drink_price=? where "
                "drink_id=?",
                (drink.get(), type.get(), discount.get(), in_stock.get(), price.get(), drink_id.get()))
            conn.commit()
            conn.close()
            show_all()
            messagebox.showinfo("Success", "Drink Updated Successfully")  

        def clear_all():
            drink_id.set("")
            drink.set("")
            type.set("")
            discount.set("")
            in_stock.set("")
            price.set("")

        #*********************************** Delete Button ***********************************************
        self.button3 = Button(coverFrame3)
        self.button3.place(relx=0.539, rely=0.680, width=86, height=25)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#fd6a36")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="black")
        self.button3.configure(background="#ffb3c1")
        self.button3.configure(font="-family {Poppins SemiBold} -size 10")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Delete""")
        self.button3.configure(command=delete_records) 
        self.button3.configure(activebackground='#ffb3c1', activeforeground='#f20089')    

        #*********************************** Add Button ***********************************************

        self.button4 = Button(coverFrame3)
        self.button4.place(relx=0.039, rely=0.680, width=84, height=25)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#fd6a36")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="black")
        self.button4.configure(background="#ffb3c1")
        self.button4.configure(font="-family {Poppins SemiBold} -size 10")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Add""")
        self.button4.configure(command=add_drink)
        self.button4.configure(activebackground='#ffb3c1', activeforeground='#f20089')  

        #*********************************** Update Button ***********************************************

        self.button5 = Button(coverFrame3)
        self.button5.place(relx=0.039, rely=0.770, width=86, height=25)
        self.button5.configure(relief="flat")
        self.button5.configure(overrelief="flat")
        self.button5.configure(activebackground="#fd6a36")
        self.button5.configure(cursor="hand2")
        self.button5.configure(foreground="black")
        self.button5.configure(background="#ffb3c1")
        self.button5.configure(font="-family {Poppins SemiBold} -size 10")
        self.button5.configure(borderwidth="0")
        self.button5.configure(text="""Update""")
        self.button5.configure(command=update)
        self.button5.configure(activebackground='#ffb3c1', activeforeground='#f20089')  

        #*********************************** Clear Button ***********************************************

        self.button6 = Button(coverFrame3)
        self.button6.place(relx=0.539, rely=0.770, width=86, height=25)
        self.button6.configure(relief="flat")
        self.button6.configure(overrelief="flat")
        self.button6.configure(activebackground="#fd6a36")
        self.button6.configure(cursor="hand2")
        self.button6.configure(foreground="black")
        self.button6.configure(background="#ffb3c1")
        self.button6.configure(font="-family {Poppins SemiBold} -size 10")
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Clear""")
        self.button6.configure(command=clear_all)
        self.button6.configure(activebackground='#ffb3c1', activeforeground='#f20089')  

        #*********************************** Purchase Button ***********************************************

        #coverFrame = Frame(product_page, bg='red')
        #coverFrame.place(x=200, y=50, width=150, height=110)

        #**************************************************************************************************
        coverFrame = Frame(product_page, bg='white')
        coverFrame.place(x=315, y=98, width=1065, height=630)

        style = ttk.Style()
        style.theme_use("clam")
        scrollbarx = Scrollbar(product_page, orient=HORIZONTAL)
        scrollbary = Scrollbar(product_page, orient=VERTICAL)
        drink_tree = ttk.Treeview(coverFrame)
        drink_tree.place(relx=0.040, rely=0.1228, width=900, height=410)
        drink_tree.configure(yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
        drink_tree.configure(selectmode="extended")

        scrollbary.configure(command=drink_tree.yview)
        scrollbarx.configure(command=drink_tree.xview)
        scrollbary.place(relx=0.972, rely=0.220, width=25, height=412)

        #********************************* Setting the headings and the columns of the tree *******************************************

        drink_tree.configure(
            columns=(
                "DrinkID",
                "DrinkName",
                "Type",
                "Discount",
                "Price",
                "InStock")
                )
        
        drink_tree.heading("DrinkID", text="#", anchor=N)
        drink_tree.heading("DrinkName", text="DRINK", anchor=N)
        drink_tree.heading("Type", text="TYPE", anchor=N)
        drink_tree.heading("Discount", text="DISCOUNT", anchor=N)
        drink_tree.heading("InStock", text="IN STOCK", anchor=N)
        drink_tree.heading("Price", text="PRICE ( Dh )", anchor=N)

        drink_tree.column("#0", stretch=NO, minwidth=0, width=0)
        drink_tree.column("#1", stretch=NO, minwidth=0, width=50, anchor=N)
        drink_tree.column("#2", stretch=NO, minwidth=0, width=288, anchor=N)
        drink_tree.column("#3", stretch=NO, minwidth=0, width=176, anchor=N)
        drink_tree.column("#4", stretch=NO, minwidth=0, width=110, anchor=N)
        drink_tree.column("#5", stretch=NO, minwidth=0, width=110, anchor=N)
        drink_tree.column("#6", stretch=NO, minwidth=0, width=160, anchor=N)
        drink_tree.bind("<ButtonRelease-1>", drink_info)
        show_all()

        #********************************************* BILL PAGE *******************************************

         #Item Classe

    class drinkItem:
            def __init__(self, drink, price, qty):
                self.product_name = drink
                self.price = price
                self.qty = qty

def page():
    window = Tk()
    Manage(window)
    window.mainloop()


if __name__ == '__main__':
    page()
