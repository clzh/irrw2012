import os

from  qt_gui.qt_binding_helper import loadUi
from QtCore import QEvent, QObject, Qt, QTimer, Signal, Slot
from QtGui import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

import roslib
roslib.load_manifest('rqt_gui_rescue_control_plugin')
import rospy

from std_msgs.msg import String

class RescueControlDialog(QObject):

    _print_message_signal = Signal(str)

    def __init__(self, context):
        super(RescueControlDialog, self).__init__(context)
        self.setObjectName('RescueControlDialog')

        self.joint_states_pub={}
        self._widget = QWidget()
        
        vbox = QVBoxLayout()

        
        #Add a Pushbutton for resetting the system state
        resetPushButton = QPushButton("Reset State")       
        resetPushButton.pressed.connect(self.handleReset)
        self._syscommand_pub = rospy.Publisher('syscommand', String)
        vbox.addWidget(resetPushButton)
        
        #add stretch at end so all GUI elements are at top of dialog
        vbox.addStretch(1)
                  
        self._widget.setLayout(vbox) 
        
        context.add_widget(self._widget)
        
                 
    #Slot for  resetting the system state    
    def handleReset(self):
        tmp = String("reset")
        self._syscommand_pub.publish(tmp)
        
        
    #Stuff below needed for rqt_gui, do not edit (unless you know what you're doing)           
    def _unregisterPublisher(self):
        if self._publisher is not None:
            self._publisher.unregister()
            self._publisher = None
            
    def _unregisterSubscriber(self):
        if self._subscriber is not None:
            self._subscriber.unregister()
            self._subscriber = None

    def shutdown_plugin(self):
        self._unregisterPublisher()
        self._unregisterSubscriber()
