# Educational test file
import sys
#
class __Dog:
    # Class attribute
    #species = 'Canis familiaris'
    #
    def __init__(self,number:int,name:str,age:int,species:str='Canis familiaris'):
        self.number = number
        self.species = species
        self.name = name
        self.age = age
    
    # Private is 2 underscore protected is one     
    def get_dog_attributes(self,number:int,name:str,age:int,species:str):
        plist=[]
        for each in self:
            plist.append(each.number,each.name,each.age,each.species)
            
    def set_attributes(self,number:int,name:str,age:int,species:str) -> bool:
        try:
            Dog(number,name,age,species)
        except Exception as e:
            raise e
            return False
        else:
            return True
        
   #    return plist
        
        
#dog1=Dog(123,"Golden Retriewer","Lassie",5)
#dog2=Dog(123,"Rotweiler","Fist",4)

#print(dog1.number,dog1.species,dog1.name,dog1.age)
#print(dog2.number,dog2.species,dog2.name,dog2.age)


