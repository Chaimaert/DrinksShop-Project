from tkinter import *
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import os


class FirstPage:
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
        homepage = Frame(dashboard_window)
        dashboard_page = Frame(dashboard_window)

        for frame in (homepage, dashboard_page):
            frame.grid(row=0, column=0, sticky='nsew')


        def show_frame(frame):
            frame.tkraise()


        show_frame(homepage)

        # ************************************* HOME PAGE *************************************
        homepage.config(background='white')

        # ************************************* BAR MENU *************************************

        menuBar_line = Canvas(homepage, width=2600, height=1.5, bg='#f20089', highlightthickness=0)
        menuBar_line.place(x=0, y=90)

        home_bgImg = Image.open('images/biglogo.png')
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='white')
        home_bg.image = photo
        home_bg.place(x=700, y=92)

        home_bgImg = Image.open('images/pulpaa.png')
        photo = ImageTk.PhotoImage(home_bgImg)
        home_bg = Label(homepage, image=photo, bg='white')
        home_bg.image = photo
        home_bg.place(x=0, y=0)


        heading = Label(homepage, text='© Pulpa Drinks shop', bg='white', fg='black', font=("yu gothic ui", 15, "italic"))
        heading.place(x=1150, y=650)

        heading2 = Label(homepage, text='Trending', bg='white', fg='black', font=("Microsoft YaHei UI Light", 20, "bold "))
        heading2.place(x=130, y=182)

        #************************************* The trending images *************************************
        drinkImage = Image.open('images/cliparttt.png')
        photo = ImageTk.PhotoImage(drinkImage)
        drinkImg = Label(homepage, image=photo, bg='white')
        drinkImg.image = photo
        drinkImg.place(x=50, y=240)

        drinkImage2 = Image.open('images/mojitoo.png')
        photo = ImageTk.PhotoImage(drinkImage2)
        drinkImg2 = Label(homepage, image=photo, bg='white')
        drinkImg2.image = photo
        drinkImg2.place(x=160, y=240)

        drinkImage3 = Image.open('images/martiniii.png')
        photo = ImageTk.PhotoImage(drinkImage3)
        drinkImg3 = Label(homepage, image=photo, bg='white')
        drinkImg3.image = photo
        drinkImg3.place(x=280, y=240)

        drinkImage4 = Image.open('images/mart.png')
        photo = ImageTk.PhotoImage(drinkImage4)
        drinkImg4 = Label(homepage, image=photo, bg='white')
        drinkImg4.image = photo
        drinkImg4.place(x=42, y=390)

        drinkImage5 = Image.open('images/strawberryy.png')
        photo = ImageTk.PhotoImage(drinkImage5)
        drinkImg5 = Label(homepage, image=photo, bg='white')
        drinkImg5.image = photo
        drinkImg5.place(x=168, y=390)

        drinkImage6 = Image.open('images/orangejuicee.png')
        photo = ImageTk.PhotoImage(drinkImage6)
        drinkImg6 = Label(homepage, image=photo, bg='white')
        drinkImg6.image = photo
        drinkImg6.place(x=280, y=390)

        heading3 = Label(homepage, text='Daiquiri Delight', bg='white', fg='black', font=("Microsoft YaHei UI Light", 9, "bold"))
        heading3.place(x=25, y=340)

        heading4 = Label(homepage, text='Mojito Night', bg='white', fg='black', font=("Microsoft YaHei UI Light", 9, "bold"))
        heading4.place(x=150, y=340)

        heading5 = Label(homepage, text='Flirtini Martini', bg='white', fg='black', font=("Microsoft YaHei UI Light", 9, "bold"))
        heading5.place(x=260, y=340)

        heading6 = Label(homepage, text="Sea Breeze", bg='white', fg='black', font=("Microsoft YaHei UI Light", 9, "bold"))
        heading6.place(x=30, y=490)

        heading7 = Label(homepage, text='Drunk In Love', bg='white', fg='black', font=("Microsoft YaHei UI Light", 9, "bold"))
        heading7.place(x=140, y=490)

        heading8 = Label(homepage, text='Cocktail Souls', bg='white', fg='black', font=("Microsoft YaHei UI Light", 9, "bold"))
        heading8.place(x=260, y=490)

         # ************************************* HOME BUTTON **************************************************
        home_button = Button(homepage, text='Home', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), bd=0, fg='#f20089',
                             cursor='hand2', activebackground='white', activeforeground='#f20089')
        home_button.place(x=110, y=31)

        """def manage():
            dashboard_window.withdraw()
            os.system("python Employee.py")
            dashboard_window.destroy()"""

        # ************************************* MANAGE BUTTON *************************************
        manage_button = Button(homepage, text='Manage', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), bd=0, fg='#000',
                               cursor='hand2', activebackground='white', activeforeground='#f20089')
        manage_button.place(x=200, y=31)

        # ************************************* PURCHASE BUTTON *************************************
        manage_button = Button(dashboard_window, text='Purchase', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), bd=0, fg='#000',
                               cursor='hand2', activebackground='white', activeforeground='#f20089')
        manage_button.place(x=300, y=31)

        #************************************* The logout button *************************************

        def logout():
            dashboard_window.destroy()
            import login

        logout_button = Button(dashboard_window, text='Logout', bg='white', font=("Microsoft YaHei UI Light", 13, "bold"), bd=0, fg='#000',
                               cursor='hand2', activebackground='#eee', activeforeground='#f20089', command=logout)
        logout_button.place(x=420, y=31)

        def exit2():
            sure = messagebox.askyesno("Exit", "Are you sure you want to exit?", parent=dashboard_window)
            if sure == True:
                 dashboard_window.destroy()
                #Manage_window.destroy()

        self.button6 = Button(dashboard_window)
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




def page():
    window = Tk()
    FirstPage(window)
    window.mainloop()


if __name__ == '__main__':
    page()       