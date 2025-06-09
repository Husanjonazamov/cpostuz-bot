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
    return response.json()
    
    
    
def getBranch(lang):
    url = f"{BASE_URL}/branch/"
    
    headers = {
        "Accept-Language": lang  
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data['data']
    else:
        return []
    
    
    
def getBranchId(branch_name):
    url = f"{BASE_URL}/branch/{branch_name}/"
    response = requests.get(url)
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
        results = data['data']['results']
        active_categories = [cat for cat in results if cat.get('is_active') == True]
        return active_categories
    else:
        return

    
    
def SearchId(cargo_id):
    url = f"{BASE_URL}/excel-file/me/"
    id = str(cargo_id)
    try:
        response = requests.post(url, json={"id": id}, timeout=10)
        response.raise_for_status()
        data = response.json()
        
        if data and "data" in data and data["data"]: 
            return data
        else:
            return None
    except Exception as e:
        return None



def ExcelCreate(file_obj, file_name):
    url = f"{BASE_URL}/excel/create/"
    files = {
        'file': (file_name, file_obj, 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    }
    try:
        response = requests.post(url, files=files)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return None



def getUserAll():
    url = f"{BASE_URL}/users/"
    
    response = requests.get(url)
    
    return response.json()



def getIdBranch(branch_id):
    url = f"{BASE_URL}/branch/branch-id/{branch_id}/"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return None



def getLocation():
    url = f"{BASE_URL}/location/"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        all_locations = data['data']['results']
        active_locations = [loc for loc in all_locations if loc.get('is_active') is True]
        return active_locations
    else:
        return []
