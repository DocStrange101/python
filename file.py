from sys import argv

script, filename, newfile = argv

a = filename.read


oldlist = ()

for i in a:
    oldlist.append(i)

def thing (b,c,list):
    newlist = ()

    b = raw_input ("enter a number")
    c = raw_input ("enter a letter")

    for i in a:
        if i[0] == c and len(i) == b:
            newlist.append(i)
    return newlist

thing1 = thing(b,c,oldlist)

thing1.write(newfile)
