class NodeNotFoundError(Exception):
	def __init__(self, message="Node not found"):
		self.message = message
		super().__init__(self.message)
