## Christmas Face Application

App for Decathlon Canada AI Team christmas coding party. Done by Hasib Zunair, Guillaume Brassard and 
Samuel Mercier. 

### Installation

```
conda create -n xmas python=3.8
conda install -c conda-forge jupyterlab
pip install kivy, kivymd
```

### What it does

Use this library to create the perfect picture for your christmas cards!

This library uses machine learning (face detection) to add a nice christmas app and christma beard to your background. Based on KivyMD, run the `app.py` to see two screens appear: one will be the regular video as captured by your webcam, while the other screen will show you
the modified image with a santa claus hat and bear, a nice christmas background and even a Mariah Carey song to boost your christmas spirit!

To properly run this file, you'll need to:
- install Kivy and KivyMD (beware of your Python version, we ran this project using Python 3.7-3.9)
- install python-opencv library
If you want to modify the background image or the song, simply head over to the data/ folder and switch the background images and wav file to anything you would like!
You'll need to have an available Webcam (camera) to capture your beautiful face :) 


### References
* [https://pythontic.com/app/kivy/camera](https://pythontic.com/app/kivy/camera)
* [https://github.com/XavierJiezou/opencv-christmas-hat](https://github.com/XavierJiezou/opencv-christmas-hat)