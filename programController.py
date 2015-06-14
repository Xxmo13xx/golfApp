#Create the program controller.
import playerDatabase
import programIO


Controller = programIO.FileController()

"""
	Should get the players from the allPlayers.csv file
	Returns a list of players
"""

def startMenu():
	playerList =Controller.getPlayers()
	courseDict = Controller.getCourses()
	menuList = "\t1) New player. \n  \t2) New golf course. \n \t3) Select a player."
	for i in playerList:
		menuList += "\n\t\t" + str(i)
	menuList += "\n\t4) Select a golf course. "
	# print(type(courseDict))
	for i in courseDict.keys():
		menuList += "\n\t\t" + str(i)
	
	choice = input(menuList)

	if choice == "1":
		print("Choose 1")
		Controller.newPlayer()
		startMenu()
	elif choice == "2":
		print("Choose 2")
		Controller.newGolfCourse()
		startMenu()
	elif choice == "3":
		print("Choose 3")
		Controller.getPlayers()
		startMenu()
	else:
		#Create method to update player lists and then update golf course lists. 
		print("No choice seleced.")
	# return choice

def getPlayers():
	pass

"""
		Fill in the player lists
		Fill in the golf course lists. 
"""
def initiateProgram():
	pass



# print (courseDict)
startMenu()
# Controller.getPlayers()
# Controller.getCourses()