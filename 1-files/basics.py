'''
Code for lecture 1 file and i/o examples.
'''

files = ['data/colors.dat', 'data/document.txt', 'data/blank.abc']


'''
1. Example code for opening and reading files in python
'''
def open_and_read():
	for file in files: #iterate through the files above
		fp = open(file, 'r') #creates a 'file pointer' and sets the mode to read
		data = fp.read() #return the whole data

		#print out what we just read
		print('--',file,'--')
		print(data)
		print()

		#always close the file
		fp.close()


'''
2. Example code for opening and reading files in python
'''
def open_and_readlines():
	for file in files: #iterate through the files above
		fp = open(file, 'r') #creates a 'file pointer' and sets the mode to read
		data = fp.readlines() #return the data split into a list of lines

		#print out what we just read
		print('--',file,'--')
		print(data)
		print()

		#always close the file
		fp.close()


'''
3. Example code for opening and reading files in python
'''
def open_and_read_linexline():
	for file in files: #iterate through the files above
		fp = open(file, 'r') #creates a 'file pointer' and sets the mode to read
		

		print('--',file,'--')
		line = fp.readline()
		while line:
			print(line)
			line = fp.readline()

		#print out what we just read
		print()

		#always close the file
		fp.close()


'''
4. Example code for opening and writing files in python
'''
def open_and_write():
	mynum = '142687621\n'

	f = open('data/new_file.txt', 'w') #opens the file in "write" mode
	f.write(mynum)

	f.close()



'''
6. Example code for opening and appending to files in python
'''
def open_and_append():
	mynum = '821321772\nx'

	f = open('data/new_file.txt', 'a') #opens the file in "write" mode
	f.write(mynum)

	f.close()



#example 1
#open_and_read()

#example 2
#open_and_readlines()

#example 3


#open_and_read_linexline()

open_and_write()

open_and_append()