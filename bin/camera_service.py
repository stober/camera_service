#! /usr/bin/env python
"""
Author: Jeremy M. Stober
Program: CAMERA_SERVICE.PY
Date: Thursday, January 12 2012
Description: User topic server to generate a camera service that returns Images.
"""

import roslib;roslib.load_manifest('camera_service')
import rospy
from topic_service import Topic2Service
from sensor_msgs.msg import Image
from camera_service.srv import ImageSrv

def transform(msg):
    return msg

cs = Topic2Service('camera_service','camera/image_raw','camera/image_request', Image, ImageSrv, transform)
cs.spin()
