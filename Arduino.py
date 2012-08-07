class Arduino:
    """
    Arduino is the code that will be replicated on the actual microcontroller.
    Any SET functions will NOT be translated into the real application,
    but are present for use in simulation to present the sensors with data.
    """
    def __init__(self):
        
        return
    
    
    def getXAcceleration(self):
        """
        Read X acceleration in the world cordinate system
        This is a computed value based on sensors
        """
        
        return
    
    def getYAcceleration(self):
        """
        Read Y acceleration world cordinate system
        This is a computed value based on sensors
        """
        return
    
    def getZAcceleration(self):
        """
        Read Z acceleration world cordinate system
        This is a computed value based on sensors
        """
        return

    def getZDistance(self):
        """
        Read Z distance sensor
        """
        return

    """
    --------------------------------------------------------------------------------
    SIMULATION ONLY
    --------------------------------------------------------------------------------
    """

    def setSensorData(self):
        """
        Updates all the "real" data that the sensors will read.  This data will be used 
        by the ardiuno to calculate its precieved measurements.
        INPUTS: data
        """
        return
    
    def setUserInput(self):
        """
        Insert the user input that will come from a WII remote or keyboard
        from the current user.  This will enable real simulation from a 
        remote control in the real QuadCopter
        """
        return
    