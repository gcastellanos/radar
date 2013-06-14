from Menu import *
from EventHandlers import *

#pygame initialize
pygame.init()
pygame.display.set_mode((1200, 720))

#menu constructors
mainMenu = Menu()
menu2 = Menu()
pauseMenu = Menu()
statsMenu = Menu()

#menu initialization
s = open('Text.py', 'r').read()
tpanel = Panel((400, 720), (0, 0))
tpanel.setOptions([Option((tpanel.getCenter()[0] - 15, 100), "Button 1", button1Click, [mainMenu]),\
                   Option((tpanel.getCenter()[0] - 15, 200), "Button 2", button2Click, []),\
                   Option((tpanel.getCenter()[0] - 15, 300), "Button 3", button3Click, [menu2]),\
                   Option((tpanel.getCenter()[0] - 15, 400), "Exit", button4Click, [])])
mainMenu.addPanel(tpanel)
mainMenu.setFocus(0)
tpanel = Panel((800, 720), (400, 0))
tpanel.setTexts([Text((0, 0), 25, maxwidth = tpanel.getMaxWidth())])
mainMenu.addPanel(tpanel)
mainMenu.addText(s, 1, 0)

panel = Panel((1200, 720), (0, 0))
panel.setTexts([Text((0, panel.getCenter()[1]), 50)])
menu2.addPanel(panel)
menu2.addText("You Pressed button 3!!", 0, 0)

panel = Panel((400, 720), (0,0))
panel2 = Panel((800, 720), (400, 0))
panel.setOptions([Option((panel.getCenter()[0] - 15, 100), "1: Stats", pauseMenuRunStats, [statsMenu])])
pauseMenu.addPanel(panel)
pauseMenu.addPanel(panel2)

panel = Panel((1200, 720), (0, 0))
statsMenu.addPanel(panel)
