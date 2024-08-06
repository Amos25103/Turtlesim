#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose

class Getlocation(Node):

    def __init__(self):
        super().__init__("pose_subsciber")
        #this is use to create a subscriber , give it a name and use the function
        self.pose_subsriber_ = self.create_subscription(
            Pose, "/turtle1/pose",self.pose_callback,10)

    def pose_callback(self, msg:Pose):
        self.get_logger().info("(" + str(msg.x) + "," + str(msg.y) + ")")


def main(args=None):
    rclpy.init(args=args)
    node=Getlocation()

    rclpy.spin(node)
    rclpy.shutdown()