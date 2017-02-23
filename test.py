from sys import argv
script, fileName = argv
list1 = []
txt = open(fileName)
for i in txt:
    if i[0] == 'q':
        list1.append(i,rstrip())
print list1


print list2
#print txt.read()
