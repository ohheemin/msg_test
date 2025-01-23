#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from msg_test.msg import Sum  

class SumPublisher(Node):

    def __init__(self):
        super().__init__('sum_publisher')
        self.publisher_ = self.create_publisher(Sum, 'sum_topic', 1)
        self.timer_ = self.create_timer(1.0, self.publish_sum)
        self.get_logger().info("Sum Publisher Node has been started.")

    def publish_sum(self):
        a = int(input("Enter the first number (a): "))
        b = int(input("Enter the second number (b): "))

        msg = Sum()
        msg.a = a
        msg.b = b
        msg.sum = a + b 

        self.publisher_.publish(msg)
        self.get_logger().info(f"Publishing: a={a}, b={b}, sum={msg.sum}")

def main(args=None):
    rclpy.init(args=args)

    sum_publisher = SumPublisher()

    rclpy.spin(sum_publisher)

    sum_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
