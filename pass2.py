

import sys
input_files=[]
input_files=sys.argv
input_files.pop(0)

for infile in input_files:
	fin = open(infile,'r')
	fout = open(infile+'_ass','w')
	fout2 = open(infile+'_ass$', 'w')
	symfile=open(infile+'_ass_sym','r')
	litfile=open(infile+'_ass_lit','r')


symboldict={}
symbol_list=[]

for line in symfile:
	word,num1,num2 = line.split()
	symboldict[word]=[int(num1),int(num2)]
	symbol_list.append(word)
symfile.close()



literaldict={}
literal_list=[]

for line in litfile:
	word,num=line.split()
	literaldict[word]=int(num)
	literal_list.append(word)
litfile.close()
halt=False
for line in fin:
	if line=="\n":
		#print 'New line found'
		continue
	words=line.split()
	ind=0
	for word in words:
		if word[0]!=';':
			if word[len(word)-1]==':':

				if word.isdigit() or word[:-1].isdigit():
					
					words[ind]='$'+word
					#print word[:-1]


				if word[:-1] in symboldict.keys():
					words.pop(0)
					#break
					#fout.write(''.join(words))

				elif word[:-1] in literaldict.keys():
					words=''
					break
				else:
					print 'Error!!!'
			else:

				if word.isdigit() or word[:-1].isdigit():
					
					words[ind]='$'+word
					#print word[:-1]

				#Code for normal words
				if word in symboldict.keys():
					words[ind]=str(symboldict[word][0])
					
				elif word in literaldict.keys():
					words[ind]=str(literaldict[word])
				else:
					for entry in symbol_list:
						if entry in word:
							#print 'True'
							#print entry,word
							words[ind]=words[ind].replace(entry,str(symboldict[entry][0]))
							#print word
					for entry in literal_list:
						if entry in word:
			
							words[ind]=words[ind].replace(entry,str(literaldict[entry]))
		else:
			break
			#Code for printing comments as-is
		ind+=1
	if words!='\n':
		fout2.write(' '.join(words)+'\n')
fin.seek(0)

for line in fin:
	if line=="\n":
		#print 'New line found'
		continue
	words=line.split()
	ind=0
	for word in words:
		if word[0]!=';':
			if word[len(word)-1]==':':

				


				if word[:-1] in symboldict.keys():
					words.pop(0)
					#break
					#fout.write(''.join(words))

				elif word[:-1] in literaldict.keys():
					words=''
					break
				else:
					print 'Error!!!'
			else:

				

				#Code for normal words
				if word in symboldict.keys():
					words[ind]=str(symboldict[word][0])
					
				elif word in literaldict.keys():
					words[ind]=str(literaldict[word])
				else:
					for entry in symbol_list:
						if entry in word:
							#print 'True'
							#print entry,word
							words[ind]=words[ind].replace(entry,str(symboldict[entry][0]))
							#print word
					for entry in literal_list:
						if entry in word:
			
							words[ind]=words[ind].replace(entry,str(literaldict[entry]))
		else:
			break
			#Code for printing comments as-is
		ind+=1
	if words!='\n':
		fout.write(' '.join(words)+'\n')

fin.close()
fout.close()
fout2.close()
