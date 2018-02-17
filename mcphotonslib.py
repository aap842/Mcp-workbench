
from PySide import QtCore

import os
import sys

freePath = '/usr/lib/freecad/lib'
sys.path.append(freePath)

path_mcphotons = os.path.dirname(__file__)
path_mcphotons_resources = os.path.join(
    path_mcphotons, 'Gui', 'Resources', 'resources.rcc')
resourcesLoaded = QtCore.QResource.registerResource(path_mcphotons_resources)
assert resourcesLoaded
# update resources file using
# $rcc -binary  Gui/Resources/resources.qrc -o Gui/Resources/resources.rcc

__dir__ = path_mcphotons
wb_globals = {}
__dir2__ = os.path.dirname(__file__)
GuiPath = os.path.expanduser("~")  # GuiPath = os.path.join( __dir2__, 'Gui' )
