'''Setup File For The Project'''
import os

path = os.path.realpath(__file__)[:-8]

length = int(input('How many sites would you like to enter: '))

time1 = input('From What Time Do YOu Want To Start Stopping These Sites(0-23): ')
time2 = input('What Time Do You Wanna Stop Banning You From These Sites(0-23): ')

file = open('{}setup.txt'.format(path), 'w+')
file.write(str(length)+'\n')
file.write(time1+'\n')
file.write(time2+'\n')

for i in range(0,length):
	site = input('Enter Site {}: '.format(i+1))
	file.write(site+'\n')