import pygame, sys
from pygame.locals import *
from Menu import *
from Decision import *

def button1Click(menu):
    menu.panels[1].setTexts([Text((0, 0), 100)])
    menu.addText("Hello, World!!!", 1, 0)

def button2Click():
    pygame.mixer.Sound('enemy_death.ogg').play()

def button3Click(menu):
    menu.run()

def button4Click():
    pygame.quit()
    sys.exit()

def runPauseMenu(menu, char):
    pauseMenuPrintStats(menu, char)
    menu.run()

def pauseMenuRunStats(menu, char):
    s ='Stats:\n\n'
    s += 'HP:  ' + str(int(char.health)) + ' / ' + str(char.maxHealth) + '\n\n'
    s += 'Attack:  ' + str(char.weapon.attack) + '\n\n'
    s += 'Defense:  ' + str(char.armor.defense) + '\n\n'
    menu.addText(s, 1, 0)
    try:
        menu.run()
    except SystemExit:
        return

def pauseMenuPrintStats(menu, char):
    s ='Stats:\n\n'
    s += 'HP:  ' + str(int(char.health)) + ' / ' + str(char.maxHealth) + '\n\n'
    s += 'Attack:  ' + str(char.weapon.attack) + '\n\n'
    s += 'Defense:  ' + str(char.armor.defense) + '\n\n'
    panel = menu.panels[1]
    panel.setTexts([Text((panel.getCenter()[0], 100), panel.tsize, True)])
    menu.addText(s, 1, 0)

def generalBackButton():
    sys.exit()

def pauseMenuRunWeapons(menu, char, promptmenu):
    panel = menu.panels[0]
    panel.clearOptions()
    for i in range(len(char.weapons)):
        weapon = char.weapons[i]
        panel.addOptions([Option(weapon.type, panel.osize, weaponMenuSelectWeapon, [i, promptmenu, char, menu],\
                                   weaponMenuPrintWeapon, [weapon, menu, char])])
    menu.run()

def weaponMenuPrintWeapon(weapon, menu, char):
    s = "Current: "
    s += str(char.weapon.attack)
    if char.weapon.attack > weapon.attack:
        s += " (*)"
    s += " -> Selected: "
    s += str(weapon.attack)
    if weapon.attack > char.weapon.attack:
        s += " (*)"
    panel = menu.panels[1]
    panel.setTexts([Text((panel.getCenter()[0] - 15, panel.getCenter()[1] - 30),\
                         panel.tsize, True)])
    menu.addText(s, 1, 0)

def weaponMenuSelectWeapon(num, menu, char, wmenu):
    decision = Decision()
    panel = menu.panels[0]
    panel.clearOptions()
    panel.addOptions([Option("Yes", panel.osize, promptMenuYes, [decision]),\
                      Option("No", panel.osize, promptMenuNo, [decision])])
    menu.addText("Equip?", 0, 0)
    try:
        menu.run()
    except SystemExit:
        pass
    if decision.bool:
        char.equipWeapon(num)
    wpanel = wmenu.panels[0]
    sel = wpanel.selected
    weapon = char.weapons[sel]
    weaponMenuPrintWeapon(weapon, wmenu, char)

def pauseMenuRunArmor(menu, char, promptmenu):
    panel = menu.panels[0]
    panel.clearOptions()
    for i in range(len(char.armors)):
        armor = char.armors[i]
        panel.addOptions([Option(armor.type, panel.osize, armorMenuSelectArmor, [i, promptmenu, char, menu],\
                                   armorMenuPrintArmor, [armor, menu, char])])
    menu.run()

def armorMenuPrintArmor(armor, menu, char):
    s = "Current: "
    s += str(char.armor.defense)
    if char.armor.defense > armor.defense:
        s += " (*)"
    s += " -> Selected: "
    s += str(armor.defense)
    if armor.defense > char.armor.defense:
        s += " (*)"
    panel = menu.panels[1]
    panel.setTexts([Text((panel.getCenter()[0] - 15, panel.getCenter()[1] - 30),\
                         panel.tsize, True)])
    menu.addText(s, 1, 0)

def armorMenuSelectArmor(num, menu, char, amenu):
    decision = Decision()
    panel = menu.panels[0]
    panel.clearOptions()
    panel.addOptions([Option("Yes", panel.osize, promptMenuYes, [decision]),\
                      Option("No", panel.osize, promptMenuNo, [decision])])
    menu.addText("Equip?", 0, 0)
    try:
        menu.run()
    except SystemExit:
        pass
    if decision.bool:
        char.equipArmor(num)
    apanel = amenu.panels[0]
    sel = apanel.selected
    armor = char.armors[sel]
    armorMenuPrintArmor(armor, amenu, char)

def promptMenuYes(decision):
    decision.bool = True
    sys.exit()

def promptMenuNo(decision):
    decision.bool = False
    sys.exit()





















