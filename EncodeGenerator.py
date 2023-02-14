import os
import pickle
import cv2
import face_recognition
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage


cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://face-attendance-project-b984e-default-rtdb.firebaseio.com/",
    'storageBucket': "face-attendance-project-b984e.appspot.com"
})


# Importing the images
folderPath = 'Images'
# getting the list from Images folder by listdir('Images')
pathList = os.listdir(folderPath)
imgList = []
studentIds = []

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    studentIds.append(os.path.splitext(path)[0])
    # os.path.join(folderPath, path) with this line creating a full path (for example Images/321654.png)
    # print(os.path.splitext(path)) -> print(os.path.splitext(path)[0])
    # ('321654', '.png') with the split text, path is splitted into two parts recognized as array elements. Since we're doing a student
    # attendance system, and the image names are the ID numbers, we don't want .png or .jpeg parts therefore we need 0'th element only.
    fileName = f'{folderPath}/{path}'
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)

# print(studentIds)  # ['321654', '852741', '963852']


def findEncodings(imagesList):

    encodeList = []

    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)

    return encodeList


print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
print(encodeListKnown)
print("Encoding Complete")


print("Writing Into File...")
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
file.close()
print("File saved")
