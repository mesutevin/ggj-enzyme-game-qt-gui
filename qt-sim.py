from aktos_dcs import *
from aktos_dcs_lib import Qt
import random

Qt.initialize()

class MainWindow(Actor, Qt.QtGui.QMainWindow):
    def __init__(self):
        Qt.QtGui.QMainWindow.__init__(self)
        Actor.__init__(self)
        self.ui = Qt.loadUI('test.ui')

    def action(self):
        test = FlowingObject(self.ui.checkBox)
        test2 = FlowingObject(self.ui.checkBox_2)
        test3 = FlowingObject(self.ui.checkBox_3)
        test4 = FlowingObject(self.ui.checkBox_4)
        test5 = FlowingObject(self.ui.checkBox_5)
        test.level = 5
        test2.level = 1
        test3.level = 3
        test4.level = 0
        test5.level = 8
        
class FlowingObject(Actor):
    def __init__(self, checkbox):
        Actor.__init__(self)
        self.checkbox_actor = checkbox
        self.x =self.checkbox_actor.x()
        self.y =self.checkbox_actor.y()
        self.level = 4
        self.delay_time = 1
        
    def action(self):
        self.delay_time = 1 if self.level == 0 else 0.01*self.level
        while True:
            for i in range(2,600):
                print i
                self.checkbox_actor.move(i, self.y)
                i = i - 2
                sleep(self.delay_time)


if __name__ == "__main__":
    import sys
    #ProxyActor(brokers='192.168.2.164:5012:5013')
    ProxyActor()
    app = Qt.QtGui.QApplication(sys.argv)
    win = MainWindow()
    win.ui.show()
    Qt.greenlet_exec(app)
