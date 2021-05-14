# This Python file uses the following encoding: utf-8
import os
from pathlib import Path
import sys
from PySide2 import QtGui
from PySide2 import QtCore
from PySide2.QtCore import QObject, SIGNAL

from PySide2.QtGui import QGuiApplication
from PySide2.QtQml import QQmlApplicationEngine, QtQml

def test():
    print("test")

if __name__ == "__main__":
    app = QGuiApplication(sys.argv)
    engine = QQmlApplicationEngine()
    engine.load(os.fspath(Path(__file__).resolve().parent / "main.qml"))  
    
    screen = engine.rootObjects()[0]
    button = screen.findChild(QtCore.QObject, "button")
    QObject.connect(button, SIGNAL ('clicked()'), test)    

    if not engine.rootObjects():
        sys.exit(-1)
    sys.exit(app.exec_())
