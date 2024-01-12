class ErrorHandler:
    def handle(self, exception):
        # This method would handle different types of exceptions
        # Placeholder for actual implementation
        if isinstance(exception, SomeSpecificException):
            print(f"A specific error occurred: {exception}")
        else:
            print(f"An error occurred: {exception}")
