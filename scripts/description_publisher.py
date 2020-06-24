#!/usr/bin/python
# Get the robot_description and publish it on a latched topic to be retrieved by ROS 2 if needed

import rospy
from std_msgs.msg import String

rospy.init_node('description_publisher')

description = rospy.get_param('/robot_description')

pub = rospy.Publisher('/robot_description', String, queue_size=10, latch=True)

#while not rospy.is_shutdown():
pub.publish(description)
#    rospy.sleep(0.5)
rospy.spin()
    
