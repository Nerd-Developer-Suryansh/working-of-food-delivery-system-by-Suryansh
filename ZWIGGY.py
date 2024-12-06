import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings('ignore')
import pandas as pd
import mysql.connector as mc

import numpy as np
from datetime import datetime
from datetime import date
import pyttsx3 
import random
import speech_recognition as sr 
import pyaudio

otp=b=v=n=cgst=sgst=y=org=i1=p1=discount=total=i2=0

#IMPORTING CURRENT DATE AND TIME ENDS
dt = date.today()
now = datetime.now()
tt= now.strftime("%H:%M:%S")
#IMPORTING CURRENT DATE AND TIME CODE ENDS
# MySQL  CONNECTION CODE

x= 10
x=mc.connect(host = 'localhost',user = 'root',password = 'wasd')
u=mc.connect(host = 'localhost',user = 'root',password = 'wasd')
c= x.cursor()

c.execute("create database if not exists zora") # database creation
c.execute("use zora") # using database
# TABLE 1
c.execute("create table  khalo(food_id int,chaap_khazana varchar(99),price1 int,rOlls varchar(99),price3 int);")
c.execute("insert into khalo values(1,'malai chaap',180,'malai chaap roll',200);")
c.execute("insert into khalo values(2,'stuff chaap',180,'stuff roll',200);")
c.execute("insert into khalo values(3,'afghani chaap',180,'afghani chaap roll',200);")
c.execute("insert into khalo values(4,'lemon chaap',180,'paneer tikka roll',200);")
c.execute("insert into khalo values(5,'haryali chaap',180,'garlic chaap roll',200);")
c.execute("insert into khalo values(6,'achari chaap',180,'lemon chaap roll',200);")
c.execute("insert into khalo values(7,'punjabi chaap',180,'hariyali chaap roll',200);")
c.execute("insert into khalo values(8,'crunchy chaap',180,'achari chaap roll',200);")
c.execute("insert into khalo values(9,'crisp chaap',180,'punjabi chaap roll',200);")

#  TABLE 2

c.execute("create table foodingadda(food_id int,burgers varchar(99),price1 int,vada_pav varchar(99),price2 int,wraps varchar(99),price3 int,snacks varchar(99),price4 int);")
c.execute("insert into foodingadda values(1,'aloo tikki burger',49,'classic vada pav',40,'aloo thick wrap',59, 'french fries',70);")
c.execute("insert into foodingadda values(2,'veg tikki burger',59,'chatpata vada pav',50,'veg wrap',69, 'loaded french fries',100);")
c.execute("insert into foodingadda values(3,'veg king(cheese) burger',75,'cheese vada pav',60,'masala wrap',69,'masala french fries',79);")
c.execute("insert into foodingadda values(4,'punjabi (cheese) burger',85,'punjabi vada pav',70,'paneer wrap',79,'cheese triangle(samosa)',65);")
c.execute("insert into foodingadda values(5,'cheese corn burger',95,'maharaja vada pav',80,'cheese wrap',79,'veg nuggets',85);")
# table 3

c.execute("create table eatnrepeat(food_id int,pizzas varchar(99),price4 int,sandwich varchar(99),price5 int,pasta varchar(99),price7 int,garlic_bread varchar(99),price8 int);")
c.execute("insert into eatnrepeat values(1,'margherita pizza',140,'veg cheese sandwich',50,'white sauce pasta',100,'stuffed garlic bread',130);")
c.execute("insert into eatnrepeat values(2,'cheese n corn pizza',130,'mexican cheese sandwich',60, 'red sauce pasta',100,'garlic bread',90);")
c.execute("insert into eatnrepeat values(3 ,'veggie exravagenza pizza',180,'cheese corn sandwich',70, null,null,null,null);")
c.execute("insert into eatnrepeat values(4,'paneer makhni pizza',170,'paneer chilli sandwich',80,null,null,null,null);")

# LOGIN TABLE

c.execute("create table login(id int not null auto_increment,name varchar(99),mobile_no varchar(99),primary key(id),location varchar(200));")

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)
engine.setProperty('rate', 180) 
engine.setProperty('volume', 1)
engine.say("HELLO EVERY ONE INVENTORS  OF THIS CODE IS SURYANSH ")
engine.say("TO START THE CODE PLEASE SAY SOMETHING")
engine.runAndWait()

