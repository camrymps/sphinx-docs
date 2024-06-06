class Circle:
    """
    A class representing a circle.

    Attributes:
        radius : float
            The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius : float
                The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float:
                The area of the circle.
        """
        return 3.14159 * self.radius**2

    def circumference(self):
        """
        Calculates the circumference of the circle.

        Returns:
            float:
                The circumference of the circle.
        """
        return 2 * 3.14159 * self.radius
