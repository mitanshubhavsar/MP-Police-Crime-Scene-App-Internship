import os
import image_slicer
from imageai.Detection import ObjectDetection
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image

class MainApp(App):
    def build(self):
        layout = BoxLayout(orientation='vertical', spacing=10, padding=40)
        img = Image(source='pic.jpg')
        button = Button(text='Scan', size_hint=(None,None), width=100, height=50, pos_hint={'center_x': 0.5})
        button.bind(on_press=self.scan)
        layout.add_widget(img)
        layout.add_widget(button)
        return layout

    @staticmethod
    def scan(self):
        img = 'pic.jpg'
        num_tiles = 4
        tiles = image_slicer.slice(img, num_tiles, save=False)
        os.makedirs('pic_slices')
        image_slicer.save_tiles(tiles, directory='pic_slices', prefix='slice', format='jpeg')

        for filename in os.listdir('pic_slices'):
            if filename.endswith(".jpg"):
                execution_path = os.getcwd()

                detector = ObjectDetection()
                detector.setModelTypeAsYOLOv3()
                detector.setModelPath(os.path.join(execution_path, "yolo.h5"))
                detector.loadModel()

                detections, objects_path = detector.detectObjectsFromImage(
                    input_image=os.path.join(execution_path, "pic.jpg"),
                    output_image_path=os.path.join(execution_path,
                                                   "picpearced.jpg"),
                    minimum_percentage_probability=30,
                    extract_detected_objects=True)

                for eachObject, eachObjectPath in zip(detections, objects_path):
                    print(eachObject["name"], " : ", eachObject["percentage_probability"], " : ",
                          eachObject["box_points"])
                    print("Object's image saved in " + eachObjectPath)
                    print("--------------------------------")


MainApp().run()