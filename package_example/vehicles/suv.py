class SUV:
    """
    A class used to represent an SUV (Sport Utility Vehicle).

    ...

    Attributes:
        make : str
            The manufacturer of the SUV
        model : str
            The model of the SUV
        year : int
            The year the SUV was manufactured
        color : str
            The color of the SUV
        mileage : float
            The mileage of the SUV
        all_wheel_drive : bool
            Indicates if the SUV has all-wheel drive

    Methods:
        drive(distance: float):
            Simulates driving the SUV a certain distance, increasing the mileage.
        repaint(new_color: str):
            Changes the color of the SUV.
        enable_all_wheel_drive():
            Enables the all-wheel drive feature.
        disable_all_wheel_drive():
            Disables the all-wheel drive feature.
        get_description() -> str:
            Returns a string representation of the SUV's details.
    """

    def __init__(
        self,
        make: str,
        model: str,
        year: int,
        color: str,
        mileage: float = 0.0,
        all_wheel_drive: bool = False,
    ):
        """
        Constructs all the necessary attributes for the SUV object.

        Parameters:
            make : str
                The manufacturer of the SUV
            model : str
                The model of the SUV
            year : int
                The year the SUV was manufactured
            color : str
                The color of the SUV
            mileage : float, optional
                The mileage of the SUV (default is 0.0)
            all_wheel_drive : bool, optional
                Indicates if the SUV has all-wheel drive (default is False)
        """
        self.make = make
        self.model = model
        self.year = year
        self.color = color
        self.mileage = mileage
        self.all_wheel_drive = all_wheel_drive

    def drive(self, distance: float):
        """
        Simulates driving the SUV a certain distance, increasing the mileage.

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
        Changes the color of the SUV.

        Parameters:
            new_color : str
                The new color of the SUV
        """
        self.color = new_color

    def enable_all_wheel_drive(self):
        """
        Enables the all-wheel drive feature.
        """
        self.all_wheel_drive = True

    def disable_all_wheel_drive(self):
        """
        Disables the all-wheel drive feature.
        """
        self.all_wheel_drive = False

    def get_description(self) -> str:
        """
        Returns a string representation of the SUV's details.

        Returns:
            str
                A string containing the make, model, year, color, mileage, and all-wheel drive status of the SUV.
        """
        awd_status = "enabled" if self.all_wheel_drive else "disabled"
        return f"{self.year} {self.make} {self.model}, {self.color}, {self.mileage:.1f} miles, AWD: {awd_status}"
