'''
Install cloudmounter for this to work 
'''

#will help us time things
import time 

#will help us figure out the size of things
import sys


mount_path = '/Users/sanjaykrishnan/Library/Containers/com.eltima.cloudmounter.mas/Data/.CMVolumes/Sanjay Krishnan/CMSC13600-Data/'

files = [mount_path+'colors.dat', mount_path+'document.txt', mount_path+'blank.abc']


#calculates the read latency in milliseconds
def calculate_read_latency():
	start = time.time()
	fp = open(files[2], 'r') #open blank file
	fp.read()# read blank file
	end = time.time()
	return (end - start)*1e6

#calculates the read latency in milliseconds
def calculate_read_bandwidth():
	
	#first figure out what the basic cost is
	latency = calculate_read_latency()

	start = time.time() + latency/1e6 #remove that cost from the timer

	fp = open(files[0], 'r') #open biggest file
	size = sys.getsizeof(fp.read())/1e9# read biggest file get the size
	end = time.time()

	return size/(end - start)


#calculates the read latency in milliseconds
def calculate_write_latency():
	start = time.time()
	fp = open(mount_path+'blank.file', 'w') #open blank file
	fp.write('')# write blank file
	end = time.time()
	return (end - start)*1e6

#calculates the read latency in milliseconds
def calculate_write_bandwidth():

	#open biggest file
	fp = open(files[0], 'r')
	data = fp.read() #get all the data
	size = sys.getsizeof(data)/1e9 # figure out how much data

	
	#first figure out what the basic cost is
	latency = calculate_write_latency()
	start = time.time() + latency/1e6 #remove that cost from the timer
	fp = open(mount_path+'notblank.file', 'w') #open biggest file
	fp.write(data)
	end = time.time()

	return size/(end - start)


print('Read Latency', calculate_read_latency(),'mu s')
print('Read Bandwidth', calculate_read_bandwidth(),'GB/s')

print('Write Latency', calculate_write_latency(),'mu s')
print('Write Bandwidth', calculate_write_bandwidth(),'GB/s')