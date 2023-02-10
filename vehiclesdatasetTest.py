#!/usr/bin/env python
# coding: utf-8

# In[110]:


import unittest


# In[111]:


from Vehicles import numbersInterval,randomCountries,randomLicensePlate,randomVehicleBrand,randomVehicleClassification,randomYearVehicle,randomColor,randomCylinder,randomFuel,randomSwitch,randomService,randomTypeBox,randomOwner,randomAge,randomEmail,randomID,randomPhone,randomIden,randomSurnames,randomEngineSize


# In[112]:


class TestVehiclesdataset(unittest.TestCase):
    
    
    def test_randomNumber(self):
        self.assertIsNotNone(numbersInterval(10,20) , msg=None)
    
    def test_randomCountries(self):
        self.assertIsNotNone(randomCountries(), msg=None)
    
    def test_sizeLicenseplate(self):
        licenseplate = randomLicensePlate()
        self.assertEqual(6,len(licenseplate), msg=None)
    
    def test_numbersinLicenseplate(self):
        numbers = ['0','1','2','3','4','5','6','7','8','9']
        licenseplate = randomLicensePlate()
        licenseplate.split(' ')
        licenseplate_set = set(licenseplate)
        numbers_set = set(numbers)
        self.assertTrue(licenseplate_set & numbers_set)
        
    def test_lettersinLicenseplate(self):
        letters = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        licenseplate = randomLicensePlate()
        licenseplate.split(' ')
        licenseplate_set = set(licenseplate)
        letter_set = set(letters)
        self.assertTrue(licenseplate_set & letter_set)
           
    def test_randomVehicleBrand(self):
        self.assertIsNotNone(randomVehicleBrand(), msg=None)
    
    def test_randomVehicleClassification(self):
        vehicles = ['car','motorbike','bus','lorry','train','tram','underground']
        self.assertIn(randomVehicleClassification(),vehicles)
    
    def test_randomYearVehicle(self):
        self.assertGreater(randomYearVehicle(), 1990)
    
    def test_randomYearVehicle(self):
        self.assertLess(randomYearVehicle(), 2023)
        
    
    def test_randomColor(self):
        self.assertIsNotNone(randomColor(), msg=None)
        
    def test_randomCylinder(self):
        cylinder = [125,150,180,200,250,300,50,500,600,800,80]
        self.assertIn(randomCylinder(),cylinder)
        
    def test_notrandomCylinder(self):
        cylinder = [127,151,184,240,260,380,90,590,690,890,890]
        self.assertNotIn(randomCylinder(),cylinder)
        
    def test_randomFuel(self):
        fuels = ['Gasoline','Diesel','Bio-diesel','hybrid','electric']
        self.assertIn(randomFuel(),fuels)
        
    def test_randomNotFuel(self):
        fuels = ['Gasolines','Dies','Bidiesel','electric']
        self.assertNotIn(randomFuel(),fuels)
        
    def test_randomSwitch(self):
        imported = ['yes','no']
        self.assertIn(randomSwitch(),imported)
        
    def test_randomService(self):
        services = ['Public','Private']
        self.assertIn(randomService(),services)
    
    def test_randomTypeBox(self):
        typeboxes = ['MT','AT','DSG']
        self.assertIn(randomTypeBox(),typeboxes)
        
    def test_randomOwner(self):
        self.assertIsNotNone(randomOwner(), msg=None)
    
    def test_randomAge(self):
         self.assertIsNotNone(randomAge(), msg=None)
    
    def test_ageLess(self):
        self.assertLess(randomAge(), 90)
    
    def test_ageGreater(self):
        self.assertGreater(randomAge(), 18)
    
    def test_randomEmail(self):
        domains = ['oulook.com','gmail.com','hotmail.com']
        email = randomEmail().split('@')
        domains_set = set(domains)
        email_set = set(email)
        self.assertTrue(domains_set & email_set)
    
    def test_randomID(self):
        self.assertIsNotNone(randomID(3), msg=None)
        
    def test_randomIDsize(self):
        id_set = randomID(3)
        self.assertEqual(len(id_set),3)
    
    def test_randomPhone(self):
        phones = randomPhone(2)
        self.assertEqual(len(phones),2)
    
    def test_randomsizePhone(self):
        phones = randomPhone(2)
        self.assertEqual(len(list(phones)[0]),10)
    
    def test_randomIden(self):
        self.assertEqual(len(randomIden(2)),2)
    
    def test_randomIden(self):
        identi= randomIden(2) 
        self.assertEqual(len(list(identi)[0]),10)
        
    def test_randomSurnames(self):
        self.assertIsNotNone(randomSurnames(), msg=None)
    
    def test_randomEngineLess(self):
        self.assertLess(randomEngineSize(), 8.4)
    
    def test_randomEngineGreater(self):
        self.assertGreater(randomEngineSize(), 0.9)
        


# In[113]:


unittest.main(argv=[''], verbosity=2, exit=False)


# In[ ]:





# In[ ]:




