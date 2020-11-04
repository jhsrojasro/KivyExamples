import kivy

from kivy.app import App
from kivy.lang.builder import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.uix.tabbedpanel import TabbedPanel


Builder.load_file("usuarios.kv")

usuarios = {"Sebastian":"sebasdeloco"}

class Login(BoxLayout):
    exito_popup = Popup(title='Usuario Autenticado', content=Label(text='Usuario Autentificado Exitosamente'),
                        size_hint=(None, None), size=(400, 400))
    fail_popup = Popup(title='Error en la Autenticacion', content=Label(text='Credenciales no validas'),
                       size_hint=(None, None), size=(400, 400))
    def verificarLogin(self, usuario, password):
        if usuario and password:
            for u, p in usuarios.items():
                if usuario == u and password == p:
                    self.exito_popup.open()
                return
        self.fail_popup.open()
        #print(usuario, password)


class Registro(BoxLayout):
    registro_popup = Popup(title='Usuario Registrado', content=Label(text='Usuario Registrado Exitosamente'),
                        size_hint=(None, None), size=(400, 400))
    fail_registro_popup = Popup(title='Error', content=Label(text='No se ha podido registrar a el usuario, revise los campos'),
                           size_hint=(None, None), size=(400, 400))
    def registrar(self, nombre, correo, usuario, password, sexo, rol):
        if(rol != "Rol" and sexo != "Genero" and nombre and correo and usuario and password):
            print("Nombre:",nombre)
            print("Correo:", correo)
            print("Usuario:", usuario)
            print("Password:", password)
            print("Genero:", sexo)
            print("Rol:", rol)
            self.registro_popup.open()
            return
        self.fail_registro_popup.open()



class UsuariosApp(App, TabbedPanel):

    def build(self):
        return self


if __name__ == '__main__':
    UsuariosApp().run()
