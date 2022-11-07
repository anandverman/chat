from PyQt6 import QtWidgets, QtCore
import threading

class Window(QtWidgets.QMainWindow):
    signal_start_background_job = QtCore.pyqtSignal()

    def __init__(self):
        super(Window, self).__init__()
        self.button = QtWidgets.QPushButton(self)

        self.worker = WorkerObject()
        # self.thread = QtCore.QThread()
        # self.worker.moveToThread(self.thread)
        self.t1=threading.Thread(target=self.start_background_job)


        self.signal_start_background_job.connect(lambda:self.worker.background_job(self.button))

        self.button.clicked.connect(self.startthread)

    def startthread(self):
        self.t1.start()

    def start_background_job(self):
        # No harm in calling thread.start() after the thread is already started.
        # self.thread.start()
        print(threading.current_thread().getName())

        self.signal_start_background_job.emit()
        
class WorkerObject(QtCore.QObject):
    @QtCore.pyqtSlot()
    def background_job(self, button):
        button.setText("Hi")
        print("hello")
        print(threading.current_thread().getName())
        #Do stuff
        pass

def main():
    app=QtWidgets.QApplication([])
    win=Window()
    win.show()
    app.exec()

main()