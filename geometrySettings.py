import FreeCADGui
from PySide import QtGui
from PySide import QtCore, QtGui

import pysideuic
import xml.etree.ElementTree as xml

class GeometryCommand:
    def Activated(self):
        # pass
        import PyQt4
        from PyQt4 import QtGui
        import FreeCADGui
        w=FreeCADGui.PySideUic.loadUi(":/MCPhotons/ui/GeometrySettings.ui")
        w.show()

    def GetResources(self):
        msg = 'Geometry'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg
        }

geometryCommand = GeometryCommand()
FreeCADGui.addCommand('geometrySettings', geometryCommand)
