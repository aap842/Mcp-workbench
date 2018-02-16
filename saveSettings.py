import FreeCADGui


class SaveCommand:
    def Activated(self):
        pass

    def GetResources(self):
        msg = 'Save'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg
        }

saveCommand = SaveCommand()
FreeCADGui.addCommand('saveSettings', saveCommand)
