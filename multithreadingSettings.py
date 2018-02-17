import FreeCADGui
from PySide import QtGui
from PySide import QtCore, QtGui

import pysideuic
import xml.etree.ElementTree as xml

class MultithreadingCommand:
    def Activated(self):
        # pass
        import PyQt4
        from PyQt4 import QtGui
        import FreeCADGui
        w=FreeCADGui.PySideUic.loadUi(":/MCPhotons/ui/MultithreadingSettings.ui")
        w.show()

    def GetResources(self):
        msg = 'Multithreading'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg
        }

multithreadingCommand = MultithreadingCommand()
FreeCADGui.addCommand('multithreadingSettings', multithreadingCommand)
