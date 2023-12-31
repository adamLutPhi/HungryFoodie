#Hungry foodie

# Dinner
# ---------

## 1. Tofu

## 2. Rice

## 3. Veggies ^_^

import enum

"""

## Rice


---
## Technique

The functionality or the Way we `Cook` it

Estimated time: 5 minutes
---

### How

1.
- Measure the amount of rice required:

0.5 cups [default]

2.

- measure the amoutn of Water requied:
1 cup [default]

-3.
-1/2 cup per person (

Rice Interval
[ 1/2 , 3/4 ] [unoptimized]

Optimal point: in between [assuming naive drawing, and a gaussian normal
'bell-curve' distribution]



Ratio:

- a =  (1.5) water to
-- b =  1 rice

 a / b 


"""

a = 1
b = 1.5
#we're Interested in the ratio
abRatio = 0.66666 # a/b = 1 / 1.5

print( "a /b = ", abRatio)

# Rice
## #Rice Type
riceType = ["Basmati", "Jasmine" ] 
riceCupSize= [ 0, 1/2 , 3/4, 1 ] #[unoptimized]


""" varieties selected for characteristics such as texture, smell, and firmness.

"""
exceptionMsg = "Execption: please recheck input, then retry"
# Level 1 Information

## rice by color
            
uncookedRiceType =[ "white", "red", "brown" , "japanese", "black"  ]

##rice size

riceSize = ["short" , "medium" , "long"]

#level 2 Information:
charactersticRice = ["Aromatic" , "Glutinous" , "Basmati", "Jasmine"]

#level 3 Information
"""Calrose has a sweet and subtle aroma and flavor.
developed from the Indian Basmati rice,
Wehani is nutty and slightly chewy,
and has aroma of hot penuts
infused with it """
CalifornianRiceList = [ "Calrose", "Wehani"]

CookedRiceList =     \
[ "Arroz Con Pollo" ,
"Asopao",
"Biryani",
"Boiled Rice",
"Champorado", "Congee",
"Gimbap",
"Gumbo",
"Kabsa",
"Lamprais",
"Paella",
"Pilaf",
"Puto",
"Risotto",
"Spanish Rice",
"Tahchin",
"Tuwon Shinkafa",
"Yellow Rice" ]

Lambda = lambda k , A,  t1, t2 : - k * A * (max(t1, t2) - min(t1, t2) )/ d

"""rice cooking main stages"""

cookingItem = ["pan", "skillet", "pot"]

class cookingItem(object):
    
    def __init__(self, diameter, volume):

        self.diameter = diameter
        self.volume = volume 
        #pass


    
def heat( k , A, fromDegree : float, toDegree : float ):
    """Heat equation Q=m⋅c⋅delta(T)  Q=m⋅c⋅ΔT
        source: 
        Diameter: the inner diameter
        ( of your stove

        while measuring the induction of heat , it'd better to differentiate between
        The lips of the stovetop (or the cooking surface
        2. and the inner lops of the cooking item [To be measured]
        Attention: size marking might be misleading:
        you can measure the inner lip of the stove top 20 cms (7.87 (taking off 2 cms 
        -taking off 2 cms for more accuracy (18 cms = 7.09 ins)

        heating is done via the Eddy (simulation technique) 

        -Rule of Thumb: taking off 0.5 to get a tghe effective Diameter
Reference:
[1]: College dunia: https://collegedunia.com/exams/heat-transfer-formula-chemistry-articleid-6454
[2]:Serious Eats: https://www.seriouseats.com/equipment-whats-the-difference-between-a-skillet-a-fry-pan-and-a-saute-pan
[3]:PIV Measure of Flow:https://www.researchgate.net/profile/Yasuo-Hattori-2/publication/265915285_PIV_MEASUREMENT_OF_THERMAL_CONVECTIVE_FLOW_ABOVE_A_COOKING_OVEN_INSIGHT_INTO_TURBULENCE_STRUCTURE_NEAR_A_HEAT_SOURCE/links/5bdfa439a6fdcc3a8dbed0b4/PIV-MEASUREMENT-OF-THERMAL-CONVECTIVE-FLOW-ABOVE-A-COOKING-OVEN-INSIGHT-INTO-TURBULENCE-STRUCTURE-NEAR-A-HEAT-SOURCE.pdf

"""    
    return Lambda(k, A, fromDegree, toDegree)
   
