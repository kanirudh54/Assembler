import sys
import re
input_arg=[]
input_arg=sys.argv
input_arg.pop(0)
emp = re.compile('\S')
num = len(input_arg)

input_file=[]
input_add=[]
input_sort=[]
fileadd_dict={}
for x in range(0, num):
	if x%2==0:
		fileadd_dict[input_arg[x]]=input_arg[x+1]
		input_file.append(input_arg[x])
	else:
		input_add.append(input_arg[x])

strtt=''
print fileadd_dict
temp=0
temp2=0
off=0
for infile in input_file:
	fin=open(infile,'r')
	lines=fin.readlines()
	off = int(fileadd_dict[infile])
	fnew = open(infile+"_ld1", 'w')
	for line in lines:
		if not(emp.search(line)):
			continue
		words=line.split()
		ind=0
		for word in words:
			if word.isdigit():
				temp= int(words[ind])
				temp = temp + off
				words[ind]=str(temp)

			elif '+' in word:
				temp= int(word.split("+")[0])
				temp2=int(word.split("+")[1])
				temp = temp + off + temp2
				words[ind]=str(temp)					

			elif word[0]=='$':
				words[ind] = word.replace("$", "")

			elif '/' in word:
				strtt= (word.split("/")[0])
				temp = int(word.split("/")[1])
				strtt = strtt + '_lin'
				temp = temp + int(fileadd_dict[strtt])
				words[ind]= str(temp)


			else:
				words[ind]=word
			ind+=1	


		
		if words!='\n':
			fnew.write(' '.join(words)+'\n')

	fin.close()
	fnew.close()

input_add.sort()

for x in range (0, len(input_add)):
	for y in range(0, len(input_file)):

		if input_add[x]==fileadd_dict[input_file[y]]:
			input_sort.append(input_file[y])
			break



outfile = open("loaded1.txt", 'w')
for infile in input_sort:
	fin=open(infile+"_ld1",'r')
	
	lines=fin.readlines()
	for line in lines:
		if 'hlt' in line:
			continue
		outfile.write(line)

	fin.close()
outfile.write('hlt')
outfile.close()
				
lenfile={}
for infile in input_sort:
	fin = open(infile[:-8]+'_sym', 'r')
	lines=fin.readlines()
	for line in lines:
		words=line.split()
		if words[0]=='temp':
			lenfile[infile]=int(words[1])


lol={}
t=0
for infile in input_sort:
	lol[infile]=t
	t = t + lenfile[infile]+1

off=0


for infile in input_sort:
	fin=open(infile,'r')

	lines=fin.readlines()
	
	fnew = open(infile+"_ld2", 'w')

	for line in lines:
		if not(emp.search(line)):
			continue
		words=line.split()
		ind=0
		for word in words:
			if word.isdigit():
				temp= int(words[ind])
				temp = temp + off
				words[ind]=str(temp)

			elif '+' in word:
				temp= int(word.split("+")[0])
				temp2=int(word.split("+")[1])
				temp = temp + off + temp2
				words[ind]=str(temp)					

			elif word[0]=='$':
				words[ind] = word.replace("$", "")

			elif '/' in word:
				strtt= (word.split("/")[0])
				temp = int(word.split("/")[1])
				strtt = strtt + '_lin'
				temp = temp + lol[strtt]
				words[ind]= str(temp)


			else:
				words[ind]=word
			ind+=1	


		
	
		if words!='\n':
			fnew.write(' '.join(words)+'\n')

	fin.close()
	fnew.close()
	off= off + lenfile[infile]+1


outfile = open("loaded2.txt", 'w')
for infile in input_sort:
	fin=open(infile+"_ld2",'r')
	
	lines=fin.readlines()
	for line in lines:
		if 'hlt' in line:
			continue
		outfile.write(line)

	fin.close()
outfile.write('hlt')
outfile.close()
