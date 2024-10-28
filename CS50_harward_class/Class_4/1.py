#libraries: a collection of functions and other features
import random #loads the module "random"
print(random.choice(["a", "b"])) #uses function "choice" from random  
         
#do not want to import whole range of functions from the entire module?
from random import choice
#imports the fn "choice into our namespace or scope"
print(choice(("1","2")))

   #choice in random module takes a sequence (list like)