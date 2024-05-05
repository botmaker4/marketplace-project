#----IMPORTING PACKAGES----#
import sys
from turtle import clear
from getmac import get_mac_address as gma
from pymongo import MongoClient , errors
import colorama
from colorama import Fore,Back,Style
import random
import getpass
from datetime import date
from datetime import datetime
from subprocess import call
import os
import wget
import time
from time import sleep
import socket
import pickle
import hashlib
from os.path import exists
import string
import smtplib
import ssl
from email.message import EmailMessage
# Add SSL (layer of security)
context = ssl.create_default_context()
#----INITIALIZING MAIN FILES----#
os.system('')
current_update='1.0'
colorama.init(autoreset=True)
cluster="DISCONTINUED"
time_create=date.today()
client = MongoClient(cluster)
db = client['S']
store = db.logincreds
licenses=db.licenses
inventory=db.inventory
version=db.version
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)
connection_true=Fore.YELLOW+" CONNECTION TO DATABASE SUCCESSFUL "
connection_try=Fore.YELLOW+" CONNECTING TO DATABASE  "
connection_false=Fore.YELLOW+" CONNECTION TO DATABASE UNSUCCESSFUL "
exit=Fore.RED+"press enter to exit "
#----EMAIL MANAGEMENT----#

#exit function
def clear_exit(timer):
     k=input(exit)  
     sleep(timer)
     print("exiting..")
     sys.exit()
     
def inventory_data_insertion(iden):
 for x in store.find({'iden':iden},{'_id':0}):
  x=x
  for key, a in x.items():
         if 'username' in  key: 
            for x in store.find({'iden':iden},{'_id':0}):
               x=x
               for key, b in x.items():
                     if 'email_account' in  key:
                        return a,b


def inventory_data_count(item,iden):
 for x in inventory.find({'iden':iden},{'_id':0}):
  x=x
  for key, a in x.items():
         if item in  key: 
            return a

def full_fetch(email):
   for x in store.find({'email_account':email},{'_id':0}):
     x=x
     for key, a in x.items():
            if 'email_account' in  key: 
               for x in store.find({'email_account':email},{'_id':0}):
                  x=x
                  for key, b in x.items():
                        if 'username' in  key:
                            for x in store.find({'email_account':email},{'_id':0}):
                             x=x
                             for key, c in x.items():
                                   if 'backup_code' in  key:
                                      for x in store.find({'email_account':email},{'_id':0}):
                                         x=x
                                         for key, d in x.items():
                                               if 'password' in  key:
                                                  for x in store.find({'email_account':email},{'_id':0}):
                                                   x=x
                                                   for key, e in x.items():
                                                         if 'Creation_Time' in  key:
                                                            for x in store.find({'email_account':email},{'_id':0}):
                                                              x=x
                                                              for key, f in x.items():
                                                                    if 'Total Logins' in  key:
                                                                       for x in store.find({'email_account':email},{'_id':0}):
                                                                        x=x
                                                                        for key, g in x.items():
                                                                              if 'Logged_in_checker' in  key:
                                                                                 for x in store.find({'email_account':email},{'_id':0}):
                                                                                   x=x
                                                                                   for key, h in x.items():
                                                                                         if 'ip' in  key:
                                                                                            for x in store.find({'email_account':email},{'_id':0}):
                                                                                             x=x
                                                                                             for key, i in x.items():
                                                                                                   if 'bank' in  key:
                                                                                                      return a,b,c,d,e,f,g,h,i
def full_fetch_again(email):
   for x in store.find({'email_account':email},{'_id':0}):
     x=x
     for key, j in x.items():
           if 'debit_card_num' in  key:
              for x in store.find({'email_account':email},{'_id':0}):
               x=x
               for key, k in x.items():
                     if 'debit_card_cvv' in  key:
                        for x in store.find({'email_account':email},{'_id':0}):
                         x=x
                         for key, l in x.items():
                               if 'debit_card_bal' in  key:
                                  for x in store.find({'email_account':email},{'_id':0}):
                                   x=x
                                   for key, m in x.items():
                                        if 'phone_number' in  key:
                                         return j,k,l,m                                                                                                                                       
def email_license(license):
   for x in licenses.find({'license':license},{'_id':0}):
         x=x
         for key, val in x.items(): 
          if 'email' in key:
           return val
                                                                                                                                                                       
#-----TASK Manager-----#
tasks = ["You sold of 12 oranges for ", "You worked in cafe for ", "You worked as a taxi driver for ", "You worked as a cleaner for ",
         "You worked as a sales manager for ", "You worked as a baby sitter for ", "You worked as a tutor for ",
         "You worked a fruit seller for ", "You worked as a cashier for "]
def task_select():
   choose=random.choice(tasks)
   
   return choose
   
#---- STORE PURCHASE----#
def market():
   mark=Fore.GREEN+"""What would you like to buy ? :- 
   \n1.Smartphone \n2.Laptop \n3.Graphics_Card \n4.CPU \n5.PC_Cabinet \n6.Bag \n7.Food
    \nPlease respond with number."""
   market = int(input(mark))
    
   if(market==1):
       buy="Smartphone"
       return buy,market
   if(market==2):
       buy="Laptop"
       return buy,market
   if(market==3):
       buy="Graphics_card"
       return buy,market
   if(market==4):
       buy="CPU"
       return buy,market
   if(market==5):
       buy="PC_Cabinet"
       return buy,market
   if(market==6):
       buy="Bag"
       return buy,market
   if(market==7):
       buy="Food"
       return buy,market
       
#----STORE BILLER----#
def shop_billing(item):
     
     if(item==1):
        spend=1000
        return spend
     elif(item==2):
        spend=4000
        return spend
     elif(item==3):
        spend=5000
        return spend
     elif(item==4):
        spend=3500
        return spend
     elif(item==5):
        spend=4500
        return spend
     elif(item==6):
        spend=800
        return spend
     elif(item==7):
         spend=500
         return spend
    
def fetch_inventory_insertion(iden):
   a=licenses.count_documents({'iden':iden}) > 0; 
   if(a==True):
      insertion_needed=False
      return insertion_needed
   else:
      insertion_needed=True
      return insertion_needed
#----MONEY PROVIDER----#
def money_select():
    choose=task_select()
    if(choose=="You sold of 12 oranges for "):
       income = random.randint(150,250)
       return income
    elif(choose=="You worked in cafe for "):
       income = random.randint(300,550)
       return income
    elif(choose=="You worked as a taxi driver for "):
         income = random.randint(350,600)
         return income
    elif(choose=="You worked as a cleaner for "):
         income = random.randint(200,400)
         return income
    elif(choose=="You worked as a sales manager for "):
         income = random.randint(450,750)
         return income
    elif(choose=="You worked as a baby sitter for "):
         income = random.randint(300,500)
         return income
    elif(choose=="You worked as a tutor for "):
         income = random.randint(450,550)
         return income
    elif(choose=="You worked a fruit seller for "):
         income = random.randint(150,250)
         return income
    elif(choose=="You worked as a cashier for "):
         income = random.randint(200,350)
         return income
       
finance=Fore.CYAN+"""
███████╗██╗███╗░░██╗░█████╗░███╗░░██╗░█████╗░███████╗  ███╗░░░███╗░█████╗░███╗░░██╗░█████╗░░██████╗░███████╗██████╗░
██╔════╝██║████╗░██║██╔══██╗████╗░██║██╔══██╗██╔════╝  ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
█████╗░░██║██╔██╗██║███████║██╔██╗██║██║░░╚═╝█████╗░░  ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
██╔══╝░░██║██║╚████║██╔══██║██║╚████║██║░░██╗██╔══╝░░  ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
██║░░░░░██║██║░╚███║██║░░██║██║░╚███║╚█████╔╝███████╗  ██║░╚═╝░██║██║░░██║██║░╚███║██║░░██║╚██████╔╝███████╗██║░░██║
╚═╝░░░░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝╚═╝░░╚══╝░╚════╝░╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝"""
 
