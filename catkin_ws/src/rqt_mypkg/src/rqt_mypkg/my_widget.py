import os
import time
import sys
import rospy
import rospkg

from python_qt_binding import loadUi
from python_qt_binding.QtCore import Qt
from python_qt_binding.QtGui import QFileDialog, QGraphicsView, QIcon, QWidget,QDoubleValidator, QIntValidator

class MyGraphicsView(QGraphicsView):
    def __init__(self, parent=None):
        super(MyGraphicsView, self).__init__()

class MyWidget(QWidget):
    def __init__(self,context):
        super(MyWidget, self).__init__()
        rp = rospkg.RosPack()
        ui_file = os.path.join(rp.get_path('rqt_mypkg'), 'resource', 'MyPlugin.ui')
        loadUi(ui_file, self, {'MyGraphicsView': MyGraphicsView})

        rospy.set_param('/parameter/button/playbutton',False)
        rospy.set_param('/parameter/button/frwdbutton',False)
        rospy.set_param('/parameter/button/backbutton',False)
        rospy.set_param('/parameter/button/leftbutton',False)
        rospy.set_param('/parameter/button/rightbutton',False)
        rospy.set_param('/parameter/button/servo_up',False)
        rospy.set_param('/parameter/button/servo_down',False)
        rospy.set_param('/parameter/button/screw_in',False)
        rospy.set_param('/parameter/button/screw_out',False)
        rospy.set_param('/parameter/indiv',False)
        rospy.set_param('/parameter/combo',False)
        rospy.set_param('/parameter/motor/pwm_val',0)
       

        self.setObjectName('MyWidget')
        
        self.pause_icon = QIcon.fromTheme('media-playback-pause')
        self.forward_icon = QIcon.fromTheme('up')
        self.backward_icon = QIcon.fromTheme('down')
        self.left_icon = QIcon.fromTheme('back')
        self.right_icon = QIcon.fromTheme('forward')

        self.servo_icon = QIcon.fromTheme('up')
        self.screw_in_icon = QIcon.fromTheme('back')
        self.screw_out_icon = QIcon.fromTheme('forward')

        self.up_linear_push_button.setIcon(self.forward_icon)
        self.back_linear_push_button.setIcon(self.backward_icon)
        self.left_linear_push_button.setIcon(self.left_icon)
        self.right_linear_push_button.setIcon(self.right_icon)
        self.servo_up_push_button.setIcon(self.servo_icon)
        
        self.screw_in_push_button.setIcon(self.screw_in_icon)
        self.screw_out_push_button.setIcon(self.screw_out_icon)

        self.up_linear_push_button.clicked[bool].connect(self._handle_frwd_clicked)
        self.back_linear_push_button.clicked[bool].connect(self._handle_back_clicked)
        self.left_linear_push_button.clicked[bool].connect(self._handle_left_clicked)
        self.right_linear_push_button.clicked[bool].connect(self._handle_right_clicked)

        self.servo_up_push_button.clicked[bool].connect(self._handle_servo_clicked)
        self.screw_in_push_button.clicked[bool].connect(self._handle_screw_in_clicked)
        self.screw_out_push_button.clicked[bool].connect(self._handle_screw_out_clicked)

     
        self.up_linear_push_button.setEnabled(True)
        self.back_linear_push_button.setEnabled(True)
        self.left_linear_push_button.setEnabled(True)
        self.right_linear_push_button.setEnabled(True)
        self.servo_up_push_button.setEnabled(True)
        self.screw_in_push_button.setEnabled(True)
        self.screw_out_push_button.setEnabled(True)      

        self.indiv_check_box.clicked.connect(self.indiv_callback)
        self.combo_check_box.clicked.connect(self.combo_callback)
        self.robot1_check_box.clicked.connect(self.robot1_callback)
        self.robot2_check_box.clicked.connect(self.robot2_callback)
        self.robot3_check_box.clicked.connect(self.robot3_callback)
        self.robot4_check_box.clicked.connect(self.robot4_callback)
        self.robot5_check_box.clicked.connect(self.robot5_callback)
        self.robot6_check_box.clicked.connect(self.robot6_callback)
        self.robot7_check_box.clicked.connect(self.robot7_callback)
        self.robot8_check_box.clicked.connect(self.robot8_callback)
        


        rospy.Timer(rospy.Duration(0.05), self.value_cb)

    
    print "stopped"

    def _handle_frwd_clicked(self,checked):
        if checked:
            rospy.set_param('/parameter/button/frwdbutton',True)
            #self.max_x_linear_double_spin_box.value()
            #print (rospy.get_param('/parameter/button/frwdbutton'))
            print "forward movement"
        else:
            rospy.set_param('/parameter/button/frwdbutton',False)
            #print (rospy.get_param('/parameter/button/frwdbutton'))
            print "stopped"

    def _handle_back_clicked(self,checked):
        if checked:
            rospy.set_param('/parameter/button/backbutton',True)
            #print (rospy.get_param('/parameter/button/backbutton'))
            print "backward turn"
        else:
            rospy.set_param('/parameter/button/backbutton',False)
            #print (rospy.get_param('/parameter/button/backbutton'))
            print "stopped"

    def _handle_left_clicked(self,checked):
        if checked:
            rospy.set_param('/parameter/button/leftbutton',True)
            #print (rospy.get_param('/parameter/button/leftbutton'))
            print "left turn"
        else:
            rospy.set_param('/parameter/button/leftbutton',False)
            #print (rospy.get_param('/parameter/button/leftbutton'))
            print "stopped"

    def _handle_right_clicked(self,checked):
        if checked:
            rospy.set_param('/parameter/button/rightbutton',True)
            #print (rospy.get_param('/parameter/button/rightbutton'))
            print "right movement"
        else:
            rospy.set_param('/parameter/button/rightbutton',False)
            #print (rospy.get_param('/parameter/button/rightbutton'))
            print "stopped"

    def _handle_servo_clicked(self,checked):
        if checked:
        	print "servo up"
        	rospy.set_param('/parameter/button/servo_up',True)
        	rospy.set_param('/parameter/button/servo_down',False)
        	
        else:
        	print "servo down"
        	rospy.set_param('/parameter/button/servo_up',False)
        	rospy.set_param('/parameter/button/servo_down',True)

    def _handle_screw_in_clicked(self,checked):
        if checked:
        	rospy.set_param('/parameter/button/screw_in',True)
        	#print "screw in"
        	#rospy.set_param('/parameter/button/servo_down',False)
        else:
        	rospy.set_param('/parameter/button/screw_in',False)
        	#rospy.set_param('/parameter/button/servo_up',False)
        	#rospy.set_param('/parameter/button/servo_down',True)

    def _handle_screw_out_clicked(self,checked):
        if checked:
        	rospy.set_param('/parameter/button/screw_out',True)
        	#print "screw out"
        	#rospy.set_param('/parameter/button/servo_down',False)
        else:
        	rospy.set_param('/parameter/button/screw_out',False)
        	#rospy.set_param('/parameter/button/servo_up',False)
        	#rospy.set_param('/parameter/button/servo_down',True)

    def indiv_callback(self,checked):
        if checked:
            print "indiv selected"
            rospy.set_param('/parameter/indiv',True)
            rospy.set_param('/parameter/robot1',False)
            rospy.set_param('/parameter/robot2',False)
            rospy.set_param('/parameter/robot3',False)
            rospy.set_param('/parameter/robot4',False)
            rospy.set_param('/parameter/robot5',False)
            rospy.set_param('/parameter/robot6',False)
            rospy.set_param('/parameter/robot7',False)
            rospy.set_param('/parameter/robot8',False)


        else:
        	rospy.set_param('/parameter/indiv',False)
        	rospy.delete_param('/parameter/robot1')
        	rospy.delete_param('/parameter/robot2')
        	rospy.delete_param('/parameter/robot3')
        	rospy.delete_param('/parameter/robot4')
        	rospy.delete_param('/parameter/robot5')
        	rospy.delete_param('/parameter/robot6')
        	rospy.delete_param('/parameter/robot7')
        	rospy.delete_param('/parameter/robot8')

    def combo_callback(self,checked):
        if checked:
            print "combo selected"
            rospy.set_param('/parameter/combo',True)
        else:
            rospy.set_param('/parameter/combo',False)
    def robot1_callback(self,checked):
    	if checked:
    		rospy.set_param('/parameter/robot1',True)
    	else:
    		rospy.set_param('/parameter/robot1',False)
    		#rospy.delete_param('/parameter/robot1')
    def robot2_callback(self,checked):
    	if checked:
    		rospy.set_param('/parameter/robot2',True)
    	else:
    		rospy.set_param('/parameter/robot2',False)
    		#rospy.delete_param('/parameter/robot2')
    def robot3_callback(self,checked):
    	if checked:
    		rospy.set_param('/parameter/robot3',True)
    	else:
    		rospy.set_param('/parameter/robot3',False)
    		#rospy.delete_param('/parameter/robot3')
    def robot4_callback(self,checked):
    	if checked:
    		rospy.set_param('/parameter/robot4',True)
    	else:
    		rospy.set_param('/parameter/robot4',False)
    		#rospy.delete_param('/parameter/robot4')
    def robot5_callback(self,checked):
    	if checked:
    		rospy.set_param('/parameter/robot5',True)
    	else:
    		rospy.set_param('/parameter/robot5',False)
    		#rospy.delete_param('/parameter/robot5')
    def robot6_callback(self,checked):
    	if checked:
    		rospy.set_param('/parameter/robot6',True)
    	else:
    		rospy.set_param('/parameter/robot6',False)
    		#rospy.delete_param('/parameter/robot6')
    def robot7_callback(self,checked):
    	if checked:
    		rospy.set_param('/parameter/robot7',True)
    	else:
    		rospy.set_param('/parameter/robot7',False)
    		#rospy.delete_param('/parameter/robot7')
    def robot8_callback(self,checked):
    	if checked:
    		rospy.set_param('/parameter/robot8',True)
    	else:
    		rospy.set_param('/parameter/robot8',False)
    		#rospy.delete_param('/parameter/robot8')


    def value_cb(self,event=None):
        #print self.max_x_linear_double_spin_box.value()
        rospy.set_param('/parameter/motor/pwm_val',self.max_x_linear_double_spin_box.value())
    





















































