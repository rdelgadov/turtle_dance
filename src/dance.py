#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
	rospy.loginfo(rospy.get_caller_id() + "Received instruction: %s", data.data)

def dance():
	rospy.init('dance', anonymous = True)
	
