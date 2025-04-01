import mysql.connector
import random
import bcrypt
import re
from tkinter import ttk
conn = mysql.connector.connect(
    host = "localhost",
    user= "root",
    password = "Mysql0109@",
    database = "Library"
)

class Library:
    books = []
    my_book = {}
    def getAllBooks(self):
        crsr = conn.cursor()
        sql = f"SELECT title FROM books"
        crsr.execute(sql)
        self.books = crsr.fetchall()
        print("\tAll books in Library\n\t-----------------\n")
        for book in self.books:
            print("\t",*book)
        crsr.close()
        return self.books
        print()
    
    def addBook(self,book,author):
        crsr = conn.cursor()
        sql = f"INSERT INTO books(book_id , title , author_name , isbn , publication , availability , price ) VALUES(?,?,?,?,?,?,?)"
        values = (book,title,author, isbn, publication, availability, price)
        crsr.execute(sql,values)
        conn.commit()
        crsr.close()
        print()
    
    def getBookByAuthourName(self,author):
        crsr = conn.cursor()
        sql = f"SELECT title FROM books WHERE author_name = '{author}'"
        crsr.execute(sql)
        books = crsr.fetchall()
        print(f"\tThe available books of {author}\n\t-----------------------\n")
        for book in books:
            print("\t",book[0])
        conn.commit()
        crsr.close()
        print()
    def getBookByName(self,title):
        crsr = conn.cursor()
        sql = f"SELECT distinct(title) FROM books WHERE title = '{title}'"
        crsr.execute(sql)
        books = crsr.fetchall()
        print(f"\tThe available books\n\t-----------------------\n")
        for book in books:
            print("\t",book[0])
        conn.commit()
        crsr.close()
        print()
    def sortBooksByTopologicalOrder():

        pass
    
    def getAllSubscribers(self):
        crsr = conn.cursor()
        sql = "select m.user_name , b.title from books b , members m , borrowings br where br.book_id=b.book_id and m.member_id=br.user_id;"
        crsr.execute(sql)
        subscribers = crsr.fetchall()
        print("\tAll Subscribers\n\t----------------------")
        print("\t Subscriber Name \t \t\t\tBook\n\t-------------\t\t------------------\n")
        for subs in subscribers:
            print("\t",subs[0],"\t\t" ,subs[1])
        print()
        pass
    
    def getAllEarnigns(self):
        crsr = conn.cursor()
        sql = f"select round(sum(b.price),2) as Sum from books b , borrowings br where b.book_id in (select br.book_id)"
        crsr.execute(sql)
        sum = crsr.fetchall()
        for i in sum:
            print(*i)
        pass
    
    def getUnAvailabelBooks(self):
        crsr = conn.cursor()
        sql = """select b.title as Title from books b 
        left join borrowings br on b.book_id = br.book_id where br.book_id is not null or b.availability=0"""
        crsr.execute(sql)
        books = crsr.fetchall()
        conn.commit()
        crsr.close()
        print("\tThe unavailable books\n\t------------------------\n")
        for book in books:
            print("\t",*book)
        print()
    
    def mapAuthorWithBook(self,book,author):
        author_book_map = {}
        if author in author_book_map:
            author_book_map[author].append(book)
        else :
            author_book_map[author] = book
        pass

    def getAvailableBooks(self):
        crsr = conn.cursor()
        sql = """select b.title as Title , b.author_name as Author from books b 
                left join borrowings br on b.book_id = br.book_id where  -- to get all unavailable books.
                br.book_id is null and availability=1;"""
        crsr.execute(sql)
        print("\tAvailable books\n\t---------------\n")
        availables = crsr.fetchall()
        for book in availables:
            print("\t",book[0])
        return availables
        crsr.close
        print()
l = Library()
#l.getAllBooks()
# l.getBookByAuthourName(input("Enter author name : "))
# l.getUnAvailabelBooks()
# l.getAllSubscribers()
# l.addBook(list(map(input())))
# l.getAvailableBooks()
# l.getAllEarnigns()
class MyLibrary(Library):
    def getFavouriteBook():
        pass
    
    def getFavoriteCustomer():
        pass
    
    def borrowBook(self,book_name,isbn='',author_name='Little',user_name='John Doe'):
        crsr = conn.cursor()
        sql = f"select b.title from books b where (b.title='{book_name}' or b.isbn = '{isbn}' or b.author_name='{author_name}') and b.availability=1;"
        crsr.execute(sql)
        books = crsr.fetchall()
        ch = 'no'
        if(books):
            print("The book your searching is available")
            ch = input("If you wish to continue Enter Yes otherwise NO : ")
        else :
            print("Sorry the book is currently unavailable..")
        
        if ch=="yes":
            addBookInBorrow = f"""insert into borrowings(borrowing_id , user_id , book_id , borrowing_date , due_date,return_date,status)
                            select 7,m.member_id ,b.book_id , curdate(), date_add(curdate(), interval 14 day) ,
                            date_add(curdate(), interval 30 day), 1 from books b , members m where b.title='{book_name}' and 
                             m.user_name='{user_name}';"""
            crsr.execute(addBookInBorrow)
            conn.commit()
            updateBooks = f"update books b set b.availability=0 where b.title='{book_name}'"
            crsr.execute(updateBooks)
            books = crsr.fetchall()
            print(*[book for book in books])
            crsr.close()
            conn.commit()
        
        else:
            print("The transaction has been cancelled ")



