from PySide6 import QtWidgets, QtCore
import threading

class Window(QtWidgets.QMainWindow):
    signal_start_background_job = QtCore.Signal()

    def __init__(self):
        super(Window, self).__init__()
        self.button = QtWidgets.QPushButton(self)
        self.flag=True

        # self.worker = WorkerObject()
        # self.thread = threading.Thread()
        # self.worker.moveToThread(self.thread)

        self.signal_start_background_job.connect(self.background_job)

        self.button.clicked.connect(self.start_background_job)  

    def start_background_job(self):
        # No harm in calling thread.start() after the thread is already started.
        
        self.signal_start_background_job.emit()
        
# class WorkerObject(QtCore.QObject):
    
    def background_job(self):
        print("hello")
        #Do stuff
        pass

def main():
    app=QtWidgets.QApplication([])
    win=Window()
    win.show()
    app.exec()

main()