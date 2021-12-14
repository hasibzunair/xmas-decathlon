from kivymd.app import MDApp
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton, MDFloatingActionButton, \
    MDFloatingActionButtonSpeedDial
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.toolbar import MDToolbar
from kivy.core.audio import SoundLoader

from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import MDList, OneLineListItem

import cv2

def christmas_hat(img):
    
    cname = 'data/haarcascade_frontalface_alt.xml'
    faces = face_detect(img, cname)
    
    if faces is not None:
        #hats = [cv2.imread(f'img/hats/hat_{i+1}.png', -1) for i in range(3)]
        hat = cv2.imread('./data/h1.png', -1)
        for face in faces:
            #hat = hats[]#c_hat[0] #random.choice(hats)
            scale = face[3] / hat.shape[0] * 2
            hat = cv2.resize(hat, (0, 0), fx=scale, fy=scale)
            x_offset = int(face[0] + face[2] / 2 - hat.shape[1] / 2)
            y_offset = int(face[1] - hat.shape[0] / 2)

            x1 = max(x_offset, 0)
            x2 = min(x_offset + hat.shape[1], img.shape[1])
            y1 = max(y_offset, 0)
            y2 = min(y_offset + hat.shape[0], img.shape[0])
            hat_x1 = max(0, -x_offset)
            hat_x2 = hat_x1 + x2 - x1
            hat_y1 = max(0, -y_offset)
            hat_y2 = hat_y1 + y2 - y1

            alpha_h = hat[hat_y1:hat_y2, hat_x1:hat_x2, 3] / 255
            alpha = 1 - alpha_h

            for c in range(3):
                img[y1:y2, x1:x2, c] = alpha_h * hat[hat_y1:hat_y2, hat_x1:hat_x2, c] + alpha * img[y1:y2, x1:x2, c]


            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            return img
        
        else:
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            return img


def blend_images(hat_img):
    background = cv2.imread("./data/background.png")
    background = cv2.cvtColor(background, cv2.COLOR_BGR2RGB)
    background = cv2.resize(background, (hat_img.shape[1], hat_img.shape[0]))
    result = cv2.addWeighted(hat_img, 1., background, 1., 0)
    return result
    
    
def christmas_beard(img):
    
    cname = './data/haarcascade_frontalface_alt.xml'
    faces = face_detect(img, cname)
    
    if faces is not None:

        moustache = cv2.imread('./data/b1.png', -1)
        print(faces)
        for face in faces:
            hat = moustache #hats[2] #random.choice(hats)
            scale = face[3] / hat.shape[0]
            #sf = 0.5
            hat = cv2.resize(hat, (0, 0), fx=scale, fy=scale)
            x_offset = int(face[0] + face[2] / 2 - hat.shape[1] / 2)
            y_offset = int(face[1] - hat.shape[0] / 2) + 250

            x1 = max(x_offset, 0)
            x2 = min(x_offset + hat.shape[1], img.shape[1])
            y1 = max(y_offset, 0)
            y2 = min(y_offset + hat.shape[0], img.shape[0])
            hat_x1 = max(0, -x_offset)
            hat_x2 = hat_x1 + x2 - x1
            hat_y1 = max(0, -y_offset)
            hat_y2 = hat_y1 + y2 - y1

            alpha_h = hat[hat_y1:hat_y2, hat_x1:hat_x2, 3] / 255
            alpha = 1 - alpha_h

            for c in range(3):
                img[y1:y2, x1:x2, c] = alpha_h * hat[hat_y1:hat_y2, hat_x1:hat_x2, c] + alpha * img[y1:y2, x1:x2, c]


            #img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            return img

        else:
            return img
    
    
def face_detect(img, cname):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_hist = cv2.equalizeHist(img_gray)
    face_cascade = cv2.CascadeClassifier(cname)
    faces = face_cascade.detectMultiScale(img_hist)
    return faces


class CamApp(MDApp):

    def save_image(self):
        cv2.imwrite('./data/your_avatar.png', self.modified_image)

    def build(self):
        self.sound = SoundLoader.load("data/xmas.wav")
        self.sound.volume = 0.05
        self.sound.play()
        self.modified_image = None
        sv = ScrollView()
        ml = MDList()
        sv.add_widget(ml)
        contacts = ["Paula", "John", "Kate", "Vlad"]
        for c in contacts:
            ml.add_widget(
                OneLineListItem(
                    text=c
                )
            )
        self.toolbar = MDToolbar(title="Create your Christmas avatar!")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["content-save", lambda x: self.save_image()]]
        #self.toolbar.left_action_items = [['menu',lambda x: app.navigation_draw()]]
        self.img1=Image()
        self.img1.size_hint = (0.7, 1.0)
        self.img1.pos_hint = {"center_x": 0.5, "center_y": 0.5}
        #self.save_button = MDRectangleFlatButton(text='Save image',
        #                                         pos_hint={"center_x": 0.5, "center_y": 0.95})
        #self.prompt_button1 = MDFloatingActionButtonSpeedDial(pos_hint={'x': .1, 'y': .1})
        #self.prompt_button1.data = {'left hat': 'opencv_image.png'}
        layout = MDScreen()
        layout.add_widget(self.toolbar)
        #layout.add_widget(self.save_button)
        layout.add_widget(self.img1)
        #layout.add_widget(sv)
        #layout.add_widget(self.prompt_button1)
        #layout.add_widget(self.card)
        #opencv2 stuffs
        self.capture = cv2.VideoCapture(0)
        cv2.namedWindow("CV2 Image")
        Clock.schedule_interval(self.update, 1.0/33.0)
        return layout

    def update(self, dt):
        # display image from cam in opencv window
        ret, frame = self.capture.read()
        cv2.imshow("CV2 Image", frame)
        # convert it to texture

        #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        hat_img = christmas_hat(frame)
        hat_img = christmas_beard(hat_img)
        hat_img = blend_images(hat_img)
        
        self.modified_image = cv2.cvtColor(hat_img, cv2.COLOR_BGR2RGB)
        buffer = cv2.flip(hat_img, 0).tostring()
        texture1 = Texture.create(size=(hat_img.shape[1], hat_img.shape[0]), colorfmt='rgb')
        texture1.blit_buffer(buffer, colorfmt='rgb', bufferfmt='ubyte')

        # display image from the texture
        self.img1.texture = texture1

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()