# m.getUnAvailabelBooks()
# m.getAvailableBooks()
# m.borrowBook(input("Enter book name : "))

import tkinter as tk
root = tk.Tk()
root.geometry("1440x1440+0+0")


class Implementation(Library):
    
    def showAvailableBooks():
        l = Library()
        new_window = tk.Toplevel()
        new_window.title("All Books of Library")
        new_window.geometry("420x420+100+100")
        books = l.getAllBooks()
        txt=""
        for book in books:
            txt = txt+"\n"+ book[0]
        label = tk.Label(new_window , text=txt)
        label.grid_configure()
    
    def register():
        signup_window = tk.Toplevel()
        signup_window.title("Register Screen")
        signup_window.geometry("420x420+100+100")
        signup_window.configure(bg="#00FF00",borderwidth=1,border=1)
        
        user_name = tk.Label(signup_window,text="Enter Username : ",font=("sans-serif",10))
        user_name.grid_configure(row=0,column=0,padx=10,pady=10,ipadx=2,ipady=2)
        entry_username = tk.Entry(signup_window,bg="#ccc",font=("sans-serif",10))
        entry_username.grid_configure(row=0,column=1,padx=10,pady=10,ipadx=2,ipady=2)
        
        user_email = tk.Label(signup_window,text="Enter Email Address : ",font=("sans-serif",10))
        user_email.grid_configure(row=1,column=0,padx=10,pady=10,ipadx=2,ipady=2)
        entry_email = tk.Entry(signup_window,bg="#ccc",font=("sans-serif",10))
        entry_email.grid_configure(row=1,column=1,padx=10,pady=10,ipadx=2,ipady=2)

        password = tk.Label(signup_window,text="Enter Password : ")
        password.grid_configure(row=2,column=0,padx=10,pady=10,ipadx=2,ipady=2)
        entry_password = tk.Entry(signup_window,show="*",bg="#ccc",font=("sans-serif",10))
        entry_password.grid_configure(row=2,column=1,padx=10,pady=10,ipadx=2,ipady=2)
        
        submit_btn = tk.Button(signup_window, text="Sign Up",font=("sans-serif",10),command=lambda : Implementation.validateRegister(entry_username.get(),entry_email.get(),entry_password.get(),signup_window))
        submit_btn.grid_configure(row=3,column=0,padx=5,pady=5,ipadx=2,ipady=2)
        
    def validateRegister(username,email,password,signup_window):
        error_label = tk.Label(signup_window,text="")
        
        if len(username.strip())>8 :
            pat = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
            
            if  re.fullmatch(pat , email.strip()):
                print("Valid Email")
                pat = r'[A-Za-z0-9@#$%^&+=]{8,}'
                
                if re.search(pat,password):
                    print("Valid Password")
                    crsr = conn.cursor()
                    sql = f"select user_name from members where user_name='{username}'"
                    crsr.execute(sql)
                    unique_usernames = crsr.fetchall()
                    
                    if unique_usernames:
                        error_msg = "Username already exists! Please enter a different Username."
                    else:
                        error_msg=""
                        i.store_details(username,email,password)
                else:
                    error_msg = "Invalid Password!"
            else:
                error_msg = "Invalid Email!"
        else:
            error_label.config(text="")
            error_msg = "Invalid UserName!"
        
        error_label.config(text=error_msg,fg="red")
        error_label.grid(row=4,column=0,padx=5)
    def hashPassword(password):

        # Generate a salt
        salt = bcrypt.gensalt()

        # Hash the password using the salt
        hashed_password = bcrypt.hashpw(password.encode(), salt)
        return hashed_password


    def store_details(user_name, email, password):
        crsr = conn.cursor()
        member_ids = f"select member_id from members"
        crsr.execute(member_ids)
        ids = []
        for id in crsr.fetchall():
            ids.append(*id)
        mid = random.randint(1,10000)
        while mid in ids:
            mid = random.randint(1,10000)
        password = Implementation.hashPassword(password)
        sql = f"Insert into members (member_id ,user_name,email,password,phone) values(%s , %s , %s, %s, %s)"
        crsr.execute(sql , (mid , user_name, email , password,''))
        conn.commit()
        crsr.close()
        print("Data Inserted Successfully!")
    
    def login():
        login_window = tk.Toplevel()
        login_window.title("Loing Screen")
        login_window.geometry("420x420+100+100")
        user_email = tk.Label(login_window,text="Enter Email Address : ",background="#ccc")
        user_email.grid_configure(row="0",column=0,pady=10,padx=10)
        
        entry_email = tk.Entry(login_window,background="#fff",border=2,width=25)
        entry_email.grid_configure(row="0",column=1,pady=10,padx=10)

        password = tk.Label(login_window,text="Enter Password : ",background="#ccc")
        password.grid_configure(row=1,column=0,padx=10)
        entry_password = tk.Entry(login_window,show="*",background="#fff",border=2,width=25)
        entry_password.grid_configure(row=1,column=1,padx=10)

        submit_btn = tk.Button(login_window,background="#4169E1",width=15, text="Login",command=lambda : Implementation.validateLogin(entry_email.get(),entry_password.get(),login_window))
        submit_btn.grid_configure(row=2,column=0,padx=10,pady=10,ipadx=2,ipady=2)
        
    def validateLogin(user_name , password,login_window):
        crsr = conn.cursor()
        sql = f"select user_name, password from members where email='{user_name}'"
        crsr.execute(sql)
        data = crsr.fetchall()
        if data:
            hashedPassword = data[0][1]
            if bcrypt.checkpw(password.encode(),hashedPassword.encode()):
                print("You are Loggied In!")
                pass
            else:
                # print("Incorrect email and password")
                incorrect_Label = tk.Label(login_window,text="Incorrect Email or Password!",fg="#FF4500")
                incorrect_Label.grid(row=3,column=0,padx=5,pady=5)
        else :
            no_account = tk.Label(login_window,text="You don't have any account!",fg="#FF4500")
            no_account.grid(row=3,column=0,padx=5,pady=5)
            # print("You don't have account yet!")
    
        
        
