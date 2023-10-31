#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import Float32

class pubsubNode():
    def __init__(self):
        # Subscriberの作成
        self.sub = rospy.Subscriber('/power', Float32, self.callback)
        # Publisherの作成
        self.pub = rospy.Publisher('/touched_status', String, queue_size=1)

    def callback(self, data):
        pub_msg = String()
        if data.data >= 50:
            pub_msg.data = "touched"
        else:
            pub_msg.data = "released"

        self.publish(pub_msg)

    def publish(self, data):
        self.pub.publish(data)

if __name__ == '__main__':
    rospy.init_node('power_to_touch')

    time.sleep(3.0)
    node = pubsubNode()

    while not rospy.is_shutdown():
        rospy.sleep(0.1)
