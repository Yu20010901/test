#!/usr/bin/env python
import rospy
rospy.init_node("hello_ptyhon_node")
rospy.loginfo("Hello World")
from time import sleep
n=0
while n<10:
    n=n+1	
    print(n)
    sleep(1)
print("times up")
