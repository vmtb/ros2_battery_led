#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from example_interfaces.srv import SetBool;

class ResetCounter(Node):

    def __init__(self): 
        super().__init__("number_publisher")
        
        self.resetCounter(True)
        self.get_logger().info("Reset Counter has been started")
        
    def resetCounter(self, a):
        client = self.create_client(SetBool, 'reset_counter')
        while(not client.wait_for_service(1.0)): 
            self.get_logger().info("We are waiting for server to start")
        request = SetBool.Request()
        request.data = a 
        future = client.call_async(request)
        future.add_done_callback(self.onceResetIsDone)
            
    def onceResetIsDone(self, future):  
        try:
            response = future.result()
            self.get_logger().info("The reset is "+str(response.success)+" and the msg "+str(response.message))
        except Exception as e:
            self.get_logger().error("Service call failed %r"% (e))
    
def main(args = None):
    rclpy.init(args=args) #init communication
    node = ResetCounter()
    rclpy.spin(node) # will pause the program and continue to be alive
    rclpy.shutdown() #exit ros2 communication

if __name__ == "__main__":
    main()