# Introduction #

This tutorial shows how to demonstrate a simulated Hector Lightweight UGV (HLUGV) in gazebo, including SLAM, mapping of objects of interest as well as optionally autonomous exploration.


# Details #
  * Build the hlugv\_apps package, this should result in all dependencies getting built:
```
rosmake hlugv_apps
```
  * Open a terminal, start a roscore
```
roscore
```
  * In a new terminal (press "CTRL" + "t" to create a new terminal tab) start a gazebo simulation scenario, for example
```
roslaunch hector_nist_arena_worlds thailand_robot_championship_2012_flat.launch
```
  * Spawn the simulated HLUGV into the scenario:
```
roslaunch hlugv_gazebo spawn_hlugv_cam_lidar.launch
```
  * Start the mapping, geotiff writing and object tracker using
```
roslaunch hlugv_apps hlugv_worldmodel_all.launch
```
  * There are now options on how to proceed:
    * You can now manually control the robot by using some method of publishing a [geometry\_msgs/Twist](http://www.ros.org/doc/api/geometry_msgs/html/msg/Twist.html) message on the 'cmd\_vel' topic.
    * You can start autonomous exploration using
```
 roslaunch hlugv_apps hector_simple_exploration.launch
```