def allowed_dating_age(my_age):
    g_age = my_age/2.0 + 7
    return g_age

fw = open("sample.txt",'w')
for x in range(25,50):
	fString = "if you are %d you can date a %.2f female \n"%(x,allowed_dating_age(x))
	fw.write(fString)
fw.close()

fr = open("sample.txt",'r')
ftext = fr.read()
print ftext
fr.close()