def boil(unCookedRiceMass, fromDegree : float, toDegree : float ):
    
    heat(unCookedRiceMass, fromDegree, toDegree)
    
def simmer():

    pass

def steam():
    pass

from enum import Enum
"""Wishful Thinking
cookedRiceType = [ ]          
  
class food:

    def __init__(self, name):
        self.name = name
"""

# Tofu
class Tofu(Enum):
    """Plain tofu has no specific flavor and is honestly, quite bland.-it's a love hate relationship
    """
    value = -1
    
    WhiteTofu = 0
    BlackTofu = 1
    #rice = 1
    #veggies = 2

    def __init__(self, value):

        #Assign values to self instance

        self.WhiteTofu = 0
        self.BlackTofu = 1
        
        try:

            if 0 <=value <=1:
                return self.WhiteTofu
            elif 0 >value >1:
                return self.BlackTofu
            
        except:
            raise Exception(exceptionMsg)
    

from unittest import TestCase

def handlevalue():
    pass
# Temp
class Temp(Enum):
    """
A Temp` temperature class
Inherits from `Enum` object

we have 4 options:
0. frozen
1. roomTemperature
2. warm
3. hot
4. boiling
"""
    # Field Member Attributes (propoerties)
    value = -1

    # enum Temp state from 0 to 4
    
    frozen = 0
    roomTemperature = 1
    warm = 2
    hot = 3
    boiling = 4

    
    def __init__(self, value)-> enum:
        
        self.frozen = 0
        self.roomTemperature = 1
        self.warm = 2
        self.hot = 3
        self.boiling = 4
        try:
            print("checking value ...") 
            if 0 <= value <=4 :
                #Value is corrent
                #How to match int with enum
                print("value is valid")

                print("switch statement)")
                if value==0:
                    return self.frozen
                elif value ==1:
                    return self.roomTemperature
                elif value ==2:
                    return self.warm
                elif value ==3:
                    return self.hot
                elif value == 4:
                    return self.boiling        
                
            elif 0 > value > 4 :
                raise ValueError()
        except: #raises error
            raise Exception()
        
      
#temp =
print("check temp(o)")
res = Temp(0)

print("res = ",res)
print(( Temp.boiling)) 




def show(enm : Enum) -> None:
    for i in enm:
        print(enm[i]+"\t")
        print(type(enm[i])+"\t")
        print(repr(enum[i])+"\t")
    

#https://www.thekitchn.com/whats-the-difference-between-pickling-and-fermenting-229536
# Fermented Food

## fermentedFoodList
fermentedFoodList = [ "sauerkraut", "kimchi", "kombucha", "coconutYogurt", "miso", "tempeh"]


class Fermentation(Enum):
    """AFermentation class 
    inherits from Enum` class
    has (2) modes:
    0. normal
    1. fermented
    
    """
    normal = 0
    fermented = 1

    def __init__(self, value)-> None:
        self.normal =0
        self.fermented = 1
        #assign to self the values, accordingly
        self.normal
        try:

            if 0 <= value <=1 :
                #value is corrent
                #how to match int with enum
                
                #self.value = value value is read only
                print("switch statement)")
                if value==0:
                    self.normal
                elif value ==1:
                    self.fermented
                    
            elif 0 > value > 1 :
                raise ValueError()
        except:
            raise Exception()
Fermentation(0)


class MainDish():
    """ main dish"""
    

sideDishList = ["mac n cheese", "salad", "corn on cobb"]
class SideDish(Enum):# future issues

    #DB: requres: N-f Normalization
    #pass

    macNCheese = 0,
    salad = 1,
    cornNCobb =2
    
class Meal():

    def __init__(self,  sideDish : SideDish ):
    #self.mainDish = mainDish
        self.sideDish = sideDish

    

