import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter import scrolledtext as tkst
from PIL import ImageTk, Image
import os
import tempfile

class Manage:
        
    def __init__(self, dashboard_window):

        self.dashboard_window = dashboard_window
        self.dashboard_window.rowconfigure(0, weight=1)
        self.dashboard_window.columnconfigure(0, weight=1)
        screen_width = self.dashboard_window.winfo_screenwidth()
        screen_height = self.dashboard_window.winfo_height()
        app_width = 1340
        app_height = 690
        x = (screen_width/2)-(app_width/2)
        y = (screen_height/160)-(app_height/160)
        self.dashboard_window.geometry(f"{app_width}x{app_height}+{int(x)}+{int(y)}")

        # window Icon
        icon = PhotoImage(file='images/pulpaa.png')
        self.dashboard_window.iconphoto(True, icon)
        self.dashboard_window.title('Welcome to Pulpa drinks shop')

        # Navigating through windows
        product_page = Frame(self.dashboard_window)
        purchase_page = Frame(self.dashboard_window)

        for frame in (product_page, purchase_page):
            frame.grid(row=0, column=0, sticky='nsew')

        def show_frame(frame):
            frame.tkraise()

        show_frame(product_page)

        # Declaration :
        self.cart = Cart()
        self.total=0

        #*********************************** DB CONNECTION ***************************************

        with sqlite3.connect("./Database/drinkShop.db") as db:
            self.cur = db.cursor()

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

        def exitt2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.dashboard_window)
            if sure == True:
                 self.dashboard_window.destroy()

         # ************************************* HOME BUTTON **************************************************
        def Home():
            dashboard_window.withdraw()
            os.system("python dashboard.py")
            dashboard_window.destroy()

        home_button = Button(product_page, text='Home', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), bd=0, fg='#000',
                             cursor='hand2', activebackground='white', activeforeground='#f20089', command=Home)
        home_button.place(x=110, y=31)

        # ************************************* MANAGE BUTTON *************************************
        def Manage():
            dashboard_window.withdraw()
            os.system("python manage.py")
            dashboard_window.destroy()

        manage_button = Button(product_page, text='Manage', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), bd=0, fg='black',
                               cursor='hand2', activebackground='white', activeforeground='#f20089', command=Manage)
        manage_button.place(x=200, y=31)

        # ************************************* PURCHASE BUTTON *************************************

        manage_button = Button(product_page, text='Purchase', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), bd=0, fg='#f20089',
                               cursor='hand2', activebackground='white', activeforeground='#f20089')
        manage_button.place(x=310, y=31)

        #************************************* The logout button *************************************

        def logout():
            self.dashboard_window.destroy()
            import login

        logout_button = Button(product_page, text='Logout', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), bd=0, fg='black',
                               cursor='hand2', activebackground='#eee', activeforeground='#f20089', command=logout)
        logout_button.place(x=420, y=31)

        def exit2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=self.dashboard_window)
            if sure == True:
                 self.dashboard_window.destroy()
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
        self.button6.configure(font=("Microsoft YaHei UI Light", 13, "bold"))
        self.button6.configure(borderwidth="0")
        self.button6.configure(text="""Exit""")
        self.button6.configure(fg='black', bg='white')
        self.button6.configure(command=exit2)
        self.button6.configure(activebackground='#eee', activeforeground='#f20089')

        # **************************************************************************************************

        self.cust_name = StringVar()
        self.cust_num = StringVar()
        self.cust_new_bill = StringVar()
        self.cust_search_bill = StringVar()
        self.bill_date = StringVar()

        self.coverFrame2 = Frame(self.dashboard_window, bg='#eee')
        self.coverFrame2.place(x=0, y=92, width=575, height=600)

        self.coverFrame3 = LabelFrame(self.coverFrame2, bg='#eee', bd='2.4')
        self.coverFrame3.place(x=20, y=55, width=535, height=770)

        self.coverFrame5 = Frame(self.dashboard_window, bg='#eee')
        self.coverFrame5.place(x=1060, y=140, width=275, height=490)

        self.coverFrame6 = LabelFrame(self.coverFrame5, bg='#eee', bd='2.4')
        self.coverFrame6.place(x=10, y=10, width=255, height=475)

        #********************************************************************************************************

        self.genBill_no = Label(self.coverFrame6, text='Bill Number', font=("yu gothic ui", 10, "bold"),
                                bg='#eee', fg='#f20089')
        self.genBill_no.place(relx=0.330, rely=0.140)

        self.genBill_date = Label(self.coverFrame6, text='Bill Date', font=("yu gothic ui", 10, "bold"),
                                bg='#eee', fg='#f20089')
        self.genBill_date.place(relx=0.370, rely=0.400)

        self.genCashier_name = Label(self.coverFrame6, text='Cashier Name', font=("yu gothic ui", 10, "bold"),
                                bg='#eee', fg='#f20089')
        self.genCashier_name.place(relx=0.330, rely=0.660)

        #**********************************************************************************************************

        self.cashier_name = Label(self.dashboard_window)
        self.cashier_name.place(x=45, y=170)
        self.cashier_name.configure(font="-family {Poppins Light} -size 11")
        self.cashier_name.configure(foreground="#f20089")
        self.cashier_name.configure(text="Cashier Name")
        self.cashier_name.configure(background="#eee")

        self.payment_method = Label(self.dashboard_window)
        self.payment_method.place(x=45, y=240)
        self.payment_method.configure(font="-family {Poppins Light} -size 11")
        self.payment_method.configure(foreground="#f20089")
        self.payment_method.configure(text="Payment Method")
        self.payment_method.configure(background="#eee")

        self.discount = Label(self.dashboard_window)
        self.discount.place(x=45, y=315)
        self.discount.configure(font="-family {Poppins Light} -size 11")
        self.discount.configure(foreground="#f20089")
        self.discount.configure(text="Discount ( % )")
        self.discount.configure(background="#eee")

        self.drink_name = Label(self.dashboard_window)
        self.drink_name.place(x=45, y=390)
        self.drink_name.configure(font="-family {Poppins Light} -size 11")
        self.drink_name.configure(foreground="#f20089")
        self.drink_name.configure(text="Drink Name")
        self.drink_name.configure(background="#eee")

        self.quantity = Label(self.dashboard_window)
        self.quantity.place(x=45, y=460)
        self.quantity.configure(font="-family {Poppins Light} -size 11")

        self.quantity.configure(foreground="#f20089")
        self.quantity.configure(text="Quantity")
        self.quantity.configure(background="#eee")

        self.entry1 = ttk.Entry(self.dashboard_window)
        self.entry1.place(relx=0.035, rely=0.300, width=477, height=24)
        self.entry1.configure(font="-family {Poppins} -size 12")
        self.entry1.configure(textvariable=self.cust_name)

        self.entry3 = Entry(self.dashboard_window, highlightthickness=2,)
        self.entry3.place(relx=0.420, rely=0.050, width=350, height=29)
        self.entry3.configure(font="-family {Poppins} -size 11")
        self.entry3.configure(relief="flat")
        self.entry3.configure(highlightbackground="#6b6a69", highlightcolor="#f20089")
        self.entry3.configure(textvariable=self.cust_search_bill)
        self.search_txt = "Enter Bill Number to Search ..."
        self.entry3.insert(0, self.search_txt)
        self.entry3.bind("<1>", self.clear_search)

        searchIcon = Image.open('images/search.png')
        photo = ImageTk.PhotoImage(searchIcon)
        search = Label(self.dashboard_window, image=photo, bg='white')
        search.image = photo
        search.place(relx=0.389, rely=0.050)

        self.button2 = Button(self.dashboard_window)
        self.button2.place(relx=0.688, rely=0.050, width=76, height=29)
        self.button2.configure(relief="flat")
        self.button2.configure(overrelief="flat")
        self.button2.configure(activebackground="#fd6a36")
        self.button2.configure(cursor="hand2")
        self.button2.configure(foreground="black")
        self.button2.configure(background="#ffb3c1")
        self.button2.configure(font="-family {Poppins SemiBold} -size 12")
        self.button2.configure(borderwidth="0")
        self.button2.configure(text="""Search""")
        self.button2.configure(activebackground='#fd6a36', activeforeground='#f20089')
        self.button2.configure(command=self.search_bill)

        self.button3 = Button(self.dashboard_window)
        self.button3.place(relx=0.045, rely=0.810, width=86, height=25)
        self.button3.configure(relief="flat")
        self.button3.configure(overrelief="flat")
        self.button3.configure(activebackground="#fd6a36")
        self.button3.configure(cursor="hand2")
        self.button3.configure(foreground="black")
        self.button3.configure(background="#ffb3c1")
        self.button3.configure(font="-family {Poppins SemiBold} -size 10")
        self.button3.configure(borderwidth="0")
        self.button3.configure(text="""Total""")
        self.button3.configure(activebackground='#ffb3c1', activeforeground='#f20089')
        self.button3.configure(command=self.total_bill)


        self.button4 = Button(self.dashboard_window)
        self.button4.place(relx=0.160, rely=0.810, width=84, height=25)
        self.button4.configure(relief="flat")
        self.button4.configure(overrelief="flat")
        self.button4.configure(activebackground="#fd6a36")
        self.button4.configure(cursor="hand2")
        self.button4.configure(foreground="black")
        self.button4.configure(background="#ffb3c1")
        self.button4.configure(font="-family {Poppins SemiBold} -size 10")
        self.button4.configure(borderwidth="0")
        self.button4.configure(text="""Generate""")
        self.button4.configure(activebackground='#ffb3c1', activeforeground='#f20089')
        self.button4.configure(command=self.gen_bill)
    
        self.button7 = Button(self.dashboard_window)
        self.button7.configure(text="""Add To Cart""")
        self.button7.place(relx=0.045, rely=0.890, width=88, height=26)
        self.button7.configure(relief="flat")
        self.button7.configure(overrelief="flat")
        self.button7.configure(activebackground="#fd6a36")
        self.button7.configure(cursor="hand2")
        self.button7.configure(foreground="black")
        self.button7.configure(background="#ffb3c1")
        self.button7.configure(font="-family {Poppins SemiBold} -size 10")
        self.button7.configure(borderwidth="0")
        self.button7.configure(text="Add To Cart")
        self.button7.configure(activebackground='#ffb3c1', activeforeground='#f20089')
        self.button7.configure(command=self.add_to_cart)

        self.button8 = Button(self.dashboard_window)
        self.button8.place(relx=0.158, rely=0.890, width=84, height=26)
        self.button8.configure(relief="flat")
        self.button8.configure(overrelief="flat")
        self.button8.configure(activebackground="#fd6a36")
        self.button8.configure(cursor="hand2")
        self.button8.configure(foreground="black")
        self.button8.configure(background="#ffb3c1")
        self.button8.configure(font="-family {Poppins SemiBold} -size 10")
        self.button8.configure(borderwidth="0")
        self.button8.configure(text="Clear")
        self.button8.configure(activebackground='#ffb3c1', activeforeground='#f20089')
        self.button8.configure(command=self.clear_selection)

        self.button9 = Button(self.dashboard_window)
        self.button9.place(relx=0.270, rely=0.890, width=90, height=26)
        self.button9.configure(relief="flat")
        self.button9.configure(overrelief="flat")
        self.button9.configure(activebackground="#fd6a36")
        self.button9.configure(cursor="hand2")
        self.button9.configure(foreground="black")
        self.button9.configure(background="#ffb3c1")
        self.button9.configure(font="-family {Poppins SemiBold} -size 10")
        self.button9.configure(borderwidth="0")
        self.button9.configure(text="Remove")
        self.button9.configure(activebackground='#ffb3c1', activeforeground='#f20089')
        self.button9.configure(command=self.remove_product)

        text_font = ("Poppins", "9")
        style = ttk.Style()
        style.theme_use("clam")

        self.combo1 = ttk.Combobox(self.dashboard_window, font="-family {Poppins SemiBold} -size 9")
        self.combo1.place(relx=0.035, rely=0.400, width=477, height=26)
        find_category = "SELECT type FROM drink_category"
        self.cur.execute(find_category)
        result1 = self.cur.fetchall()
        cat = []
        for item in result1:
            if item[0] not in cat:
                cat.append(item[0])

        self.combo1['values'] = cat
        self.combo1.configure(state="readonly")
        self.combo1.option_add("*TCombobox*Listbox.font", text_font)
        self.combo1.option_add("*TCombobox*Listbox.selectBackground", "#ffb3c1")
        self.combo1.bind('<<ComboboxSelected>>', self.get_category)

        self.combo2 = ttk.Combobox(self.dashboard_window, font="-family {Poppins SemiBold} -size 9")
        self.combo2.place(relx=0.035, rely=0.510, width=477, height=26)
        self.combo2.configure(state="disabled") 

        self.combo3 = ttk.Combobox(self.dashboard_window, font="-family {Poppins SemiBold} -size 9")
        self.combo3.place(relx=0.035, rely=0.610, width=477, height=26)
        self.combo3.configure(state="disabled")
        self.combo3.option_add("*TCombobox*Listbox.font", text_font)

        self.entry4 = ttk.Entry(self.dashboard_window, font="-family {Poppins SemiBold} -size 9", foreground="#ffb3c1")
        self.entry4.place(relx=0.035, rely=0.720, width=477, height=26)
        self.entry4.configure(state="disabled")

        self.Scrolledtext1 = tkst.ScrolledText(self.dashboard_window)
        self.Scrolledtext1.place(relx=0.452, rely=0.200, width=450, height=490)
        self.Scrolledtext1.configure(borderwidth=0)
        self.Scrolledtext1.configure(font="-family {Podkova} -size 9")
        self.Scrolledtext1.configure(state="normal")
        head = "\n\n\t\t    PULPA    DRINKS    SHOP  \n" \
                "\t\t          M2 Gueliz Marrakech   \n\n\t\t THANK YOU FOR CHOOSING US\n" \
                "\t\t         Come back Soon \n\n\n" + "\tDRINK\t  -----  \tQUANTITY\t  -----  \tPRICE ( Dh )\n"
        self.Scrolledtext1.insert('insert', head)
        self.combo1.bind("<<ComboboxSelected>>", self.get_category)


        btn_print = Button(self.dashboard_window, text="""Print""", command=lambda: self.print_area(self.Scrolledtext1.get('1.0', END)),
                                overrelief="flat", bd=0, foreground="black", relief="flat", cursor="hand2",
                                font="-family {Poppins SemiBold} -size 10", bg='#ffb3c1', activebackground="#ff6c38")
        btn_print.place(relx=0.272, rely=0.810, width=86, height=25)
    
    
    def print_area(txt):
         temp_file = tempfile.mktemp('.txt')
         open(temp_file, 'w').write(txt)
         os.startfile(temp_file, 'print')
        # Optionally, remove the temporary file after printing
        # os.remove(temp_file.name)


   

    def drinkItem(self, drink, price, qty):  
        return {"price":price,"qty": qty,"product":drink}

    def get_category(self, event):
        try:
            self.combo2.configure(state="readonly")
            self.combo2.set('') 
            self.combo3.set('')
            find_subcat = "SELECT discount FROM drink_category WHERE type = ?"
            self.cur.execute(find_subcat, [self.combo1.get()])
            result2 = self.cur.fetchall()
            subcat = []
            for j in range(len(result2)):
                if (result2[j][0] not in subcat):
                    subcat.append(result2[j][0])

            self.combo2.configure(values=subcat)
            self.combo2.bind("<<ComboboxSelected>>", self.get_subcat)
            self.combo3.configure(state="disabled")
        except Exception as ex:
            print("get_category : ",ex)
        

    def get_subcat(self, event):
        try:
            self.combo3.configure(state="readonly")
            self.combo3.set('')
            find_product = "SELECT drink_name FROM drink_category WHERE type = ? and discount = ?"
            self.cur.execute(find_product, [self.combo1.get(), self.combo2.get()])
            result3 = self.cur.fetchall()
            pro = []
            for k in range(len(result3)):
               pro.append(result3[k][0])

            self.combo3.configure(values=pro)
            self.combo3.bind("<<ComboboxSelected>>", self.show_qty)
            self.entry4.configure(state="disabled")
        except Exception as ex:
            print("get_subcat : ",ex)

    def show_qty(self, event):
        try:
            self.entry4.configure(state="normal")
            self.qty_label = Label(self.dashboard_window)
            self.qty_label.place(relx=0.045, rely=0.760, width=82, height=26)
            self.qty_label.configure(font="-family {Poppins SemiBold} -size 9")
            self.qty_label.configure(anchor="w")

            product_name = self.combo3.get()
            find_qty = "SELECT in_stock FROM drink_category WHERE drink_name = ?"
            self.cur.execute(find_qty, [product_name])
            results = self.cur.fetchone()
            self.qty_label.configure(text="In Stock: {}".format(results[0]))
            self.qty_label.configure(background="#eee")
            self.qty_label.configure(foreground="#333333")
        except Exception as ex:
            print("show_qty : ",ex)

    #**************************************** Add to cart **********************************************
    
    def add_to_cart(self):
        try:
            self.Scrolledtext1.configure(state="normal")
            strr = self.Scrolledtext1.get('1.0', END)

            if strr.find('Total') == -1:
                product_name = self.combo3.get()

                if (product_name != ""):
                    product_qty = self.entry4.get()
                    find_mrp = "SELECT drink_price, in_stock FROM drink_category WHERE drink_name = ?"
                    self.cur.execute(find_mrp, [product_name])
                    results = self.cur.fetchall()
                    stock = results[0][1]
                    mrp = results[0][0]

                    if product_qty.isdigit() == True:
                        if (stock - int(product_qty)) >= 0:
                            sp = mrp * int(product_qty)
                            items = self.drinkItem(product_name, mrp, int(product_qty)) 
                            self.cart.add_item(items)
                            self.Scrolledtext1.configure(state="normal")
                            divide = "\t" + ("-" * 70) + "\n"
                            self.Scrolledtext1.insert('insert', divide)
                            bill_text = "\t{}\t  -----  \t{}\t  -----  \t{}\n".format(product_name, product_qty, sp)
                            self.Scrolledtext1.insert('insert', bill_text)
                            self.Scrolledtext1.configure(state="disabled")
                        else:
                            messagebox.showerror("Oops!", "Out of stock. Check quantity.", parent=self.dashboard_window)
                    else:
                        messagebox.showerror("Oops!", "Invalid quantity.", parent=self.dashboard_window)
                else:
                    messagebox.showerror("Oops!", "Choose a product.", parent=self.dashboard_window)
            else:
                self.Scrolledtext1.delete('1.0', END)
                self.Scrolledtext1.delete('1.0', END)
                new_li = []
                li = strr.split("\n")
                for i in range(len(li)):
                    if len(li[i]) != 0:
                        if li[i].find('Total') == -1:
                            new_li.append(li[i])
                        else:
                            break
                for j in range(len(new_li) - 1):
                    self.Scrolledtext1.insert('insert', new_li[j])
                    self.Scrolledtext1.insert('insert', '\n')
                product_name = self.combo3.get()
                if (product_name != ""):
                    product_qty = self.entry4.get()
                    find_mrp = "SELECT drink_price, in_stock, drink_id FROM drink_category WHERE drink_name = ?"
                    self.cur.execute(find_mrp, [product_name])
                    results = self.cur.fetchall()
                    stock = results[0][1]
                    mrp = results[0][0]
                    if product_qty.isdigit() == True:
                        if (stock - int(product_qty)) >= 0:
                            sp = results[0][0] * int(product_qty)
                            item = self.drinkItem(product_name, mrp, int(product_qty))
                            self.cart.add_item(item)
                            self.Scrolledtext1.configure(state="normal")
                            bill_text = "{}\t\t\t\t\t\t{}\t\t\t\t\t   {}\n".format(product_name, product_qty, sp)
                            self.Scrolledtext1.insert('insert', bill_text)
                            self.Scrolledtext1.configure(state="disabled")
                        else:
                            messagebox.showerror("Oops!", "Out of stock", parent=self.dashboard_window)
                    else:
                        messagebox.showerror("Oops!", "Invalid quantity", parent=self.dashboard_window)
                else:
                    messagebox.showerror("Oops!", "Choose a product", parent=self.dashboard_window)

        except Exception as ex:
            print("add_to_cart : ",ex)

        
    #******************************************* Remove from cart ************************************************

    def remove_product(self):
                if(self.cart.isEmpty()!=True):
                    self.Scrolledtext1.configure(state="normal")
                    strr = self.Scrolledtext1.get('1.0', END)
                    if strr.find('Total')==-1:
                        try:
                            self.cart.remove_item()
                        except IndexError:
                            messagebox.showerror("Oops!", "The Cart is empty!!", parent=self.dashboard_window)
                        else:
                            self.Scrolledtext1.configure(state="normal")
                            get_all_bill = (self.Scrolledtext1.get('1.0', END).split("\n"))
                            new_string = get_all_bill[:len(get_all_bill)-3]
                            self.Scrolledtext1.delete('1.0', END)
                            for i in range(len(new_string)):
                                self.Scrolledtext1.insert('insert', new_string[i])
                                self.Scrolledtext1.insert('insert','\n')

                            self.Scrolledtext1.configure(state="disabled")
                    else:
                        try:
                            self.cart.remove_item()
                        except IndexError:
                            messagebox.showerror("Oops!", "Cart is empty!!", parent=self.dashboard_window)
                        else:
                            self.Scrolledtext1.delete('1.0', END)
                            new_li = []
                            li = strr.split("\n")
                            for i in range(len(li)):
                                if len(li[i])!=0:
                                    if li[i].find('Total')==-1:
                                        new_li.append(li[i])
                                    else:
                                        break
                            new_li.pop()
                            for j in range(len(new_li)-1):
                                self.Scrolledtext1.insert('insert', new_li[j])
                                self.Scrolledtext1.insert('insert','\n')
                            self.Scrolledtext1.configure(state="disabled")

                else:
                    messagebox.showerror("Oops!", "Please add a product", parent=self.dashboard_window)

    def wel_bill(self):
                self.name_message = Text(self.dashboard_window)
                self.name_message.place(relx=0.820, rely=0.782, width=176, height=30)
                self.name_message.configure(font="-family {Podkova} -size 10")
                self.name_message.configure(borderwidth=0)
                self.name_message.configure(background="#eee")

                self.num_message = Text(self.dashboard_window)
                self.num_message.place(relx=0.820, rely=0.652, width=90, height=30)
                self.num_message.configure(font="-family {Podkova} -size 10")
                self.num_message.configure(borderwidth=0)
                self.num_message.configure(background="#eee")

                self.bill_message = Text(self.dashboard_window)
                self.bill_message.place(relx=0.820, rely=0.392, width=176, height=26)
                self.bill_message.configure(font="-family {Podkova} -size 10")
                self.bill_message.configure(borderwidth=0)
                self.bill_message.configure(background="#eee")

                self.bill_date_message = Text(self.dashboard_window)
                self.bill_date_message.place(relx=0.820, rely=0.520, width=90, height=26)
                self.bill_date_message.configure(font="-family {Podkova} -size 10")
                self.bill_date_message.configure(borderwidth=0)
                self.bill_date_message.configure(background="#eee")

    def total_bill(self):
                
                self.total = 0
                if self.cart.isEmpty():
                    messagebox.showerror("Oops!", "Please Add a product.", parent=self.dashboard_window)
                else:
                    self.Scrolledtext1.configure(state="normal")
                    strr = self.Scrolledtext1.get('1.0', END)
                    if strr.find('Total')==-1:
                        self.Scrolledtext1.configure(state="normal")
                        divider = "\n\n" + "\t" + ("-" * 70) + "\n"
                        self.Scrolledtext1.insert('insert', divider)
                        self.total = "\tTotal\t\t\t$. {}\n".format(self.cart.total())
                        self.Scrolledtext1.insert('insert',  self.total)
                        divider2 = "\t" + ("-" * 70) + "\n\n\tCashier : "+self.cust_name.get()
                        self.Scrolledtext1.insert('insert', divider2)
                        self.Scrolledtext1.configure(state="normal")
                    else:
                        return 
                    
    state = 1

    def gen_bill(self):
         
        if self.state == 1:

            strr = self.Scrolledtext1.get('1.0', END)
            self.wel_bill()

            if(self.cust_name.get()==""):
                messagebox.showerror("Oops!", "Please enter a name.", parent=self.dashboard_window)

            elif(self.cust_num.get()==""):
                messagebox.showerror("Oops!", "Please enter a number.", parent=self.dashboard_window)

            elif self.valid_phone(self.cust_num.get())==False:
                  messagebox.showerror("Oops!", "Please enter a valid number.", parent=self.dashboard_window)

            elif(self.cart.isEmpty()):
                  messagebox.showerror("Oops!", "Cart is empty.", parent=self.dashboard_window)

            else:
                  if strr.find('Total')==-1:
                        self.total_bill()
                        self.gen_bill()
                  else:
                        self.name_message.insert(END, self.cust_name.get())
                        self.name_message.configure(state="disabled")
                        self.num_message.insert(END, self.cust_num.get())
                        self.num_message.configure(state="disabled")
                        self.cust_new_bill.set(self.random_bill_number(8))
                        self.bill_message.insert(END, self.cust_new_bill.get())
                        self.bill_message.configure(state="disabled")

                        self.bill_date.set(str(date.today()))

                        self.bill_date_message.insert(END, self.bill_date.get())
                        self.bill_date_message.configure(state="disabled")

                        self.Scrolledtext1.insert(END, self.cust_name.get())
                        s1 = "\t     - RECEIPT # : "
                        self.Scrolledtext1.insert('insert', s1)
                        self.Scrolledtext1.insert(END, self.cust_new_bill.get())
                        s2 = "\n\n\tDATE : "
                        self.Scrolledtext1.insert('insert', s2)
                        self.Scrolledtext1.insert(END, self.bill_date.get())
                        s3 = "\n\t" + ("-"*70) + "\n\t     FOR COMPLAINTS CALL : "
                        self.Scrolledtext1.insert('insert', s3)
                        self.Scrolledtext1.insert(END, self.cust_num.get())

                        with sqlite3.connect("./Database/drinkShop.db") as db:
                            cur = db.cursor()
                        insert = (
                                "INSERT INTO stock_list(bill_number, date, cashier_name, bill_details) VALUES(?,?,?,?,?)"
                            )
                        cur.execute(insert, [self.cust_new_bill.get(), self.bill_date.get(), self.cust_name.get(), self.cust_num.get(), self.Scrolledtext1.get('1.0', END)])
                        db.commit()
                        #print(self.cart.items)
                        print(self.cart.allCart())
                        for name, qty in self.cart.dictionary.items():
                                update_qty = "UPDATE drnk_category SET in_stock = in_stock - ? WHERE drink_name = ?"
                                cur.execute(update_qty, [qty, name])
                                db.commit()
                        messagebox.showinfo("Success!!", "Bill Generated Successfully", parent=self.dashboard_window)
                        self.entry1.configure(state="disabled", background="#eee", foreground="#000000")
                        self.entry2.configure(state="disabled", background="#eee", foreground="#000000")
                        self.state = 0
        else:
                return
                
    def clear_bill(self):
                
                self.wel_bill()
                self.entry1.configure(state="normal")
                self.entry2.configure(state="normal")
                self.entry1.delete(0, END)
                self.name_message.configure(state="normal")
                self.num_message.configure(state="normal")
                self.bill_message.configure(state="normal")
                self.bill_date_message.configure(state="normal")
                self.Scrolledtext1.configure(state="normal")
                self.name_message.delete(1.0, END)
                self.num_message.delete(1.0, END)
                self.bill_message.delete(1.0, END)
                self.bill_date_message.delete(1.0, END)
                self.Scrolledtext1.delete(1.0, END)
                self.name_message.configure(state="disabled")
                self.num_message.configure(state="disabled")
                self.bill_message.configure(state="disabled")
                self.bill_date_message.configure(state="disabled")
                self.cart.remove_items()
                self.state = 1
                head = "\n\n\t\t    PULPA    DRINKS    SHOP  \n" \
                    "\t\t          M2 Gueliz Marrakech   \n\n\t\t THANK YOU FOR CHOOSING US\n" \
                    "\t\t         Come back Soon \n\n\n" + "\tDRINK\t  -----  \tQUANTITY\t  -----  \tPRICE ( Dh )\n"
                self.Scrolledtext1.insert('insert', head)

    def clear_selection(self):
                
                self.entry4.delete(0, END)
                self.combo1.configure(state="normal")
                self.combo2.configure(state="normal")
                self.combo3.configure(state="normal")
                self.combo1.delete(0, END)
                self.combo2.delete(0, END)
                self.combo3.delete(0, END)
                self.combo2.configure(state="disabled")
                self.combo3.configure(state="disabled")
                self.entry4.configure(state="disabled")
                try:
                    self.qty_label.configure(foreground="#eee")
                except AttributeError:
                    pass

    def clear_search(self, events):
        self.entry3.delete(0, "end")

    def search_bill(self):
                
                find_bill = "SELECT * FROM stock_list WHERE bill_number = ?"
                self.cur.execute(find_bill, [self.cust_search_bill.get().rstrip()])
                results = self.cur.fetchall()
                if results:

                    self.wel_bill()
                    self.name_message.insert(END, results[0][2])
                    self.name_message.configure(state="disabled")

                    self.num_message.insert(END, results[0][3])
                    self.num_message.configure(state="disabled")

                    self.bill_message.insert(END, results[0][0])
                    self.bill_message.configure(state="disabled")

                    self.Scrolledtext1.delete(1.0, END)
                    self.bill_date_message.insert(END, results[0][1])
                    self.bill_date_message.configure(state="disabled")

                    self.Scrolledtext1.configure(state="normal")
                    self.Scrolledtext1.insert(END, results[0][4])
                    self.Scrolledtext1.configure(state="disabled")

                    self.state = 0

                else:
                    messagebox.showerror("Error!!", "Bill not found.", parent=self.dashboard_window)
                    self.entry3.delete(0, END)

class Cart:
    def __init__(self):
        self.items = []
        self.dictionary = {}

    def add_item(self, item):
        self.items.append(item)
        

    def remove_item(self):
        self.items.pop()

    def remove_items(self):
        self.items.clear()

    def total(self):
        total = 0.0
        print(self.items)
        for i in self.items:
            total+=i["price"]*i["qty"]
            print(total)
        return total

    def isEmpty(self):
        if len(self.items) == 0:
            return True

    def allCart(self):
        for i in self.items:
            if i.product_name in self.dictionary:
                self.dictionary[i.product_name] += i.qty
            else:
                self.dictionary.update({i.product_name: i.qty})


def page():
    window = Tk()
    Manage(window)
    window.mainloop()


if __name__ == '__main__':
    page()