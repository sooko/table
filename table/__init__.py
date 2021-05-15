from ast import Num
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty,DictProperty,ListProperty,NumericProperty
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.clock import Clock


Builder.load_string("""



<LabelItem@Label>
    canvas.before:
        Color: 
            rgba:1,1,1,.1
        Rectangle:
            size:self.size
            pos:self.pos


<TableItem>:

    spacing:dp(1)
    fonts_size:self.height*.4
    list_size:[.5,1,1]
    cols:4
    item:""
    val1:""
    val2:""
    font_names:"design/fonts/cavian.ttf"
    bg_color:1,1,1,0
    bg_round_color:1,1,1,0
    canvas.before:
        Color:
            rgba:root.bg_color
        Rectangle:
            size:self.size
            pos:self.pos
        Color:
            rgba:root.bg_round_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
        
    LabelItem
        font_size:root.fonts_size
        text:root.item
        font_name:root.font_names
    LabelItem
        font_size:root.fonts_size
        text:root.val1
        font_name:root.font_names
        size_hint:.3,1
    LabelItem
        font_size:root.fonts_size
        text:root.val2
        font_name:root.font_names
        size_hint:.3,1
<TableHeader@BoxLayout>:
    fonts_size:self.height*.4
    list_size:[.5,1,1]
    cols:4
    item:""
    val1:""
    val2:""
    font_names:"design/fonts/cavian.ttf"
    bg_color:1,1,1,0
    bg_round_color:1,1,1,0
    canvas.before:
        Color:
            rgba:root.bg_color
        Rectangle:
            size:self.size
            pos:self.pos
        Color:
            rgba:root.bg_round_color
        RoundedRectangle:
            size:self.size
            pos:self.pos
            radius:[dp(7),dp(7),0,0]
    Label
        font_size:root.fonts_size
        text:root.item
        font_name:root.font_names
    Widget:
        size_hint:None,1
        width:dp(1)
        canvas:
            Color:
                rgba:0,0,0,1
            Rectangle:
                size:self.size
                pos:self.pos
    Label
        font_size:root.fonts_size
        text:root.val1
        font_name:root.font_names
        size_hint:.3,1
    Widget:
        size_hint:None,1
        width:dp(1)
        canvas:
            Color:
                rgba:0,0,0,1
            Rectangle:
                size:self.size
                pos:self.pos
    Label
        font_size:root.fonts_size
        text:root.val2
        font_name:root.font_names
        size_hint:.3,1

<Table>:
    root_row:root_row
    pos_hint: {'center_x':.5 , 'center_y':.5 }
    FloatLayout
        pos_hint: {'center_x':.5 , 'center_y':.5}
        BoxLayout:
            pos_hint: {'center_x':.5 , 'center_y':.5}
            orientation:"vertical"
            spacing:dp(1)
            TableHeader:
                fonts_size:self.height*.5
                size_hint:1,None
                height:root.height*.1
                bg_color:[1,1,1,0]
                bg_round_color:[1,1,1,.3]
                item:"ITEM"
                val1:"VALUE"
                val2:"VOLT"
                
                
            ScrollView
                GridLayout
                    spacing:dp(1)
                    cols:1
                    row_default_height:root.height*.1
                    id:root_row
                    size_hint:1,None
                    height:self.minimum_height



                  

















""")



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
            


    






