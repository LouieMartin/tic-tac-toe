class IllegalSquareError(Exception):
    def __init__(self):
        """
            Raise an error if the player tries to put a piece on an invalid square.
        """
        self.message = f'IllegalSquareError: You placed a piece on an invalid square.'

        super().__init__(self.message)
