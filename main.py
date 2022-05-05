from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.config import Config


Config.set('kivy', 'keyboard_mode', 'systemanddock')
#Window.size = (240, 426)

from kivymd.theming import ThemeManager

x1 = x2 = x3 = x4 = x5 = x6 = 0

class Container(GridLayout):

    def pr(self, instance, value, y):

        global x1, x2, x3, x4, x5, x6

        if y == "p1":
            if value:
                x1 = 200
            else:
                x1 = 0
        if y == "p2":
            if value:
                x2 = 140
            else:
                x2 = 0
        if y == "p3":
            if value:
                x3 = 250
            else:
                x3 = 0
        if y == "p4":
            if value:
                x4 = 170
            else:
                x4 = 0
        if y == "p5":
            if value:
                x5 = 80
            else:
                x5 = 0
        if y == "p6":
            if value:
                x6 = 900
            else:
                x6 = 0

    def calculate(self):
        try:
            itog = 0
            vvod = float(self.text_input.text)
            vvod2 = vvod * 2.4
            vvod3 = vvod * 1.2

            if x1:
                itog = vvod2 * x1

            if x2:
                itog = itog + (vvod2 * x2)

            if x3:
                itog = itog + (vvod * x3)

            if x4:
                itog = itog + (vvod * x4)

            if x5:
                itog = itog + (vvod3 * x5)

            if x6:
                itog = itog + (vvod * x6)

            self.item_label.text = str(itog)

        except:
            vvod = 0

class MyApp(MDApp):
    theme_cls = ThemeManager()
    title = 'VPK-расчет'

    def build(self):
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.primary_palette = "DeepPurple"
        return Container()

root = MyApp()
root.run()
#dsfgbfsgbfgbnfgbfgb