class CapacityReachedError(Exception):
    """Exception raised when the array has reached its maximum capacity."""
    def __init__(self, message="Maximum capacity reached"):
        self.message = message
        super().__init__(self.message)