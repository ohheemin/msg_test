#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from msg_test.msg import Sum  

class SumSubscriber(Node):

    def __init__(self):
        super().__init__('sum_subscriber')
        self.subscription = self.create_subscription(
            Sum,
            'sum_topic',
            self.listener_callback,
            1)
        self.subscription 
        self.get_logger().info("Sum Subscriber Node has been started.")

    def listener_callback(self, msg):
        self.get_logger().info(f"Received: a={msg.a}, b={msg.b}, sum={msg.sum}")
        
        new_number = int(input("Enter a new number to multiply with the sum: "))

        result = msg.sum * new_number

        self.get_logger().info(f"The result of sum * new number ({msg.sum} * {new_number}) is: {result}")

def main(args=None):
    rclpy.init(args=args)

    sum_subscriber = SumSubscriber()

    rclpy.spin(sum_subscriber)

    sum_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
