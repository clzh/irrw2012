# Introduction #

We use ROS fuerte on a Ubuntu 12.04 machine. To be able to make the most of the workshop you should set it up like described. You can also use a virtual machine, but this might not work well with some of the ROS visualization tools.

# Details #

## ROS Setup ##

  * ROS needs to be installed. Very detailed instructions for that are available [here](http://www.ros.org/wiki/fuerte/Installation/Ubuntu). Choose the "ros-fuerte-desktop-full" install if you have the disk space and bandwidth available to do so.
  * After installation, open a new terminal and try to use a ROS command:
```
roscd
```
> If this complains about "ROS\_WORKSPACE", the installation worked.
  * Install additional useful packages:
```
sudo apt-get install ros-fuerte-rqt ros-fuerte-pr2-simulator
```


## Repository Setup ##

  * To use some existing software, we need to check out software from different repositories. These are:
    * [tu darmstadt ros pkg](http://tu-darmstadt-ros-pkg.googlecode.com/svn/trunk/) (svn)
    * The repository belonging to this workshop [irrw2012](http://irrw2012.googlecode.com/svn/trunk/) (svn)
  * We use a quick manual setup of repositories (a rosinstall based method could also be used)
    * Enter your '/opt' directory and create a new 'repositories' directory:
```
cd /opt
sudo mkdir repositories
```
    * Change the user rights so you have full access:
```
sudo chown $USER repositories
```
    * Check out the used repositories:
```
cd repositories
svn co https://irrw2012.googlecode.com/svn/trunk/ irrw2012
svn co https://tu-darmstadt-ros-pkg.googlecode.com/svn/trunk/ tu-darmstadt-ros-pkg
```
> > Note that the second repository URL has been changed recently due to a repository structure change
    * Add the 'repositories' directory to the ROS\_PACKAGE\_PATH, so ROS "knows it". This is done by adding a line to your '~/.bashrc' file:
```
echo export ROS_PACKAGE_PATH=/opt/repositories:\$ROS_PACKAGE_PATH >> ~/.bashrc
```
    * Open a new terminal and try building hector\_mapping:
```
rosmake hector_mapping
```

## Updating Repositories ##
  * Use this line to update both repositories to the most recent state:
```
svn up /opt/repositories/irrw2012/ /opt/repositories/tu-darmstadt-ros-pkg/
```