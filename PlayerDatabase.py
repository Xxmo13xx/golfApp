# Player database
import os.path




class Player(object):

	def __init__(self, name, hasScores=False, playerScores=list()):
		self.playerName = name
		self.hasScores = hasScores
		self.playerScores = playerScores

	def getPlayerName(self):
		return self.playerName

	def getPlayerScores(self):
		playerFile = open(os.path.join(os.getcwd(),"playerDatabase\\",self.playerName+".csv"),'r')
		for i in playerFile.readlines():
			print(i)
		playerFile.close()
		return self.playerScores



	def getMyScores(self):
		#returns a list of this players scores. 
		pass

	def getMyScores(self):
		pass


# newPlayer = Player("Willie","False")
# newPlayer.getPlayerScores()