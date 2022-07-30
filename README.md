# Microsoft Engage 2022 Internship Program
# Project Name: Siksha Mitra (Drowsiness Detection System using Face Recognition) 👩‍🎓👨‍🎓

### About: 📜📜
    Siksha Mitra is a web application designed for drowsiness detection of a person. People tends to feel drowsy after sometime while studying or doing some work. And this drowsiness affect concentration on that specific work.
    In this web application, I have designed a system which keeps a track of the drowsiness of the person. The landing page of the web application will describe the project and the benefits of the project. Clicking on the ‘Get Started’ button of the landing page of the web will land you to the next page. On clicking the ‘start’ button, the camera of the system will be enabled and the face recognition will start.
    The model will run and detect the face, left-eye and right-eye of the person. Whenever the person gets drowsy or sleepy, the system will alert the user by alarm. 
The webpage also displays some tips to get rid of drowsiness. The user can feel fresh and active after following those tips. The articles of those tips are also attached in each slide so that user can visit their page to get a detailed view. 
    After the tips, some motivational quotes are being displayed. On clicking the ‘new quote’ button, new quotes will be generated using API. The quotes can be heard by clicking the speech button. It can be copied to clip board and can be posted on twitter also. 

### Technologies Used: 👩‍💻
The webpages are designed using HTML, CSS. The interaction between the webpage is established using javascript and python. The drowsiness detection model is made using the concept of deep learning by using keras in python. Several libraries like keras, numpy, OpenCV , pygame are used for the face detection. The drowsiness detection model and the front-end part is being assembled together using web application framework in python called flask. The interaction between the model and the page is established using web template engine for the Python programming called jinja template.

### TechStacks Used: 👨‍💻
HTML, CSS, javascript, python, flask

### Video Presentation: 
https://drive.google.com/file/d/1muxQ9VnFzNCpRj0RsWFQLNxT0EKnrLAP/view?usp=sharing

### Installation guide:

Open the project folder in VSCode.
Python and pip should be installed.

Install virtualenv
```shell
pip install virtualenv
```
Create a virtual environment within the project folder.
```shell
python -m venv my_venv
```

Create a virtual environment within the project folder.
```shell
python -m venv sample_venv
```

Activate virtual environment
```shell
.\sample_venv\Scripts\activate
```

Install opencv python
```shell
pip install opencv-python
```

Install flask
```shell
pip install flask
```

Install pygame
```shell
pip install pygame
```

Install tensorflow
```shell
pip install tensorflow
```

Install keras
```shell
pip install keras
```


To run the flask project, run app.py
To open your default browser to the rendered page, Ctrl+click the http://127.0.0.1:5000/ URL in the terminal.
index.html file is the main page and detection_page.html is the second page.



