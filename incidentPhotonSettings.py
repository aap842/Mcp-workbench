import FreeCADGui
from PySide import QtGui
from PySide import QtCore, QtGui

import pysideuic
import xml.etree.ElementTree as xml

class IncidentPhotonCommand:
    def Activated(self):
        import FreeCADGui
        w=FreeCADGui.PySideUic.loadUi(":/MCPhotons/ui/IncidentPhotonSettings.ui")
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
