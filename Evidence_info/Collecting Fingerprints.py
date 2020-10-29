from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
FloatLayout:
    MDLabel:
        text:"Collecting Fingerprints"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.318,"y":0.85}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->Collecting fingerprints can comprise several different techniques, such as developing with powders, which are available in black, colored, copper, magnetic, fluorescent and white. After dusting, the print is lifted onto tape and attached to the back of a card.  "
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.70}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->In the case of prints left on porous surfaces, such as paper, treatments of ninhydrin, iodine, or a rarely used process using silver nitrate are used."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.50}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->Other methods, such as the use of lasers, often yields results that other methods don't."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.35}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->The oldest method of obtaining latent fingerprints on porous surfaces is through the use of iodine.  As iodine vapor is toxic and corrosive. Results are not permanent, so cameras should be on standby when such a procedure is used."
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.10}





'''
class CollectingFingerprints(MDApp): # <- Main Class
    def build(self):
        return Builder.load_string(KV)


CollectingFingerprints().run()