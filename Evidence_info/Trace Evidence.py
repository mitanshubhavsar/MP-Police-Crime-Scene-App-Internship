from kivy.lang import Builder
from kivymd.app import MDApp
KV = '''
FloatLayout:
    MDLabel:
        text:"Trace Evidence"
        font_size:30
        text_size:self.size
        pos_hint:{"x":0.318,"y":0.85}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->The collection and preservation of trace evidence is more difficult than other, larger forms of physical evidence.   "
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.70}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->It's better to collect and seal it in a separate and correctly labelled evidence envelope or container.  "
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.50}

    MDLabel:
        text_size: root.width, None
        size: self.texture_size
        text:"->Small items of trace evidence should always be double-wrapped or packaged. Then, the item should be placed in a larger container and labelled with the appropriate information collecting evidence. Some of the most common containers for trace evidence are pillboxes, paper bundles, or small envelopes.   "
        font_size:20
        text_size:self.size
        pos_hint:{"y":0.20}
'''
class TraceEvidence(MDApp): # <- Main Class
    def build(self):
        return Builder.load_string(KV)


TraceEvidence().run()