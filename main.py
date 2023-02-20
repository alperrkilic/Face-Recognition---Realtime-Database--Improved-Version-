import os
import pickle
import numpy as np
import cv2
import face_recognition
import cvzone
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-project-b984e-default-rtdb.firebaseio.com/",
    'storageBucket': "face-attendance-project-b984e.appspot.com"
})

# storing database and storageBucket

bucket = storage.bucket()

# capture the video with the 0'th camera, if you have more than 1 camera you can use 1'st element
cap = cv2.VideoCapture(0)

cap.set(3, 640)  # setting the height and width to webcam
cap.set(4, 480)

imgBackground = cv2.imread('Resources\\background.png')  # background image


# Importing the mode images
folderModePath = 'Resources\\Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []

for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))

# print(len(imgModeList))

# Load the encoding file

print("Loading Encode File...")
file = open('EncodeFile.p', 'rb')
# since EncodeFile.p contains binary data we open file in rb mode which is a mode used when opening a file to read binary data, such as images, audio, or video files.
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print("Encode file Loaded")
# print(studentIds)
# print(encodeListKnown)


modeType = 0
counter = 0
id = -1
imgStudent = []

while True:
    success, img = cap.read()

    # imgS is an abbreviation of image Small
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    # resizing the image by 1/4 so that we can process faster.
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)
    # openCV library uses BGR so we have to convert it to RGB by cv2.cvtColor(imgS,cv2.COLOR_BGR2RGB)

    faceCurFrame = face_recognition.face_locations(imgS)
    # print(faceCurFrame)
    # faceCurFrame holds the locations of the face
    encodeCurFrame = face_recognition.face_encodings(imgS, faceCurFrame)
    # encodeCurFrame is the output of face_recognition.face_encodings(imgS,faceCurFrame) first parameter is image in a moment and the second one is the location of the face

    imgBackground[162:162+480, 55:55+640] = img
    # attaching the camera to our user interface (webcam)
    imgBackground[44:44+633, 808:808+414] = imgModeList[modeType]
    # attaching the mode on to right of our user interface (active, data , already marked , no match)

    if faceCurFrame:  # if there's a face in current frame

        for encodeFace, faceLoc in zip(encodeCurFrame, faceCurFrame):
            matches = face_recognition.compare_faces(
                encodeListKnown, encodeFace)
            # matches store whether there's a match or not in boolean variable
            faceDis = face_recognition.face_distance(
                encodeListKnown, encodeFace)
            # faceDis stores the distance of the current face and the images
            print(matches)  # [False, False, False]
            print(faceDis)  # [0.72079832 0.81759772 0.70714724]

            # matches [] holds boolean elements and matchIndex is the index of the smallest distance
            # so if we check in matches[matchIndex] meaning that if face is recognized by the list in another words if True: then execute the statements
            matchIndex = np.argmin(faceDis)
            # matchIndex holds the minimum distance among all faces

            if matches[matchIndex]:  # for example 3. index is the smallest distance it will check as, if matches[3] true while matches holds the boolean values for face_comparisons
                y1, x2, y2, x1 = faceLoc  # the same order with the location coordinates
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                # since size was reduced to 1/4 we have to multiply coordinates by 4
                bbox = 55+x1, 162+y1, x2-x1, y2-y1
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                # creating a detected indicator onto our image with bbox, 55 and 162 are given according to the coordinates of the image
                id = studentIds[matchIndex]
                # id variable holds the student Id at matched index
                # print(id) checking whether the id is true
                if counter == 0:
                    cvzone.putTextRect(imgBackground, "Loading", (275, 400))
                    # since detection might take a long time, we should prompt the user with loading text.
                    cv2.imshow("Face Attendance", imgBackground)
                    cv2.waitKey(1)
                    counter = 1
                    modeType = 1
            else:
                y1, x2, y2, x1 = faceLoc  # the same order with the location coordinates
                y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
                # since size was reduced to 1/4 we have to multiply coordinates by 4
                bbox = 55+x1, 162+y1, x2-x1, y2-y1
                modeType = 4
                imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)
                imgBackground[44:44 + 633, 808:808+414] = imgModeList[modeType]
                cv2.imshow("Face Attendance",
                           imgBackground)
                cv2.waitKey(1)

        if counter != 0:

            if counter == 1:
                # Get the data
                studentInfo = db.reference(f'Students/{id}').get()
                # print(studentInfo)  # getting the studentInfo from realtime database
                # Get the image from the storage
                blob = bucket.get_blob(f'Images/{id}.png')
                array = np.frombuffer(blob.download_as_string(), np.uint8)
                imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
                # Update data of attendance
                datetimeObject = datetime.strptime(studentInfo['last_attendance_time'],
                                                   "%Y-%m-%d %H:%M:%S")
                secondsElapsed = (
                    datetime.now() - datetimeObject).total_seconds()
                # print(secondsElapsed)
                if secondsElapsed > 20:  # if 20 seconds passed, then increase attendance by one and update the last_attendance_time
                    ref = db.reference(f'Students/{id}')
                    # above we said that id holds the value of the matched student. and ref holds the data from database.
                    # Since in database, we have Students and this element has objects that are named according to their ids.
                    # So ref will hold the data for that specific student with this statement  db.reference(f'Students/{id}')
                    # and also student info only holds the information of that student with attributes in strings. So we will increase the attendance
                    # in studentInfo variable and then set this total_attendance variable to ref value and update the database.
                    studentInfo['total_attendance'] += 1
                    ref.child('total_attendance').set(
                        studentInfo['total_attendance'])
                    ref.child('last_attendance_time').set(
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                else:
                    modeType = 3  # changing the modeType to marked.
                    counter = 0
                    imgBackground[44:44 + 633, 808:808 +
                                  414] = imgModeList[modeType]  # choosing the mode and attaching it into our system.

            if modeType != 3:

                if 10 < counter < 20:
                    modeType = 2  # between the value of counter 10 and 20 modeType will be already marked

                imgBackground[44:44 + 633, 808:808+414] = imgModeList[modeType]

                if counter <= 10:  # if not marked, then from studentInfo we will access to the data and put them into our user interface
                    # the values are given due to positions to be placed. eg. (861,125)
                    # size -> 0.6 , (255,255,255) stands for color, last attribute (1) stands for thickness and cv2.FONT_HERSHEY_COMPLEX is to determine the font.
                    cv2.putText(imgBackground, str(studentInfo['total_attendance']), (
                        861, 125), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 1)
                    # putting total_attendance into our user interface as text with font-size 1, in white color, with FONT_HERSHEY_COMPLEX and thickness is 1
                    cv2.putText(imgBackground, str(studentInfo['major']), (
                        1006, 550), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(id), (
                        1006, 493), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255, 255, 255), 1)
                    cv2.putText(imgBackground, str(studentInfo['standing']), (
                        910, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo['year']), (
                        1025, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)
                    cv2.putText(imgBackground, str(studentInfo['starting_year']), (
                        1125, 625), cv2.FONT_HERSHEY_COMPLEX, 0.6, (100, 100, 100), 1)

                    # in here we are centering the name since length of the name can vary we must center it.
                    (w, h), _ = cv2.getTextSize(
                        studentInfo['name'], cv2.FONT_HERSHEY_COMPLEX, 1, 1)
                    offset = (414-w)//2
                    cv2.putText(imgBackground, str(studentInfo['name']), (
                        808+offset, 445), cv2.FONT_HERSHEY_COMPLEX, 1, (50, 50, 50), 1)

                    imgBackground[175:175+216, 909:909+216] = imgStudent

            counter += 1

            if counter >= 20:  # after counter is greater than 20 we will reset all the values
                counter = 0
                modeType = 0
                studentInfo = []
                imgStudent = []
                imgBackground[44:44 + 633, 808:808+414] = imgModeList[modeType]

    else:
        modeType = 0
        counter = 0

    cv2.imshow("Face Attendance", imgBackground)
    cv2.waitKey(1)
