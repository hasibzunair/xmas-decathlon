## Christmas Face Application

Use this library to create the perfect picture for your christmas cards! Done by Hasib Zunair, Guillaume Brassard and 
Samuel Mercier. 

<p align="center">
    <a href="#"><img src="./data/your_avatar.png"></a> <br/>
    <em>
    Figure 1. Your christmas card picture!
    </em>
</p>


### Requirements

Python = 3.9.0 required. You'll also need to have an available Webcam (camera) to capture your beautiful face :). Then, run below commands.
```bash
conda create -n xmas python=3.9
conda install -c conda-forge jupyterlab
pip install kivy, kivymd, opencv-python
```

### What it does?

This library uses machine learning (face detection) to add a nice christmas app and christmas beard to your background. Based on KivyMD, run the `app.py` to see two screens appear: one will be the regular video as captured by your webcam, while the other screen will show you
the modified image with a santa claus hat and bear, a nice christmas background and even a Mariah Carey song to boost your christmas spirit!

### Run 

Clone this repo 
```bash
git clone https://github.com/hasibzunair/xmas-decathlon
cd xmas-decathlon
```
Then, run `app.py` and take a snapshot. You can find your christmas card in `data/your_avatar.png`.

If you want to modify the background image or the song, simply head over to the data/ folder and switch the background images and wav file to anything you would like!
### References
* [https://pythontic.com/app/kivy/camera](https://pythontic.com/app/kivy/camera)
* [https://github.com/XavierJiezou/opencv-christmas-hat](https://github.com/XavierJiezou/opencv-christmas-hat)