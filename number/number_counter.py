import rclpy
from rclpy.node import Node
import example_interfaces
from example_interfaces.msg import Int64
from example_interfaces.srv import SetBool

class NumberCounter(Node):

    def __init__(self):
        super().__init__("number_counter")
        self.srv = self.create_service(SetBool, "/reset_counter", self.counter_reset_callback)
        self.sub = self.create_subscription(Int64, "/number", self.listener_callback, 10)
        self.pub = self.create_publisher(Int64, "/number_counter", 10)
        self.timer = self.create_timer(5.0, self.pub_callback)
        self.count = 0
    
    def listener_callback(self, msg):
        self.count += msg.data
        self.get_logger().info("Recieved from number: %d, Count = %d" % (msg.data, self.count))

    def pub_callback(self):
        msg = Int64()
        msg.data = self.count
        self.pub.publish(msg)
        self.get_logger().info("Published to number counter: %d" % msg.data)
    
    def counter_reset_callback(self, request, response):
        if (request.data):
            self.count = 0
        response.success = True
        response.message = "Successfully reset the counter"
        return response

def main(args=None):
    rclpy.init(args=args)

    number_counter = NumberCounter()

    rclpy.spin(number_counter)
    number_counter.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
