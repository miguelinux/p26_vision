#!/usr/bin/env python3
# vi: set shiftwidth=4 tabstop=8 expandtab:                                                  
import cv2 as cv

import rclpy
from sensor_msgs.msg import Image
from rclpy.node import Node
from cv_bridge import CvBridge

class PublisherNodeClass(Node):

    def __init__(self):

        super().__init__('publisher_node')

        self.camera_device_number = 0
        self.camera = cv.VideoCapture(self.camera_device_number)
        self.bridge = CvBridge()

        self.topic_name = 'topic_camera_image'

        self.queue_size = 20

        self.publisher = self.create_publisher(Image, self.topic_name,
                                               self.queue_size)

        self.period_communication = 0.02

        self.timer = self.create_timer(self.period_communication,
                                       self.timer_callback_function)

        self.counter = 0

    def timer_callback_function(self):

        success, frame = self.camera.read()

        if success:
            frame = cv.resize(frame, (820,640), interpolation=cv.INTER_CUBIC)

            ROS2_image_msg = self.bridge.cv2_to_imgmsg(frame)
            self.publisher.publish(ROS2_image_msg)

            self.get_logger().info("Publishing image number %d" % self.counter)
            self.counter += 1


def main(args=None):

    rclpy.init(args=args)

    publisher = PublisherNodeClass()

    rclpy.spin(publisher)

    publisher.destroy_node()

    rclpy.shutdown()


if __name__ == '__main__':
    main()