class InterFace(Library):
    def __init__(self):
        top_frame = tk.Frame(root,width=400,height=20,highlightbackground="blue",bg="#fff")
        top_frame.grid_configure(row=1,column=0, padx=10,pady=10)
        
        self.options = ["All","Author","Title","Text","ISBN","Subject"]
        self.selected_option = tk.StringVar(top_frame)
        self.selected_option.set(self.options[0])
        
        style = ttk.Style()
        style.configure("Custom.TCombobox", padding=6, foreground="#33333", font=("Arial", 12))
        self.drop_down_menu = ttk.Combobox(top_frame, textvariable=self.selected_option, values=self.options, style="Custom.TCombobox", state="readonly" ,width=5)
        self.drop_down_menu.bind("<<ComboboxSelected>>", self.update_width)
        self.drop_down_menu.grid(row=1, column=1, padx=2, pady=2)
        
        self.search_bar = tk.Entry(top_frame,width=20,font="arial")
        self.search_bar.grid(row=1, column=2,ipadx=5,ipady=5,padx=5,pady=5)
        
        
        self.search_button = tk.Button(top_frame ,text="search",command=lambda:self.searchBook(self.search_bar.get()))
        self.search_button.grid(row=1,column=4,padx=10,pady=10,ipadx=5,ipady=5)
        
        self.home_button = tk.Button(top_frame,text="Home",height=int(0.2))
        self.home_button.grid_configure(row=1,column=5,padx=10,pady=10,ipadx=5,ipady=5)
        
        self.explore_button = tk.Button(top_frame,text="Explore")
        self.explore_button.grid_configure(row=1,column=6,padx=10,pady=10,ipadx=5,ipady=5)
        
        self.login_button = tk.Button(top_frame,text="Login",command=lambda:Implementation.login())
        self.login_button.grid_configure(row =1,column=7,padx=10,pady=10,ipadx=5,ipady=5)
        
        self.signup_button = tk.Button(top_frame,text="SignUp",command=lambda:Implementation.register())
        self.signup_button.grid(row=1,column=8,padx=10,pady=10,ipadx=5,ipady=5)
    
    def update_width(self,event):
        option = self.drop_down_menu.get()
        self.drop_down_menu.config(width=len(option))
        
        
    def searchBook(self,text):
        
        pass
    
if __name__ == '__main__':
    i = Implementation
    i2 = InterFace()
    ch = 10
    while ch:
        ch = int(input("Enter your choice : "))
        if ch==1:
            i.register()
        elif ch==2:
            i.login()
        elif ch==3:
            i.showAvailableBooks()
        elif ch==0:
            root.destroy()
    root.mainloop()
