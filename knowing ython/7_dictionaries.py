monthConversions = {
    # every key must be unique
    # key  :  value
     "Jan" : "January",
     "Feb" : "Febuary",
     "Mar" : "March",
     "Apr" : "April",
     "May" : "May",
     "Jun" : "June",
     "Jul" : "July",
     "Aug" : "August",
     "Sep" : "September",
     "Oct" : "October",
     "Nov" : "November",
     "Dec" : "December"
 }

# access to the dictionary
print(monthConversions["Feb"])

# access by method get
print(monthConversions.get("Jun")) 

# throw an error if you search for a key that does not exist
print(monthConversions.get("Luv", "Not exists in the dictionary. Check again")) 