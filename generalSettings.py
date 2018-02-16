import FreeCADGui
from PySide import QtGui
from PySide import QtCore, QtGui

import pysideuic
import xml.etree.ElementTree as xml

class GeneralCommand:
    def Activated(self):
        # pass
        import PyQt4
        from PyQt4 import QtGui
        import FreeCADGui
        w=FreeCADGui.PySideUic.loadUi("/home/cis/.FreeCAD/Mod/MCPhotons/Gui/Resources/ui/GeneralSettings.ui")
        w.show()

    def GetResources(self):
        msg = 'General'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg
        }

generalCommand = GeneralCommand()
FreeCADGui.addCommand('generalSettings', generalCommand)