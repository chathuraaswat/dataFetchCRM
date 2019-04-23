

from locust import HttpLocust, TaskSet, task 
from locust import clients
from locust.clients import HttpSession 
import requests
global BaseUrl 
class crm():
    BaseUrl = "https://qa-api.aswat.co"
    def addProfile( firstName,lastName,email,gender,salutation,maritalStatus,nationality,birthday):
        s = HttpSession("https://qa-api.aswat.co")
        response = s.post("https://qa-api.aswat.co/crm/profiles",{"firstName":firstName,"lastName": lastName,"email":email,"gender":gender,"salutation":salutation,"maritalStatus":maritalStatus,"nationality":nationality,"birthday":birthday},headers = {"access_token":"d0b59830-5ffc-11e9-a575-953c92e273b6"})
        return response
        
