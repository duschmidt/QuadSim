


quad = Vehicle()

quad._positionWorld = [0,0,0]
quad._velocityWorld = [0,0,0]
quad._accelWorld = [0,0,-9.8]
quad._upWorld = [0,0,1]
quad._fwWorld = [0,1,0]

quad._accelVehicle = [0,0,0]
quad._rollRateVehicle = 0
quad._yawRateVehicle = 0
quad._pitchRateVehicle = 0

while True:
	quad.applyControlState()