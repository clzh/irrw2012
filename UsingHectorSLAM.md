# Introduction #

Add your content here.

# Processing pre-recorded data #

Using the data logging functionality built into ROS, logfiles can be processed. A tutorial on how to do this is available on ros.org: [How to build a Map Using Logged Data](http://www.ros.org/wiki/hector_slam/Tutorials/MappingUsingLoggedData)

# Processing live data #

To process live data, a source of [sensor\_msgs/LaserScan](http://www.ros.org/doc/api/sensor_msgs/html/msg/LaserScan.html) messages (for example a Hokuyo LIDAR) and a [tf-based](http://ros.org/wiki/tf) transform between the laser and a robot base frame has to be available. There also is a tutorial on [How to set up hector\_slam for your robot](http://www.ros.org/wiki/hector_slam/Tutorials/SettingUpForYourRobot) on ros.org.