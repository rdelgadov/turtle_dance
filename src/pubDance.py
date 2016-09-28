#!/usr/bin/env python
# license removed for brevity
import rospy
from std_msgs.msg import String

def pubDance():
    pub = rospy.Publisher('dance', String, queue_size=10)
    rospy.init_node('pubDance', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while True:
		pub.publish("Un pasito maria")
		rate.sleep()

if __name__ == '__main__':
    try:
        pubDance()
    except rospy.ROSInterruptException:
        pass
