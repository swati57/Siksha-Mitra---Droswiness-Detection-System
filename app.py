import cv2
import os
from keras.models import load_model
import numpy as np
from pygame import mixer
from flask import Flask, render_template,Response
import random

app=Flask(__name__)

model = load_model('models/myModel.h5')

def generate_frames(camera_switch):
    if camera_switch==0:
        cv2.VideoCapture.release()
        cv2.destroyAllWindows()
        return 
    camera=cv2.VideoCapture(0)
    count=0
    score=0
    thicc=2
    rpred=[99]
    lpred=[99]
    face = cv2.CascadeClassifier('haar cascade files\haarcascade_frontalface_alt.xml')
    leye = cv2.CascadeClassifier('haar cascade files\haarcascade_lefteye_2splits.xml')
    reye = cv2.CascadeClassifier('haar cascade files\haarcascade_righteye_2splits.xml')
    while True:
        success,frame=camera.read()
        if not success:
            break
        else:
            mixer.init()
            sound = mixer.Sound('alarm.wav')
            lbl=['Close','Open']
            
            path = os.getcwd()
            font = cv2.FONT_HERSHEY_COMPLEX_SMALL
            
            height,width = frame.shape[:2] 

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            
            faces = face.detectMultiScale(gray,minNeighbors=5,scaleFactor=1.1,minSize=(25,25))
            left_eye = leye.detectMultiScale(gray)
            right_eye =  reye.detectMultiScale(gray)

            cv2.rectangle(frame, (0,height-50) , (200,height) , (0,0,0) , thickness=cv2.FILLED )

            for (x,y,w,h) in faces:
                cv2.rectangle(frame, (x,y) , (x+w,y+h) , (100,100,100) , 1 )

            for (x,y,w,h) in right_eye:
                r_eye=frame[y:y+h,x:x+w]
                count=count+1
                r_eye = cv2.cvtColor(r_eye,cv2.COLOR_BGR2GRAY)
                r_eye = cv2.resize(r_eye,(24,24))
                r_eye= r_eye/255
                r_eye=  r_eye.reshape(24,24,-1)
                r_eye = np.expand_dims(r_eye,axis=0)
                rpred_eye = model.predict(r_eye)
                rpred=np.argmax(rpred_eye,axis=1)
                if(rpred[0]==1):
                    lbl='Open' 
                if(rpred[0]==0):
                    lbl='Closed'
                break

            for (x,y,w,h) in left_eye:
                l_eye=frame[y:y+h,x:x+w]
                count=count+1
                l_eye = cv2.cvtColor(l_eye,cv2.COLOR_BGR2GRAY)  
                l_eye = cv2.resize(l_eye,(24,24))
                l_eye= l_eye/255
                l_eye=l_eye.reshape(24,24,-1)
                l_eye = np.expand_dims(l_eye,axis=0)
                lpred_eye = model.predict(l_eye)
                lpred=np.argmax(lpred_eye,axis=1)
                if(lpred[0]==1):
                    lbl='Open'   
                if(lpred[0]==0):
                    lbl='Closed'
                break

            if(rpred[0]==0 and lpred[0]==0):
                score=score+1
                cv2.putText(frame,"Closed",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            else:
                score=score-1
                cv2.putText(frame,"Open",(10,height-20), font, 1,(255,255,255),1,cv2.LINE_AA)
            
                
            if(score<0):
                score=0   
            if(score>20):
                #person is feeling sleepy so we beep the alarm
                try:
                    sound.play()
                except: 
                    pass
                if(thicc<16):
                    thicc= thicc+2
                else:
                    thicc=thicc-2
                    if(thicc<2):
                        thicc=2
                cv2.rectangle(frame,(0,0),(width,height),(0,0,255),thicc)
            
            ret,buffer=cv2.imencode('.jpg',frame)
            frame=buffer.tobytes()
            yield(b'--frame\r\n'
            b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/detection_page.html")
def detection():
    with open('tips.csv',encoding="utf8") as file:
        content = file.readlines()
        rows = content[1:]
        content=rows[random.randint(0,len(rows)-1)].split(',')
        return render_template("detection_page.html",quotes=rows)


@app.route('/video/<int:camera_switch>')
def video(camera_switch):
    if(camera_switch==1):
        return Response(generate_frames(camera_switch),mimetype='multipart/x-mixed-replace; boundary=frame')
    else:
        cv2.VideoCapture.release()
        cv2.destroyAllWindows()
        return

if __name__=="__main__":
    app.run(debug=False)
