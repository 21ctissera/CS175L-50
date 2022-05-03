#Chrishen Tissera
#Restaurant Program 

veggie=input("Is there someone in your party that is a vegetarian? ")
vegan=input("Is there someone in your party that is a vegan? ")
g_f=input("Is there someone in your party that is gluten-free? ")

print("Here are your restaurant choices:")
if vegan=="yes" and g_f=="yes" and veggie=="yes":
    print("Corner Cafe")
    print("The Chef's Kitchen")

elif g_f=="no" and vegan=="yes" and veggie=="yes":
    print("Corner Cafe")
    print("The Chef's Kitchen")
 
elif veggie=="no" and g_f=="yes" and vegan=="no":
    print("Corner Cafe")
    print("The Chef's Kitchen")

elif g_f=="yes" and vegan=="no" and veggie=="no":
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")

elif vegan=="no" and veggie=="yes" and g_f=="yes":
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("The Chef's Kitchen")

elif veggie=="yes" and veggie=="no" and g_f=="no":
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")

elif vegan=="yes" and veggie=="no" and gluten_free=="no":
    print("Corner Cafe")
    print("The Chef's Kitchen")

else:
    print("Joe's Gourmet Burgers")
    print("Main Street Pizza Company")
    print("Corner Cafe")
    print("Mama's Fine Italian")
    print("The Chef's Kitchen")   
