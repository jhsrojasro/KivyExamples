import kivy

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.lang import Builder

Builder.load_file("calculadora.kv")

Window.clearcolor = (0, 20, 240, 1)

class CalcBoxLayout(BoxLayout):
    def calcular(self, expresion):
        if expresion:
            try:
                self.pantalla.text = str(eval(expresion))
            except Exception:
                self.pantalla.text = "Error :c"

class CalculatorApp(App):
    def build(self):
        return CalcBoxLayout()


calculadora = CalculatorApp()
calculadora.run()