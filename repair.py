import os
from subprocess import call
from pymongo import MongoClient , errors
import wget
import zipfile
cluster="mongodb+srv://xavierlol:01632987@cluster0.usjq3sl.mongodb.net/LOGINDATA?retryWrites=true&w=majority"
client = MongoClient(cluster)
db = client['S']
store = db.logincreds
licenses=db.licenses
inventory=db.inventory
version=db.version
pending=0
if(os.path.exists('marketplace.py')==True):
    pending=pending+0
else:
    pending=pending+1
if(os.path.exists('updater.py')==True):
    pending=pending+0
else:
    pending=pending+1
    
if(pending>=1):
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
 print("downloading files ")
 wget.download(download) 
 with zipfile.Zipfile('marketplace.zip','r') as zip:
     print("extracting files")
     zip.extractall()
     print("Extracted")
     if(os.path.exists('marketplace.zip')==True):
        os.remove('marketplace.zip')
        print("repaired one file ")
        
     else:
         print("repaired one file ")
         
 


if(pending==2):
 def version_checker():
    for x in version.find({'code':'002'},{'_id':0}):
     x=x
     for key, a in x.items():
          if 'version' in  key: 
             x=x
             for key,b in x.items():
                if 'download' in key:
                 return a,b
 new_update,download=version_checker()
 print("downloading files ")
 wget.download(download) 
 with zipfile.Zipfile('updater.zip','r') as zip:
     print("extracting files")
     zip.extractall()
     print("Extracted")
     if(os.path.exists('updater.zip')==True):
        os.remove('updater.zip')
        print("repaired one file ")
        
     else:
         print("repaired one file ")
         
exit()