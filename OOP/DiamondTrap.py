from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Representing the bastard."""

    def __init__(self, first_name):
        """Initialize the king"""
        super().__init__(first_name)
