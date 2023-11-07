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
        self.pub = rospy.Publisher('/power_message', String, queue_size=1)

    def callback(self, sub_msg):
        power = sub_msg.data
        pub_msg = String()
        pub_msg.data = "Received power {}".format(power)
        self.publish(pub_msg)

    def publish(self, data):
        self.pub.publish(data)

if __name__ == '__main__':
    rospy.init_node('power_to_message')

    time.sleep(3.0)
    node = pubsubNode()

    while not rospy.is_shutdown():
        rospy.sleep(0.1)
