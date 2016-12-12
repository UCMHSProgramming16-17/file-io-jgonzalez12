#make a file to write in
file = open('makelist1.py', 'w')

# set the beginning of the loop
x = 1
while x <= 10:
    #make what you're going to write into that file 
    file.write(str(x) + ' ' + input("Give me an item. ") + '\n')    
    #loop it until you hit 10 items
    x += 1
    
file.close()