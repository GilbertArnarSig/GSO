# Gilbert Arnar Sigurðsson
# 27.01.17
# Git verkefni fyrir GSÖ

f = open("GSO.txt","w+")
f.write("Halló \r\n")
f.close()
f = open("GSO.txt","a+")
for x in range(3):
    f.write("Þetta er lína %d\r\n" % (x+1))
f.close()
f = open("GSO.txt","r+")
skilabod = f.read()
print(skilabod)
f.close()