# Face Recognizer

## Pre-request
```
sudo apt update
sudo apt install git python3 python3-pip python3-venv
```

## Setup
**1. Env**
```
python3 -m venv .venv
source .venv/bin/activate
python3 -m pip install -r requirements.txt
```

**2. Download data from OpenCV**
OpenCV Github：https://github.com/opencv/opencv/tree/4.x/data
Frontal Face Model：haarcascade_frontalface_default.xml

**3. Unzip `data_4_setup.zip` and Put all data into `data` folder**
```
data
├── catmeme.png
├── CMakeLists.txt
├── face.yml
├── haarcascade_frontalface_default.xml
├── haarcascades
├── haarcascades_cuda
├── hogcascades
├── lbpcascades
├── mona.png
├── pic
├── readme.txt
└── vec_files
```

**4. Run**
```
python3 contrib/face_detection.py
python3 read_image.py
```

###### REF
https://steam.oxxostudio.tw/category/python/ai/ai-face-dectection.html