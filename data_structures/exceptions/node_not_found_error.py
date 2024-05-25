class NodeNotFoundError(Exception):
	def __init__(self, message="Node does not exist in the data structure"):
		self.message = message
		super().__init__(self.message)