# SPEECH TO TEXT STARTED
speak=0
speech = sr.Recognizer ()
print ('I AM LISTENING...')
print()
try:
    with sr.Microphone() as source:
        audio = speech. listen (source)
        inp = speech.recognize_google (audio)
        print()
except:
    print()
   
# SPEECH TO TEXT ENDS
print("Hello I am SHY voice assistant")
print()
engine.say(" hello i am shy voice assistant")
engine.runAndWait()

#LOGIN CODE STARTS
print('='*50)
print('-'*15,"WELCOME TO ZWIGGY","-"*16)
print('='*50)
print()
engine.say("welcome  to  zwiggy ") 
engine.runAndWait()
a="please enter your name "
print(a)
engine.say("please enter your name") 
engine.runAndWait() 
name=input("")
aa=1
while(aa!=0):
        b=("please enter your mobile no. ")
        print(b)
        engine.say("please enter your mobile number") 
        engine.runAndWait()
        mobile=input("")
        m=len(str(mobile))
        if(m==10):
                a=1
                engine.say("ok") 
                engine.runAndWait() 
                break
        else:
                print()
                print('Invalid mobile no.\n')
                engine.say("invalid mobile number .  ") 
                engine.runAndWait() 
                continue
while(a==1):
        otp=random.randint(1000,9999)
        print('OTP:',otp)
        engine = pyttsx3.init()
        engine.say("your o t p number is ")
        engine.say(otp)        
        engine.runAndWait()
        aa=('please enter your otp no. :')
        print(aa)
        engine.say("please enter your o t p number sent on your mobile number")      
        engine.runAndWait()
        v=int(input(''))
        if(otp==v):
                print()
                engine.say("your mobile number has been verified")
                engine.runAndWait() 
                print("you have login successfully")
                engine.say("you have login successfully .")
                engine.runAndWait()
                print()
                loc="please enter your location"
                print(loc)
                engine.say("please enter your location")
                engine.runAndWait()
                loci=str(input(""))
                break
        else:
                print("invalid otp no.")
                engine.say("you have enter invalid o t p number") 
                engine.runAndWait()
                print()
                continue
if(otp==v or v==otp):
        cc="insert into login(name,mobile_no,location) values(%s,%s,%s)"
        dd=(name,mobile,loci)
        c.execute(cc,dd)
        x.commit()
        
# LOGIN CODE ENDS

# MENU CODE STARTS
print()
jojo=0
while(jojo!=1):
    if(otp==v and m==10):
        fat="press 1 to choose fastfood and starters "
        print(fat)
        engine.say("press 1 to choose fastfood and starters")
        engine.runAndWait()
        das=int(input(''))   
        if(das==1):
            engine.say("ok")
            engine.runAndWait()
            vs=das
            break
        elif(das!=1):
            engine.say("you have enter wrong option")
            engine.runAndWait()
            print("you have enter wrong option \n")
            continue
ojoj=0
while(ojoj!=1):
    if(vs==1):
        print()
        food="press 1 for burger \npress 2 for vadapav \npress 3 for wraps \npress 4 for pizzas \npress 5 for sandwich \npress 6 for snacks \npress 7 for pasta \npress 8 for garlic_bread  \npress 9 for chaap \npress 10 for rolls \n \nplease enter your choice : "
        print(food)
        engine.say("please select any option which you like from these options")
        engine.runAndWait()
        b=int(input(""))
        print()
        break
    elif(vs!=1):
        engine.say("you have enter wrong option") 
        engine.runAndWait()
        print("you have enter wrong option ")
        print()
        continue
