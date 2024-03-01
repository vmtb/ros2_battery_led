#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64;
from example_interfaces.srv import SetBool

class NumberPublisher(Node):

    def __init__(self): 
        super().__init__("number_publisher")
        self.counter = 0 
        self.publisher_ = self.create_publisher(Int64, 'number', 10); 
        self.timer_ = self.create_timer(1, self.publishNumber)
        self.resetcounterservice_ = self.create_service(SetBool, 'reset_counter', self.resetServiceServer)
        self.number = 0
        self.get_logger().info("Number publisher has been started")
        
    
    def publishNumber(self):
        self.number+=2
        msg= Int64()
        msg.data = self.number
        self.publisher_.publish(msg)
        
    def resetServiceServer(self, request, response): 
        reset_ = request.data 
        if(reset_):
            self.number = 0
        response.success = True 
        response.message = "Done !"
        return response
    
def main(args = None):
    rclpy.init(args=args) #init communication
    node = NumberPublisher()
    rclpy.spin(node) # will pause the program and continue to be alive
    rclpy.shutdown() #exit ros2 communication

if __name__ == "__main__":
    main()