# Golf database 

"""
	Class golfCourse:
	variables:
		courseName : String
		courseRating : decimal
		slopeRating : decimal
	methods:
		getCourseName()
		getCourseRating()
		getCourseSlopeRating()

"""


class golfCourse(object):

	def __init__(self, name, course, slope):
		self.courseName = name
		self.courseRating = course
		self.slopeRating = slope

	def getCourseName(self):
		return self.courseName

	def getCourseRating(self):
		return self.courseRating

	def getSlopeRating(self):
		return self.slopeRating



