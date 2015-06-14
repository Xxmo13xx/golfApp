from golfDatabase import golfCourse
from PlayerDatabase import Player
import os.path

#newCourse = golfCourse("Mill Creek", 130.0,72.9)

#print(newCourse.getName())

class FileController(object):
	def __init__(self):
		playerDatabasePath = os.path.join(os.getcwd(),"playerDatabase\\")
		courseDatabasePath = os.path.join(os.getcwd(),"courseData.csv")
		pass

	def saveNewCourse(self,tempGolfCourse):
		if os.path.isfile(self.courseDatabasePath):
			with open(self.courseDatabasePath,'a') as courseDatabase:
				courseDatabase.write(tempGolfCourse.getCourseName()+","+tempGolfCourse.getCourseRating()+","+tempGolfCourse.getSlopeRating()+"\n")
			print(str(tempGolfCourse.getCourseName())+" was created.")
		else:
			print ("The golf database is deleted.")

	def saveNewPlayer(self,tempPlayer):
		if os.path.isfile(os.path.join(self.playerDatabasePath,tempPlayer.getPlayerName()+".csv")):
			print("The player already exists in the database.")
		else:
			with open(os.path.join(self.playerDatabasePath,tempPlayer.getPlayerName()+'.csv'),'a') as playerDatabase:
				playerDatabase.write(tempPlayer.getPlayerName()+ ","+ str(tempPlayer.hasScores)+"\n")
			 	playerDatabase.close()

			with open(os.path.join(self.playerDatabasePath,'overallplayers.csv'),'a') as overallPlayerFile:
				overallPlayerFile.write(tempPlayer.getPlayerName() +",")
				overallPlayerFile.close()
				print("Player was created.")		

	def newGolfCourse(self):
		courseName = input("Please enter the course name.")
		courseRating = input("Please enter the slope rating.")
		slopeRating = input("Please enter the course rating.")
		tempGolfCourse = golfCourse(courseName, courseRating, slopeRating)
		self.saveNewCourse(tempGolfCourse)

	def newPlayer(self):
		playerName = input("Please enter the players name.")
		tempPlayer = Player(playerName,False)
		self.saveNewPlayer(tempPlayer)

	def openPlayerFile(self,player):
		tempFile = open(os.path.join(os.getcwd(),"playerDatabase\\",player.getPlayerName()+".csv"),'a')
		return tempFile

	def getPlayers(self):
		tempPlayerList = list()
		playerFile = open(os.path.join(os.getcwd(),"playerDatabase\\","overallPlayers.csv"),'r')
		for i in playerFile.readline().split(","):
			tempPlayerList.append(i.strip("\n"))
		return tempPlayerList


	def getCourses(self):
		tempCourseDict = dict()
		coursesFile = open(os.path.join(os.getcwd(),"courseData.csv"))
		for i in coursesFile.readlines():
			curCourseList = i.split(',')
			tempCourseDict[curCourseList[0]] =(curCourseList[1],curCourseList[2].strip("\n"))
		return tempCourseDict

# cont = FileController()
# cont.newPlayer()

"""
with open(filename,'r') as file:
	return len(file.readlines())
"""

"""
example of writing with csv
with open(testPath,'w',newline='') as file:
	writer = csv.writer(file,delimiter='\t',quoting=csv.QUOTE_MINIMAL)
	writer.writerow("This,is,a,test")
	writer.writerow("Second,test,is,here")
"""

"""
example of writing with csv from a list
with open(testpath,'w',newline='') as file:
	writer = csv.writer(file,quoting=csv.QUOTE_MINIMAL)
	writer.writerow("This,is,a,test".split(','))

"""

"""
example of reading with csv
with open(testPath,'r') as file:
	reader = csv.reader(file,escapechar="\t")
	for row in reader:
		print(row)
"""
