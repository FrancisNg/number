import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
import math
import random


class NumberPublisher(Node):

    def __init__(self):
        super().__init__("number_publisher")
        self.pub = self.create_publisher(Int64, "/number", 10)
        self.timer = self.create_timer(5.0, self.timer_callback)
        

    def timer_callback(self):
        msg = Int64()
        msg.data = math.floor(random.random() * 10)
        self.pub.publish(msg)
        self.get_logger().info("Published to number: %d" % msg.data)

def main(args=None):
    rclpy.init(args=args)

    number_publisher = NumberPublisher()

    rclpy.spin(number_publisher)
    number_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()