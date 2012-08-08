
class VehicleState():
	"""Represents the xyz position/vel/acceleration and yaw/pitch/roll rates of a vehicle"""
	_position = [0,0,0]
	_velocity = [0,0,0]
	_accel = [0,0,0]
	_rollRate = 0
	_yawRate = 0
	_pitchRate = 0

	def __init__(self, position,velocity,accel,rollRate,pitchRate,yawRate):
		"""Initial value constructor"""
		self._position = position
		self._velocity = velocity
		self._accel = accel
		self._rollRate = rollRate
		self._yawRate = yawRate
		self._pitchRate = pitchRate

	

