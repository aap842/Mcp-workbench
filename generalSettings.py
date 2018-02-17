import FreeCADGui
from PySide import QtGui
from PySide import QtCore, QtGui

import pysideuic
import xml.etree.ElementTree as xml

class GeneralCommand:
    def Activated(self):
        import FreeCADGui
        from mcphotonslib import __dir__
        w=FreeCADGui.PySideUic.loadUi(":/MCPhotons/ui/GeneralSettings.ui")
        w.show()

    def GetResources(self):
        msg = 'General'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg,
        }

generalCommand = GeneralCommand()
FreeCADGui.addCommand('generalSettings', generalCommand)