# Introduction #

This tutorial introduces how graphical user interfaces can quickly be created using [rqt\_gui](http://ros.org/wiki/rqt_gui).


# Details #

[rqt\_gui](http://ros.org/wiki/rqt_gui) is a GUI framework for ROS that allows the creation of dialogs using either C++ or Python. For simplicity, we use a Python example. There is a good generic tutorial on creating Python plugins available on [ros.org](http://ros.org/wiki/rqt/Tutorials/Writing%20a%20Python%20Plugin). As an additional example, the [rqt\_rescue\_control\_plugin](https://code.google.com/p/irrw2012/source/browse/trunk/rqt_rescue_control_plugin/) is provided in the IRRW 2012 repository. This demonstrates how you can for example send the "reset" command on the "syscommand" topic used by hector\_mapping and the object\_tracker to reset the state of these nodes.

## Creating the reset button ##
```
        #Add a Pushbutton for resetting the system state
        resetPushButton = QPushButton("Reset State")       
        resetPushButton.pressed.connect(self.handleReset)
        self._syscommand_pub = rospy.Publisher('syscommand', String)
        vbox.addWidget(resetPushButton)
```
In the init function, the reset push button widget is created. The 'pressed' signal is then connected to the 'handleReset' callback (see below). The publisher for the 'syscommand' topic is created and finally the pushbutton is added to a existing vbox layout so it actually appears correctly in the GUI.


## Creating the reset callback ##
```
    def handleReset(self):
        tmp = String("reset")
        self._syscommand_pub.publish(tmp)
```
In the reset callback, the message content of the String message is set to "reset" and the message is sent using the publisher created before.

# Running it #
Provided everything is installed as described in the system setup instructions, rqt\_gui has the be started:
```
rosrun rqt_gui rqt_gui
```
In the 'Plugins' menu, the 'Rescue Control Dialog' can be started by selecting it.