# A meal combination

#Main meals contain: A Protien Source, Carb, and  side dish
# a meal example:
meal = ["tofu", "rice" , "veggies" ]


veggies = ["spinach", "iceberg", "cabbage" ,"kale", "choy", "seaWeed"]

sauces = ["soySauce", "redHotChilli"]

"""
Ref: Varieties of Types of Lettuce
Source: https://www.epicurious.com/ingredients/varieties-and-types-of-lettuce-article
"""

# Lettuce:  which one:
iceburgLettuceList = ["icebergLettuce","butterheadLettuce", "coralLettuce",
                  "EscaroleLettuce" , "littleGemLettuce", "looseLeafLettuce"]



# Functions / behavior

## Cooking tofu ( protein)

# Relation-of relation: isThaw = lambda frozen, cooked:  ( frozen, cooked) || ( cooked, frozen)


tofuStates = ["raw", "medium", "cooked"] # frozen 

# Lambdas (4)

#1. isRaw
isRaw = lambda strRaw : True if strRaw == "raw" else False

#2. isMedium

isMedium = lambda strMedium: True if strMedium =="medium" else False

#3.isCooked
isCooked = lambda strCooked: True if strCooked == "cooked" else False #"No"

#4. isThaw       
isThaw = lambda isFrozen, cooked:  ( isFrozen or cooked)   #|| (  # ( isFrozen and cooked)   #|| ( cooked and isFrozen)

""" It is wise too cook the tofu
Between medium and cooked ,
As if there is an optimum in between
"""

#field member variables
## set a custom `waitTime` for order 
waitTime = 1

# Allow
#this returns type
#so: return the type of name, bases, attributes
#TODO: allocate dynamically all the names, bases , and Attributes

@classmethod
def dynamicAllocationExperiment(food):
    
    return type(name, bases, attributes)
    
    """dynamically allocate a new object
Classes can be created dynamically using the below syntax:
Syntax:

type(name, bases, attributes) 

Parameters:
name: The user defined name of the class
bases: A list of base classes, and its type is tuple
attributes: the data members and methods contained in the class

"""
    pass

# Class Method with ():


#1. `init` Constructor  function 
def init(self, arg):
    self.init_arg = arg
  
#2. print  method: for display 
def printMethod(self, arg): # object method 
    print(arg)
    
@classmethod
def classMethod(cls, arg): # class method 
    print(arg) # it also displays 
  
# Creating class dynamically

# Set Object Name 
objectName = "Geeks" #

# Set object Type

objectType = (object, ) # type is an `object`


# Let's  builid the following `mixedType`:

# By building a  vector of mixed types

            # type ( objectName, objectConfig

mixedType = type( objectName , objectType , {
    # Constructor
    
    ## __init__ function 
    "__init__":  init, #constructor, # constructor : is a java name for init 
      
    ## (Field variable)  Data members
    "string_attribute": "Food Attribute",
    "int_attribute": 100000,
      
    # member functions

    ## "designated_func_name" :

    ##"func_arg":  objectMethod, # object methods 
    ##"class_func": classMethod  # class methods

})


obj = mixedType("food")

print(obj.init_arg)
print(obj.string_attribute)
print(obj.int_attribute)

#print(obj.func ) #  object has no attribute 'func'

#print( type( food))

class Food:

    def __init__(self):
        pass

    
def freeze(food : Food, waitTime):
    
    """
When a substance changes its state from liquid to solid, the evolution of heat takes place from the body to its surroundings.
https://byjus.com/question-answer/what-is-the-principle-of-freezing/"""
    
    #TODO: return frozen food

    pass
    

def thaw(food, waitTime ):
    """the process of ice, snow, or another frozen substance becoming liquid or soft as a result of warming up.
-Oxford Online 
"""
    # Frozen to Liquid 
    if Temp.frozen:
        Temp.liquid


def main():

    tofu = Tofu()
    
    show(tofu)
if __name__ == "__main__":

    #main()

    tofu = Tofu(1)
    
    #show(tofu)
