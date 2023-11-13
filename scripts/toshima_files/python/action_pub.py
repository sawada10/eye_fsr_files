#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16

class pubNode():
    def __init__(self):
        # Publisherの作成
        self.pub = rospy.Publisher('/action', String, queue_size=1)
    def publish(self, data):
        # publishする関数の作成
        self.pub.publish(data)

def sample_func(pub_msg, statement):
    """
    "元気だね"という入力が来たら、/eye_statusに"6"をpublishする関数
    """
    if statement == "元気だね":
        pub_msg.data = "nod"


def original_func(pub_msg, emotion):
    """
    この関数を編集してみましょう
    """
    if statement == "元気だね":
        pub_msg.data = "shake"
    # elif statement == "hoge":
    #   pub_msg.data = number

if __name__ == '__main__':
    # nodeを作る
    rospy.init_node("action_test")
    # 3秒間sleepする
    time.sleep(3.0)
    # pubslishするノードを作る
    node = pubNode()

    while True:
        # emotionを入力する
        statement =input("やあ！どうしたの？: ")
        # メッセージを初期化する
        pub_msg = String()
        # もし"終わり"が入力したらプログラムを止める
        if statement == "終わり":
            break
        sample_func(pub_msg, statement)
        # publishする
        node.publish(pub_msg)
