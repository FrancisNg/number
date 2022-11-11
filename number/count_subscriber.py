import rclpy
from rclpy.node import Node

from example_interfaces.msg import Int64


class CountSubscriber(Node):

    def __init__(self):
        super().__init__('count_subscriber')
        self.subscription = self.create_subscription(Int64, "/number_counter", self.listener_callback, 10)
        self.subscription

    def listener_callback(self, msg):
        self.get_logger().info("Recieved from number counter: %d" % msg.data)


def main(args=None):
    rclpy.init(args=args)

    count_subscriber = CountSubscriber()

    rclpy.spin(count_subscriber)
    count_subscriber.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()