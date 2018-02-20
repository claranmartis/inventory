from kivy.app import App
from kivy.graphics import Color, Rectangle
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.uix.image import AsyncImage
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView

class ClaranApp(App):

    title='KAKABOKA'

    
        
    def build(self):
        self.root = root = FloatLayout()
        root.bind(size=self._update_rect, pos=self._update_rect)
        self.bar_str=''
        self.qty_str=''

#Product name label
        label_qty=Label(text='Product',
                    color=(0,0,0,0.25),
                    font_size=20,
                    pos_hint={'center_x':0.175,'center_y':0.8})
        root.add_widget(label_qty)

#barcode label
        label_bar=Label(text='Barcode',
                    color=(0,0,0,0.25),
                    font_size=20,
                    pos_hint={'center_x':0.175,'center_y':0.7})
        root.add_widget(label_bar)

#quantity label
        label_qty=Label(text='Quantity',
                    color=(0,0,0,0.25),
                    font_size=20,
                    pos_hint={'center_x':0.175,'center_y':0.6})
        root.add_widget(label_qty)

#price label
        label_price=Label(text='Price',
                    color=(0,0,0,0.25),
                    font_size=20,
                    pos_hint={'center_x':0.175,'center_y':0.5})
        root.add_widget(label_price)

#price label
        label_man=Label(text='Manufacturer',
                    color=(0,0,0,0.25),
                    font_size=20,
                    pos_hint={'center_x':0.175,'center_y':0.4})
        root.add_widget(label_man)
        

#text box for Product name
        name = TextInput(hint_text='Name',
                              multiline=False,
                              pos_hint={'center_x':0.5,'center_y':0.8},
                              size_hint=(0.5,0.075))
        root.add_widget(name)
#text box for barcode
        barcode = TextInput(hint_text='barcode',
                              multiline=False,
                              pos_hint={'center_x':0.5,'center_y':0.7},
                              size_hint=(0.5,0.075))

        def on_text(instance, value):
            #use try to check if value in database
            self.bar_str=barcode.text
            
        barcode.bind(text=on_text)
        root.add_widget(barcode)

#text box for quantity
        quantity = TextInput(text='1',
                              multiline=False,
                              pos_hint={'center_x':0.5,'center_y':0.6},
                              size_hint=(0.5,0.075))

        root.add_widget(quantity)



#text box for Price
        price = TextInput(hint_text='USD',
                              multiline=False,
                              pos_hint={'center_x':0.5,'center_y':0.5},
                              size_hint=(0.5,0.075))
        root.add_widget(price)

#text box for Manufacturer
        man = TextInput(hint_text='Brand',
                              multiline=False,
                              pos_hint={'center_x':0.5,'center_y':0.4},
                              size_hint=(0.5,0.075))
        root.add_widget(man)
        
#company name
        label2=Label(text='KAKABOKA',
                    color=(0,0,0,1),
                    font_size=30,
                    pos_hint={'center_x':0.12,'center_y':0.95})
        root.add_widget(label2)



#Done button
        button2=Button(text='Done',
                   size_hint=(0.2,0.15),
                   pos_hint={'center_x':0.5,'center_y':0.2})
        
        def callback2(instance):
            label1.text=label1.text + '\n Done'
        
        button2.bind(on_press=callback2)
        root.add_widget(button2)



        with root.canvas.before:
            self.rect=Rectangle(source='background.png',size=root.size,pos=root.pos)
            return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        



if __name__ == '__main__':
    ClaranApp().run()
