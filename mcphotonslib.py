freePath ='/usr/lib/freecad/lib'
import numpy, os, sys
sys.path.append(freePath)
import FreeCAD
import FreeCADGui
import Part
from PySide import QtGui, QtCore
from lib3D import fit_plane_to_surface1, fit_rotation_axis_to_surface1
from viewProviderProxies import ImportedPartViewProviderProxy, ConstraintViewProviderProxy,\
     create_constraint_mirror, repair_tree_view

path_mcphotons = os.path.dirname(__file__)
#path_assembly2_icons =  os.path.join( path_assembly2, 'Resources', 'icons')
#path_assembly2_ui =  os.path.join( path_assembly2, 'Resources', 'ui')
path_mcphotons_resources = os.path.join( path_mcphotons, 'Gui', 'Resources', 'resources.rcc')
resourcesLoaded = QtCore.QResource.registerResource(path_mcphotons_resources)
assert resourcesLoaded
#update resources file using 
# $rcc -binary  Gui/Resources/resources.qrc -o Gui/Resources/resources.rcc 

__dir__ = path_mcphotons
wb_globals = {}
__dir2__ = os.path.dirname(__file__)
GuiPath = os.path.expanduser ("~") #GuiPath = os.path.join( __dir2__, 'Gui' )
