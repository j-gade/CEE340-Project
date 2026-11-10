class Alarm:
    '''
    A class representing an alarm.
    
    An alarm has a state of "disarmed", "armed", or "triggered".
    Change state using the proper method.
    The alarm can only be triggered if it is in the armed state, at which
    case it will go through its list of outputs and turn them all on.
    The alarm can only be armed or disarmed if it is already in the disarmed
    or armed state, respectively.
    The alarm can be reset at any time and is the only way to turn off the
    outputs.
    '''
	def __init__(self):
		self.state = "disarmed"
		self.outputs = {}
		
	def reset(self):
        '''Reset the alarm to the disarmed state and turn off outputs'''
		self.state = "disarmed"
		for output in outputs.values():
			output.off()
		
	def disarm(self):
        '''Sets the alarm to the disarmed state if it is armed'''
		if self.state == "armed":
			self.state == "disarmed"
		
	def arm(self):
        '''Sets the alarm to the armed state if it is disarmed'''
		if self.state == "disarmed":
			self.state == "armed"
		
	def trigger(self):
        '''Set the alarm to the triggered state and turn on outputs'''
		if self.state == "armed"
			for output in outputs.values():
				output.on()
		
	def add_output(self, name, output):
        '''Adds an output to be turned on or off by the alarm'''
		self.outputs[name] = output

class Sensor:
    '''
    Sensor class
    
    start
    stop
    trigger
    '''
    pass
    
class Output:
    '''
    Output class
    
    on
    off
    '''
    pass
    