paisa = Fore.GREEN+"Choose one:- \n1.Work \n2.Check_Balance \n3.Shop \n4.Bank \n5.Exit  \n \nPlease respond with number. "
bank_options=Fore.GREEN+"Choose one:- \n1.Apply_For_Card \n2.View_Cards \n3.Send_Money \n4.Receive_Money "
#----FINANCE MANAGER OPTIONS----#
def finance_select():
     print(finance)
     print(Fore.RESET)
     print(Fore.YELLOW+"""
 █▄▄ █▄█   █▀ █░█ █▀█ █░█ █▀█ █▄█ ▄▀█   █▀▀ █░█ █▀█ ▀█▀ ▄▀█
 █▄█ ░█░   ▄█ █▀█ █▄█ █▄█ █▀▄ ░█░ █▀█   █▄█ █▄█ █▀▀ ░█░ █▀█""")
     print(Fore.RESET)
     print('\n')
     earn_select=int(input(paisa))
     print(Fore.RESET)
     #Case 1
     if(earn_select==1):
      earn="Work"
      return earn
     #Case 2
     if(earn_select==2):
      earn="Check_bal"
      return earn
      #Case 3
     if(earn_select==3):
      earn="Shop"
      return earn
       #Case 3
     if(earn_select==4):
      earn="Bank"
      return earn
     #Case 3
     if(earn_select==5):
      earn="Exit"
      return earn
 #----FETCHING EMAIL FROM DB----#
def fetcher_card_email():
     for x in store.find({'iden':get_id},{'_id':0}):
         x=x
         for key, val in x.items(): 
          if 'email_account' in key:
           return val
def card_debit():
   card_name=fetcher_username()
   card_bal=0
   card_number=random.randint(100000,999999)
   card_cvv=random.randint(100,999)
   card_email=fetcher_card_email()
   card_type='debit'
   return card_name,card_bal,card_number,card_cvv,card_email,card_type

def fetch_cards():
   for x in store.find({'iden':get_id},{'_id':0}):
     x=x
     for key, a in x.items():
            if 'debit_card_num' in  key: 
               for x in store.find({'iden':get_id},{'_id':0}):
                  x=x
                  for key, val in x.items():
                        if 'debit_card_cvv' in  key:
                           
                            x=x
                            return a,val
                           
def fetch_card_bal():
 for x in store.find({'iden':get_id},{'_id':0}):
         x=x
         for key, val in x.items(): 
          if 'debit_card_bal' in key:
           return val
      
def bank_select():
   bank_sel=int(input(bank_options))
   if(bank_sel==1):
      change='card'
      return change
   if(bank_sel==2):
      change='view_card'
      return change
   if(bank_sel==3):
      change='send'
      return change
   if(bank_sel==4):
      change='receive'
      return change

#----FETCH ACC IP FOR AUTO-LOGIN----#
def fetch_acc_ip():
     for x in store.find({'iden':get_id},{'_id':0}):
         x=x
         for key, val in x.items(): 
          if 'ip' in key:
           return val

#----FETCH CURRENT IP FOR AUTOLOGIN----#
def fetch_ip():
    ip={ip_address}
    return ip
 
def fetch_bank():
 for x in store.find({'iden':get_id},{'_id':0}):
     x=x
     for key, a in x.items():
            if 'username' in  key: 
               for x in store.find({'iden':get_id},{'_id':0}):
                  x=x
                  for key, val in x.items():
                        if 'bank' in  key:
                           return a,val

            
def fetch_bal_receiver():
   for x in store.find({'phone_number':send_to},{'_id':0}):
     x=x
     for key, a in x.items():
            if 'username' in  key: 
               for x in store.find({'phone_number':send_to},{'_id':0}):
                  x=x
                  for key, val in x.items():
                        if 'bank' in  key:
                           return a,val
                        
def fetch_bal_sender():
   for x in store.find({'phone_number':receive_from},{'_id':0}):
     x=x
     for key, a in x.items():
            if 'username' in  key: 
               for x in store.find({'phone_number':receive_from},{'_id':0}):
                  x=x
                  for key, val in x.items():
                        if 'bank' in  key:
                           return a,val
                        
def fetch_email_sender():
   for x in store.find({'phone_number':receive_from},{'_id':0}):
     x=x
     for key, a in x.items():
            if 'username' in  key: 
               for x in store.find({'phone_number':receive_from},{'_id':0}):
                  x=x
                  for key, val in x.items():
                        if 'email_account' in  key:
                           return a,val
                        
def activities_write(activity):
  file_checker= os.path.exists('data/util')
  if(file_checker==True):
   file='data/util/activites.dat'
   file_obj=open(file,'a')
   activity=str(activity)
   activity=activity+'\n'
   s=activity
   file_obj.write(s)
   file_obj.close()
  
     
def activites_read():
   file_checker= os.path.exists('data/util/activites.dat')
   if(os.stat("data/util/activites.dat").st_size != 0 and file_checker==True):
      file='data/util/activites.dat'
      file_obj=open(file,'r')
      print(file_obj.read())
      file_obj.close()
   else:
    print("No recent activites")
   
def fetch_time():
 now = datetime.now()
 current_time = now.strftime("%H:%M:%S")
 return current_time 

def fetch_autologin(license):
  a=licenses.count_documents({'license':license}) > 0;
  if(a==True):
      for x in licenses.find({'license':license},{'_id':0}):
        x=x
        for key, a in x.items():
               if 'license' in  key: 
                  for x in licenses.find({'license':license},{'_id':0}):
                     x=x
                     for key, val in x.items():
                           if 'autologin' in  key:
                              return a,val

#----CHECKING IF DATABASE CONNECTION WAS SUCCESSFUL----#
def check_db():
    print(connection_try)
    try:
         client = MongoClient(cluster, serverSelectionTimeoutMS = 2000)
         client.server_info() # will throw an exception
         return True
    except:
         return False
def check_license_key(license):
     a=licenses.count_documents({'license':license}) > 0;
     if(a==True):
        for x in licenses.find({'license':license},{'_id':0}):
          x=x
          for key, a in x.items():
                 if 'license' in  key: 
                    for x in licenses.find({'license':license},{'_id':0}):
                       x=x
                       
                       for key, val in x.items():
                             if 'huid' in  key:
                                
                                return a,val                        
     else:
        a ='NONE'
        b= 'NONE'
        return a , b
     
#----CONNECTION SYSTEM----#                       
check = check_db()
if(check==True):
  
 print(connection_true)
 if(os.path.exists("updater.py")==False):
    call(['python','repair.py'])
    exit() 
 def version_checker():
   for x in version.find({'code':'001'},{'_id':0}):
    x=x
    for key, a in x.items():
          if 'version' in  key: 
             x=x
             for key,b in x.items():
                if 'download' in key:
                 return a,b
 new_update,download=version_checker()
 if(current_update!=new_update):
    call(['python','updater.py'])
    exit()

 # Define email sender and receiver
 email_sender = 'DISCONTINUED'
 email_password = "DISCONTINUED"
 em = EmailMessage()
 em['From'] = email_sender
 
