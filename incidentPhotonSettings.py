import FreeCADGui
from PySide import QtGui
from PySide import QtCore, QtGui

import pysideuic
import xml.etree.ElementTree as xml

class IncidentPhotonCommand:
    def Activated(self):
        # pass
        import PyQt4
        from PyQt4 import QtGui
        import FreeCADGui
        w=FreeCADGui.PySideUic.loadUi("/home/cis/.FreeCAD/Mod/MCPhotons/Gui/Resources/ui/IncidentPhotonSettings.ui")
        w.show()

    def GetResources(self):
        msg = 'Incident Photon'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg
        }

incidentPhotonCommand = IncidentPhotonCommand()
FreeCADGui.addCommand('incidentPhotonSettings', incidentPhotonCommand)
