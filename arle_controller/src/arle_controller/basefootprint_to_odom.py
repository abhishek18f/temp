#!/usr/bin/env python
import rospy 
import roslib

# to get commandline arguments
import sys

# because of transformations
import tf

import tf2_ros
import geometry_msgs.msg

if __name__ == '__main__':
  
  rospy.init_node('basefootprint_to_odom')
  rate = rospy.Rate(100)
  br = tf.TransformBroadcaster()

  while 1:

    br.sendTransform((0,0, 0),
                     tf.transformations.quaternion_from_euler(0, 0, 0),
                     rospy.Time.now(),
                     "odom",
                     "base_footprint")
    rate.sleep()
  rospy.spin()
