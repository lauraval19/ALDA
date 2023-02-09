#!/usr/bin/env python
# coding: utf-8

# In[23]:


import pandas as pd


# In[24]:


import numpy as np


# In[25]:


import random


# In[26]:


def numbersInterval(initial,final):
    """Selecting random ID of information about vehicles
        returns:
            int: random number
    """
    data = np.random.randint(initial,final)
    return data


# In[27]:


def randomCountries():
    """Selecting random countries
        returns:
            str: Country random selected
    """
    myfile = open("countries.txt")
    txt = myfile.read()
    words = txt.split()
    word_position = random.randint(0, len(words)-1)
    return words[word_position]


# In[28]:


def randomLicensePlate():
    """
    Generate random License Plate
    returns:
        str: license plate of vehicle
    """
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    license_plate = ''.join([random.choice(letters) for i in range(3)]+[random.choice(number) for i in range(3)])
    return license_plate


# In[29]:


def randomVehicleBrand():
    """
    Generate random vehicle Brand
    return:
        str: band of vehicle
    """
    myfile = open("car'sBands.txt")
    txt = myfile.read()
    bands = txt.split()
    band_position = random.randint(0, len(bands)-1)
    return bands[band_position]


# In[30]:


def randomVehicleClassification():
    """
    Generate random Classification of vehicle
    return:
        str: vehicle category
    """
    vehicles = ['car','motorbike','bus','lorry','train','tram','underground']
    vehicles_position = random.randint(0, len(vehicles)-1)
    return vehicles[vehicles_position]


# In[31]:


def randomYearVehicle():
    """
    Generate random year of model vehicle
    return:
        int: model year of car
    """
    year = np.random.randint(1990,2023)
    return year


# In[32]:


def randomColor():
    """
    Generate random color vehicle
    return:
        str: color of car
    """
    myfile = open("colors.txt")
    txt = myfile.read()
    colors = txt.split()
    color_position = random.randint(0, len(colors)-1)
    return colors[color_position]


# In[33]:


def randomCylinder():
    """
    Generate random color vehicle
    return:
        int: value of cylinder capacity
    """
    cylinder = [125,150,180,200,250,300,50,500,600,800,80]
    cylinder_position = random.randint(0, len(cylinder)-1)
    return cylinder[cylinder_position]


# In[34]:


def randomFuel():
     """
    Generate fuel type of the vehicle
    return:
        str: fuel type
    """
    fuels = ['Gasoline','Diesel','Bio-diesel','hybrid','electric']
    fuelposition = random.randint(0, len(fuels)-1)
    return fuels[fuelposition]


# In[35]:


def randomSwitch():
     """
    Generate value if the vehicle is imported 
    return:
        str: yes or not the vehicles is imported
    """
    switch = ['yes','no']
    binary = random.randint(0, len(switch)-1)
    return switch[binary]


# In[36]:


def randomService():
    """
    Generate value of service type
    return:
        str: service type between public or private
    """
    services = ['Public','Private']
    service = random.randint(0, len(services)-1)
    return services[service]


# In[37]:


def randomTypeBox():
    """
        Generate Gearbox type of vehicle
        return:
            str: Gearbox type
    """
    typeboxes = ['MT','AT','DSG']
    typebox = random.randint(0, len(typeboxes)-1)
    return typeboxes[typebox]


# In[38]:


def randomOwner():
    """
        Generate number of owner from names file
        return:
            str: owner name of vehicle
    """
    namesfile = open("names.txt")
    readnames = namesfile.read()
    names = readnames.split()
    names_position = random.randint(0, len(names)-1)
    return names[names_position]


# In[39]:


def randomAge():
    """
        Generate age of owner
        return:
            int: age of owner from 18 to 90
    """
    return random.randint(18,90)


# In[40]:


def randomEmail():
    """
        Generate owner's email
        return:
            str: owner's email
    """
    num = randomAge()
    name = randomOwner()
    domains = ['oulook.com','gmail.com','hotmail.com']
    domain_position = random.randint(0, len(domains)-1)
    return name + str(num) + '@' + domains[domain_position]


# In[103]:


def randomID(size):
    """
        Generate ID of dataset
        args:
            number of dataset rows
        return:
            set: row identification of vehicle dataset
    """
    minValue = 0;
    maxValue = size;
    set_id = set()
    if(maxValue -(minValue + 1) > size):
        return "error is not validate intervals"
    elif(maxValue - (minValue + 1) == size):
        set_id.add(maxValue);
        set_id.add(minValue);
    elif(minValue > maxValue):
        return "error maxValue is less than minValue"  
    while(len(set_id) != size):
        set_id.add(numbersInterval(minValue,maxValue))
    return set_id


# In[183]:


def randomPhone(size):
    """
        Generate owner's phone
        args:
            number of dataset rows
        return:
            set: numbers of each owner of the dataset
    """
    minValue = 0
    maxValue = 10;
    phone = []
    set_id = set()
    while(len(set_id) != size):
        for i in range(10):
            phone.append(numbersInterval(minValue,maxValue))
            phone[0] = 3
        phones = ''.join(map(str,phone))
        set_id.add(phones)
        phone.clear()
    return set_id


# In[206]:


def randomIden(size):
    """
        Generate owner's ID
        args:
            number of dataset rows
        return:
            set: identification of each owner of the dataset
    """
    minValue = 0
    maxValue = 10;
    ident_card = []
    set_ident = set()
    while(len(set_ident) != size):
        for i in range(10):
            ident_card.append(numbersInterval(minValue,maxValue))
        iden_cards = ''.join(map(str,ident_card))
        set_ident.add(iden_cards)
        ident_card.clear()
    return set_ident


# In[223]:


def randomSurnames():
    """
    Generate random surnames of owner
    return:
        str: last name of the owner
    """
    myfile = open("surnames.txt")
    txt = myfile.read()
    surnames = txt.split()
    lastname = random.randint(0, len(surnames)-1)
    return surnames[lastname]. lower()


# In[231]:


def randomEngineSize():
    """
        Generate engine power size 
        return:
            set: engine power of vehicle
    """
    return round(random.uniform(0.9,8.4), 1)


# In[237]:


def generateData(cant):
    """
        Create dataset with library pandas
        return:
            vehicle dataset
    """
    df = pd.DataFrame(columns=['Country','License Plate','Vehicle Brand','Vehicle Classification','Year Vehicle','Color','CylinderCapacity (cc)','Fuel type','Imported',
                          'Service','Engine power (Kw)','Engine Size (L)','Gearbox type','Owner name','owner last name','Owner age','Owner' +"'s"+" email"])
    for i in range(cant):
        df.loc[len(df.index)] = [randomCountries(),randomLicensePlate(),randomVehicleBrand(),randomVehicleClassification(),randomYearVehicle(),randomColor(),randomCylinder(),randomFuel(),randomSwitch(),randomService(),numbersInterval(100,200),randomEngineSize(),randomTypeBox(),randomOwner(),randomSurnames(),randomAge(),randomEmail()] 
    df.insert(0,'ID',list(randomID(cant)))
    df.insert(15,'Owner' +"'s"+" phone",list(randomPhone(cant)))
    df.insert(13,'Owner' +"'s"+" ID",list(randomIden(cant)))
    return df


# In[239]:


def main():
    amount = int(input('put the amount of data: '))
    return generateData(amount)


# In[240]:


main()


# In[ ]:





# In[ ]:




