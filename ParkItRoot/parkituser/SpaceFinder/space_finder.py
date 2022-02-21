"""Parking Space Finder module."""

class SpaceFinder:
    """Parking Space Finder class."""
    def __init__(self):
        """Initialise the instances."""
        self.city = None
        self.area = None
    
    def get_spaces_list(self):
        """Get list of available spaces.
        
        Returns
        -------
            List[dict]
                The list of all the available spaces.
        """
        return [{
            "name": "ABC",
            "address": "XYZ--192--111",
            "SpaceAvailabeFor": "2 cars SUV",
            "Cost": 10
        },
        {
            "name": "ABC",
            "address": "XYZ--192--111",
            "SpaceAvailabeFor": "2 cars SUV",
            "Cost": 10
        },
        {
            "name": "ABC",
            "address": "XYZ--192--111",
            "SpaceAvailabeFor": "2 cars SUV",
            "Cost": 10
        }]