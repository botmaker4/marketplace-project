import os
import zipfile
import sys
import time
from time import sleep
from subprocess import call
from pymongo import MongoClient , errors
import wget
cluster="mongodb+srv://xavierlol:01632987@cluster0.usjq3sl.mongodb.net/LOGINDATA?retryWrites=true&w=majority"
client = MongoClient(cluster)
db = client['S']
store = db.logincreds
licenses=db.licenses
inventory=db.inventory
version=db.version



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

print(f'updating to latest version {new_update}')
wget.download(download)
restart_confirmation='Y'
if(restart_confirmation=='Y'):
  file_name= os.path.basename(sys.argv[0])
  if(os.path.exists("marketplace.py")==True):
   print("removing old files")
   os.remove('marketplace.py')
   sleep(2)
   print("removed old files")
  else:
     pass
  with zipfile.ZipFile('marketplace.zip','r') as zip_object:
      print("Extracting packages")
      sleep(2)
      zip_object.extractall()
      zip_object.close()
      print("Extracted!")
      sleep(1)
      if(os.path.exists("marketplace.zip")==True):
       print("removing old downloaded files")
       os.remove('marketplace.zip')
       sleep(2)
      else:
         pass
      call(['python','marketplace.py'])
      
exit()