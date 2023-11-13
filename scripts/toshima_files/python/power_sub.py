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
        ## もしも、コールバック関数を編集したいときは、下の行の"#"を外す
        # self.sub = rospy.Subscriber('/power', Float32, self.original_callback)

    def callback(self, sub_msg):
        # SubscribeしたメッセージからFSRのセンサ値を取り出す
        power_value = sub_msg.data
        print("received power :{}".format(power_value))

    def original_callback(self, sub_msg):
        # SubscribeしたメッセージからFSRのセンサ値を取り出す
        power_value = sub_msg.data
        print("received power :{}".format(power_value))
        if power_value >= 0 and power_value <= 50:
            print ("ド")
        elif power_value > 50 and power_value <= 100:
            print("レ")
        elif power_value > 100 and power_value <= 150:
            print("ミ")
        else:
            print("ファ")

if __name__ == '__main__':
    rospy.init_node('power_to_message')

    time.sleep(3.0)
    node = pubsubNode()

    while not rospy.is_shutdown():
        rospy.sleep(0.1)
