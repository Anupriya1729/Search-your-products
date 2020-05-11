from tkinter import *
import sqlite3 as sql
import re
from tkinter import messagebox
import bs4
import requests as r
from selenium import webdriver

class Gui:
    def __init__(s):
        s.client=sql.connect('user.db')
        s.cu=s.client.cursor()
        try:
            s.cu.execute("create table user(id int auto_increment,name varchar(50),password varchar(20),email varchar(100))")
        except:
            pass
        s.loginpage()
        
    def register(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('1200x600+0+0')#'widthxheight+x+y
        s.scr.configure(background='white')
        l=Label(s.scr,bg='SeaGreen2',font=('Chasing Hearts',30,'bold'),text='Shop')
        l.pack(side=TOP,fill=X)
        l1=Label(s.scr,bg='SeaGreen3',fg='white',font=('Arial',25,'bold'),text='Username')
        l1.place(x=300,y=100)
        l2=Label(s.scr,bg='SeaGreen3',fg='white',font=('Arial',25,'bold'),text='Password')
        l2.place(x=300,y=200)
        l3=Label(s.scr,bg='SeaGreen3',fg='white',font=('Arial',25,'bold'),text='Re-enter password')
        l3.place(x=300,y=300)
        l4=Label(s.scr,bg='SeaGreen3',fg='white',font=('Arial',25,'bold'),text='Email')
        l4.place(x=300,y=400)
        user=Entry(s.scr,bg='SeaGreen3',fg='white',font=('Arial',25,'bold'))
        user.place(x=600,y=100)
        ps=Entry(s.scr,show='*',bg='SeaGreen3',fg='white',font=('Arial',25,'bold'))
        ps.place(x=600,y=200)
        ps1=Entry(s.scr,show='*',bg='SeaGreen3',fg='white',font=('Arial',25,'bold'))
        ps1.place(x=600,y=300)
        email=Entry(s.scr,bg='SeaGreen3',fg='white',font=('times',25,'bold'))
        email.place(x=600,y=400)
        b=Button(s.scr,relief=RAISED,command=lambda :s.regi(user.get(),ps.get(),ps1.get(),email.get()),text='Register',bg='gray37',fg='white',font=('Open Sans',20,'bold'))
        b.place(x=600,y=500)
        b1=Button(s.scr,relief=RAISED,command=s.loginpage,text='Back',bg='gray37',fg='white',font=('Open Sans',20,'bold'))
        b1.place(x=300,y=500)
        s.scr.mainloop()
        
    def regi(s,u,p,p1,e):
        if not(re.search(r'^\S+$',u)):
               messagebox.showerror('register','user name must not contain spaces')
        elif not(re.search(r'^\S+$',p)) or not(re.search(r'^\S+$',p1)):
            messagebox.showerror('register','password must not contain spaces')
        elif not(re.search(r'^\S+@\w+[.][a-z]{2,3}$',e)):
            messagebox.showerror('register','invalid email')
        else:
            if p!=p1:
                messagebox.showerror('register','both passwords did not match')
            else:
                s.cu.execute('insert into user (name,password,email) values (%r,%r,%r)'%(u,p,e))
                s.client.commit()
                s.loginpage()

    
    def login(s,u,p):
        if not(re.search(r'^\S+$',u)):
               messagebox.showerror('login','user name must not contain spaces')
        elif not(re.search(r'^\S+$',p)):
            messagebox.showerror('login','password must not contain spaces')
        else:
            s.cu.execute('select count(*) from user where name=%r and password=%r'%(u,p))
            if s.cu.fetchone()[0]!=0:
                s.productpage()
            else:
                messagebox.showerror('login','invalid credentials')
            
    def loginpage(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('1200x600+0+0')#'widthxheight+x+y
        s.scr.config(bg='white')
        l=Label(s.scr,bg='SeaGreen2',font=('Chasing Hearts',30,'bold'),text='Shop')
        l.pack(side=TOP,fill=X)
        l1=Label(s.scr,bg='SeaGreen3',fg='white',font=('times',30,'bold'),text='Username')
        l1.place(x=300,y=200)
        l2=Label(s.scr,bg='SeaGreen3',fg='white',font=('times',30,'bold'),text='Password')
        l2.place(x=300,y=300)
        user=Entry(s.scr,bg='SeaGreen3',fg='white',font=('times',30,'bold'))
        user.place(x=600,y=200)
        ps=Entry(s.scr,show='*',bg='SeaGreen3',fg='white',font=('times',30,'bold'))
        ps.place(x=600,y=300)
        b=Button(s.scr,relief=RAISED,command=lambda :s.login(user.get(),ps.get()),text='Login',bg='gray37',fg='white',font=('Open Sans',20,'bold'))
        b.place(x=300,y=400)
        b1=Button(s.scr,relief=RAISED,command=s.register,text='New user',bg='gray37',fg='white',font=('Open Sans',20,'bold'))
        b1.place(x=600,y=400)
        s.scr.mainloop()

    def productpage(s):
        try:
            s.scr.destroy()
        except:
            pass
        s.scr=Tk()
        s.scr.geometry('1200x600+0+0')#'widthxheight+x+y
        s.scr.config(bg='white')
        l=Label(s.scr,bg='SeaGreen2',font=('Chasing Hearts',30,'bold'),text='Search any item on your favourite shopping site')
        l.pack(side=TOP,fill=X)
        l3=Label(s.scr,bg='SeaGreen2',font=('Chasing Hearts',25,'bold'),text='Shein, Myntra, Amazon, Flipkart, Clubfactory')
        l3.pack(side=TOP,fill=X)
        l1=Label(s.scr,bg='SeaGreen3',fg='black',font=('Arial Rounded MT Bold',30),text='Product Name')
        l1.place(x=300,y=200)
        l2=Label(s.scr,bg='SeaGreen3',fg='black',font=('Arial Rounded MT Bold',30),text='Website Name')
        l2.place(x=300,y=300)
        pn=Entry(s.scr,bg='SeaGreen3',fg='black',font=('Arial',30))
        pn.place(x=600,y=200)
        pw=Entry(s.scr,bg='SeaGreen3',fg='black',font=('Arial',30))
        pw.place(x=600,y=300)
        b=Button(s.scr,text='Go',relief=RAISED,command=lambda :s.productsearch(pn.get(),pw.get()),bg='gray37',fg='white',font=('Arial Rounded MT Bold',25,'bold'))
        b.place(relx=0.5,rely=0.6)
        s.scr.mainloop()

    def productsearch(s,pn,pw):
        #data=r.request('get',"https://www.1mg.com/search/all?name={}".format(ps))
        #s=bs4.BeautifulSoup(data.text,'html.parser') for i in
        #s.findAll('div',{"class": "style__product-box___3oEU6"}):
        #x=i.find('a')
        
            
            if(pw=='Shein' or pw=='shein'):
                ch=webdriver.Chrome(r'C:\chromedrivers\chromedriver')
                ch.get("https://www.shein.in/pdsearch/{}".format(pn))
                
            elif(pw=='Myntra' or pw=='myntra'):
                ch=webdriver.Chrome(r'C:\chromedrivers\chromedriver')
                ch.get("https://www.myntra.com/{}".format(pn))



            elif(pw=='Flipkart' or pw=='flipkart'):
                ch=webdriver.Chrome(r'C:\chromedrivers\chromedriver')
                ch.get("https://www.flipkart.com/search?q={}".format(pn))



            elif(pw=='Amazon' or pw=='amazon'):
                ch=webdriver.Chrome(r'C:\chromedrivers\chromedriver')
                ch.get("https://www.amazon.com/s?k={}".format(pn))


            elif(pw=='clubfactory' or pw=='Clubfactory' or pw=='Club factory' or pw=='club factory'):
                ch=webdriver.Chrome(r'C:\chromedrivers\chromedriver')
                ch.get("https://www.clubfactory.com/search?q={}".format(pn))

            
            else:
                messagebox.showerror('Invalid website','Products can be searched from- shein, flipkart, amazon, clubfactory, myntra')
                
            
        
            
           
Gui()
