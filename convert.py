import re
import sys
input_files=[]
input_files=sys.argv
input_files.pop(0)
for infile in input_files:

	f1 = open(infile, 'r')
	f3 = open(infile+'_8085', 'w')
f2 = open('inter.txt',  'w')

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
				if char == "," :

					f2.write(" ")
				else:
					f2.write(char)
				
				

	else:
		words=[]
		words=line.split()
		for char in line:

			if char == "," and words[0]!='global' :

				f2.write(" ")
			else:
				f2.write(char)
		
f2.close()
f2 = open('inter.txt',  'r')
fmac=open('inter.txt',  'r')
f4 = open('isetsame.txt', 'r')
isetsame_dict={}
isetsame_list=[]
for line in f4:
	word1, word2 = line.split()
	isetsame_list.append(word1)
	isetsame_dict[word1]=int(word2)

f4.close()


f4 = open('isetpd.txt', 'r')
isetpd_dict={}
isetpd_list=[]
for line in f4:
	word1, word2 = line.split()
	isetpd_list.append(word1)
	isetpd_dict[word1]=int(word2)


f4.close()
reg = ['b', 'B', 'c', 'C', 'D', 'd', 'e', 'E']
acc = ['A', 'a']
equvar=[]
var=[]
pdfile = open('isetpredef.txt', 'r')

flag=0

arg_dict={}
mac_dict={}
mac_list=[]
arg_dict['regd']=''
arg_dict['regs']=''
arg_dict['vard']=''
arg_dict['vars']=''
arg_dict['num']=''
temp=[]
arg=['regd', 'regs', 'vard', 'vars', 'num']

macflag=0

for line in f2:
	i=0
	if not(emp.search(line)):
		continue
	words=line.split()
	if len(words)>2 :
		if words[1]=='equ':
			temp=re.findall(r"[\w']+|[:,.]", words[0])
				
			equvar.append(temp[0])






