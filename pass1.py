

import sys
input_files=[]
input_files=sys.argv
input_files.pop(0)

f = open('mnemonictab.txt', 'r')


mnemonic={}
for line in f:
	word1,word2=line.split()
	#print word1
	mnemonic[word1]=[int(word2)]
	#for word in words:
	#	print word
f.close()
for infile in input_files:
	codefile = open(infile,'r')
	symfile = open(infile+'_ass_sym','w')
	litfile=open(infile+'_ass_lit','w')

symboltable={}
symbol_list=[]
literaltable={}
literal_list=[]

counter=0
for line in codefile:
	if line=="\n":
		continue
	words=line.split()
	ind=0
	for word in words:
		if word[0]!=';':
			if word[len(word)-1]!=':':

				if word in mnemonic.keys():
					#print 'boohoo',word
					counter+=mnemonic[word][0]
				elif words[0].lower()=='global':
					if words[ind+2]=='ds':
						
						symbol_list.append(words[1])
						symboltable[words[1]]=[counter,int(words[ind+3])]
						counter+=int(words[ind+3])
						break
					elif words[ind+2]=='db':
						symbol_list.append(words[1])
						nums=words[ind+3].count(',')
						#print 'nums:',nums,words
						
						symboltable[words[1]]=[counter,nums+1]
						counter+=(nums+1)
						break
					elif words[ind+2]=='equ':
						break
					else:
						if words[ind+2] in mnemonic.keys():
							counter+=mnemonic[words[ind+1]][0]
						break					#print 'Error!!!',word
				break
			elif word[len(word)-1]==':':
				if words[ind+1]=='ds':
					symbol_list.append(word[:-1])
					symboltable[word[:-1]]=[counter,int(words[ind+2])]
					counter+=int(words[ind+2])
					break
				elif words[ind+1]=='db':
					symbol_list.append(word[:-1])
					nums=words[ind+2].count(',')
					#print 'nums:',nums,words
					word=word[:-1]
					symboltable[word]=[counter,nums+1]
					counter+=(nums+1)
					break
				elif words[ind+1]=='equ':
					literal_list.append(word[:-1])
					literaltable[word[:-1]]=int(words[ind+2])
					break
				else:
					if words[ind+1] in mnemonic.keys():
						symbol_list.append(word[:-1])
						#print '231321',word
						word=word[:-1]
						symboltable[word]=[counter,mnemonic[words[ind+1]][0]]
						counter+=mnemonic[words[ind+1]][0]
						break
				
		else:
			break
		ind+=1
print symboltable
print literaltable

#print symbol_list
for entry in symbol_list:
#	print entry
	symfile.write(entry+" "+str(symboltable[entry][0])+" "+str(symboltable[entry][1])+"\n")

for entry in literal_list:
	litfile.write(entry+" "+str(literaltable[entry])+"\n")
litfile.close()
symfile.close()
codefile.close()
