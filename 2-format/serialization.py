'''
Class code on serialization and deserialization
'''

import json


#serializing a dictionary
def example1():
	d = {} #create a dictionary
	d['s'] = 1 #add value of 1 to key k
	d['a'] = 6 #add value of 6 to key a
	d['136'] = [1,2,3,4,5]

	print('JSON Representation', json.dumps(d))


#serializing a dictionary and saving to a file
def example2():
	d = {} #create a dictionary
	d['s'] = 1 #add value of 1 to key k
	d['a'] = 6 #add value of 6 to key a
	d['136'] = [1,2,3,4,5]

	fp = open('mydata.json','w')


	#write to file
	print('Writing the JSON string to a file...')
	json.dump(d, fp)
	fp.close()



#serializing a dictionary and saving to a file
def example3():
	fp = open('mydata.json','r')

	#write to file
	print('Loading json from a file...')
	d = json.load(fp)
	fp.close()

	print('What is the value of s', d['s'])
	print('What is the value of s', d['a'])
	print('What is the value of s', d['136'])



#serializing a dictionary and saving to a file (error)
def example4():
	d = {} #create a dictionary
	d['s'] = 1 #add value of 1 to key k
	d['a'] = 6 #add value of 6 to key a
	d['136'] = lambda x: 2*x

	fp = open('mydata.json','w')

	#write to file
	print('Writing the JSON string to a file...')
	json.dump(d, fp)
	fp.close()

example1()