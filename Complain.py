class Complaint:
	identity = 0
	def __init__(self, content, identity = 0):
		self.score = 0
		self.content = content
		self.identity = identity
		Complaint.identity += 1

	def __str__(self):
		return "[{0},{1},{2}]".format(self.score, self.content, self.identity)

	def salt_it(self):
		"""
		>>> com = Complaint("This sucks...")
		>>> com.score
		0
		>>> com.content
		'This sucks...'
		>>> com.salt_it()
		>>> com.score
		1
		"""
		self.score += 1

	def pepper_it(self):
		"""
		>>> com = Complaint("This sucks...")
		>>> com.score
		0
		>>> com.content
		'This sucks...'
		>>> com.pepper_it()
		>>> com.score
		-1
		"""
		self.score -= 1

	def get_content(self):
		return self.content
class Complaint_List:
	def __init__(self):
		"""
		>>> com = Complaint("This sucks...")
		>>> com2 = Complaint("This really sucks...")
		>>> my_lst = Complaint_List([com, com2])
		>>> com2.salt_it()
		>>> com2.score
		1
		>>> my_lst.sort()
		>>> str(my_lst)
		"['[1,This really sucks...]', '[0,This sucks...]']"
		"""
		self.lst = []

	def __str__(self):
		if self.lst != []:
			return str([str(each) for each in self.lst])
		return "empty list!"

	def unique_complaint(self, complaint):
		for c in self.lst:
			if c.get_content() == complaint.get_content():
				return False
		return True

	def add_complaint(self, string):
		new_complaint = Complaint(string, Complaint.identity)
		if self.unique_complaint(new_complaint):
			self.lst.append(new_complaint)
	
	def sort(self):
		def key(complaint):
			return -complaint.score
		self.lst.sort(key = key)

	def get_complaints(self):
		self.sort()
		return self.lst

	def salt(self, complaint_id):
		for complaint in self.lst:
			if complaint.identity == complaint_id:
				complaint.salt_it()	

	def pepper(self, complaint_id):
		for complaint in self.lst:
			if complaint.identity == complaint_id:
				complaint.pepper_it()

	def print_list(self):
		for i in range(len(self.lst)):
			print('element', i, 'is', self.lst[i].score)



