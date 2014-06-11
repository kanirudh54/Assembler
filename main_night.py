import os

var1=1
name=raw_input('Enter your name : ')
print ("Hi %s, Let us start." % name);

print " Enter your choice of options"
print "type 1 for assembling file"
print "type 2 for linking files"
print "type 3 for loading files"
print "type 4 to exit"
choice=raw_input('Enter your choice:')
#print ("%s dsf" % choice);
#choice = 1#ji=raw_input()
while choice!='4':
	if choice == '1':
		file1 =raw_input ('Enter file Name:')
		os.system("python convert.py " +file1)
		os.system("python pass1.py " +file1+ "_8085")
		os.system("python pass2.py " +file1+ "_8085")
	elif choice =='2':
		number_of_files=raw_input('how many files you want to link:')
		link_files=[]
		string1=""
		for x in range (0,int(number_of_files)):
			tempname=raw_input(''+str(x)+' file name :')
			link_files.append(tempname)
			string1=string1+" "+tempname
		os.system("python linker.py " + string1 )
	elif choice=='3':
		number_of_files=raw_input('how many files you want to load:')
		link_files=[]
		string1=""
		print "type the file name followed by the address where it should be loaded"
		for x in range (0,int(number_of_files)):
			tempname=raw_input(''+str(x)+' file name: ')
			tempname2=raw_input(''+str(x)+' address :')
			link_files.append(tempname)
			link_files.append(tempname2)
			string1=string1+" "+tempname + " " +tempname2
		os.system("python loader.py " + string1 )


	choice=raw_input('Enter your choice:')
