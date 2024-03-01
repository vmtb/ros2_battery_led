#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import LedState
from my_robot_interfaces.srv import SetLed

class LedPanel(Node):

    def __init__(self): 
        super().__init__("led_panel")
        self.get_logger().info("LedPanel node has been started")
        self.states = [0,0,0]
        self.service_ = self.create_service(SetLed, 'set_led', self.setLedRequest)
        self.publisher_ = self.create_publisher(LedState, 'led_panel_state', 10)
        self.timer_ = self.create_timer(2, self.publishLedState)
        self.counter = 0 
    
    
    def setLedRequest(self, request, response):
        pos = request.number 
        if(pos < 0 or pos >2):
            response.success = False
        else: 
            self.states[pos] = 1 if (request.state=="on") else 0
            response.success = True
        return response
    
    def publishLedState(self):
        msg = LedState()
        msg.ledstates = self.states
        self.publisher_.publish(msg)
        
        
def main(args = None):
    rclpy.init(args=args) #init communication
    node = LedPanel()
    rclpy.spin(node) # will pause the program and continue to be alive
    rclpy.shutdown() #exit ros2 communication < >

if __name__ == "__main__":
    main()