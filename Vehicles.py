# %%
import pandas as pd

# %%

# %%
import random

# %%
def numbersInterval(initial,final):
    """Selecting random ID of information about vehicles
        returns:
            int: random number
        Complexity O(1)
    """
    data = random.randint(initial,final)
    return data

# %%
def randomCountries():
    """Selecting random countries
        returns:
            str: Country random selected
    """
    with open("./TxtFiles/countries.txt", 'r') as myfile:
        txt = myfile.read()
        words = txt.split()
        wordPosition = random.randint(0, len(words)-1)
    return words[wordPosition]

# %%
def randomLicensePlate():
    """
    Generate random License Plate
    returns:
        str: license plate of vehicle
        Complexity O(1)
    """
    letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    number = '0123456789'
    licensePlate = ''.join([random.choice(letters) for i in range(3)]+[random.choice(number) for i in range(3)])
    return licensePlate

# %%
def randomVehicleBrand():
    """
    Generate random vehicle Brand
    return:
        str: band of vehicle
        Complexity O(1)
    """
    with open("./TxtFiles/car'sBands.txt", 'r') as carsfile:
        band_car = carsfile.read()
        bands = band_car.split()
        bandPosition = random.randint(0, len(bands)-1)
    return bands[bandPosition]

# %%
def randomVehicleClassification():
    """
    Generate random Classification of vehicle
    return:
        str: vehicle category
        Complexity O(1)
    """
    vehicles = ['car','motorbike','bus','lorry','train','tram','underground']
    vehiclesposition = random.randint(0, len(vehicles)-1)
    return vehicles[vehiclesposition]

# %%
def randomYearVehicle():
    """
    Generate random year of model vehicle
    return:
        int: model year of car
        Complexity O(1)
    """
    year = random.randint(1990,2023)
    return year

# %%
def randomColor():
    """
    Generate random color vehicle
    return:
        str: color of car
        Complexity O(1)
    """
    with open("./TxtFiles/colors.txt", 'r') as colorfile:
        color_file = colorfile.read()
        colors = color_file.split()
        colorPosition = random.randint(0, len(colors)-1)
    return colors[colorPosition]

# %%
def randomCylinder():
    """
    Generate random color vehicle
    return:
        int: value of cylinder capacity
        Complexity O(1)
    """
    cylinder = [125,150,180,200,250,300,50,500,600,800,80]
    cylinderPosition = random.randint(0, len(cylinder)-1)
    return cylinder[cylinderPosition]

# %%
def randomFuel():
    """
    Generate fuel type of the vehicle
    return:
        str: fuel type
        Complexity O(1)
    """
    fuels = ['Gasoline','Diesel','Bio-diesel','hybrid','electric']
    fuelPosition = random.randint(0, len(fuels)-1)
    return fuels[fuelPosition]

# %%
def randomSwitch():
    """
    Generate value if the vehicle is imported 
    return:
        str: yes or not the vehicles is imported
        Complexity O(1)
    """
    switch = ['yes','no']
    binary = random.randint(0, len(switch)-1)
    return switch[binary]

# %%
def randomService():
    """
    Generate value of service type
    return:
        str: service type between public or private
        Complexity O(1)
    """
    services = ['Public','Private']
    service = random.randint(0, len(services)-1)
    return services[service]

# %%
def randomTypeBox():
    """
        Generate Gearbox type of vehicle
        return:
            str: Gearbox type
            Complexity O(1)
    """
    typeboxes = ['MT','AT','DSG']
    typebox = random.randint(0, len(typeboxes)-1)
    return typeboxes[typebox]

# %%
def randomOwner():
    """
        Generate number of owner from names file
        return:
            str: owner name of vehicle
    """
    with open("./TxtFiles/names.txt", 'r') as namesfile:
        readnames = namesfile.read()
        names = readnames.split()
        namesPosition = random.randint(0, len(names)-1)
    return names[namesPosition]

# %%
def randomAge():
    """
        Generate age of owner
        return:
            int: age of owner from 18 to 90
            Complexity O(1)
    """
    return random.randint(18,90)

# %%
def randomEmail():
    """
        Generate owner's email
        return:
            str: owner's email
            Complexity O(1)
    """
    num = randomAge()
    name = randomOwner()
    domains = ['oulook.com','gmail.com','hotmail.com']
    domainPosition = random.randint(0, len(domains)-1)
    return name + str(num) + '@' + domains[domainPosition]

# %%
def randomID(size):
    """
        Generate ID of dataset
        args:
            number of dataset rows
        return:
            set: row identification of vehicle dataset
            Complexity O(n)
    """
    minValue = 0;
    maxValue = size;
    setId = set()
    if(maxValue -(minValue + 1) > size):
        return "error is not validate intervals"
    elif(maxValue - (minValue + 1) == size):
        setId.add(maxValue);
        setId.add(minValue);
    elif(minValue > maxValue):
        return "error maxValue is less than minValue"  
    while(len(setId) != size):
        setId.add(numbersInterval(minValue,maxValue))
    return setId

# %%
def randomPhone(size):
    """
        Generate owner's phone
        args:
            number of dataset rows
        return:
            set: numbers of each owner of the dataset
        Complexity O(n)
    """
    minValue = 0
    maxValue = 10;
    phone = []
    setId = set()
    while(len(setId) != size):
        for i in range(10):
            phone.append(numbersInterval(minValue,maxValue))
            phone[0] = 3
        phones = ''.join(map(str,phone))
        setId.add(phones)
        phone.clear()
    return setId

# %%
def randomIden(size):
    """
        Generate owner's ID
        args:
            number of dataset rows
        return:
            set: identification of each owner of the dataset
         Complexity O(n)
    """
    minValue = 0
    maxValue = 10;
    identCard = []
    setIdent = set()
    while(len(setIdent) != size):
        for i in range(10):
            identCard.append(numbersInterval(minValue,maxValue))
        idenCards = ''.join(map(str,identCard))
        setIdent.add(idenCards)
        identCard.clear()
    return setIdent

# %%
def randomSurnames():
    """
    Generate random surnames of owner
    return:
        str: last name of the owner
         Complexity O(n)
    """
    with open("./TxtFiles/surnames.txt",'r') as surnamefile:
        surname_txt = surnamefile.read()
        surnames = surname_txt.split()
        lastname = random.randint(0, len(surnames)-1)
    return surnames[lastname]. lower()

# %%
def randomEngineSize():
    """
        Generate engine power size 
        return:
            set: engine power of vehicle
         Complexity O(1)
    """
    return round(random.uniform(0.9,8.4), 1)

# %%
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

# %%
def main():
    amount = int(input('put the amount of data: '))
    return generateData(amount)

# %%
main()

# %%


# %%



