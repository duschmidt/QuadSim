class Vehicle():
	_positionWorld = [0,0,0]
	_velocityWorld = [0,0,0]
	_accelWorld = [0,0,0]
	_upWorld = [0,0,1]
	_fwWorld = [0,1,0]

	_accelVehicle = [0,0,0]
	_rollRateVehicle = 0
	_yawRateVehicle = 0
	_pitchRateVehicle = 0

	_myArduino = Arduino()


	def applyControlState(self, controlState):
		"""This method applies a given controlstate to this vehicle's state _myState"""
		_myArduino.setSensorData(self)
		_myArduino.pollControlState()
		state = _myArduino.getControlState()

		#math to apply new control state anh update all world parameters
