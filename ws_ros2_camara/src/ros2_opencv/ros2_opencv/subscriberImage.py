#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:                                                  
import cv2 as cv

import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class SubscriberNodeClass(Node):

    def __init__(self):

        super().__init__('subscriber_node')

        self.bridge = CvBridge()

        self.topic_name = 'topic_camera_image'

        self.queue_size = 20

        self.subscription = self.create_subscription(Image, self.topic_name,
                                                     self.listener_callback_function,
                                                     self.queue_size)

    def listener_callback_function(self, image_msg):

        self.get_logger().info('The image frame is recieved')
        opencv_img = self.bridge.imgmsg_to_cv2(image_msg)

        cv.imshow("Camera video", opencv_img)
        cv.waitKey(1)

def main(args=None):

    rclpy.init(args=args)

    subscriber = SubscriberNodeClass()

    rclpy.spin(subscriber)

    subscriber.destroy_node()

    rclpy.shutdown()

    
if __name__ == '__main__':
    main()
