'''
Code to measure latency and bandidwith of "read"
'''
#will help us figure out the memory usage
import psutil
import os

file = 'data/colors.dat'


#helper function to get the memory usage
def get_process_memory():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss

'''
1. Example code for opening and reading files in python
'''
def open_and_read():
	fp = open(file, 'r') #creates a 'file pointer' and sets the mode to read
	data = fp.read() #return the whole data

	#print out what we just read
	print('--',file,'--')
	print('Memory Usage: ', get_process_memory()/1e6,'MB')
	print()

	#always close the file
	fp.close()

	#clear it out!
	data = None


'''
3. Example code for opening and reading files in python
'''
def open_and_read_linexline():
	fp = open(file, 'r') #creates a 'file pointer' and sets the mode to read
		
	print('--',file,'--')
	line = fp.readline()
	mem = 0
	while line:
		mem = max(get_process_memory(),mem) #get peak memory usage
		line = fp.readline()

	print('Memory Usage: ', mem/1e6,'MB')

	#always close the file
	fp.close()


#example 1
#open_and_read()

#example 3
open_and_read_linexline()