#Property of ek33

import json

class Followers:

	def __init__(self, previousFollowersFileName, currentFollowersFileName, followingsFileName):
		self.previousFollowersFileName = previousFollowersFileName
		self.currentFollowersFileName = currentFollowersFileName
		self.followingsFileName = followingsFileName
		

		previousFollowersFile = open(previousFollowersFileName)
		currentFollowersFile = open(currentFollowersFileName)
		followingsFile = open(followingsFileName)

		self.previousFollowers = []
		self.currentFollowers = []
		self.followings = []

		self.oldFollowers = []
		self.newFollowers = []
		self.nonFollowers = []

		for i in json.load(previousFollowersFile): 
			self.previousFollowers.append((i["string_list_data"][0])["value"])

		for i in json.load(currentFollowersFile): 
			self.currentFollowers.append((i["string_list_data"][0])["value"])

		for i in json.load(followingsFile)["relationships_following"]:
			self.followings.append((i["string_list_data"][0])["value"])



	def compare(self):
		
		for i in self.previousFollowers:
			if not i in self.currentFollowers:
				self.oldFollowers.append(i)
		
		for i in self.currentFollowers:
			if not i in self.previousFollowers:
				self.newFollowers.append(i)

		for i in self.followings:
			if not i in self.currentFollowers:
				self.nonFollowers.append(i)

		print("Old Followers\n", self.oldFollowers, "\n\nNew Followers\n", self.newFollowers, "\n\nNon Followers\n", self.nonFollowers)

			


followers = Followers("previousFollowers.json", "currentFollowers.json", "currentFollowings.json")
followers.compare()