phrase1 = "University of Klagenfurt"
#concatination of strings
print(phrase1 + " is awesome")

phrase2 = "University of Klagenfurt"
#make them all lower function
print(phrase2.lower())

phrase3 = "University of Klagenfurt"
#make them all upper function
print(phrase3.upper())

phrase4 = "University of Klagenfurt"
#ask if every letter is upper
print(phrase4.isupper())

phrase5 = "University of Klagenfurt"
#ask if every letter is lower
print(phrase5.islower())

phrase6 = "University of Klagenfurt"
#combine two functions
print(phrase6.upper().isupper())

phrase7 = "University of Klagenfurt"
#get the lenght of the string
print(len(phrase7))

phrase8 = "University of Klagenfurt"
#get an individual character from the string
print(phrase8[0])
print(phrase8[3])

phrase9 = "University of Klagenfurt"
#get the index of string i want
print(phrase8.index("v"))
print(phrase8.index("U"))
print(phrase8.index("Klag"))

phrase10 = "University of Klagenfurt"
#replace something from the string 
print(phrase10.replace("Klagenfurt","Thessaloniki"))