jooo=0
while(jooo!=0):
    if(b==1):
        engine.say("you have choose option 1 which is burger.") 
        engine.runAndWait()
        i1=pd.read_sql("select burgers,price1 as prices from foodingadda where burgers is not null",x)
        print(i1)
        print()
        break
    elif(b==2):
        engine.say("you have choose option 2  which is vadapav.")
        engine.runAndWait()
        i1=pd.read_sql("select vada_pav,price2 as prices from foodingadda where vada_pav is not null",x)
        print(i1)
        print()
        break
    elif(b==3):
        engine.say("you have choose option 3 which is wraps.")
        engine.runAndWait()
        i1=pd.read_sql("select wraps,price3 as prices from foodingadda where wraps is not null",x)
        print(i1)
        print()
        break
    elif(b==4):
        engine.say("you have choose option 4 which is pizzas.")
        engine.runAndWait()
        i1=pd.read_sql("select pizzas,price4 as prices from eatnrepeat where pizzas is not null",x)
        print(i1)
        print()
        break
    elif(b==5):
        engine.say("you have choose option 5 which is sandwiches.")
        engine.runAndWait()
        i1=pd.read_sql("select sandwich,price5 as prices from eatnrepeat where sandwich is not null",x)
        print(i1)
        print()
        break
    elif(b==6):
        engine.say("you have choose option 6 which is snacks.")
        engine.runAndWait()
        i1=pd.read_sql("select snacks,price4 as prices from foodingadda where snacks is not null",x)
        print(i1)
        print()
        break
    elif(b==7):
        engine.say("you have choose option 7 which is pasta.")
        engine.runAndWait()
        i1=pd.read_sql("select pasta,price7 as prices from eatnrepeat where pasta is not null",x)
        print(i1)
        print()
        break
    elif(b==8):
        engine.say("you have choose option 8 which is garlic bread.")
        engine.runAndWait()
        i1=pd.read_sql("select garlic_bread,price8 as prices from eatnrepeat where garlic_bread is not null",x)
        print(i1)
        print()
        break
    elif(b==9):
        engine.say("you have choose option 9 which is chaap.")
        engine.runAndWait()
        i1=pd.read_sql("select chaap_khazana,price1 as prices from khalo where chaap_khazana is not null",x)
        print(i1)
        print()
        break
    elif(b==10):
        engine.say("you have choose option 10 which is rolls.")
        engine.runAndWait()
        i1=pd.read_sql("select rolls,price3 as prices from khalo where rolls is not null ",x)
        print(i1)
        print()
        break
    else:
        engine.say("you have choose incorrect option .")
        engine.runAndWait()
        print()
        continue
# MENU CODE ENDS

