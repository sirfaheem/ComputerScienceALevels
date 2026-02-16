import csv
# Read a basic CSV file
f = open("csmod.csv","r")
for r in csv.reader(f):
    lastname, firstname, street, city, zip = r
    print("{0} {1} {2} {3} {4}".format(*r))
# Using a DictReader instead
f = open("csmod.csv")
r = csv.DictReader(f,['lastname','firstname','street','city','zip'])
for a in r:
    print("{firstname} {lastname} {street} {city} {zip}".format(**a))
# Write a basic CSV file
data = [
['Blues','Elwood','1060 W Addison','Chicago','IL','60613' ],
['McGurn','Jack','4802 N Broadway','Chicago','IL','60640' ],
]
f = open("csmod.csv","w")
w = csv.writer(f)
w.writerows(data)
f.close()
