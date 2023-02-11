import sqlite3
import tkinter
try:
    cnt=sqlite3.connect('shop.db')
    print("opened database successfully!")
except:
    print("Error!")
#-----create users table------------------------
##query='''CREATE TABLE users
##    (ID INTEGER PRIMARY KEY,
##    user CHAR(25) NOT NULL,
##    password CHAR(25) NOT NULL,
##    addr CHAR(50) NOT NULL
##    )'''
##cnt.execute(query)
##cnt.close()
#--------insert date to users table----------------------
#query='''INSERT INTO users (user,password,addr)
#    VALUES ("admin","12345678a9","rasht")'''
#cnt.execute(query)
#cnt.commit()
#cnt.close()
#------------functions----------------------------
def login():
    user=txt_user.get()
    pas=txt_pass.get()
    query='''SELECT id FROM  users WHERE user=? AND password=? '''
    result=cnt.execute(query,(user,pas))
    rows=result.fetchall()
    if(len(rows)==0):
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return
    btn_login.configure(state="disabled")
    lbl_msg.configure(text="welcome to your account!",fg="green")  
def submit():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2    
    win2=tkinter.Toplevel(win)
    win2.geometry("300x300")
#------------add widget2---------------------------------    
    lbl_user2=tkinter.Label(win2,text="username: ")
    lbl_user2.pack()

    txt_user2=tkinter.Entry(win2,width=15)
    txt_user2.pack()
    

    lbl_pass2=tkinter.Label(win2,text="password: ")
    lbl_pass2.pack()

    txt_pass2=tkinter.Entry(win2,width=15)
    txt_pass2.pack()


    lbl_addr=tkinter.Label(win2,text="address: ")
    lbl_addr.pack()

    txt_addr=tkinter.Entry(win2,width=15)
    txt_addr.pack()
    

    lbl_msg2=tkinter.Label(win2,text="")
    lbl_msg2.pack()

    btn_submit2=tkinter.Button(win2,text="Submit",command=submit2)
    btn_submit2.pack(pady=10)
    
    
    win2.mainloop()

def submit2():
    global txt_user2
    global txt_pass2
    global txt_addr
    global lbl_msg2
    
    user2=txt_user2.get()
    pas2=txt_pass2.get()
    addr=txt_addr.get()
    
    query='''SELECT id FROM users WHERE user=?'''
    result=cnt.execute(query,(user2,pas2))
    rows=result.fetchall()

    if(len(rows)!=0):
        lbl_msg2.configure(text="you have already have an account with this username!",fg="red")
        return
    if(len(user2)<4):
        lbl_msg2.configure(text="username lenght should be at least 4 characters!",fg="red")
        return
    if(len(pas2)<8):
        lbl_msg2.configure(text="password lenght should be at least 8 characters!",fg="red")
        return
    if(len(addr)==0):
        lbl_msg2.configure(text="yuor address field is blank!",fg="red")
        return
    query2='''INSERT INTO users(user,password,addr)
    VALUES(?,?,?)'''
    cnt.execute(query2,(user2,pas2,addr))
    cnt.commit()
    lbl_msg2.configure(text="submit done!!!",fg="green")

def delete():

    win3=tkinter.Toplevel(win)
    win3.geometry("300x300")
#------------add widget3--------------------------------- 
    lbl_msg3=tkinter.Label(win3,text="are you sure?")
    lbl_msg3.pack()
    
    btn_yes3=tkinter.Button(win3,text="yes")
    btn_yes3.pack(pady=10)
    
    btn_no3=tkinter.Button(win3,text="no")
    btn_no3.pack(pady=10)

    win3.mainloop()    
 
     
  
   


def yes():
    global lbl_msg3
    global user
    global pas
    global islogin
    if(islogin==True):
        query='''Delete FROM users WHERE user=? AND password=?'''
        cnt.execute(query,(user,pas))
        cnt.commit()
        
        btn_login.configure(state="normal")
        btn_delete.configure(state="disable")
        btn_logout.configure(state="disable")
        
        lbl_msg3.configure(text="your account has been deleted successfully!!!",fg="green")
        
def no():
    global lbl_msg3
    lbl_msg3.configure(text="activity canceled",fg="red")
    return

  
    
def logout():
    user3=txt_user.get()
    pas3=txt_pass.get()
    
    query='''SELECT id FROM  users WHERE user=? AND password=?'''
    result=cnt.execute(query,(user3,pas3))
    rows=result.fetchall()
    
    if(len(rows)==0):
        lbl_msg.configure(text="wrong username or password!",fg="red")
        return
    else:   
        btn_login.configure(state="normal")
        btn_logout.configure(state="disable")
        btn_delete.configure(state="disable")
        lbl_msg.configure(text="your logout done successfully!!! ",fg="green")
      
#------------Main window---------------------------------
win=tkinter.Tk()
win.geometry("400x300")
#------------add widget---------------------------------
lbl_user=tkinter.Label(text="username: ")
lbl_user.pack()

txt_user=tkinter.Entry(width=25)
txt_user.pack()


lbl_pass=tkinter.Label(text="password: ")
lbl_pass.pack()

txt_pass=tkinter.Entry(width=25)
txt_pass.pack()


lbl_msg=tkinter.Label(text="")
lbl_msg.pack()

btn_login=tkinter.Button(text="Login",command=login)
btn_login.pack(pady=10)


btn_submit=tkinter.Button(text="Submit",command=submit)
btn_submit.pack(pady=10)

btn_delete=tkinter.Button(text="Delete",command=delete)
btn_delete.pack(pady=10)
btn_delete.configure(state="disabled")

btn_logout=tkinter.Button(text="logout",command=logout)
btn_logout.pack(pady=10)
btn_logout.configure(state="disabled")

win.mainloop()

























