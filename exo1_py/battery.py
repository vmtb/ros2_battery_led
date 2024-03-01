#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from functools import partial
from my_robot_interfaces.srv import SetLed

class Battery(Node):

    def __init__(self): 
        super().__init__("battery")
        self.get_logger().info("Battery Node has been started")
        self.battery_state = True # Full 
        self.timer_ = self.create_timer(4, partial(self.fullOrEmptyBattery, full=False))
        self.counter = 0 
    
    def fullOrEmptyBattery(self, full): 
        self.battery_state = full 
        self.get_logger().info("Changing state to "+str(full))
        self.timer_.cancel()
        if(full): 
            self.timer_ = self.create_timer(4, partial(self.fullOrEmptyBattery, full=False))
        else:
            self.timer_ = self.create_timer(6, partial(self.fullOrEmptyBattery, full=True))
        self.callSetLed()
    
    def callSetLed(self):  
        client = self.create_client(SetLed, 'set_led') 
        while(not client.wait_for_service(1.0)): 
            self.get_logger().info("We are waiting for server to start")
        request = SetLed.Request()
        request.number = 2 
        request.state = "off" if self.battery_state else "on"
        future = client.call_async(request)
        future.add_done_callback(self.displaySetLedResult)
    
    def displaySetLedResult(self, future):
        try:
            response = future.result()
            if(response.success):
                self.get_logger().info("Led switched successfully")
            else:
                self.get_logger().info("Fatal error while switching the Led") 
        except: 
            self.get_logger().error("Something were wrong during the request")
    
def main(args = None):
    rclpy.init(args=args) #init communication
    node = Battery()
    rclpy.spin(node) # will pause the program and continue to be alive
    rclpy.shutdown() #exit ros2 communication < >

if __name__ == "__main__":
    main()