from ast import Num
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,DictProperty,ListProperty,NumericProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock

# print(d)
Builder.load_file("table/table.kv")
class TableItem(BoxLayout):
    bg_color=ListProperty([1,1,1,0])
    def __init__(self, **kwargs):
        super(TableItem,self).__init__(**kwargs)
class Table(FloatLayout):
    rows=NumericProperty(0)
    is_ready=False
    row_item=DictProperty({})
    def __init__(self, **kwargs):
        super(Table,self).__init__(**kwargs)
    def on_rows(self,a,b):
        self.is_ready=False
        self.childerns={}
        self.is_ready=False
        self.root_row.clear_widgets()
        Clock.unschedule(self.delay,1)
        Clock.schedule_once(self.delay,1)
    def delay(self,dt):
        blinker=0
        light=0
        for i in range(self.rows):
            tb=TableItem(bg_color=[1,1,1,blinker])
            self.row_item[i]=tb
            self.root_row.add_widget(tb)
            blinker+=.1
            if blinker==.2:
                blinker=0
        self.is_ready=True
            


    






