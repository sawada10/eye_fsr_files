#!/usr/bin/python3
# -*- coding: utf-8 -*-

import rospy
import time
from std_msgs.msg import String
from std_msgs.msg import UInt16

"""
~~~ eye_status 対応表 ~~~
0: 通常
1: 瞬き
2: 驚き
3: 眠い
4: 怒り
5: 悲しむ/困る
6: 喜ぶ
"""     

class pubNode():
    def __init__(self):
        # Publisherの作成
        self.pub = rospy.Publisher('/eye_status', UInt16, queue_size=1)
    def publish(self, data):
        # publishする関数の作成
        self.pub.publish(data)

def sample_func(pub_msg, emotion):
    """
    "嬉しい"という入力が来たら、/eye_statusに"6"をpublishする関数
    """
    if emotion == "嬉しい":
        pub_msg.data = 6

def original_func(pub_msg, emotion):
    """
    この関数を編集してみましょう
    """
    if emotion == "嬉しい":
        pub_msg.data = 6
    elif emotion == "悲しい":
        pub_msg.data = 5
    elif emotion == "キレた":
        pub_msg.data = 4
    elif emotion == "寝たい":
        pub_msg.data = 3
    # elif emotion == "hoge":
    #   pub_msg.data = number

if __name__ == '__main__':
    # nodeを作る
    rospy.init_node('eye_test')
    # 3秒間sleepする
    time.sleep(3.0)
    # pubslishするノードを作る
    node = pubNode()


    while True:
        # emotionを入力する
        emotion =input("感情は?: ")
        # メッセージを初期化する
        pub_msg = UInt16()
        # もし"終わり"が入力したらプログラムを止める
        if emotion == "終わり":
            break
        #sample_func(pub_msg, emotion)
        original_func(pub_msg, emotion)
        # publishする
        node.publish(pub_msg)
