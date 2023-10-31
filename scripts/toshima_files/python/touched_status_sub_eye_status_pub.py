#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16

class pubsubNode():
    def __init__(self):
        # Subscriberの作成
        self.sub = rospy.Subscriber('/touched_status', String, self.callback)
        # Publisherの作成
        self.pub = rospy.Publisher('/eye_status', UInt16, queue_size=1)

    def callback(self, data):
        pub_msg = UInt16()
        if data.data == "touched":
            pub_msg.data = 6
        else:
            pub_msg.data = 0

        self.publish(pub_msg)

    def publish(self, data):
        self.pub.publish(data)

if __name__ == '__main__':
    rospy.init_node('touch_to_eye')

    time.sleep(3.0)
    node = pubsubNode()

    while not rospy.is_shutdown():
        rospy.sleep(0.1)
