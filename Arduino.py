class Arduino:
    """
    Arduino is the code that will be replicated on the actual microcontroller.
    Any SET functions will NOT be translated into the real application,
    but are present for use in simulation to present the sensors with data.
    """

    _sensZRange = 0

    def __init__(self):
        
        return


    def getResponse(self):
        """
        Get Ardiuno output based on current vehicle stateread.
        this function maps sensor data -> modified User Input
        """
        return

    """
    --------------------------------------------------------------------------------
    SIMULATION ONLY
    --------------------------------------------------------------------------------
    """

    def setSensorData(self, vehicleState):
        """
        Accepts a vehicle state object and uses it's parameters to update this Arudino's sensors as necessary
        INPUTS: vehicleState instance of VehicleState
        """
        _sensZRange = vehicleState._position[2]
        return
    
    def setUserInput(self):
        """
        Insert the user input that will come from a WII remote or keyboard
        from the current user.  This will enable real simulation from a 
        remote control in the real QuadCopter
        """
        return


