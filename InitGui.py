import os
import FreeCAD
import FreeCADGui


class MCPhotonsWorkbench(Workbench):

    MenuText = "MCPhotons"
    ToolTip = "A description of MCPhotons workbench"
    Icon = """
        /* XPM */
        static char * arch_xpm[] = {
        "17 17 45 1",
        "   c None",
        ".  c #00F000",
        "+  c #00F200",
        "@  c #00E200",
        "#  c #00F100",
        "$  c #00FF00",
        "%  c #00F300",
        "&  c #00FC00",
        "*  c #00F400",
        "=  c #00F700",
        "-  c #00D600",
        ";  c #00CD00",
        ">  c #00D800",
        ",  c #00F800",
        "'  c #00DD00",
        ")  c #00F600",
        "!  c #008F00",
        "~  c #008800",
        "{  c #009800",
        "]  c #009700",
        "^  c #00A600",
        "/  c #007F00",
        "(  c #00E500",
        "_  c #00A700",
        ":  c #00FA00",
        "<  c #008900",
        "[  c #00CA00",
        "}  c #00FD00",
        "|  c #00FB00",
        "1  c #00F900",
        "2  c #009A00",
        "3  c #007A00",
        "4  c #00B200",
        "5  c #00EF00",
        "6  c #00FE00",
        "7  c #00AD00",
        "8  c #007200",
        "9  c #008400",
        "0  c #00C300",
        "a  c #00BE00",
        "b  c #007400",
        "c  c #00DC00",
        "d  c #007000",
        "e  c #008300",
        "f  c #00B600",
        "                 ",
        "                 ",
        "                 ",
        "      .+@        ",
        "     #$$$$%@     ",
        "    %$$$$$$$$&$  ",
        "   *$$=-;>,$$$$$'",
        "  )$$)!~{]^=$$$*/",
        " =$$$(_    %$$:< ",
        "[}$$$|    #1$&2  ",
        " 345$$|61=$$67   ",
        "   890:$$$$$a    ",
        "      b2c$$c     ",
        "        defb     ",
        "                 ",
        "                 ",
        "                 "};"""


    def Initialize(self):
        "This function is executed when FreeCAD starts"
        print('this is initilize')
        import PartGui
        import Part
        print(PartGui, Part)
        print(dir(PartGui), '\n')
        print(dir(Part), '\n')

        # import MyModuleA, MyModuleB # import here all the needed files that create your FreeCAD commands
        self.list = ["PartGui, Part"]  # A list of command names created in the line above
        self.appendToolbar("My Commands", self.list)  # creates a new toolbar with your commands
        self.appendMenu("My New Menu", self.list)  # creates a new menu
        self.appendMenu(["An existing Menu", "My submenu"], self.list)  # appends a submenu to an existing menu

    def Activated(self):
        "This function is executed when the workbench is activated"
        return

    def Deactivated(self):
        "This function is executed when the workbench is deactivated"
        return

    def ContextMenu(self, recipient):
        "This is executed whenever the user right-clicks on screen"
        # "recipient" will be either "view" or "tree"
        self.appendContextMenu("My commands",self.list) # add commands to the context menu

    def GetClassName(self):
        # this function is mandatory if this is a full python workbench
        return "Gui::PythonWorkbench"


Gui.addWorkbench(MCPhotonsWorkbench())
