"""
Arduino is the code that will be replicated on the actual microcontroller.
Any SET functions will NOT be translated into the real application,
but are present for use in simulation to present the sensors with data.
"""
class Arduino:
    def __init__(self):
        
        return
    
    """
    Read X acceleration in the world cordinate system
    This is a computed value based on sensors
    """
    def getXAcceleration(self):
        
        return
    
    """
    Read Y acceleration world cordinate system
    This is a computed value based on sensors
    """
    def getYAcceleration(self):
        
        return
    
    """
    Read Z acceleration world cordinate system
    This is a computed value based on sensors
    """
    def getZAcceleration(self):
        
        return

    """
    Read Z distance sensor
    """
    def getZDistance(self):
        
        return

    """
    --------------------------------------------------------------------------------
    SIMULATION ONLY
    --------------------------------------------------------------------------------
    """

    """
    Updates all the "real" data that the sensors will read.  This data will be used 
    by the ardiuno to calculate its precieved measurements.
    INPUTS: data
    """
    def setSensorData(self):
        
        return
    
    """
    Insert the user input that will come from a WII remote or keyboard
    from the current user.  This will enable real simulation from a 
    remote control in the real QuadCopter
    """
    def setUserInput(self):
        
        return
    