from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
FloatLayout:
    MDLabel:
        text:"Explosive Evidence"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.318,"y":0.85}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"Analysis of pre-blast (intact) and post-blast explosives evidence: "
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.75}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"-> All outside packaging and its condition is noted."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.70}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"-> The evidence container is opened and any distinctive odors are noted."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.62}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->  A macroscopic (visual) examination is performed as follows:"
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.30}
    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"a. General appearance of the device/ debris is noted" 
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.25}
    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"b. Locate and identify fragments/ components of the device (i.e. pipe/ container, blasting cap, electric matches, leg wires, wrappers, timing devices, batteries, etc." 
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.16} 
    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"c. Remove and isolate intact explosives." 
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.11}         
    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"-> Note the location the explosives were found."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.52}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"-> Get an approximate weight of the intact explosive removed from the device, if feasible or requested."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.40}




'''
class ExplosiveEvidence(MDApp): # <- Main Class
    def build(self):
        return Builder.load_string(KV)


ExplosiveEvidence().run()






