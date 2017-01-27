# Gilbert Arnar Sigurðsson
# 27.01.17
# Git verkefni fyrir GSÖ

f = open("GSO.txt","w+") # notað til að búa til texta skrá
f.write("Halló \r\n") # Notað til að skrifa í texta skrána
f.close() # Lokar texta skráni
f = open("GSO.txt","a+") # Opnar texta skrána til að bæta inní hana
for x in range(3): # For lykkja til að prenta þrjár línur
    f.write("Þetta er lína %d\r\n" % (x+1)) # Skrifar inní texta skrána
f.close() # lokar texta skráni
f = open("GSO.txt","r+") # opnar texta skrána til að lesa úr henni
skilabod = f.read() # breyta til þess að prenta út textan
print(skilabod) # byrtir innihald skránar
f.close() # Lokar skráni