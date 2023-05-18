import sqlite3
from tkinter import *
from tkinter import messagebox
import dashboard

root = Tk()
root.title('Pulpa Shop - Sign in')
root.geometry('925x500+300+200')
root.configure(bg="#ECBCFD")
root.resizable(False, False)

Username = StringVar()
Password = StringVar()

def signin():
            
            conn1 = sqlite3.connect("./Database/drinkShop.db")
            cursor1 = conn1.cursor()
            find_user = 'SELECT * FROM user_account WHERE user_username = ? and user_password = ?'
            cursor1.execute(find_user, [(user.get()), (code.get())])
            result = cursor1.fetchall()

            if result:
                messagebox.showinfo("Success", 'Logged in Successfully,\n\nClick "OK" to continue.')
                root.destroy()
                import dashboard
                
            else : 
                 messagebox.showerror("Failed", "Wrong Login details, please try again.")


def forgot_password():
    win = Toplevel()
    window_width = 350
    window_height = 350
    screen_width = win.winfo_screenwidth()
    screen_height = win.winfo_screenheight()
    position_top = int(screen_height / 4 - window_height / 4)
    position_right = int(screen_width / 2 - window_width / 2)
    win.geometry(f'{window_width}x{window_height}+{position_right}+{position_top}')
    win.title('Forgot Password')
    win.configure(background='#ECBCFD')
    win.resizable(0, 0)

    # ======================================== Email ========================================
    email_entry2 = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), highlightthickness=2)
    email_entry2.place(x=40, y=30, width=256, height=34)
    email_entry2.config(highlightbackground="black", highlightcolor="black")
    email_label2 = Label(win, text='• Email', fg="#89898b", bg='#ECBCFD',
                         font=("yu gothic ui", 11, 'bold'))
    email_label2.place(x=40, y=0)

    # ==================================== New Password ==========================================
    new_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    new_password_entry.place(x=40, y=110, width=256, height=34)
    new_password_entry.config(highlightbackground="black", highlightcolor="black")
    new_password_label = Label(win, text='• New Password', fg="#89898b", bg='#ECBCFD', font=("yu gothic ui", 11, 'bold'))
    new_password_label.place(x=40, y=80)

    # ================================ Confirm Password =============================================
    confirm_password_entry = Entry(win, fg="#a7a7a7", font=("yu gothic ui semibold", 12), show='•', highlightthickness=2)
    confirm_password_entry.place(x=40, y=190, width=256, height=34)
    confirm_password_entry.config(highlightbackground="black", highlightcolor="black")
    confirm_password_label = Label(win, text='• Confirm Password', fg="#89898b", bg='#ECBCFD',
                                   font=("yu gothic ui", 11, 'bold'))
    confirm_password_label.place(x=40, y=160)

    # ======= Update password Button ============
    update_pass = Button(win, fg='#202020', text='Update Password', bg='#ECBCFD', font=("yu gothic ui bold", 14),
                         cursor='hand2', activebackground='#1b87d2')
    update_pass.place(x=40, y=240, width=256, height=50)

design_frame4 = Frame(bg='#ECBCFD', width=100, height=33, highlightthickness=0, borderwidth=0)
design_frame4.place(x=650, y=106)

def hide():
    closeeyeButton.config(file="Images/closeeye.png")
    code.config(show='*')
    eyeButton.config(command=show)

def show():
    closeeyeButton.config(file="Images/openeye.png")
    code.config(show='')
    eyeButton.config(command=hide)

def signup_page():
    root.destroy()
    import signup

"""------------------Image------------------------"""
img = PhotoImage(file="images/pulpalogo.png")
Label(root, image=img, bg='#ECBCFD', border=0).place(x=55, y=49)

frame = Frame(root, width=350, height=350, bg="#ECBCFD")
frame.place(x=430, y=70)

heading = Label(frame, text='Sign In', fg="black", bg="#ECBCFD", font=('Microsoft YaHei UI Light', 30, 'italic'))
heading.place(x=120, y=3)

"""-----------------Username------------------------"""
def on_enter(e):
    user.delete(0, 'end')
def on_leave(e):
    name = user.get()
    if name == '':
        user.insert(0, 'Username')

user = Entry(frame, width=25, fg="black", border=0, bg="#ECBCFD", font=("Microsoft YaHei UI Light", 11))
user.place(x=50, y=80)
user.insert(0, 'Username')
user.bind('<FocusIn>', on_enter)
user.bind('<FocusOut>', on_leave)
Frame(frame, width=295, height=2, bg="black").place(x=45, y=107)

"""-----------------password-----------------------"""
def on_enter(e):
    code.delete(0, 'end')
def on_leave(e):
    name = code.get()
    if name == '':
        user.insert(0, 'Password')
code = Entry(frame, width=25, fg="black", border=0, bg="#ECBCFD", font=("Microsoft YaHei UI Light", 11))
code.place(x=50, y=150)
code.insert(0, 'Password')
code.bind('<FocusIn>', on_enter)
code.bind('<FocusOut>', on_leave)

Frame(frame, width=295, height=2, bg="black",).place(x=45, y=177)
closeeyeButton= PhotoImage(file="Images/closeeye.png")
eyeButton = Button(root, image=closeeyeButton, bd=0, bg='#ECBCFD', activebackground='white', cursor='hand2', command=hide)
eyeButton.place(x=740, y=220)

"""--------------------Forgot Button------------------------"""
forgetButton = Checkbutton(text='Forgot Password ?', bd=0, bg='#ECBCFD', activebackground='white',
                           cursor='hand2', fg="#202020", font=("Microsoft YaHei UI Light", 9),
                           command=forgot_password)
forgetButton.place(x=690, y=255)

forgotPassword = Button(design_frame4, text='Forgot password', font=("yu gothic ui", 8, "bold underline"), bg='#f8f8f8',
                        borderwidth=0, activebackground='#f8f8f8', cursor="hand2")
forgotPassword.place(x=290, y=290)

""""--------------------Buttons-----------------------------"""
Login = Button(frame, width=15, pady=7, text='Sign in', bg='#9D4EDD', fg='black', border=0, font=("Microsoft YaHei UI Light", 11), command=signin).place(x=125, y=230)
label = Label(frame, text="Don't have an account ?", fg="black", bg="#ECBCFD", font=("Microsoft YaHei UI Light", 9))
label.place(x=95, y=290)

sign_up = Button(frame, width=6, text="Sign up", border=0, bg="#ECBCFD", cursor="hand2", fg="#9D4EDD", font=("Microsoft YaHei UI Light", 11, 'bold', 'italic'), command=signup_page)
sign_up.place(x=240, y=285)



root.mainloop()
