from time import *
from termcolor import colored

startTime = time()

#--------------------------------

def setup_plot(X,X_MIN,X_MAX,LABEL,UNIT):
	POSITION = int((10 - 0)*(X - X_MIN)/(X_MAX - X_MIN))
	draw(X,POSITION,LABEL,UNIT)
 	return    
#--------------------------------

def draw(X,POSITION,LABEL,UNIT):
	print colored('Time = {0:.1f}  s,','red') .format(time()-startTime),
	print colored(LABEL,'cyan') .format(X),		
	print colored('= {0:.3f}','cyan') .format(X),
	print colored(UNIT,'cyan') .format(X),			
	for i in range(0,POSITION):
		print colored('-','blue'),
	print colored('>','blue')
	return
