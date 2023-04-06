import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.config import Config
Config.set('graphics', 'resizable', True)

import os

class MainPage(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=1
        self.layout = AnchorLayout( 
        anchor_x ='right', anchor_y ='bottom') 
        btn = Button(text ='Hello World', 
                     size_hint =(.3, .3), 
                     background_color =(1.0, 0.0, 0.0, 1.0)) 
      
       
        ##  Intro
        self.add_widget(Label(text="Would you like to add or view files?", halign="center", valign="middle", font_size=30))
        
        ##  Add Record Button
        self.join = Button(text="Add Record", size=(50, 50))
        self.join.bind(on_press=self.add_button)
        self.add_widget(self.join)

        ## View Record Button
        self.join = Button(text="View Record", size=(100, 100))
        self.join.bind(on_press=self.view_button)
        self.add_widget(self.join)

        layout.add_widget(btn) 
        return layout

    def add_button(self, instance):
        order_app.screen_manager.current = "Add"

    def view_button(self, instance):
        order_app.view_page.update_view()
        order_app.screen_manager.current = "View"

class AddPage(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols=2

        ##  Order Number 
        self.add_widget(Label(text="Order Number:", size=(100, 100)))
        self.orderNum = TextInput(multiline=False)
        self.add_widget(self.orderNum)

        ##  Customer Name 
        self.add_widget(Label(text="Customer Name:", size=(100, 100)))
        self.customer = TextInput(multiline=False)
        self.add_widget(self.customer)

        ##  Ship Via 
        self.add_widget(Label(text="Ship Via:", size=(100, 100)))
        self.shipVia = TextInput(multiline=False)
        self.add_widget(self.shipVia)

        ##  Order Date 
        self.add_widget(Label(text="Order Date:", size=(100, 100)))
        self.orderDate = TextInput(multiline=False)
        self.add_widget(self.orderDate)
        
        ##  Button
        self.join = Button(text="Add Record")
        self.join.bind(on_press=self.join_button)
        self.add_widget(Label())
        self.add_widget(self.join)

    def join_button(self, instance):
        orderNum = self.orderNum.text
        customer = self.customer.text
        shipVia = self.shipVia.text
        orderDate = self.orderDate.text

        with open("file.txt", "a+") as f:
            line = orderNum + "\t\t" + customer + "\t\t\t" + shipVia + "\t\t" + orderDate
            f.write("\n")
            f.write(line)
            f.close()

        order_app.view_page.update_view()
        order_app.screen_manager.current = "View"
        

class ViewPage(AnchorLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 1
        self.message = Label(halign="left", valign="middle", font_size=30)
        self.message.bind(width=self.update_text_width)
        self.add_widget(self.message)

        self.join = Button(text="Main Menu", size =(50, 50))
        self.join.bind(on_press=self.main_menu_button)
        self.add_widget(self.join)

    def main_menu_button(self, instance):
        order_app.screen_manager.current = "Main"

    def update_view(self):    
        with open("file.txt", "r") as f:
            data = f.read()
            self.message.text = data
            f.close()

    def update_text_width(self, *_):
        self.message.text_size = (self.message.width*0.9, None)


class EpicApp(App):
    def build(self):
        self.screen_manager = ScreenManager()

        self.main_page = MainPage()
        screen=Screen(name="Main")
        screen.add_widget(self.main_page)
        self.screen_manager.add_widget(screen)

        self.connect_page = AddPage()
        screen = Screen(name="Add")
        screen.add_widget(self.connect_page)
        self.screen_manager.add_widget(screen)

        self.view_page = ViewPage()
        screen=Screen(name="View")
        screen.add_widget(self.view_page)
        self.screen_manager.add_widget(screen)

        return self.screen_manager


if __name__ == "__main__":
   order_app = EpicApp()
   order_app.run()