#!/bin/bash
# vi: ts=8 sw=4 sts=4 et filetype=sh
#
# SPDX-License-Identifier: GPL-3.0-or-later

DEST_DIR=${1:-$HOME}

source /opt/ros/jazzy/setup.bash

mkdir -p ${DEST_DIR}/ws_ros2_camara/src

cd ${DEST_DIR}/ws_ros2_camara

colcon build

cd src

ros2 pkg create \
    --build-type ament_python \
    --license Apache-2.0 \
    ros2_opencv \
    --dependencies sensor_msgs std_msgs rclpy image_transport cv_bridge python3-opencv


# cd ${DEST_DIR}/ws_ros2_camara
#
# rosdep install -i --from-path src/ --rosdistro $ROS_DISTRO
# 
# sudo rosdep init
# rosdep update
# 
# colcon build
# 
###################################
#
## source /opt/ros/jazzy/setup.bash
## source ${DEST_DIR}/ws_ros2_camara/install/setup.bash
# ros2 run ros2_opencv publisher_node
# ros2 run ros2_opencv subscriber_node
# rqt_graph
