from __future__ import annotations
import numpy as np 
import cv2

from visual_odometry import PinholeCamera, VisualOdometry

import numpy as np
import matplotlib.pyplot as plt

cam = PinholeCamera(1241.0, 376.0, 718.8560, 718.8560, 607.1928, 185.2157)
ground_truth = VisualOdometry(cam, '/home/xxs90/Documents/orb-slam3/data_odometry/data_odometry_poses/00.txt')
orb_slam3 = VisualOdometry(cam, '/home/xxs90/Documents/orb-slam3/ORB_SLAM3/Examples/traj00.txt')
# ground_truth = VisualOdometry(cam, '/home/xxs90/Documents/orb-slam3/data_odometry/data_odometry_poses/05.txt')
# orb_slam3 = VisualOdometry(cam, '/home/xxs90/Documents/orb-slam3/ORB_SLAM3/Examples/traj05.txt')
# ground_truth = VisualOdometry(cam, '/home/xxs90/Documents/orb-slam3/data_odometry/data_odometry_poses/07.txt')
# orb_slam3 = VisualOdometry(cam, '/home/xxs90/Documents/orb-slam3/ORB_SLAM3/Examples/traj07.txt')

traj = np.zeros((600,600,3), dtype=np.uint8)

data_length = min(ground_truth.getSize() // 2, orb_slam3.getSize())
print('Ground Truth: ', (ground_truth.getSize() // 2))
print('ORB_SLAM3:', orb_slam3.getSize())

for img_id in range(data_length):

	ground_truth.getAbsoluteScale(img_id*2)
	orb_slam3.getAbsoluteScaleORB(img_id)

	# true_x, true_y = int(ground_truth.trueX)+290, int(ground_truth.trueZ)+300 # 07
	# orb3_x, orb3_y = int(orb_slam3.orb3_X)*10+290, int(orb_slam3.orb3_Z)*9+300 # 07
	true_x, true_y = int(ground_truth.trueX)+290, int(ground_truth.trueZ)+90 # 00
	orb3_x, orb3_y = int(orb_slam3.orb3_X)*16+290, int(orb_slam3.orb3_Z)*17+90 # 00
	# true_x, true_y = int(ground_truth.trueX)+290, int(ground_truth.trueZ)+150 # 05
	# orb3_x, orb3_y = int(orb_slam3.orb3_X)*24+290, int(orb_slam3.orb3_Z)*24+150 # 05
	

	cv2.circle(traj, (true_x, true_y), 2, (0, 0, 255), 2)
	#(InputOutputArray, Point, radius, color, thickness)
	cv2.circle(traj, (orb3_x, orb3_y), 1, (0,255,0), 2)
	cv2.rectangle(traj, (10, 20), (600, 60), (0,0,0), -1)
	text1 = "Coordinates: x=%2fm y=%2fm"%(true_x, true_y)
	text2 = "Coordinates: x=%2fm y=%2fm"%(orb3_x, orb3_y)
	cv2.putText(traj, text1, (20,40), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, 8)
	cv2.putText(traj, text2, (20,60), cv2.FONT_HERSHEY_PLAIN, 1, (255,255,255), 1, 8)
	
	cv2.imshow('Trajectory', traj)
	cv2.waitKey(10)

cv2.imwrite('map.png', traj)
plt.show()
