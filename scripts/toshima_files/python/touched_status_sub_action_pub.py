#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String

class pubsubNode():
    def __init__(self):
        # Subscriberの作成
        self.sub = rospy.Subscriber('/touched_status', String, self.callback, queue_size = 1)
        # Publisherの作成
        self.pub = rospy.Publisher('/action', String, queue_size=1)

    def callback(self, data):
        pub_msg = String()
        if data.data == "touched":
            pub_msg.data = "nod"
            self.publish(pub_msg)
            time.sleep(10)
        else:
            pub_msg.data = "nothing"
            self.publish(pub_msg)

    def publish(self, data):
        self.pub.publish(data)

if __name__ == '__main__':
    rospy.init_node('touch_to_action')

    time.sleep(3.0)
    node = pubsubNode()

    while not rospy.is_shutdown():
        rospy.sleep(0.1)
