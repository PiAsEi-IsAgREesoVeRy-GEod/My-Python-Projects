#Subprogram 
# Procedure
def Mother():
    print("The strongest person I know.")
    print("Loves her children.")
    print("Lovely and gorgeous.")
# Call my subprogram
Mother()
# Function
def average(a,b):
    return (a+b) / 2
print (average (4,6))
# Procedure (Activity 1)
def places():
    print("You should visit the West Baray.")
    print("Koulen Mountain should be on your bucket list.")
    print("You should visit Koh Rong Island during the dry season.")
places()
# Function (Activity 1)
def increase(l,r):
        return (l*r/100)
print (increase (45,67))
# Function (Activity 2) Subprogram
import random
def outfit():
    Clothes = ["A sweather.","Thermal leggings.","A flannel pajamas.","A jacket."]
    return(random.choice(Clothes))
# Main program
question = input("Is it cold today? ")
if question == "Yes":
     print("How about...", outfit())
else:
     print("You don't have to wear these clothes today.")
        
