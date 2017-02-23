from sys import argv

script, filename = argv

thing = open(filename, 'w')

div3 = []

for i in range(0,1000):
    if i%6 == 0:
        div3.append(i)

div3 = str(div3)

thing.write(div3)
