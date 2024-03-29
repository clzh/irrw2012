import os

from python_qt_binding.QtCore import QEvent, QObject, Qt, QTimer, Signal, Slot
from python_qt_binding.QtGui import QWidget, QPushButton, QHBoxLayout, QVBoxLayout, QLabel

import roslib
roslib.load_manifest('rqt_rescue_control_plugin')
import rospy

from std_msgs.msg import String
from worldmodel_msgs.srv import AddObject
from worldmodel_msgs.msg import ObjectState

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
        
        #Add a Pushbutton for adding a victim in front of the robot and projecting it against the wall
        addVictimInFrontOfRobotPushButton = QPushButton("Add victim in front of robot")       
        addVictimInFrontOfRobotPushButton.pressed.connect(self.on_add_victim_in_front_of_robot_pressed)
        vbox.addWidget(addVictimInFrontOfRobotPushButton)
        
        
        #add stretch at end so all GUI elements are at top of dialog
        vbox.addStretch(1)
                  
        self._widget.setLayout(vbox) 
        
        context.add_widget(self._widget)
        
                 
    #Slot for  resetting the system state    
    def handleReset(self):
        tmp = String("reset")
        self._syscommand_pub.publish(tmp)
        
        
    def on_add_victim_in_front_of_robot_pressed(self):
            
        try:
            add_victim = rospy.ServiceProxy('worldmodel/add_object', AddObject)
            
            req = AddObject._request_class()
            req.object.header.frame_id = 'base_link'
            req.object.header.stamp = rospy.Time(0)
            req.map_to_next_obstacle = True
            req.object.info.class_id = "victim"
            req.object.info.support = 100
            req.object.pose.pose.position.x = 0.1
            req.object.pose.pose.position.y = 0
            req.object.pose.pose.position.z = 0
            req.object.pose.pose.orientation.w = 1
            req.object.state.state = ObjectState.CONFIRMED

            resp = add_victim(req)
            
            status_msg = "added Victim, id = "
            status_msg += resp.object.info.object_id
            print(status_msg)
            
            #self._task_id = resp.object.info.object_id
            #self._victimAnswer = VictimAnswer.CONFIRM
            #self._publish_answer()
            
        except rospy.ServiceException, e:
	    #@TODO: Make this more expressive
	    print("service call failed")
  
        
        

