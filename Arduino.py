class Arduino:
    """
    Arduino is the code that will be replicated on the actual microcontroller.
    Any SET functions will NOT be translated into the real application,
    but are present for use in simulation to present the sensors with data.
    """

    _sensZRange = 0
    _sensUserRollRate = 0
    _sensUserPitchRate = 0
    _sensUserYawRate = 0
    _sensUserThrottle = 0

    def __init__(self):
        
        return


    def getControlState(self):
        """
        Get Ardiuno output based on current vehicle state read.
        this function maps current sensor data -> new vehicle control state
        """

        return {'rollRate':0,'yawRate':0,'pitchRate':0,'throttle':20}

    """
    --------------------------------------------------------------------------------
    SIMULATION ONLY
    --------------------------------------------------------------------------------
    """

    def setSensorData(self, vehicle):
        """
        Accepts a vehicle state object and uses it's parameters to update this Arudino's sensors as necessary
        INPUTS: vehicleState instance of VehicleState
        """
        _sensZRange = vehicleState._position[2]

        return
    
    def pollControlInput(self):
        """
        Poll for user input that will come from a WII remote or keyboard
        from the current user.  This will enable real simulation from a 
        remote control in the real QuadCopter
        This method sets:
            _sensControlRollRate
            _sensControlPitchRate
            _sensControlYawRate
            _sensControlThrottle
        """
        self._sensUserRollRate = 0
        self._sensUserPitchRate = 0
        self._sensUserYawRate = 0
        self._sensUserThrottle = 20
        return


