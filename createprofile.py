import csv
import string
import json
import requests


from locust import HttpLocust, TaskSet, task 
from locust.stats import RequestStats
from locust.clients import HttpSession 
import requests



token = "890763f0-64b2-11e9-a575-953c92e273b6"

class createprofile(TaskSet):
    
    
    @task
    def on_start(self):
        with open('/home/aux-120/LoadTestScripts/PushViaAPI/globe/MOCK_DATA.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader: 
#Create Profile                
                s = HttpSession("https://qa-api.aswat.co")
                crtProfile = s.post("https://qa-api.aswat.co/crm/profiles",{"firstName":row[1],"lastName": row[2],"email":row[3],"gender":row[4],"salutation":row[5],"maritalStatus":row[8],"nationality":row[6],"birthday":row[7]},headers = {"access_token":token})
                json_dataProfile =json.loads(crtProfile.text)
                AgentID =json_dataProfile['content']["id"] 
                AgentName =json_dataProfile['content']["firstName"] 
                print AgentName
                print AgentID
#Create Number
                crtNumber = s.post("https://qa-api.aswat.co/crm/numbers",{"number":row[9],"type": row[10]},headers= {"access_token":token})
                print row[9]
                print row[10]
                json_dataNumber =json.loads(crtProfile.text)
                NumberID =json_dataNumber['content']["id"]
                print  NumberID
# #Create Address
                crtAddress = s.post("https://qa-api.aswat.co/crm/addresses",{"addressLine1":row[10],"addressLine2": row[11],"city":row[12],"state":row[13],"country":row[14],"type":row[15],"zip":row[16]},headers= {"access_token":token})
                print row[10]
                print row[14]
                json_dataAddress =json.loads(crtAddress.text)
                AddressID =json_dataAddress['content']["id"]
                print  AddressID



class createprofile(HttpLocust):
    task_set = createprofile
