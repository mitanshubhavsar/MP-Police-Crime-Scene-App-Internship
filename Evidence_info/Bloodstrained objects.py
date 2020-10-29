from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
FloatLayout:
    MDLabel:
        text:"Bloodstained Object"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.318,"y":0.80}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->If the bloodstained object is large, it should be loosely wrapped or placed in thick wrapping paper or paper bags. Newspaper should never be used to wrap such objects, as ink will contaminate the item. Never package fresh, wet or damp blood in airtight containers. "
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.50}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"-> In the case of extremely large objects, such as bloodstained carpets or mattresses, for example, a section may be cut out of them and then stored in separate packing materials. When removing sections of mattresses, carpets, curtains, drapes, and so forth, the crime scene investigator must also remember to cut a control, or sample section from the same object for testing as well. "
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.20}




'''
class BloodStrainedObjects(MDApp): # <- Main Class
    def build(self):
        return Builder.load_string(KV)


BloodStrainedObjects().run()