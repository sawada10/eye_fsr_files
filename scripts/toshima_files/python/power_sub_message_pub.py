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
        #self.sub = rospy.Subscriber('/power', Float32, self.original_callback)
        # Publisherの作成
        self.pub = rospy.Publisher('/power_message', String, queue_size=1)

    def callback(self, sub_msg):
        # SubscribeしたメッセージからFSRのセンサ値を取り出す
        power = sub_msg.data
        print("received power :{}".format(power))
        # Publishするメッセージのテンプレート
        pub_msg = String()
        # センサ値をPublishするメッセージに入れる
        pub_msg.data = "Received power {}".format(power)
        # メッセージをPublishする
        self.publish(pub_msg)

    def original_callback(self, sub_msg):
        # SubscribeしたメッセージからFSRのセンサ値を取り出す
        power = sub_msg.data
        print("received power :{}".format(power))
        if power >= 0 and power <= 50:
            print ("ド")
        elif power > 50 and power <= 100:
            print("レ")
        elif power > 100 and power <= 150:
            print("ミ")
        else:
            print("ファ")
        # Publishするメッセージのテンプレート
        pub_msg = String()
        # センサ値をPublishするメッセージに入れる
        pub_msg.data = "Received power {}".format(power)
        # メッセージをPublishする
        self.publish(pub_msg)

    def publish(self, data):
        self.pub.publish(data)

if __name__ == '__main__':
    rospy.init_node('power_to_message')

    time.sleep(3.0)
    node = pubsubNode()

    while not rospy.is_shutdown():
        rospy.sleep(0.1)
