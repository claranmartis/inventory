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

#barcode label
        label_qty=Label(text='Quantity',
                    color=(0,0,0,0.25),
                    font_size=20,
                    pos_hint={'center_x':0.175,'center_y':0.7})
        root.add_widget(label_qty)

#quantity label
        label_bar=Label(text='Barcode',
                    color=(0,0,0,0.25),
                    font_size=20,
                    pos_hint={'center_x':0.175,'center_y':0.8})
        root.add_widget(label_bar)  
#text box for barcode
        barcode = TextInput(hint_text='barcode',
                              multiline=False,
                              pos_hint={'center_x':0.5,'center_y':0.8},
                              size_hint=(0.5,0.075))

        def on_text(instance, value):
            #use try to check if value in database
            self.bar_str=barcode.text
            
        barcode.bind(text=on_text)
        root.add_widget(barcode)

#text box for quantity
        quantity = TextInput(text='1',
                              multiline=False,
                              pos_hint={'center_x':0.5,'center_y':0.7},
                              size_hint=(0.5,0.075))

        def on_text(instance, value):
            #use try to check if value in database
            self.qty_str=quantity.text
            
        quantity.bind(text=on_text)
        root.add_widget(quantity)
        
        
#company name
        label2=Label(text='KAKABOKA',
                    color=(0,0,0,1),
                    font_size=30,
                    pos_hint={'center_x':0.12,'center_y':0.95})
        root.add_widget(label2)

#Enter the barcode
        button1=Button(text='Enter',
                   size_hint=(0.15,0.1),
                   pos_hint={'right':0.95,'center_y':0.8})
        def callback1(instance):
            #in response of the button click
            label1.text=label1.text+self.bar_str + self.qty_str+'\nEntered\n'
        
        button1.bind(on_press=callback1)
        root.add_widget(button1)

#To finish entry and get the final total.
        button2=Button(text='Done',
                   size_hint=(0.2,0.15),
                   pos_hint={'center_x':0.5,'center_y':0.2})
        
        def callback2(instance):
            label1.text=label1.text + '\n Done'
        
        button2.bind(on_press=callback2)
        root.add_widget(button2)

#add item
        button_add=Button(text='+',
                   size_hint=(0.15,0.1),
                   pos_hint={'right':0.85-0.01,'center_y':0.075})
        #def callback1(instance):
            #in response of the button click

        button_add.bind(on_press=callback1)
        root.add_widget(button_add)

#reports
        button_report=Button(text='Reports',
                   size_hint=(0.15,0.1),
                   pos_hint={'right':1-0.01,'center_y':0.075})
        #def callback1(instance):
            #in response of the button click
            #label1.text=label1.text+self.bar_str + self.qty_str+'\nEntered\n'
        
        button_report.bind(on_press=callback1)
        root.add_widget(button_report)

#tip
        button_tip=Button(text='tip',
                   size_hint=(0.15,0.1),
                   pos_hint={'center_x':0.5,'center_y':0.05})
        #def callback1(instance):
            #in response of the button click
            #label1.text=label1.text+self.bar_str + self.qty_str+'\nEntered\n'
        
        button_tip.bind(on_press=callback1)
        root.add_widget(button_tip)
        
#display the item name and total in this place. This widget could be changed
        label1=Label(text=self.bar_str + self.qty_str,
                    color=(0,0,0,1),
                    pos=(0.9,0.9))
        root.add_widget(label1)

        with root.canvas.before:
            self.rect=Rectangle(source='background.png',size=root.size,pos=root.pos)
            return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size
        



if __name__ == '__main__':
    ClaranApp().run()