# ORDER CODE STARTS 
p05=0
while(p05!=1):          
        if(b==1):
                burger="press 1 to order aloo tikki burger \npress 2 to order veg tikki burger \npress 3 to order veg king cheese burger \npress 4 to order punjabi double cheese burger \npress 5 to order cheese corn burger \n \nplease enter your choice"
                print(burger)
                engine.say("please choose any option for burger which you want to order ") 
                engine.runAndWait()
                c=int(input(""))
                if(c==1):
                        i1=pd.read_sql("select burgers from foodingadda where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from foodingadda where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(c==2):
                        i1=pd.read_sql("select burgers from foodingadda where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from foodingadda where food_id=2",x)
                        org=p1.values
                        print()
                        break
                elif(c==3):
                        i1=pd.read_sql("select burgers from foodingadda where food_id=3",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from foodingadda where food_id=3",x)
                        org=p1.values
                        print()
                        break
                elif(c==4):
                        i1=pd.read_sql("select burgers from foodingadda where food_id=4",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from foodingadda where food_id=4",x)
                        org=p1.values
                        print()
                        break
                elif(c==5):
                        i1=pd.read_sql("select burgers from foodingadda where food_id=5",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from foodingadda where food_id=4",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option ") 
                        engine.runAndWait()
                        continue
        elif(b==2):
                vadapav="press 1 to order classic vada pav \npress 2 to order chatpata vada pav \npress 3 to order cheese vada pav \npress 4 to order punjabi vada pav \npress 5 to order maharaja vada pav \n \nplease enter your choice"
                print(vadapav)
                engine.say("please choose the option for vada pav which you want to order are given below") 
                engine.runAndWait()
                v1=int(input(""))
                if(v1==1):
                        i1=pd.read_sql("select vada_pav from foodingadda where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price2 as prices from foodingadda where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(v1==2):
                        i1=pd.read_sql("select vada_pav from foodingadda where food_id=2",x)
                        i1.values
                        p1=pd.read_sql("select price2 as prices from foodingadda where food_id=2",x)
                        org=p1.values
                        print()
                        break
                elif(v1==3):
                        i1=pd.read_sql("select vada_pav from foodingadda where food_id=3",x)
                        i2=i1.values
                        p1=pd.read_sql("select price2 as prices from foodingadda where food_id=3",x)
                        org=p1.values
                        print()
                        break
                elif(v1==4):
                        i1=pd.read_sql("select vada_pav from foodingadda where food_id=4",x)
                        i2=i1.values
                        p1=pd.read_sql("select price2 as prices from foodingadda where food_id=4",x)
                        org=p1.values
                        print()
                        break
                elif(v1==5):
                        i1=pd.read_sql("select vada_pav from foodingadda where food_id=5",x)
                        i2=i1.values
                        p1=pd.read_sql("select price2 as prices from foodingadda where food_id=5",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        print()
                        continue
        elif(b==3):
                wrap="press 1 to order aloo tikki wrap \npress 2 to order veg wrap \npress 3 to order masala wrap \npress 4 to order paneer wrap \npress 5 to order cheese wrap \n \nplease enter your choice:"
                print(wrap)
                engine.say("please choose the option for wraps which you want to order") 
                engine.runAndWait()
                w1=int(input(""))
                if(w1==1):
                        i1=pd.read_sql("select wraps from foodingadda where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from foodingadda where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(w1==2):
                        i1=pd.read_sql("select wraps from foodingadda where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from foodingadda where food_id=2",x)
                        org=p1.values
                        print()
                        break
                elif(w1==3):
                        i1=pd.read_sql("select wraps from foodingadda where food_id=3",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from foodingadda where food_id=3",x)
                        org=p1.values
                        print()
                        break
                elif(w1==4):
                        i1=pd.read_sql("select wraps from foodingadda where food_id=4",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from foodingadda where  food_id=4",x)
                        org=p1.values
                        print()
                        break
                elif(w1==5):
                        i1=pd.read_sql("select wraps from foodingadda where food_id=5",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from foodingadda where food_id=5",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        print()
                        continue 
        elif(b==4):
                pizza="press 1 to order margherita pizza  \npress 2 to order cheese n corn pizza \npress 3 to order veggie exravagenza pizza \npress 4 to order paneer makhni pizza \n \nplease enter your choice"
                print(pizza)
                engine.say("please choose the option for pizzas which you want to order are given below") 
                engine.runAndWait()
                pi1=int(input(""))
                if(pi1==1):
                        i1=pd.read_sql("select pizzas from eatnrepeat where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from eatnrepeat where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(pi1==2):
                        i1=pd.read_sql("select pizzas from eatnrepeat where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from eatnrepeat where food_id=2",x)
                        org=p1.values
                        print()
                        break
                elif(pi1==3):
                        i1=pd.read_sql("select pizzas from eatnrepeat where food_id=3",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from eatnrepeat where food_id=3",x)
                        org=p1.values
                        print()
                        break
                elif(pi1==4):
                        i1=pd.read_sql("select pizzas from eatnrepeat where food_id=4",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from eatnrepeat where food_id=4",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        print()
                        continue
        elif(b==5):
                sandwich="press 1 to order veg cheese sandwich \npress 2 to order mexican cheese sandwich \npress 3 to order cheese corn sandwich \npress 4 to order paneer chilli sandwich \n \nplease enter your choice"
                print(sandwich)
                engine.say("please choose the option for sandwichs which you want to order") 
                engine.runAndWait()
                sa=int(input(""))
                if(sa==1):
                        i1=pd.read_sql("select sandwich from eatnrepeat where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price5 as prices from eatnrepeat where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(sa==2):
                        i1=pd.read_sql("select sandwich from eatnrepeat where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price5 as prices from eatnrepeat where food_id=2",x)
                        org=p1.values
                        print()
                        break
                elif(sa==3):
                        i1=pd.read_sql("select sandwich from eatnrepeat where food_id=3",x)
                        i2=i1.values
                        p1=pd.read_sql("select price5 as prices from eatnrepeat where food_id=3",x)
                        org=p1.values
                        print()
                        break
                elif(sa==4):
                        i1=pd.read_sql("select sandwich from eatnrepeat where food_id=4",x)
                        i2=i1.values
                        p1=pd.read_sql("select price5 as prices from eatnrepeat where food_id=4",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        print()
                        continue
        elif(b==6):
                snack="press 1 to order french fries \npress 2 to order loaded french fries \npress 3 to order masala french fries \npress 4 to order cheese triangle samosa \npress 5 to order veg nuggets \n \nplease enter your choice"
                print(snack)
                engine.say("please choose the option for snacks which you want to order are given below") 
                engine.runAndWait()
                k1=int(input(""))
                if(k1==1):
                        i1=pd.read_sql("select snacks from foodingadda where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from foodingadda where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(k1==2):
                        i1=pd.read_sql("select snacks from foodingadda where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from foodingadda where food_id=2",x)
                        org=p1.values
                        print()
                        break
                elif(k1==3):
                        i1=pd.read_sql("select snacks from foodingadda where food_id=3",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from foodingadda where food_id=3",x)
                        org=p1.values
                        print()
                        break
                elif(k1==4):
                        i1=pd.read_sql("select snacks from foodingadda where food_id=4",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from foodingadda where food_id=4",x)
                        org=p1.values
                        print()
                        break
                elif(k1==5):
                        i1=pd.read_sql("select snacks from foodingadda where food_id=5",x)
                        i2=i1.values
                        p1=pd.read_sql("select price4 as prices from foodingadda where food_id=5",x)
                        org=p1.values
                        print()
                        break
                else: 
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        continue
        elif(b==7):
                pasta="press 1 to order white sauce pasta \npress 2 to order red sauce  pasta"
                print(pasta)
                engine.say("please choose the option for pastas which you want to order  are given below") 
                engine.runAndWait()
                pa1=int(input(""))
                if(pa1==1):
                        i1=pd.read_sql("select pasta from eatnrepeat where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price7 as prices from eatnrepeat where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(pa1==2):
                        i1=pd.read_sql("select pasta from eatnrepeat where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price7 as prices from eatnrepeat where food_id=2",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        continue
        elif(b==8):
                garb="press 1 to order stuffed garlic bread \npress 2 to order garlic bread"
                print(grab)
                engine.say("please choose the option for garlic bread which you want to  order are given below") 
                engine.runAndWait()
                gb1=int(input(""))
                if(gb1==1):
                        i1=pd.read_sql("select garlic_bread from eatnrepeat where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price7 as prices from eatnrepeat where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(gb1==2):
                        i1=pd.read_sql("select garlic_bread from eatnrepeat where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price7 as prices from eatnrepeat where food_id=2",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        print()
                        continue
        elif(b==9):
                chaap="press 1 to order malai chaap \npress 2 to order stuffed chaap \npress 3 to order afgani chaap \npress 4 to order lemon chaap \npress 5 to order hariyali chaap \npress 6 to order achari chaap \npress 7 to order punjabi chaap \npress 8 to order crunchy chaap \npress 9 to order crisp chaap \n \nplease enter your choice "
                print(chaap)
                engine.say("please choose the option for chaap which you want to order are given below") 
                engine.runAndWait()
                mc1=int(input(""))
                if(mc1==1):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(mc1==2):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=2",x)
                        org=p1.values
                        print()
                        break
                elif(mc1==3):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=3",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=3",x)
                        org=p1.values
                        print()
                        break
                elif(mc1==4):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=4",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=4",x)
                        org=p1.values
                        print()
                        break
                elif(mc1==5):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=5",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=5",x)
                        org=p1.values
                        print()
                        break
                elif(mc1==6):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=6",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=6",x)
                        org=p1.values
                        print()
                        break
                elif(mc1==7):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=7",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=7",x)
                        org=p1.values
                        print()
                        break
                elif(mc1==8):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=8",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=8",x)
                        org=p1.values
                        print()
                        break
                elif(mc1==9):
                        i1=pd.read_sql("select chaap_khazana from khalo where food_id=9",x)
                        i2=i1.values
                        p1=pd.read_sql("select price1 as prices from khalo where food_id=9",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        continue
        elif(b==10):
                roll="press 1 to order malai chaap roll \npress 2 to order stuff roll \npress 3 to order afghani chaap roll \npress 4 to order paneer tikka roll \npress 5 to order garlic chaap roll \npress 6 to order lemon chaap roll \npress 7 to order hariyali chaap roll \npress 8 to order achari chaap roll \npress 9 to order punjabi chaap roll \n \nplease enter your choice"
                print(roll)
                engine.say("please choose the option for rolls which you want to order are ") 
                engine.runAndWait()
                cr1=int(input(""))
                if(cr1==1):
                        i1=pd.read_sql("select rolls from khalo where food_id=1",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=1",x)
                        org=p1.values
                        print()
                        break
                elif(cr1==2):
                        i1=pd.read_sql("select rolls from khalo where food_id=2",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=2",x)
                        org=p1.values
                        print()
                        break
                elif(cr1==3):
                        i1=pd.read_sql("select rolls from khalo where food_id=3",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=3",x)
                        org=p1.values
                        print()
                        break
                elif(cr1==4):
                        i1=pd.read_sql("select rolls from khalo where food_id=4",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=4",x)
                        org=p1.values
                        print()
                        break
                elif(cr1==5):
                        i1=pd.read_sql("select rolls from khalo where food_id=5",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=5",x)
                        org=p1.values
                        print()
                        break
                elif(cr1==6):
                        i1=pd.read_sql("select rolls from khalo where food_id=6",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=6",x)
                        org=p1.values
                        print()
                        break
                elif(cr1==7):
                        i1=pd.read_sql("select rolls from khalo where food_id=7",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=7",x)
                        org=p1.values
                        print()
                        break
                elif(cr1==8):
                        i1=pd.read_sql("select rolls from khalo where food_id=8",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=8",x)
                        org=p1.values
                        print()
                        break
                elif(cr1==9):
                        i1=pd.read_sql("select rolls from khalo where food_id=9",x)
                        i2=i1.values
                        p1=pd.read_sql("select price3 as prices from khalo where food_id=9",x)
                        org=p1.values
                        print()
                        break
                else:
                        engine.say("you have choose incorrect option .") 
                        engine.runAndWait()
                        continue
#ORDER CODE ENDS

#BILLING CODE STARTS
p11=0
while(p11!=1):
        if(b==1 or b==2 or b==2 or b==3 or b==4 or b==5 or b==6 or b==7 or b==8 or b==9 or b==10):
                llib="press 1 to generate bill "
                print(llib)
                engine.say("press one to generate bill")      
                engine.runAndWait()
                bill=int(input(""))
                if(bill==1):
                        print()
                        print("*"*50)
                        print("                    ZWIGGY")
                        print("="*50)
                        billid=str(random.randint(1000000000,9999999999))
                        print('ORDER ID: ',billid)
                        print("-"*50)
                        print("NAME: ",name)
                        print("MOBILE NO.: ",mobile)
                        print("DATE: ",dt)
                        print("TIME: ",tt)
                        print("BILLING ADDRESS: ",loci)
                        print("-"*50)
                        i3=str(i1.iat[0,0])
                        ogp=p1.iat[0,0]
                        orgp=float(ogp)
                        print(i3,' price: ',orgp)
                        cgst=orgp*2.5/100
                        sgst=orgp*2.5/100
                        discount=orgp*2.5/100
                        rn=orgp-discount+cgst+sgst
                        nr=round(rn)                                               
                        print("CGST @ 2.5%: ",cgst)
                        print("SGST @ 2.5%: ",sgst)
                        print("discount  @ 2.5%: ",discount)
                        print("\nround off amount is",nr-rn)
                        print("-"*50)
                        print("TOTAL: ",nr)
                        print("*"*50)
                        print()
                        engine.say("your order total is ")
                        engine.say(nr)
                        engine.say("rupees")
                        engine.runAndWait()
                        kook="press 1 for payment with cash"
                        print(kook)
                        engine.say("press 1 for payment with cash .")
                        engine.runAndWait()
                        ret=int(input(''))
                        if(ret==1):
                            ptc="press 1 to conform your order"
                            print(ptc)
                            engine.say("press 1 to conform your order")
                            engine.runAndWait()
                            cpc=int(input(""))
                            if(cpc==1):
                                print()
                                engine.say("your order has been conformed.")
                                engine.say("your will reached to your destination with in 30 minutes.")
                                engine.runAndWait()
                                print('Thanks For Ordering Food From Us And Visit Us Again')
                                engine.say("thank you for ordering food from us and visit us again . Have a nice day  ")
                                engine.say(name)
                                engine.runAndWait()
                                u=mc.connect(host = 'localhost',user = 'root',password = 'wasd',database='zwiggy')
                                f=u.cursor()
                                f.execute("create table if not exists billing(bill_id varchar(99) not null,name  varchar(99),mobile_no  varchar(99),date varchar(99),time varchar(99),billing_address varchar(200),item_name varchar(99),org_price varchar(99),csgt float,sgst float,discount float,round_off float,total_price float);")
                                aa="insert into billing values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
                                bb=(billid,name,mobile,dt,tt,loci,i3,orgp,cgst,sgst,discount,nr,total)
                                f.execute(aa,bb)
                                u.commit()
                                break

                            elif(cpc!=1):                            
                                engine.say("your order will not placed because you have press wrong option") 
                                engine.runAndWait()
                                continue
                        elif(ret!=1):
                            engine.say("you have entered invalid option") 
                            engine.runAndWait()
                            continue            
                elif(bill!=1):
                        engine.say("your bill is not generated because you have entered  wrong option .") 
                        engine.runAndWait()
                        continue
# BILLING CODE ENDS

# MAP CODE STARTS 
p06=0

while(p06!=1):
        if( p06!=1):
                mak="press 1 to view the maps"
                print(mak)
                engine.say("press 1 for viewing map")      
                engine.runAndWait()
                mapy=int(input(""))
                if(mapy==1):
                        engine.say("map 1 shows the food items along with rating of  khalo restaurant. ")      
                        engine.runAndWait()
                        pl32=[3.5,4.6]
                        pl33=['chaap_khazana','rolls']
                        pl34=np.array([1,2])
                        plt.bar(pl34,pl32,width=0.50,label=pl33,color=['m','silver','y'])
                        plt.legend()
                        plt.xlabel("food items")
                        plt.ylabel("ratings")
                        plt.xticks(pl34,pl33)
                        plt.title(" best selling items of khalo")
                        plt.show()

                        engine.say("map 2 shows the food items along with rating of fooding adda restaurant. ")      
                        engine.runAndWait()
                        pl35=[1.9,2.3,5,2.5,3.9]
                        pl36=['burger','vada_pav ','wraps','sandwich','snacks']
                        pl37=np.array([1,2,3,4,5])
                        plt.bar(pl37,pl35,width=0.50,label=pl36,color=['m','silver','r','y','green'])
                        plt.legend()
                        plt.xlabel("food items")
                        plt.ylabel("ratings")
                        plt.title(" best selling items of foodingadda")
                        plt.xticks(pl37,pl36)
                        plt.show()

                        engine.say("map 3 shows the food items along with rating of eat n repeat restaurant. ")      
                        engine.runAndWait()
                        pl3=[2.5,5,3.9,4.3]
                        p6=['pizzas','sandwich','pasta',' garlicbread']
                        pl7=np.array([1,2,3,4])
                        plt.bar(pl7,pl3,width=0.50,label=p6,color=['m','silver','y','grey'])
                        plt.legend()
                        plt.xlabel("food items")
                        plt.ylabel("ratings")
                        plt.title(" best selling items of eatnrepeat")
                        plt.xticks(pl7,p6)
                        plt.show()

                        engine.say("map 4 shows restaurants rating ")      
                        engine.runAndWait()
                        pl1=np.array([1,2,3])
                        pl2=['khalo','foodingadda','eatnrepeat']
                        pl3=[3.5,4.3,3.8]
                        plt.bar(pl1,pl3,width=0.25,label=pl2,color=['m','silver','yellow'])
                        plt.legend()
                        plt.xlabel("restaurant names")
                        plt.ylabel("rating")
                        plt.title("restaurent ratings")
                        plt.xticks(pl1,pl2)
                        plt.show()
                        break
                elif(mapy!=1):
                    engine.say("you have press wrong option .") 
                    engine.runAndWait()
                    continue
# MAP CODE ENDS
last=0
while(last!=1):
    if(mapy==1):
        engine.say("thankyou  ")
        engine.runAndWait()
        break
    elif(mapy!=1):
        continue