f2.seek(0)
for line in f2:
	i=0
	if not(emp.search(line)):
		continue
	words=line.split()

	if words[0].lower()=='macro':
		macflag=1

	if words[0].lower()=='end':
		macflag=0

	if macflag==1:
		continue

	if words[0].lower()=='global' or words[0].lower()=='extern':
		f3.write(line)
		f3.write("\n")
		continue


	if words[0][len(words[0])-1]==':':
  		#print "hello"
		f3.write(words[i] + " ")
		i=1

		if words[1].lower()=='equ':
			f3.write("equ ")
			if len(words)==(3):
				f3.write(words[2])
				
				f3.write("\n")
			else:
				print "Error - EQU"

		elif words[1].lower()=='ds':
			f3.write("ds ")
			if len(words)==(3):
				f3.write(words[2])
				var.append(words[0])
				f3.write("\n")
			else:
				print "Error - DS"

		elif words[1].lower()=='db':
			f3.write("db ")
			var.append(words[0])
			for x in range(2, len(words)-1):
				f3.write(words[x]+", ")
			
			f3.write(words[(len(words)-1)])
			f3.write("\n")

	#print equvar

	if len(words)==i:
		print "Error - Missing instruction/declaration after " + words[i-1]
		break;


	if (words[i].lower()) in isetsame_list:
		
		#print words[i]
		
		
		if len(words)==(isetsame_dict[words[i].lower()]+i+1):
			f3.write(words[i] + " ")
			if len(words)>(i+1):
				f3.write(words[i+1])
				for x in range(i+2, len(words)):
					f3.write(", " + words[x])
			f3.write("\n")

		else:
			print "Error - Missing operand after " + words[i]
			break

	
	elif (words[i].lower()) in isetpd_list:

		pdins=''
		if len(words)==(isetpd_dict[words[i].lower()]+i+1):
			pdins=words[i].lower()
			#print pdins
			for x in range (i+1, len(words)):
				if words[x] in reg:
					pdins = pdins + 'reg'
					if x==i+1:
						arg_dict['regd']=words[x]
					else:
						arg_dict['regs']=words[x]

				elif words[x] in acc:
					pdins = pdins + 'acc'
					if x==i+1:
						arg_dict['regd']=words[x]
					else:
						arg_dict['regs']=words[x]

				elif words[x] in equvar or words[x].isdigit():
					pdins = pdins + 'num'
					arg_dict['num']=words[x]
				else:
					pdins = pdins + 'var'
					if x==i+1:
						arg_dict['vard']=words[x]
					else:
						arg_dict['vars']=words[x]
				

			
			pdfile.seek(0)
			for line in pdfile:
				if not(emp.search(line)):
					continue
				words=line.split()
				

				if flag==1:
					if(words[0]!='end'):


						f3.write(words[0]+ ' ')
						if words[1] in arg:
							f3.write(arg_dict[words[1]] )
						else:
							f3.write(words[1])
						if len(words)>i+2:

							if words[2] in arg:
								f3.write(", " + arg_dict[words[2]])
							else:
								f3.write(", " + words[2])

						f3.write("\n")

					else:
						flag = 0
						


					
				if words[0]=='pdef' and words[1]==pdins:
					flag=1	

			
		else:
			print "Error - Missing operand after " + words[i]
			break

	else:
		mac_dict={}
		mac_list=[]
		fmac.seek(0)
		flag2=0
		i=0
		for line in fmac:
			if not(emp.search(line)):
				continue
			words2=line.split()
			if flag2==1:
				if(words2[0]!='end'):
					if (words2[0].lower()) in isetsame_list:
					
						#print words[i]
						
		
						if len(words2)==(isetsame_dict[words2[0].lower()]+0+1):
							f3.write(words2[0] + " ")
							if len(words2)>(0+1):
								if words2[1] in mac_list:
									f3.write(mac_dict[words2[0+1]])	
								else:
									f3.write(words2[0+1])
								for x in range(0+2, len(words2)):
									if words2[x] in mac_list:
										f3.write(", " + mac_dict[words2[x]])
									else:
										f3.write(", " + words2[x])
							f3.write("\n")

					

	
					elif (words2[0].lower()) in isetpd_list:

						pdins=''
						if len(words2)==(isetpd_dict[words2[0].lower()]+0+1):
							pdins=words2[0].lower()
							#print pdins
							for x in range (0+1, len(words2)):
								if words2[x] in reg:
									pdins = pdins + 'reg'
									if x==i+1:
								
										arg_dict['regd']=words2[x]
									else:
										
										
										arg_dict['regs']=words2[x]

								elif words2[x] in acc:
									pdins = pdins + 'acc'
									if x==i+1:
																				
										arg_dict['regd']=words2[x]
									else:
										
										
										arg_dict['regs']=words2[x]

								



								elif words2[x] in equvar or words2[x].isdigit():
									pdins = pdins + 'num'
									arg_dict['num']=words2[x]


								elif words2[x] in mac_list:
									if mac_dict[words2[x]] in reg:
										pdins = pdins + 'reg'
										if x==i+1:
								
											arg_dict['regd']=mac_dict[words2[x]]
										else:
										
										
											arg_dict['regs']=mac_dict[words2[x]]

									elif words2[x] in acc:
										pdins = pdins + 'acc'
										if x==i+1:
																					
											arg_dict['regd']=mac_dict[words2[x]]
										else:
											
											
											arg_dict['regs']=mac_dict[words2[x]]

									elif mac_dict[words2[x]] in equvar or mac_dict[words2[x]].isdigit():
										pdins = pdins + 'num'
										arg_dict['num']=mac_dict[words2[x]]

								else:
									pdins = pdins + 'var'
									if x==i+1:
										if words2[x] in mac_list:
											arg_dict['vard']=mac_dict[words2[x]]
										else:	
											arg_dict['vard']=words2[x]
									else:
										if words2[x] in mac_list:
											arg_dict['vars']=mac_dict[words2[x]]
										else:	
											arg_dict['vars']=words2[x]
								

							
							pdfile.seek(0)
							flag=0
							for line in pdfile:
								if not(emp.search(line)):
									continue
								words3=line.split()
								

								if flag==1:
									if(words3[0]!='end'):


										f3.write(words3[0]+ ' ')
										if words3[1] in arg:
											f3.write(arg_dict[words3[1]] )
										else:
											f3.write(words3[1])
										if len(words3)>i+2:

											if words3[2] in arg:
												f3.write(", " + arg_dict[words3[2]])
											else:
												f3.write(", " + words3[2])

										f3.write("\n")

									else:
										flag = 0
										


									
								if words3[0]=='pdef' and words3[1]==pdins:
									flag=1	

							
						else:
							print "Error - Missing operand after " + words[i]
							break


					
				
				else:
					flag2 = 0
					break

			if words2[0]=='macro' and words2[1]==words[i]:
				flag2=1
				mac_dict[words2[2]]=words[i+1]
				mac_dict[words2[3]]=words[i+2]
				mac_list.append(words2[2])
				mac_list.append(words2[3])







f3.write("temp: db 0")

fmac.close()
f2.close()
f3.close()


