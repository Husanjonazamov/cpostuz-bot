# services.py fayli
import requests
from utils.env import BASE_URL



def createUser(user):
    url = f"{BASE_URL}/users/"
    response = requests.post(url, json=user)
    
    if response.status_code == 201:
        data = response.json()
        return data
    else:
        return 

    
def getUser(user_id):
    url = f"{BASE_URL}/users/{user_id}/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return
    
    

def putUser(user_id, user):
    url = f"{BASE_URL}/users/update/{user_id}/"
    
    response = requests.patch(url, json=user)  
    print("-dsadsa")
    return response.json()
    
    
    
def getBranch(lang):
    url = f"{BASE_URL}/branch/"
    
    headers = {
        "Accept-Language": lang  
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data["data"]['results']
    else:
        return []
    
    
    
def getBranchId(branch_name):
    url = f"{BASE_URL}/branch/{branch_name}/"
    response = requests.get(url)
    print(response.status_code)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return []
    
    
def getCategory(lang):
    url = f"{BASE_URL}/category/"
    
    headers = {
        "Accept-Language": lang  
    }

    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        data = response.json()
        return data['data']['results']
    else:
        return