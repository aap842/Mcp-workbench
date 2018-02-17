import FreeCADGui
from PySide import QtGui
from PySide import QtCore, QtGui

import pysideuic
import xml.etree.ElementTree as xml

class RandomNumberCommand:
    def Activated(self):
        import FreeCADGui
        w=FreeCADGui.PySideUic.loadUi(":/MCPhotons/ui/RandomNumberSettings.ui")
        w.show()

    def GetResources(self):
        msg = 'Random Number'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg
        }

randomNumberCommand = RandomNumberCommand()
FreeCADGui.addCommand('randomNumberSettings', randomNumberCommand)
