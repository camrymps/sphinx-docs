class Sedan:
    """
    A class used to represent a Sedan car.

    ...

    Attributes:
        make : str
            The manufacturer of the sedan
        model : str
            The model of the sedan
        year : int
            The year the sedan was manufactured
        color : str
            The color of the sedan
        mileage : float
            The mileage of the sedan

    Methods:
        drive(distance: float):
            Simulates driving the sedan a certain distance, increasing the mileage.
        repaint(new_color: str):
            Changes the color of the sedan.
        get_description() -> str:
            Returns a string representation of the sedan's details.
    """

    def __init__(
        self, make: str, model: str, year: int, color: str, mileage: float = 0.0
    ):
        """
        Constructs all the necessary attributes for the sedan object.

        Parameters:
            make : str
                The manufacturer of the sedan
            model : str
                The model of the sedan
            year : int
                The year the sedan was manufactured
            color : str
                The color of the sedan
            mileage : float, optional
                The mileage of the sedan (default is 0.0)
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage

    def drive(self, distance: float):
        """
        Simulates driving the sedan a certain distance, increasing the mileage.

        Parameters:
            distance : float
                The distance driven in miles

        Raises:
            ValueError
                If the distance is negative
        """
        if distance < 0:
            raise ValueError("Distance driven cannot be negative.")
        self.mileage += distance

    def repaint(self, new_color: str):
        """
        Changes the color of the sedan.

        Parameters:
            new_color : str
                The new color of the sedan
        """
        self.color = new_color

    def get_description(self) -> str:
        """
        Returns a string representation of the sedan's details.

        Returns:
            str
                A string containing the make, model, year, color, and mileage of the sedan.
        """
        return f"{self.year} {self.make} {self.model}, {self.color}, {self.mileage:.1f} miles"
