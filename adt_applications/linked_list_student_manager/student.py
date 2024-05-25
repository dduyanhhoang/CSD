class Student():
	def __init__(self, id, name):
		self.id = id
		self.name = name
		self.mark =  	0.

	@property
	def id(self) -> str:
		return self._id

	@id.setter
	def id(self, value) -> None:
		self._id = value

	@property
	def name(self):
		return self._name
	
	@name.setter
	def name(self, value):
		self._name = value

	@property
	def mark(self):
		return self._mark
	
	@mark.setter
	def mark(self, value):
		if not (isinstance(value, float) and 0 <= value <= 10):
			raise ValueError('mark must be int between 0 and 10')

		self._mark = value

	def __str__(self) -> str:
		return f"Student '{self.name}' with id '{self.id}' has mark '{self.mark}'"
