import csv
import logging, sys
import hmac
import string
import hashlib
import base64
import json
import array as arr
import redis


from globe import config 
from modules.admin import auth
from modules.agent import authAgent
from locust import HttpLocust, TaskSet, task ,seq_task
from locust.stats import RequestStats
from globe import util
from array import *

class runnerAgent(TaskSet):
    global json_data
    global accress_token
    global path
    global ccLogin
    global API_KEY
    global getAr
    global VarCD
    
    @seq_task(1)
    @task(80)
    def Login(self):
        #Object from globle file 
        conf = config.config()
        path = conf.getLocation()
        #object from Admin Auth
        login = authAgent.authAgent()
        PWConbv = util.util()
        Rcache = redis.Redis(host='127.0.0.1', port=6379, db=0)

        with open('/home/aux-120/LoadTestScripts/ziwoLoadTestv0.1/globe/credentials.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print(" Login Agent with Username--->"+row[0]+" Who has Password --->"+row[1])
                # Loginresponse=login.login(row[0],row[1])
                # assert Loginresponse.status_code is 200, "Unexpected response code: " + Loginresponse.status_code
                # json_data =json.loads(Loginresponse.text)
                # accress_token =json_data['content']["access_token"] 
                # ccLogin =json_data ['content']["ccLogin"]
                # agentID=json_data['content']['id']
                # ObjectAgent =json.dumps({ "UserName":row[0],"PassWord":row[1],"ccLogin":ccLogin,"id":agentID})
                # Rcache.set(row[0],ObjectAgent)
                # API_KEY = conf.getAPI_key()
                # if Loginresponse.status_code==200:
                #     login.AutoLog(accress_token) 
                # else:
                #     login.login(row[0],EncriptedPW)
                #positionLogout=login.Logout(accress_token) 
    
    @seq_task(2)
    @task(40)
    def load_page(self, url=None):
        print "2nd Taksk runting now" 




class LoginWithUniqueUsersTest(HttpLocust):
    task_set = runnerAgent
    