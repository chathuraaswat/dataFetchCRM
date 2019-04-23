import csv
import logging, sys
import hmac
import string
import hashlib
import base64
import json
import requests



import requests 

def on_start():
        with open('/home/aux-120/LoadTestScripts/PushViaAPI/globe/MOCK_DATA.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader: 
                print(" First Name "+row[1])
                print(" Last Name "+row[2])
                print(" Birthdaye "+row[7])
                print(" Email  "+row[3])
                print(" Gender " + row[4])
                print(" Salutation " +row[5])
                print(" maritalStatus "+ row[8])
                print(" nationality "+ row[6])
                requests.post("https://qa-api.aswat.co/crm/profiles",{"firstName":row[1],"Lname": row[2],"email":row[3],"gender":row[4],"salutation":row[5],"maritalStatus":row[8],"nationality":row[6],"birthday":row[7]},headers = {"access_token":"d0b59830-5ffc-11e9-a575-953c92e273b6"})
                print(response)

