import re

f1 = open('maininp.txt', 'r')
f2 = open('inter.txt',  'w')
f3 = open('inter2.txt', 'w')


comment = re.compile(';')
emp = re.compile('\S')
for line in f1:
	m = comment.search(line)
	if m:
		for char in line:
			if char==";":
				f2.write('\n')
				break
			else:
				if char == ",":

					f2.write(" ")
				else:
					f2.write(char)
				
				

	else:
		for char in line:
			if char == ",":

				f2.write(" ")
			else:
				f2.write(char)
		
f2.close()
f2 = open('inter.txt',  'r')
reg = ['b', 'B', 'c', 'C', 'D', 'd', 'e', 'E']
acc = ['A', 'a']

#jump = re.compile('[Jj][Mm][Pp]')

for line in f2:
	i=0
	if not(emp.search(line)):
		continue
	words=line.split()
	#print len(words)
	#for i in range(0, len(words)):
	#print words[i]
	if words[0][len(words[0])-1]==':':
                #print "hello"
		f3.write(words[i] + " ")
		i=i+1
	if words[i].lower()=='jmp':
		f3.write('jmp ')
		i=i+1
		if len(words)==(i+1):
			f3.write(words[i])
			f3.write("\n")
		else:
			print "Error - JMP"
	elif words[i].lower()=='db':
		f3.write("db ")
		for x in range(2, len(words)-1):
			f3.write(words[x]+", ")
		
		f3.write(words[(len(words)-1)])
		f3.write("\n")

	elif words[i].lower()=='equ':
		f3.write("equ ")
		if len(words)==(i+2):
			f3.write(words[i+1])
			f3.write("\n")
		else:
			print "Error - EQU"

	elif words[i].lower()=='ds':
		f3.write("ds ")
		if len(words)==(i+2):
			f3.write(words[i+1])
			f3.write("\n")
		else:
			print "Error - DS"

	elif words[i].lower()=='nop':
		f3.write('nop ')
		i=i+1
		if len(words)==(i):
			f3.write("\n")

		else:
			print "Error - NOP"

	elif words[i].lower()=='mov':
		
		
		if len(words)==(i+3):

			if words[i+1] in reg or words[i+1] in acc:
				if words[i+2].isdigit():
					f3.write("mvi " + words[i+1] + ", " + words[i+2])

					f3.write("\n")
				elif words[i+2] in reg or words[i+2] in acc:
					f3.write("mov " + words[i+1] + ", " + words[i+2])
					f3.write("\n")

				else:
					f3.write("lxi h, " + words[i+2] + "\n")
					f3.write("mov " + words[i+1]+ ", m\n")

			else:
				if words[i+2].isdigit():
					f3.write("sta temp\n")
					f3.write("mvi A, "+ words[i+2] +"\nsta " + words[i+1] + "\n")
					f3.write("lda temp\n")

					
				elif words[i+2] in reg or words[i+2] in acc:
					f3.write("sta temp" + "\nmov  A, " + words[i+2] +"\nsta " + words[i+1] + "\n")
					f3.write("lda temp\n")

				else:
					f3.write("sta temp\n")
					f3.write("lxi h,  " + words[i+2] + "\n")
					f3.write("mov A, m\n")
					f3.write("sta " + words[i+1] + "\n")
					f3.write("lda temp\n")


		else:
			print "Error - MOV"

	elif words[i].lower()=='add':
		
		
		if len(words)==(i+3):
			
			if words[i+1] in reg:

				f3.write("sta temp\n" +"mvi A, 0\n"+ "add " + words[i+1] + "\n")

				if words[i+2].isdigit():
					f3.write("adi " + words[i+2])
					f3.write("\n")
					
				else:
					if words[i+2] in reg:	
						f3.write("add " + words[i+2])
						f3.write("\n")

					else:
						f3.write("lxi h, " + words[i+2]+ "\nadd m")
						f3.write("\n")

				f3.write("mov " + words[i+1] + " , A\n" + "lda temp\n")

			elif words[i+1] in acc:
				if words[i+2].isdigit():
					f3.write("adi " + words[i+2])
					f3.write("\n")
					
				else:
					if words[i+2] in reg:	
						f3.write("add " + words[i+2])
						f3.write("\n")

					else:
						f3.write("lxi h, " + words[i+2]+ "\nadd m")
						f3.write("\n")

			else:
				f3.write("sta temp\n" +"mvi A, 0\n" + "lxi h, " + words[i+1] + "\n" + "add m\n")
				if words[i+2].isdigit():
					f3.write("adi " + words[i+2])
					f3.write("\n")
					
				else:
					if words[i+2] in reg:	
						f3.write("add " + words[i+2])
						f3.write("\n")

					else:
						f3.write("lxi h, " + words[i+2]+ "\nadd m")
						f3.write("\n")

				f3.write("sta " + words[i+1] + "\nlda temp\n")







		else:
			print "Error - ADD"



	elif words[i].lower()=='sub':
		
		
		if len(words)==(i+3):
			
			if words[i+1] in reg:

				f3.write("sta temp\n" +"mvi A, 0\n"+ "add " + words[i+1] + "\n")

				if words[i+2].isdigit():
					f3.write("sui " + words[i+2])
					f3.write("\n")
					
				else:
					if words[i+2] in reg:	
						f3.write("sub " + words[i+2])
						f3.write("\n")

					else:
						f3.write("lxi h, " + words[i+2]+ "\nsub m")
						f3.write("\n")

				f3.write("mov " + words[i+1] + " , A\n" + "lda temp\n")

			elif words[i+1] in acc:
				if words[i+2].isdigit():
					f3.write("sui " + words[i+2])
					f3.write("\n")
					
				else:
					if words[i+2] in reg:	
						f3.write("sui " + words[i+2])
						f3.write("\n")

					else:
						f3.write("lxi h, " + words[i+2]+ "\nsub m")
						f3.write("\n")

			else:
				f3.write("sta temp\n" +"mvi A, 0\n" + "lxi h, " + words[i+1] + "\n" + "add m\n")
				if words[i+2].isdigit():
					f3.write("sui " + words[i+2])
					f3.write("\n")
					
				else:
					if words[i+2] in reg:	
						f3.write("sub " + words[i+2])
						f3.write("\n")

					else:
						f3.write("lxi h, " + words[i+2]+ "\nsub m")
						f3.write("\n")

				f3.write("sta " + words[i+1] + "\nlda temp\n")







		else:
			print "Error - SUB"



	elif words[i].lower()=='hlt':
		f3.write('hlt ')
		i=i+1
		if len(words)==(i):
			f3.write("\n")

		else:
			print "Error - HLT"


f3.write("temp: db 0")