#----LICENSE SYSTEM----#  
 def gma_finder(license):
     a=licenses.count_documents({'license':license}) > 0;
     if(a==True):
       for x in licenses.find({'license':license},{'_id':0}):
           x=x
           for key, val in x.items(): 
            if 'huid' in key:
             return val
          

     else:
        huid='invalid'
        return huid
   
   
 def admin_finder(license):
     a=licenses.count_documents({'license':license}) > 0;
     if(a==True):
       for x in licenses.find({'license':license},{'_id':0}):
           x=x
           for key, val in x.items(): 
            if 'Admin_Access' in key:
             return val       
          
 def license_finder(huid):
     for x in licenses.find({'huid':huid},{'_id':0}):
         x=x
         for key, val in x.items(): 
          if 'license' in key:
           return val
   
 def admin_log_checker(huid):
    a=licenses.count_documents({'huid':huid}) > 0;
    if(a==True):
       for x in licenses.find({'huid':huid},{'_id':0}):
           x=x
           for key, val in x.items(): 
            if 'Admin_Access' in key:
             return val     
          
 def ban_checker(huid):
    a=licenses.count_documents({'huid':huid}) > 0;
    if(a==True):
       for x in licenses.find({'huid':huid},{'_id':0}):
           x=x
           for key, val in x.items(): 
            if 'banned' in key:
             return val     
    else:
       a='False'
       return a
   
        
 def license_asker():
   ban_check=ban_checker(gma())
   if(ban_check=='False'):
    auto_admin=admin_log_checker(gma())
    if(auto_admin=='True'):
       access='Admin_Granted'
       license_keys=license_finder(gma())
       return access,license_keys
    else:
     file_license='data/util/license.dat'
     file_exists_check=os.path.exists(file_license)
     if(file_exists_check==True):
        file='data/util/license.dat'
        file_obj=open(file,'r')
        license_file=file_obj.read()
        file_obj.close()
        if(os.stat("data/util/license.dat").st_size != 0):
           license_key_validity,huid=check_license_key(license_file)
           huid_check=gma()
           if(license_key_validity!='NONE' and huid_check==huid):
              access='Granted'
              return access,license_key_validity
           else:
              print('Access Denied')
              access='Denied'
              license_key_validity='NONE'
              return access,license_key_validity
              
           
     else: 
      license_key=input("enter your license key ")
      physical_address = gma()
      license_key_validity,huid=check_license_key(license_key)
      if(license_key_validity=='NONE'):
         print("license key is invalid")
         access='Denied'
         license_key_validity='NONE'
         return access , license_key_validity
         
      elif(license_key_validity!='NONE' and huid == 'NONE'):
           old_data = { "license": license_key_validity,"huid": 'NONE' }
           new_data = { "$set": { "license": license_key_validity,"huid": physical_address } }
           licenses.update_one(old_data, new_data)
           data_path=os.path.exists('data')
           if(data_path==True):
            os.mkdir("data/util")
            file_license='data/util/license.dat'
            file_obj=open(file_license,'w')
            file_obj.write(license_key)
            file_obj.close()
           else: 
            os.mkdir("data")
            os.mkdir("data/util")
            file_license='data/util/license.dat'
            file_obj=open(file_license,'w')
            file_obj.write(license_key)
            file_obj.close()
           access='Granted'
           return access , license_key_validity
      elif(license_key_validity!='NONE' and huid == gma()):
           old_data = { "license": license_key_validity,"huid": 'NONE' }
           new_data = { "$set": { "license": license_key_validity,"huid": physical_address } }
           licenses.update_one(old_data, new_data)
           data_path=os.path.exists('data')
           if(data_path==True):
            os.mkdir("data/util")
            file_license='data/util/license.dat'
            file_obj=open(file_license,'w')
            file_obj.write(license_key)
            file_obj.close()
           else: 
            os.mkdir("data")
            file_license='data/temp.dat'
            file_obj=open(file_license,'w')
            file_obj.write('license_key')
            file_obj.close()
            os.mkdir("data/util")
            file_license='data/util/license.dat'
            file_obj=open(file_license,'w')
            file_obj.write(license_key)
            file_obj.close()
            
           
           access='Granted'
           return access , license_key_validity
 
   elif(ban_check=='True'):
      access='Banned'
      license='Banned'
      return access,license


 def account_already_made():
  access,license_fetched=license_asker()
  for x in licenses.find({'license':license_fetched},{'_id':0}):
   x=x
   for key, a in x.items():
          if 'username' in  key: 
             return a
 access,license_fetched=license_asker()

 
         
 if(access=='Granted' or access=='Admin_Granted'):       
  license_valid,autologin=fetch_autologin(license_fetched)   
  if(access=='Granted'):           
   print("Access Granted")
   options_ask='What would you like to do? \n1.Account_Manager \n2.Finance_Manager \n3.Market_place ' 
   choice_ask=int(input(options_ask))
  elif(access=='Admin_Granted'):
      print("Admin Access Granted")
      options_ask='What would you like to do? \n1.Account_Manager \n2.Finance_Manager \n3.Market_place \n4.Admin_Control ' 
      choice_ask=int(input(options_ask))
  
  if(choice_ask==2 and autologin=='True'):
   os.system('cls')
   #----AUTOLOGIN SYSTEM----#
   file_exists = os.path.exists('data/autologin.dat')
   exit = Fore.MAGENTA+" PRESS ENTER TO EXIT"
   if(file_exists==True):
      if(os.stat("data/autologin.dat").st_size != 0):
        file='data/autologin.dat'
        file_obj=open(file,'rb')
        get_hash=pickle.load(file_obj)
        get_hash=hashlib.md5(get_hash.encode())
        get_id=get_hash.hexdigest()
        cu_ip=fetch_ip()
        acc_ip=fetch_acc_ip()
        acc_ip=str(acc_ip)
        cu_ip=str(cu_ip)
        file_obj.close()
        
        
        if(cu_ip==acc_ip):
           
           def fetcher_username():   
            for x in store.find({'iden':get_id},{'_id':0}):
             x=x
             for key, val in x.items(): 
              if 'username' in key:
                 return val
           
           username_read=fetcher_username()
           for x in store.find({'iden':get_id},{'_id':0}):
                       x=x
                       for key, val in x.items():
                           if 'Total Logins' in  key:
                              s=val
                              s=s+1
                              old_data = { "username": username_read,"Total Logins": val }
                              new_data = { "$set": { "username": username_read,"Total Logins": s,"Logged_in_checker":'True' } }
                              store.update_one(old_data, new_data)
                              
           print(Fore.GREEN+" AUTOLOGIN SUCCESFUL")
           print(Fore.CYAN+" Welcome Back ",username_read)
           
           #----AUTOLOGIN  MANAGER OPTIONS----#
           choice_enter='What would you like to do? \n1.Finance_Manager \n2.Recent_Activities '
           choice_enter = int(input(choice_enter))
           if(choice_enter == 1):
              os.system('cls')
              start=finance_select()
              if(start=='Work'):
                 task=task_select()
                 earned=money_select()
                 earne=str(earned)
                 earne=earne+'$'
                 print(Fore.YELLOW+task,earne)
                 time_happened=fetch_time()
                 msg=f'You last worked on {time_happened}'
                 activity_update=activities_write(msg)
                 t=120
                 while t:
                   mins, secs = divmod(t, 60)
                   timer = '{:02d}:{:02d}'.format(mins, secs)
                   print(Fore.RED+'You are on a cooldown for ',timer, end="\r")
                   time.sleep(1)
                   t -= 1
                 print('\n')
                 for x in store.find({'iden':get_id},{'_id':0}):
                      x=x
                      for key, val in x.items():
                           if 'bank' in  key:
                                ab=val
                                ab=int(ab)
                                total=ab+earned
                                total=str(total)
                                old_data = { 'iden':get_id,"bank": val }
                                new_data = { "$set": { 'iden':get_id,"bank": total } }
                                store.update_one(old_data, new_data) 
                                timer = 1
                                clear_exit(timer)
              elif(start=='Check_bal'):
                 for x in store.find({'iden':get_id},{'_id':0}):
                     x=x
                     for key, val in x.items():
                         if 'bank' in  key:
                            earne=str(val)
                            earne=earne+'$'
                            os.system('cls')
                            print(Fore.GREEN+" You bank balance is",Fore.RED+earne)
                            time_happened=fetch_time()
                            msg=f'You last checked Your balance at {time_happened}'
                            activity_update=activities_write(msg)
                            print(Fore.RESET)
                            timer = 1
                            clear_exit(timer)         
              elif(start=='Shop'):
                 item,no=market()
                 purchase=shop_billing(no)
                 confirm_buy=input("Do you want to purchase? ")
                 if(confirm_buy=="yes"):
                  for x in store.find({'iden':get_id},{'_id':0}):
                     x=x
                     for key, val in x.items():
                         if 'bank' in  key:
                            a=val
                            a=int(a)
                            if(a>=purchase):
                                a=a-purchase
                                old_data = { 'iden':get_id,"bank": val }
                                new_data = { "$set": { 'iden':get_id,"bank": a} }
                                store.update_one(old_data, new_data) 
                                need_insertion=fetch_inventory_insertion(get_id)
                                if(need_insertion==True):
                                    username,email=inventory_data_insertion(get_id)
                                    id=random.randint(1,999)
                                    account = {'_id':id,"iden" : get_id,"username":username,"email":email,'Smartphone':'0','Laptop':'0','Graphics_Card':'0','Cpu':'0','Pc_Cabinet':'0','Bag':'0','Food':'0'}
                                    result=inventory.insert_one(account)     
                                count=inventory_data_count(item,get_id)
                                count=int(count)    
                                count_updated=count+1          
                                count=str(count)                
                                old_data = { 'iden':get_id,item:count}
                                new_data = { "$set": { 'iden':get_id,item:count_updated} }
                                inventory.update_one(old_data, new_data) 
                                os.system('cls')
                                print(f"Congratulations You Bought {item} for {purchase}")
                                time_happened=fetch_time()
                                msg=f'You purchased a {item} at {time_happened}'
                                activity_update=activities_write(msg)
                                show_inventory=input("Would you like to see inventory? (Y/N) ")
                                if(show_inventory=='Y'):
                                   
                                   print("yes")
                                else:
                                   os.system('cls')
                                   print("Alright ")
                                   timer=1
                                   clear_exit(timer)                                            
                            else:
                               print("You dont have enough Money In your Bank ")
                               timer = 1
                               clear_exit(timer)
                 else:
                    timer = 1
                    clear_exit(timer)
                  
                  
              elif(start=='Bank'):
                 os.system('cls')
                 print(" Welcome to ASTA LA VISTA Bank ")
                 sel=bank_select()
                 if(sel=='card'):
                    os.system('cls')
                    choice=int(input("Choose One:- \n1.Debit_Card \n2.Credit_Card "))
                    if(choice==1):
                       os.system('cls')
                       name,money=fetch_bank()
                       if(money>3000):
                          confirm_fee=input("A 2500$ fee will be deducted as a security fee (Y/N) ")
                          if(confirm_fee=='Y'):
                                
                                money_fee=money-2500
                                card_name,card_bal,card_number,card_cvv,card_email,card_type=card_debit()
                                message=f"Your Card Name is {card_name} \nYou card number is {card_number} \nYour card cvv is {card_cvv}"
                                card_number_str=str(card_number)
                                card_cvv_str=str(card_cvv)
                                old_data = { 'iden':get_id,"bank": money,'debit_card_num':'0','debit_card_cvv':'0' }
                                new_data = { "$set": { 'iden':get_id,"bank": money_fee,'debit_card_num':card_number_str,'debit_card_cvv':card_cvv_str } }
                                store.update_one(old_data, new_data) 
                                subject = 'Your debit card Details!'
                                em['Subject'] = subject
                                em['To'] = card_email
                                message=str(message)
                                em.set_content(message)
                               # Log in and send the email
                                with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                                 smtp.login(email_sender, email_password)
                                 smtp.sendmail(email_sender, card_email, em.as_string())
                                time_happened=fetch_time()
                                msg=f'You got a debit card on {time_happened}'
                                activity_update=activities_write(msg)
                                os.system('cls')
                                timer = 1
                                clear_exit(timer)
                                
                          else:
                             print("Alright")
                             timer = 1
                             clear_exit(timer)
                          
                       else:
                          print("You dont have the required amount of balance")
                    elif(choice==2):
                       os.system('cls')
                       print("IN DEVELOPMENT")
                       
                 elif(sel=='view_card'):
                     os.system('cls')
                     card_num,card_cvv=fetch_cards()
                     card_name=fetcher_username()
                     print('Your Card Name is ',card_name,'\nYou card number is ',card_num,'\nYour card cvv is ',card_cvv)
                     further_actions=input('\n Manage Card (Y/N) ')
                     if(further_actions=='Y'):
                        manage_card_options='\n1.View_balance \n2.Add_balance \n3.Remove_balance'
                        choose_options=int(input(manage_card_options))
                        if(choose_options==1):
                           card_num,card_cvv=fetch_cards()
                           card_bal=fetch_card_bal()
                           time_happened=fetch_time()
                           msg=f'You last checked your cards on {time_happened}'
                           activity_update=activities_write(msg)
                           os.system('cls')
                           print('\nBalance of card number ',card_num,'is ',card_bal,'$')
                           
                        elif(choose_options==2):
                             os.system('cls')
                             bank_name,bank_balance = fetch_bank()
                             card_balance = fetch_card_bal()
                             amount_to_add=int(input("please enter amount of money to add "))
                             bank_balance_updated=bank_balance-amount_to_add
                             card_balance_updated=card_balance+amount_to_add
                             message="Your new card balance would be ",card_balance_updated,"$",'\n Would you like to continue? (Y/N)'
                             confirmation_changes=input(message)
                             if(confirmation_changes=='Y'):
                               old_data = { 'iden':get_id,"bank": bank_balance,'debit_card_bal':card_balance}
                               new_data = { "$set": { 'iden':get_id,"bank": bank_balance_updated,'debit_card_bal':card_balance_updated}}
                               store.update_one(old_data, new_data) 
                               time_happened=fetch_time()
                               msg=f'You added money to your card on {time_happened}'
                               activity_update=activities_write(msg)
                               os.system('cls')
                               print("Card and bank balance updated!")
                               timer = 1
                               clear_exit(timer)
                             else:
                                print("Alright!")
                                timer = 1
                                clear_exit(timer)
                        elif(choose_options==3):
                             os.system('cls')
                             bank_name,bank_balance = fetch_bank()
                             card_balance = fetch_card_bal()
                             amount_to_remove=int(input("please enter amount of money to remove "))
                             bank_balance_updated=bank_balance+amount_to_remove
                             card_balance_updated=card_balance-amount_to_remove
                             message="Your new card balance would be ",card_balance_updated,"$",'\n Would you like to continue? (Y/N)'
                             confirmation_changes=input(message)
                             if(confirmation_changes=='Y'):
                               os.system('cls')
                               old_data = { 'iden':get_id,"bank": bank_balance,'debit_card_bal':card_balance}
                               new_data = { "$set": { 'iden':get_id,"bank": bank_balance_updated,'debit_card_bal':card_balance_updated}}
                               store.update_one(old_data, new_data) 
                               time_happened=fetch_time()
                               msg=f'You updated your bank balance on {time_happened}'
                               activity_update=activities_write(msg)
                               os.system('cls')
                               print("Card and bank balance updated!")
                               timer = 1
                               clear_exit(timer)
                             else:
                                print("Alright")
                                timer = 1
                                clear_exit(timer)
                        
                     elif(further_actions=='N'):
                        print("Alright")
                        timer = 1
                        clear_exit(timer)
                        
                 elif(sel=='send'):
                   os.system('cls')
                   bank_name,bank_balance = fetch_bank()
                   amount_to_send=int(input("How much money would you like to send? "))
                   if(amount_to_send<=bank_balance):
                      send_to=input("please enter phone number to whom you would like to send ")
                      name_of_receiver,balance_of_receiver=fetch_bal_receiver()
                      message="Would you like to send money to ",name_of_receiver
                      confirm_send=input(message)
                      if(confirm_send=='Y'):
                         os.system('cls')
                         bank_balance_updated=bank_balance-amount_to_send
                         balance_of_receiver_updated=amount_to_send+balance_of_receiver
                         old_data = { 'iden':get_id,"bank": bank_balance}
                         new_data = { "$set": { 'iden':get_id,"bank": bank_balance_updated}}
                         store.update_one(old_data, new_data) 
                         old_data = { 'phone_number':send_to,"bank": balance_of_receiver}
                         new_data = { "$set": { 'phone_number':send_to,"bank": balance_of_receiver_updated}}
                         store.update_one(old_data, new_data) 
                         time_happened=fetch_time()
                         msg=f'You sent money to {name_of_receiver} at {time_happened}'
                         activity_update=activities_write(msg)
                         os.system('cls')
                         print("Money has been sent!")
                         timer = 1
                         clear_exit(timer)
                      else:
                        print("Alright ")
                        timer = 1
                        clear_exit(timer)
                   else:
                      print("You cannot send more money than what you have ")
                      timer = 1
                      clear_exit(timer)
                 elif(sel=='receive'):
                      os.system('cls')
                      bank_name,bank_balance = fetch_bank()
                      receive_from=input("please enter phone number from whom you would like to receive money ")
                      amount_to_receive=int(input("How much would you like to receive "))
                      name_of_sender,balance_of_sender=fetch_bal_sender()
                      message="Would you like to receive money from ",name_of_sender,'(Y/N)'
                      os.system('cls')
                      confirm_receive=input(message)
                      if(confirm_receive=='Y'):
                          sender_name,sender_email=fetch_email_sender()
                          otp=random.randint(1000,9999)
                          subject = 'Transaction Update!'
                          em['Subject'] = subject
                          em['To'] = sender_email
                          message=f"Your otp for amount {amount_to_receive} is {otp} \nRequested by {bank_name}"
                          message=str(message)
                          em.set_content(message)
                         # Log in and send the email
                          with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                           smtp.login(email_sender, email_password)
                           smtp.sendmail(email_sender, sender_email, em.as_string())
                           os.system('cls')
                           otp_confirm=int(input("please enter otp received from sender "))
                           if(otp_confirm==otp and amount_to_receive<=balance_of_sender):
                              bank_balance_updated=bank_balance+amount_to_receive
                              balance_of_sender_updated=balance_of_sender-amount_to_receive
                              old_data = { 'iden':get_id,"bank": bank_balance}
                              new_data = { "$set": { 'iden':get_id,"bank": bank_balance_updated}}
                              store.update_one(old_data, new_data) 
                              old_data = { 'phone_number':receive_from,"bank": balance_of_sender}
                              new_data = { "$set": { 'phone_number':receive_from,"bank": balance_of_sender_updated}}
                              store.update_one(old_data, new_data) 
                              message=f"Transaction was successful \nUpdated balance is {balance_of_sender_updated}"
                              message=str(message)
                              em.set_content(message)
                             # Log in and send the email
                              with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                               smtp.login(email_sender, email_password)
                               smtp.sendmail(email_sender, sender_email, em.as_string())
                              os.system('cls')
                              print("Money has been received")
                              timer = 1
                              clear_exit(timer)
                           elif(otp_confirm!=otp):
                              print("Transaction Failed! (Invalid Otp) ")
                              timer = 1
                              clear_exit(timer)
                           else:
                              message=f"Transaction was unsuccessful \nReason: insufficient balance"
                              message=str(message)
                              em.set_content(message)
                             # Log in and send the email
                              with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
                               smtp.login(email_sender, email_password)
                               smtp.sendmail(email_sender, sender_email, em.as_string())
                               os.system('cls')
                               print("Transaction Failed! ")
                               timer = 1
                               clear_exit(timer)
                      else:
                          
                          print("Alright")
                          timer = 1
                          clear_exit(timer)
   
           elif(choice_enter==2):
              more_choice=int(input('Choose an option: \n1.Clear_Activites \n2.See_Activites '))
              if(more_choice==1):
                 file_exists = os.path.exists('data/util/activites.dat')
                 if(file_exists==True):
                    os.system('cls')
                    file=open('data/util/activites.dat','w')
                    file.write('')
                    file.close()
                    print("Activites weree cleared succesfully")
                    timer = 1
                    clear_exit(timer)
                 
                 
              elif(more_choice==2):
               os.system('cls')
               activites_read()
               timer = 1
               clear_exit(timer)

   
  elif(choice_ask==2 and autologin=='False'):
     os.system('cls')
     print("you need to enable autologin from account manager after logging in")
     timer = 1
     clear_exit(timer)
   
   #ADMIN PANEL#
  elif(choice_ask==4 and access=='Admin_Granted'):
     os.system('cls')
     print("Welcome to Admin panel ")
     choice_options='Choose One \n1.Add_License \n2.Admin_Account \n3.Ban_Account \n4.Fetch_Data \n5.exit '  
     choice=int(input(choice_options))
     if(choice==1 and access=='Admin_Granted'):
         os.system('cls')
         custom_license=input("Would you like to make an custom license? (Y/N) ")
         if(custom_license=='N'):
          S=10
          ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S)) 
          ran=str(ran) 
          ran="SGCODES_RAN_"+ran
          id=random.randint(1,500)
          account = {'_id':id,"license" : ran,"huid" : 'NONE','username':'0','email':'0',"autologin" : 'False','Admin_Access':'False','banned':'False'}
          result=licenses.insert_one(account)
          os.system('cls')
          print("License was added succesfully")
          timer = 1
          clear_exit(timer)
         elif(custom_license=='Y'):
            id=random.randint(1,500)
            custom=input("please enter custom license key ")
            custom="SGCODES_CUS_"+custom
            account = {'_id':id,"license" : custom,"huid" : 'NONE','username':'0','email':'0',"autologin" : 'False','Admin_Access':'False','banned':'False'}
            result=licenses.insert_one(account)
            os.system('cls')
            print("License was added succesfully")
            timer = 1
            clear_exit(timer)
        
     elif(choice==2 and access=='Admin_Granted'):
        licenseverify=input("Please enter license key of the user ")
        huid=gma_finder(licenseverify)
        admin_check=admin_finder(licenseverify)
        if(huid!='NONE' and admin_check=='False'):
         admin_grant_confirm=input("Would you like to grant that user admin access? (Y/N) ")
         if(admin_grant_confirm=='Y'):
           old_data = { "license": licenseverify,'Admin_Access':'False' }
           new_data = { "$set": { "license": licenseverify,'Admin_Access':'True' } }
           licenses.update_one(old_data, new_data)
           print("User has been granted admin access ")
           timer = 1
           clear_exit(timer)
        elif(huid=='invalid'):
           print("License was invalid or the user is already and admin ")
           timer = 1
           clear_exit(timer)
        elif(huid=='NONE'):
           print("User hasnt loggined using license key yet! ") 
           timer = 1
           clear_exit(timer)
           
     elif(choice==3 and access=='Admin_Granted'):
        licenseverify=getpass.getpass(prompt="Please enter license key of that user you wish to ban ")
        huid=gma_finder(licenseverify)
        admin_check=admin_finder(licenseverify)
        if(huid!='NONE' and admin_check=='False'):
         ban_confirm=input("Would you like to ban that user? (Y/N) ")
         if(ban_confirm=='Y'):
           old_data = { "license": licenseverify,'banned':'False' }
           new_data = { "$set": { "license": licenseverify,'banned':'True' } }
           store.update_one(old_data, new_data)
           print("user has been banned ")
           timer = 1
           clear_exit(timer)
        elif(huid!='NONE' and admin_check=='True'):   
            print("An Admin is not allowed to be banned ")
            timer = 1
            clear_exit(timer)
        elif(huid=='invalid' and admin_check=='False'):
           print("License was invalid ")
           timer = 1
           clear_exit(timer)
        elif(huid=='NONE'):
           print("User hasnt loggined using license key yet! ") 
           timer = 1
           clear_exit(timer)
         
         
     elif(choice==4 and access=='Admin_Granted'): 
         licenseask=getpass.getpass(prompt='enter license key ')
         email=email_license(licenseask)
         send_type=int(input("where would you like to send the data \n1.Terminal \n2.Email "))
         emailaccount,username,backup_code,password,creation_time,total_logins,logged_in,ip,bank=full_fetch(email)
         debit_card_num,debit_card_cvv,debit_card_bal,phone_number=full_fetch_again(email)
         data = [
                    f'Your email ID is {emailaccount}',
                    f'Your username is {username}',
                    f'Your backup code is {backup_code}',
                    f'Your password is {password}',
                    f'Account was created on {creation_time}',
                    f'You logiend a total of {total_logins}', 
                    f'times Account ip is {ip}',
                    f'Your bank balance is {bank}', 
                    f'Your debit_card_number is {debit_card_num}', 
                    f'Your cards cvv is {debit_card_cvv}',
                    f'Your card balance is {debit_card_bal}', 
                    f'Your phone number linked is {phone_number}'
                    
                ]
         message = '\n'.join(data)
         if(send_type==1):
            print("Fetching..")
            sleep(2)
            print(message)
         elif(send_type==2):
            email_send_ask=input("Enter email address to which you would like to send data ")
            print("Sending..")
            subject = 'DATA REQUESTED!'
            em['Subject'] = subject
            em['To'] = email_send_ask
            em.set_content(message)
           # Log in and send the email
            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
             smtp.login(email_sender, email_password)
             smtp.sendmail(email_sender, email_send_ask, em.as_string())
            print("DATA SENT!")
         else:
            print("Not a Valid option")
            timer = 1
            clear_exit(timer)
             
     elif(choice==5 and access=='Admin_Granted'): 
         os.system("cls")
         sleep(1)
         print("exiting..")
         sys.exit()
 
  elif(choice_ask==4 and access=='Granted'):
     os.system('cls')
     print("You dont have permissions")
     timer = 1
     clear_exit(timer) 
 
 
 #ACCOUNT MANAGER#
 
  elif(choice_ask==1):
   if(check==True):
    choice='Choose One \n1.Create_Account \n2.Login_Account \n3.Reset_Account \n4.Delete_Account \n5.Account_info \n6.Exit '                   
    head="""                        
   ██║░░░░░██╔══██╗██╔════╝░██║████╗░██║  ████╗░████║██╔══██╗████╗░██║██╔══██╗██╔════╝░██╔════╝██╔══██╗
   ██║░░░░░██║░░██║██║░░██╗░██║██╔██╗██║  ██╔████╔██║███████║██╔██╗██║███████║██║░░██╗░█████╗░░██████╔╝
   ██║░░░░░██║░░██║██║░░╚██╗██║██║╚████║  ██║╚██╔╝██║██╔══██║██║╚████║██╔══██║██║░░╚██╗██╔══╝░░██╔══██╗
   ███████╗╚█████╔╝╚██████╔╝██║██║░╚███║  ██║░╚═╝░██║██║░░██║██║░╚██ █║██║░░██║╚██████╔╝███████╗██║░░██║
   ╚══════╝░╚════╝░░╚═════╝░╚═╝╚═╝░░╚══╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚══╝╚═╝░░╚═╝░╚═════╝░╚══════╝╚═╝░░╚═╝"""
    
   #----SETTINGS PACKAGE----#
    def settings():
       print(head)
       print(Fore.RESET)
       print(Fore.YELLOW+"""
   █▄▄ █▄█   █▀ █░█ █▀█ █░█ █▀█ █▄█ ▄▀█   █▀▀ █░█ █▀█ ▀█▀ ▄▀█
   █▄█ ░█░   ▄█ █▀█ █▄█ █▄█ █▀▄ ░█░ █▀█   █▄█ █▄█ █▀▀ ░█░ █▀█""")
       print(Fore.RESET)
       print('\n')
       retry_confirm=int(input(choice))
       print(Fore.RESET)
       #Case 1
       if(retry_confirm==1):
        change="Create"
        return change
       #Case 2
       if(retry_confirm==2):
        change="Login"
        return change
       #Case 3
       if(retry_confirm==3):
        change="Reset"
        return change
       #Case 4
       elif(retry_confirm==4):
        change="Delete"
        return change
       #Case 5
       elif(retry_confirm==5):
         change="info"
         return change
       elif(retry_confirm>=6):
           change='exit'
           os.system('cls')
           timer = 1
           clear_exit(timer)
   
   #----FETCHING PASSWORD FROM DB----#
    def fetcher_pass():
       for x in store.find({'password':password_ask},{'_id':0}):
              x=x
       for key, val in x.items(): 
        if 'password' in key:
         return val
   
   #----FETCHING PASSWORD INCASE OF RESET----#
    def fetcher_pass_reset():
       for x in store.find({'backup_code':backup_code_ask},{'_id':0}):
        x=x
       for key, val in x.items(): 
        if 'password' in key:
         return val
   
   #----FETCHING BACKUP CODE FROM DB----#
    def fetcher_backup():   
       for x in store.find({'backup_code':backup_code_ask},{'_id':0}):
        x=x
       for key, val in x.items(): 
        if 'backup_code' in key:
         return val
   
   #----FETCHING USERNAME FROM DB----#
    def fetcher_user():   
       for x in store.find({'username':username_ask},{'_id':0}):
        x=x
       for key, val in x.items(): 
        if 'username' in key:
         return val 
   
   #----FETCHING EMAIL FROM DB----#
    def fetcher_email():   
       for x in store.find({'email_account':email_ask},{'_id':0}):
        x=x
       for key, val in x.items(): 
        if 'email_account' in key:
              return val
  
   #----CHECKING IF USER IS LOGGED IN----#
    def fetcher_logged():     
          email_ask=input(Fore.YELLOW+"Enter your email for Email Verification ")
          for x in store.find({'email_account':email_ask},{'_id':0}):
            x=x
            for key, val in x.items(): 
             if 'Logged_in_checker' in key:
              return val
           
   #----FETCHING USER INFO FROM DB----#
    def fetcher_user_info():
       for x in store.find({'backup_code':backup_code_ask},{'_id':0}):
        x=x
       for key, a in x.items(): 
        
          if 'Creation_Time' in key:
            for key, b in x.items(): 
             if 'Total Logins' in key:
              return a,b
   
   #----FETCHING IP WHEN ACCOUNT WAS MADE----#
    def fetch_ip():
       ip={ip_address}
       return ip
    
    #----FETCHING CURRENT IP WHILE LOGGING IN----#
    def fetch_current_ip():
        for x in store.find({'backup_code':backup_code_ask},{'_id':0}):
            x=x
            for key, val in x.items(): 
             if 'ip' in key:
              return val
    def fetch_iden_dump(dump):
     for x in store.find({'email_account':dump},{'_id':0}):
            x=x
            for key, val in x.items(): 
             if 'iden_dump' in key:
              return val
   #----COLLECTING INFORMATION FOR CREATING AN ACCOUNT----#
    def activation():
       email_account=input(Fore.CYAN+"enter your email ")
       a=store.count_documents({'email_account':email_account}) > 0;
       if(a==False):
        checkup_code=random.randint(1000,598454)
        username = input(Fore.CYAN+"enter your Username ")
        a=store.count_documents({'username':username}) > 0;
        if(a==False): 
         password = getpass.getpass(prompt ='enter your password ')
         os.system('cls')
         print('verifying with server..')
         subject = 'Email Verification code'
         em['Subject'] = subject
         em['To'] = email_account
         checkup_code_str=str(checkup_code)
         message=f"Email verification code is {checkup_code_str}"
         em.set_content(message)
        # Log in and send the email
         with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
          smtp.login(email_sender, email_password)
          smtp.sendmail(email_sender, email_account, em.as_string())
         code_confirm=int(input("A verification code was sent to your email please enter "))
         if(code_confirm==checkup_code):
           backup_cod = random.randint(1000,598454)
           custom_id=random.randint(1,999)
           S=45
           ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))    
           iden= str(ran) 
           iden = hashlib.md5(iden.encode())
           iden=str(iden)
           hashed = hashlib.md5(iden.encode())
           approve=hashed.hexdigest()       
           backup_code=str(backup_cod)
           return email_account,username,password,backup_code,custom_id,iden,approve
         else:
           email_account='NONE'
           username='NONE'
           password='NONE'
           backup_code='NONE'
           custom_id='NONE'
           iden='NONE'
           approve='NONE'
           print('invalid otp ')
           return email_account,username,password,backup_code,custom_id,iden,approve
        else:
           email_account='NONE'
           username='IN_USE'
           password='NONE'
           backup_code='NONE'
           custom_id='NONE'
           iden='NONE'
           approve='NONE'
           print("Username is taken ")
           return email_account,username,password,backup_code,custom_id,iden,approve
       else:
           email_account='IN_USE'
           username='NONE'
           password='NONE'
           backup_code='NONE'
           custom_id='NONE'
           iden='NONE'
           approve='NONE'
           print("Email already in use")
           return email_account,username,password,backup_code,custom_id,iden,approve
    
    change=settings()
    #----CREATING AN ACCOUNT AND SAVING ITS INFORMATION ON DB----#
    one_acc=account_already_made()
    if(change=='Create' and one_acc!='0'):
     print("only one account creation is allowed per key ")
    if(change=="Create" and one_acc=='0'):
       
          ip=fetch_ip()
          ip=str(ip)
          email_account,username,password,backup_code,id,iden,approve=activation()
          if(username!='IN_USE'):
           if(iden!='NONE'):
             money=2000
             creation_time = time_create.strftime("%B %d, %Y")
             account = {'_id':id,"email_account" : email_account,"username" : username,"backup_code" : backup_code,"password" : password,"Creation_Time" : creation_time,'Total Logins' : 0,'Logged_in_checker' : 'False','ip':ip,'bank':money,'iden':approve,'iden_dump':iden,'debit_card_num':'0','debit_card_cvv':'0','debit_card_bal':'0','phone_number':'0'}
             if(email_account!=''and username!='' and password!='' and backup_code!=''):
                         result=store.insert_one(account)
                         print("Your backup code is",Fore.RED + backup_code, Fore.YELLOW +"\nIt is required to access or make changes to your account")
                         #UPDATING LICENSE DATA 
                         old_data = { "huid":gma(),"username": '0',"email": '0' }
                         new_data = { "$set": { "huid":gma(),"username": username,"email": email_account } }
                         licenses.update_one(old_data, new_data)  
                         auto_login=input(Fore.GREEN+"Do you want to enable auto login? ")
                         if(auto_login=='yes'):
                           data_path=os.path.exists('data')
                         if(data_path==True):
                          file_name='data/autologin.dat'
                          fileop=open(file_name,'wb')
                          pickle.dump(iden,fileop)
                          fileop.close()
                          old_data = { "license": license_valid,"autologin": 'False' }
                          new_data = { "$set": { "license": license_valid,"autologin": 'True' } }
                          licenses.update_one(old_data, new_data) 
                         elif(data_path==False):
                            os.mkdir('data')
                            file_name='data/autologin.dat'
                            fileop=open(file_name,'wb')
                            pickle.dump(iden,fileop)
                            fileop.close()
                            old_data = { "license": license_valid,"autologin": 'False' }
                            new_data = { "$set": { "license": license_valid,"autologin": 'True' } }
                            licenses.update_one(old_data, new_data)
                         else:
                              print(Fore.YELLOW+"ALRIGHT")
                         print('                                        ')
                         print(Fore.GREEN+"ACCOUNT HAS BEEN CREATED SUCCESSFULLY!")
                         print(Fore.GREEN+"2000$ has been credited into your account ")
                         print(Fore.RESET)
                         timer = 1
                         clear_exit(timer) 
             else:
                    print(Fore.RED+"ACCOUNT CREATION FAILED!")
                    timer = 1
                    clear_exit(timer) 
           else:
              print(Fore.RED+"Account creation failed!")
              timer = 1
              clear_exit(timer) 
          else:
              print(Fore.RED+"Account creation failed!")
              timer = 1
              clear_exit(timer) 
          
   #----TAKING CREDENTIALS AND FETCHING FROM DB TO LOGIN----#  
    elif(change=='Login'):
        username_ask = input(Fore.CYAN+"enter your Username. ")
        a=store.count_documents({'username':username_ask}) > 0;
        if(a==True):
         email_ask = input(Fore.CYAN+"enter your email. ")
         b=store.count_documents({'email_account':email_ask}) > 0;
         if(b==True):
          password_ask = getpass.getpass(prompt ='enter your password ')
         c=store.count_documents({'password':password_ask}) > 0;
         if(c==True):
          backup_code_ask = getpass.getpass(prompt=Fore.CYAN+"enter your backup code ")
          d=store.count_documents({'backup_code':backup_code_ask}) > 0;
          print(Fore.RESET)
        if(a==True and b==True and c == True and d==True):
           username_fetch=fetcher_user()
           password_fetch=fetcher_pass()
           backup_fetch=fetcher_backup()
           email_fetch=fetcher_email()
           current_ip=fetch_current_ip()
           account_ip=fetch_ip()
           account_ip=str(account_ip)
           current_ip=str(current_ip)
           if(current_ip==account_ip):
                  if(username_ask==username_fetch and email_ask==email_fetch and password_ask==password_fetch and backup_code_ask == backup_fetch):       
                   for x in store.find({'backup_code':backup_code_ask},{'_id':0}):
                    x=x
                   for key, val in x.items():
                        if 'Total Logins' in  key:
                           s=val
                           s=s+1
                           old_data = { "username": username_ask,"Total Logins": val }
                           new_data = { "$set": { "username": username_ask,"Total Logins": s,"Logged_in_checker":'True' } }
                           store.update_one(old_data, new_data)
                           
                           #UPDATING LICENSE DATA 
                           old_data = { "huid":gma(),"username": '0',"email": '0' }
                           new_data = { "$set": { "huid":gma(),"username": username_fetch,"email": email_fetch } }
                           licenses.update_one(old_data, new_data)  
                           file_exists = os.path.exists('data/autologin.dat')
                           if(file_exists==False):
                            auto_login=input(Fore.GREEN+" Do you want to enable auto login? ")
                            if(auto_login=='yes'):
                             old_data = { "license": license_valid,"autologin": 'False' }
                             new_data = { "$set": { "license": license_valid,"autologin": 'True' } }
                             licenses.update_one(old_data, new_data)
                             file_name='data/autologin.dat'
                             file='data/autologin.dat'
                             file_write=open(file,'w')
                             file_write.write(file)
                             file_write.close()
                             fileop=open(file_name,'wb')
                             iden=fetch_iden_dump(email_fetch)
                             pickle.dump(iden,fileop)
                             fileop.close()
                            else:
                                 print(Fore.YELLOW+" ALRIGHT")
                                 timer = 1
                                 clear_exit(timer) 
                           else:
                            print(Fore.GREEN+" LOGGED IN SUCCESSFULLY!")
                            print(Fore.RESET)
                            timer = 1
                            clear_exit(timer)          
           else:
               print(Fore.RED+"We suspect your account credentials were leaked ")    
               timer = 1
               clear_exit(timer)           
        else:
               print(Fore.RED+"oops! Looks like some of your credentials were incorrect")
               print(Fore.RESET)
               timer = 1
               clear_exit(timer) 
            
   #----RESETTING PASSWORD----#
    elif(change=="Reset"):
       logged_fetch=fetcher_logged()
       if(logged_fetch=='True'):
          choice_reset=int(input("What would you like to reset? \n1.Reset_password \n2.Change_Username \n3.Change_email \nPlease respond with number. "))
          if(choice_reset==1):
            username_ask = input(Fore.CYAN+"enter your Username. ")
            a=store.count_documents({'username':username_ask}) > 0;
            if(a==True):
             email_ask = input(Fore.CYAN+"enter your email. ")
             b=store.count_documents({'email_account':email_ask}) > 0;
             if(b==True):
                backup_code_ask = input(Fore.CYAN+"enter your backup code ")
                d=store.count_documents({'backup_code':backup_code_ask}) > 0;
                print(Fore.RESET)
                if(a==True and b==True and d==True):
                   backup_code_fetch= fetcher_backup()     
                   email_fetch=fetcher_email()
                   username_fetch= fetcher_user()
                   password_fetch=fetcher_pass_reset()
                   current_ip=fetch_current_ip()
                   account_ip=fetch_ip()
                   account_ip=str(account_ip)
                   current_ip=str(current_ip)
                   if(current_ip==account_ip):
                          if(username_ask==username_fetch and email_fetch == email_ask and backup_code_ask==backup_code_fetch):
                             new_pass=input("enter your new password ")
                             old_data = { "username": username_ask,"password": password_fetch}
                             new_data = { "$set": { "username": username_ask,"password": new_pass,"Logged_in_checker":'False' } }
                             store.update_one(old_data, new_data)
                             print(Fore.GREEN+"Account password changed successfully!")
                             print(Fore.RESET)
                             timer = 1
                             clear_exit(timer) 
                          else:
                                  print(Fore.RED+"oops! Looks like some of your credentials were incorrect") 
                                  print(Fore.RESET) 
                                  timer = 1
                                  clear_exit(timer)  
                   else:
                        print(Fore.RED+"We suspect your account credentials were leaked ") 
                        timer = 1
                        clear_exit(timer)                         
           
         #----RESETTING USERNAME----#
          elif(choice_reset==2):
              username_ask = input(Fore.CYAN+"enter your Username. ")
              a=store.count_documents({'username':username_ask}) > 0;
              if(a==True):
                email_ask = input(Fore.CYAN+"enter your email. ")
                b=store.count_documents({'email_account':email_ask}) > 0;
                if(b==True):
                  password_ask = input(Fore.CYAN+"enter your password. ")
                  c=store.count_documents({'password':password_ask}) > 0;
                  if(c==True):
                   backup_code_ask = input(Fore.CYAN+"enter your backup code ")
                   d=store.count_documents({'backup_code':backup_code_ask}) > 0;
                   print(Fore.RESET)
                   if(a==True and b==True and c==True and d==True):
                      backup_code_fetch= fetcher_backup()     
                      email_fetch=fetcher_email()
                      username_fetch= fetcher_user()
                      password_fetch=fetcher_pass_reset()
                      current_ip=fetch_current_ip()
                      account_ip=fetch_ip()
                      account_ip=str(account_ip)
                      current_ip=str(current_ip)
                      if(current_ip==account_ip):
                         if(username_ask==username_fetch and email_fetch == email_ask and backup_code_ask==backup_code_fetch and password_ask==password_fetch):
                                new_username=input("enter your new username ")
                                old_data = { "username": username_ask,"email_account": email_ask,"backup_code": backup_code_ask,"password": password_ask }
                                new_data = { "$set": { "username": new_username,"email_account": email_ask,"backup_code": backup_code_ask,"password": password_ask,"Logged_in_checker":'False' } }
                                store.update_one(old_data, new_data)
                                print(Fore.GREEN+"Account username changed successfully!")
                                print(Fore.RESET)
                                timer = 1
                                clear_exit(timer) 
                         else:
                                  print(Fore.RED+"oops! Looks like some of your credentials were incorrect") 
                                  print(Fore.RESET)
                                  timer = 1
                                  clear_exit(timer)
                      else:
                        print(Fore.RED+"We suspect your account credentials were leaked ")   
                        timer = 1
                        clear_exit(timer) 
            
         #----RESETTING EMAIL----#            
          elif(choice_reset==3):
              username_ask = input(Fore.CYAN+"enter your Username. ")
              a=store.count_documents({'username':username_ask}) > 0;
              if(a==True):
                email_ask = input(Fore.CYAN+"enter your email. ")
                b=store.count_documents({'email_account':email_ask}) > 0;
                if(b==True):
                  password_ask = input(Fore.CYAN+"enter your password. ")
                  c=store.count_documents({'password':password_ask}) > 0;
                  if(c==True):
                   backup_code_ask = input(Fore.CYAN+"enter your backup code ")
                   d=store.count_documents({'backup_code':backup_code_ask}) > 0;
                   print(Fore.RESET)
                   if(a==True and b==True and c==True and d==True):
                      backup_code_fetch= fetcher_backup()     
                      email_fetch=fetcher_email()
                      username_fetch= fetcher_user()
                      password_fetch=fetcher_pass_reset()
                      current_ip=fetch_current_ip()
                      account_ip=fetch_ip()
                      account_ip=str(account_ip)
                      current_ip=str(current_ip)
                      if(current_ip==account_ip):
                           if(username_ask==username_fetch and email_fetch == email_ask and backup_code_ask==backup_code_fetch and password_ask==password_fetch):
                               new_email=input("enter your new email ")
                               old_data = { "username": username_ask,"email_account": email_ask,"backup_code": backup_code_ask,"password": password_ask}
                               new_data = { "$set": { "username": username_ask,"email_account": new_email,"backup_code": backup_code_ask,"password": password_ask,"Logged_in_checker":'False' } }
                               store.update_one(old_data, new_data)
                               print(Fore.GREEN+"Account email changed successfully!")
                               print(Fore.RESET)
                               timer = 1
                               clear_exit(timer)
                           else:
                                  print(Fore.RED+"oops! Looks like some of your credentials were incorrect") 
                                  print(Fore.RESET)
                                  timer = 1
                                  clear_exit(timer)
                                  
                      else:
                        print(Fore.RED+"We suspect your account credentials were leaked ") 
                        timer = 1
                        clear_exit(timer)  
       else:
          print(Fore.RED+"You need to login first ")
          print(Fore.RESET)
          timer = 1
          clear_exit(timer) 
      
   #----DELETING USER'S ACCOUNT----#   
    elif(change=="Delete"):
       logged_fetch=fetcher_logged()
       if(logged_fetch=='True'):
          username_ask = input(Fore.CYAN+"enter your Username. ")
          a=store.count_documents({'username':username_ask}) > 0;
          if(a==True):
           
           email_ask = input(Fore.CYAN+"enter your email. ")
           b=store.count_documents({'email_account':email_ask}) > 0;
           if(b==True):
            password_ask = input(Fore.CYAN+"enter your password. ")
            c=store.count_documents({'password':password_ask}) > 0;
            if(c==True):
             backup_code_ask = input(Fore.CYAN+"enter your backup code ")
             d=store.count_documents({'backup_code':backup_code_ask}) > 0;
             print(Fore.RESET)
        
            if(a==True and b==True and c == True and d==True):
               username_fetcher=fetcher_user()
               password_fetcher=fetcher_pass()
               backup_code_fetcher=fetcher_backup()
               email_account_fetcher=fetcher_email()
               current_ip=fetch_current_ip()
               account_ip=fetch_ip()
               account_ip=str(account_ip)
               current_ip=str(current_ip)
               if(current_ip==account_ip):
                     if(email_ask==email_account_fetcher and password_ask==password_fetcher and username_ask == username_fetcher and backup_code_ask==backup_code_fetcher):
                                  confirm_delete=input(Fore.RED+"do you really want to delete your account? ")
                                  if(confirm_delete=="yes"):
                                     old_delete={ "username": username_ask,"password": password_ask,"email_account": email_ask,"backup_code": backup_code_ask }
                                     store.delete_one(old_delete)
                                     print(Fore.GREEN+"Account has been deleted successfully")
                                     print(Fore.RESET)
                                     timer = 1
                                     clear_exit(timer) 
                                  else:
                                    print(Fore.YELLOW+"Alright process for deleting has been stopped!")
                                    print(Fore.RESET)
                                    timer = 1
                                    clear_exit(timer) 
                     else:
                       print(Fore.RED+"oops! Looks like some of your credentials were incorrect") 
                       print(Fore.RESET)
                       timer = 1
                       clear_exit(timer)    
               else:
                  print(Fore.RED+"We suspect your account credentials were leaked ") 
                  timer = 1
                  clear_exit(timer) 
       else:
         print(Fore.RED+'You need to login first!')
         print(Fore.RESET)
         timer = 1
         clear_exit(timer)         
    elif(change=="info"):
       username_ask = input(Fore.CYAN+"enter your Username. ")
       a=store.count_documents({'username':username_ask}) > 0;
       if(a==True):
           
         email_ask = input(Fore.CYAN+"enter your email. ")
         b=store.count_documents({'email_account':email_ask}) > 0;
         if(b==True):
          password_ask = input(Fore.CYAN+"enter your password. ")
          c=store.count_documents({'password':password_ask}) > 0;
         if(c==True):
          backup_code_ask = input(Fore.CYAN+"enter your backup code ")
          d=store.count_documents({'backup_code':backup_code_ask}) > 0;
          print(Fore.RESET)
        
          if(a==True and b==True and c == True and d==True):
           username_fetcher=fetcher_user()
           password_fetcher=fetcher_pass()
           backup_code_fetcher=fetcher_backup()
           email_account_fetcher=fetcher_email()
          if(email_ask==email_account_fetcher and password_ask==password_fetcher and username_ask == username_fetcher and backup_code_ask==backup_code_fetcher):
                                  
            creation_date,login_time=fetcher_user_info()
            print(Fore.GREEN+f"Account Creation Time {creation_date} \nTotal_Logins {login_time}")
            print(Fore.RESET)
            timer = 1
            clear_exit(timer)
          else:
            print(Fore.RED+"oops! Looks like some of your credentials were incorrect")
            print(Fore.RESET)
            timer = 1
            clear_exit(timer)
    else:
      timer = 1
      clear_exit(timer)
       
   else:
      print(connection_false)
      timer = 1
      clear_exit(timer)
      
  else:
     os.system('cls')
     print("That is not a valid option ")
     timer = 1
     clear_exit(timer)
    
 elif(access=='Denied'):
     
     timer = 1
     clear_exit(timer)
     
 elif(access=='Banned' and license_fetched=='Banned'):
    os.system('cls')
    print("You are banned please contact support")
    timer = 4
    clear_exit(timer)
