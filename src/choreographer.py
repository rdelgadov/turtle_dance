#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from sensor_msgs.msg import JointState
x=0
y=0
global data 
data = JointState()
global pub
global rate
global data_delay_1
global data_delay_2
global data_delay_3
data_delay_1 = data
data_delay_2 = data
data_delay_3 = data
def callback(dat):
	global data 
	global data_delay_1
	global data_delay_2
	global data_delay_3
	data_delay_3 = data_delay_2
	data_delay_2 = data_delay_1
	data_delay_1 = data
	data=dat
	
	
			
			
def choreographer():
	global pub 
	pub= rospy.Publisher('mobile_base/commands/velocity', Twist, queue_size=10)
    
	rospy.init_node('choreographer', anonymous=True)
	global rate 
	rate = rospy.Rate(10) # 10hz
	rospy.Subscriber('joint_states', JointState, callback)
	global data
	global data_delay_3
	twist = Twist()
	
	rate.sleep()
	while True:
		twist.linear.x = 0.3
		while data.position[0] < 20 or data.position[1] < 20:
			print (data.position)
			print (1)
			pub.publish(twist)
			rate.sleep()
		twist.linear.x = 0
		while truncate(data.position[0],4) != truncate(data_delay_3.position[0],4)  and truncate(data.position[1],4) != truncate(data_delay_3.position[1],4):
			print (data.position)
			print (2)
			pub.publish(twist)
			rate.sleep()
		twist.linear.x = -0.3
		while data.position[0] > -20 or data.position[1] > -20:
			print (data.position)
			print (3)
			pub.publish(twist)
			rate.sleep()
		twist.linear.x = 0
		while truncate(data.position[0],4) != truncate(data_delay_3.position[0],4)  and truncate(data.position[1],4) != truncate(data_delay_3.position[1],4):
			print (data.position)
			print (4)
			pub.publish(twist)
			rate.sleep()
		twist.linear.x = 0.3
		while data.position[0] < 20 or data.position[1] < 20:
			print (data.position)
			print (5)
			pub.publish(twist)
			rate.sleep()
		twist.linear.x = 0
		while truncate(data.position[0],4) != truncate(data_delay_3.position[0],4)  and truncate(data.position[1],4) != truncate(data_delay_3.position[1],4):
			print (data.position)
			print (6)
			pub.publish(twist)
			rate.sleep()
		twist.angular.z = 0.5
		while data.position[0] > 10 and data.position[1] < 30:
			print (data.position)
			print (7)
			pub.publish(twist)
			rate.sleep()
		twist.angular.z = 0
		while truncate(data.position[0],4) != truncate(data_delay_3.position[0],4)  and truncate(data.position[1],4) != truncate(data_delay_3.position[1],4):
			print (data.position)
			print (8)
			pub.publish(twist)
			rate.sleep()
		twist.angular.z = -0.5
		while data.position[0] < 30 and data.position[1] > 10:
			print (data.position)
			print (9)
			pub.publish(twist)
			rate.sleep()
		twist.angular.z = 0
		while truncate(data.position[0],4) != truncate(data_delay_3.position[0],4)  and truncate(data.position[1],4) != truncate(data_delay_3.position[1],4):
			print (data.position)
			print (10)
			pub.publish(twist)
			rate.sleep()
		twist.angular.z = 0.5
		while data.position[0] > 20 and data.position[1] < 20:
			print (data.position)
			print (11)
			pub.publish(twist)
			rate.sleep()
		twist.angular.z = 0
		while truncate(data.position[0],4) != truncate(data_delay_3.position[0],4)  and truncate(data.position[1],4) != truncate(data_delay_3.position[1],4):
			print (data.position)
			print (12)
			pub.publish(twist)
			rate.sleep()
		twist.linear.x = -0.3
		while data.position[0] > 0 or data.position[1] > 0:
			print (data.position)
			print (13)
			pub.publish(twist)
			rate.sleep()
	print("done dancing")
	

def truncate(f, n):
    '''Truncates/pads a float f to n decimal places without rounding'''
    s = '{}'.format(f)
    if 'e' in s or 'E' in s:
        return '{0:.{1}f}'.format(f, n)
    i, p, d = s.partition('.')
    return '.'.join([i, (d+'0'*n)[:n]])

if __name__ == '__main__':
    try:
        choreographer()
    except rospy.ROSInterruptException:
        pass
