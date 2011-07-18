'''
robot.py

The terminal can be a dark place.  When you start getting errors in code
and you need a friend around, just hit 'import robot'.

Some instructions for use: 
	Stick this script in your home folder 
	Open up Terminal (Applications>> Utilities>>Terminal)
	
	type 'python' and hit enter
	This should open up python. 
	
	then type 
	>>>import robot
	
	Pick a name for the robot. for example, Hektor. 

	>>>Hektor = robot.robot()

	Then you can have Hektor speak things
	If you want Hektor to say "lalalala!"

	>>>Hektor.speak("lalalala!")
	
	If you want to see Hektor's face
	>>>Hektor.face()

	And if things get stressful, just type
	>>>Hektor.love()


You can put this among your python path, or you can include it in any development folder if things get difficult. 

something silly
by @kawantum
'''

class robot:
	def __init__(self):	
		print 'hello friends'

	def speak(self, s):
		print "ROBOT SAYS "+str(s)

	def face(self):
		print " -----------"
		print "|  o     o  |"
		print "|     _     |"
		print "|___________|"

	def love(self):
		self.speak("ROBOT LOVE")
		self.face()
		self.speak("<3 <3 <3")

	


