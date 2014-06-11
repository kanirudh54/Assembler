import sys
input_files=[]
input_files=sys.argv
input_files.pop(0)
global_file=open('global.txt','w')
global_dict={}
global_list=[]


for infile in input_files:
	sym = open(infile[:], 'r')
	for line in sym:
		if line=='\n':
			continue
		words=line.split()
		global_dict[words[0]]=infile+'/'+words[1]

	sym.close()








for infile in input_files:
	fin=open(infile,'r')
	for line in fin:
		if line=='\n':
			#print 'yes'
			continue
		words=line.split()
		#print words[0]
		if words[0].lower()=='extern':
			for x in range(1, len(words)):

				global_list.append(words[x])
				
		
	fin.close()


for infile in input_files:
	ind=0
	fin=open(infile,'r')
	lines=fin.readlines()
	for each_line in lines:
		if 'global' in each_line.lower():
			words=each_line.split()
			lines[ind]=lines[ind].replace('global ', "")
			lines[ind]=lines[ind].replace(words[1] + " ", "")

		if 'extern' in each_line.lower():
			lines[ind]=""
			
			
		for gl_vars in global_list:
			if ' '+gl_vars in each_line or ','+gl_vars in each_line:
				#print line
				#print 2321
				lines[ind]=lines[ind].replace(gl_vars, global_dict[gl_vars])
		ind+=1
	fin.close()
	fout=open(infile+'_lin','w')
	for line in lines:
		fout.write(line)


	fout.close()
		
