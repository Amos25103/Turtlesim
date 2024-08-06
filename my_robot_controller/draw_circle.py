#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
#use ros2 topic list, info , to find what to import 

class DrawCircleNode(Node):

    def __init__(self):
        super().__init__("draw_circle")
        #this is use to create a publisher , give it a name and use the function
        self.cmd_vel_pub_ = self.create_publisher(Twist, "/turtle1/cmd_vel",10)
        self.timer_ = self.create_timer(0.5 , self.send_velocity_msgs)
        self.get_logger().info("draw circle started")

    def send_velocity_msgs(self):
        msg=Twist()
        msg.linear.x= 2.0
        msg.angular.z = 1.0
        self.cmd_vel_pub_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node=DrawCircleNode()

    rclpy.spin(node)
    rclpy.shutdown()