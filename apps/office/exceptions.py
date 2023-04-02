class ProfileNotDoctorException(Exception):
    def __init__(self, message="Profile is not doctor!"):
        self.message = message
        super().__init__(self.message)