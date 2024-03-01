#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64

class NumberCounter(Node):

    def __init__(self): 
        super().__init__("number_counter")
        self.counter = 0 
        self.publisher_ = self.create_publisher(Int64, 'number_count', 10); 
        self.subs_ = self.create_subscription(Int64, 'number', self.getNumber, 10,)
        self.timer_ = self.create_timer(1, self.publishNumber)
        self.number = 0
        
    def getNumber(self, msg): 
        self.number = msg.data
        self.get_logger().info(f"Received number: {self.number }")
        

    def publishNumber(self): 
        msg = Int64()
        msg.data = self.number*2
        self.publisher_.publish(msg)
        
def main(args = None):
    rclpy.init(args=args) #init communication
    node = NumberCounter()
    rclpy.spin(node) # will pause the program and continue to be alive
    rclpy.shutdown() #exit ros2 communication

if __name__ == "__main__":
    main()