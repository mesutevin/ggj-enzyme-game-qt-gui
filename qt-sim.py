from aktos_dcs import *
from aktos_dcs_lib import Qt
import random

Qt.initialize()

class MainWindow(Actor, Qt.QtGui.QMainWindow):
    def __init__(self):
        Qt.QtGui.QMainWindow.__init__(self)
        Actor.__init__(self)
        self.ui = Qt.loadUI('test.ui')
        self.game_level = 1
        self.ui.lcdNumber.display(self.game_level)
        self.COMPLETED_STYLE = """
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
         }
        QProgressBar::chunk {
            background-color: #FF0000;
            width: 20px;
        }
        
        """
        self.DEFAULT_STYLE = """
        QProgressBar {
            border: 2px solid grey;
            border-radius: 5px;
            text-align: center;
        }
        QProgressBar::chunk {
            background-color: #74ACE8;
            width: 20px;
        }
        
        """
        self.ui.progressBar.setStyleSheet(self.DEFAULT_STYLE)
        
    def action(self):
        self.current_health = self.ui.progressBar.value()
        test = FlowingObject(self.ui.checkBox)
        test2 = FlowingObject(self.ui.checkBox_2)
        test3 = FlowingObject(self.ui.checkBox_3)
        test4 = FlowingObject(self.ui.checkBox_4)
        test5 = FlowingObject(self.ui.checkBox_5)
        FlowingObject(self.ui.checkBox_6)
        FlowingObject(self.ui.checkBox_7)
        FlowingObject(self.ui.checkBox_8)
        FlowingObject(self.ui.checkBox_9)
        FlowingObject(self.ui.checkBox_10)
        FlowingObject(self.ui.checkBox_11)
        FlowingObject(self.ui.checkBox_12)
        FlowingObject(self.ui.checkBox_13)
        FlowingObject(self.ui.checkBox_14)
        FlowingObject(self.ui.checkBox_15)
        FlowingObject(self.ui.checkBox_16)
        FlowingObject(self.ui.checkBox_17)
        FlowingObject(self.ui.checkBox_18)
        FlowingObject(self.ui.checkBox_19)

        test.speed = 5
        test2.speed = 1
        test3.speed = 3
        test4.speed = 2
        test5.speed = 8
        test5.direction = False
        test4.direction = False

        while True:
            print "Actors are working .... "
            sleep(2)
        
    
    def handle_HealthMessage(self, msg):
        self.current_health += 1 if msg['val'] else -1
        print "Got Healt Message, New HEALTH: ", self.current_health
        self.ui.progressBar.setValue(self.current_health)
        print "Sending LedPanelMessage.."
        self.send({'LedPanelMessage': {'message': 'Health.. '+str(self.current_health) }})
        if self.ui.progressBar.value() <= 10:
            print "WARNING... YOU WILL DIE!"
            self.ui.progressBar.setStyleSheet(self.COMPLETED_STYLE)

            

    
        
class FlowingObject(Actor):
    def __init__(self, checkbox):
        Actor.__init__(self)
        self.checkbox_actor = checkbox
        self.x =self.checkbox_actor.x()
        self.y =self.checkbox_actor.y()
        #self.speed = 4
        #self.delay_time = 1
        #self.level = 1

        self.speed = random.randrange(1,5,1)

        self.delay_time = 1
        self.speed_constant = 0.1
        self.direction = random.choice([True, False])

    def actor_callback(self):
        checked = self.checkbox_actor.isChecked()
        print self.checkbox_actor.text(), "is send message : ", checked
        self.send({self.checkbox_actor.text(): {'val': checked} })

    #Need some improve
    def handle_ParticleMessage(self, msg):
        print self.checkbox_actor.text(), " got message : ", msg['destroy']
        if self.checkbox_actor.text() in msg['destroy']:
            if self.checkbox_actor.isChecked():
                print "Closing checkbox actor..."
                self.checkbox_actor.close()

    def action(self):
        self.checkbox_actor.stateChanged.connect(self.actor_callback)
        if win.game_level == 2:
            self.speed_constant = 0.01
        if win.game_level == 3:
            self.speed_constant = 0.001
        self.delay_time = 1 if self.speed == 0 else self.speed_constant * 1 / self.speed

        while True:
            self.flow_randomly()
            self.y = random.randrange(100,600,1)

    def clean_check(self):
        self.checkbox_actor.setCheckState(False)

    def flow_randomly(self):
        if self.direction:
            for i in range(2,600):
                self.checkbox_actor.move(i, self.y)
                i = i - 2
                sleep(self.delay_time)
        else:
            for i in range(600,2,-1):
                self.checkbox_actor.move(i, self.y)
                i = i - 2
                sleep(self.delay_time)


if __name__ == "__main__":
    import sys
    ProxyActor(brokers='192.168.1.42:5012:5013 192.168.1.59:5012:5013')
    app = Qt.QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.ui.show()
    Qt.greenlet_exec(app)
