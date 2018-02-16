import FreeCADGui


class SolveCommand:
    def Activated(self):
        pass

    def GetResources(self):
        msg = 'Solve'
        return {
            'Pixmap': '',
            'MenuText': msg,
            'ToolTip': msg
        }

solveCommand = SolveCommand()
FreeCADGui.addCommand('solveSettings', solveCommand)
