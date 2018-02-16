import FreeCADGui


class ElementsCommand:
    def Activated(self):
        pass

    def GetResources(self):
        msg = 'Elements'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg
        }

elementsCommand = ElementsCommand()
FreeCADGui.addCommand('elementsSettings', elementsCommand)
