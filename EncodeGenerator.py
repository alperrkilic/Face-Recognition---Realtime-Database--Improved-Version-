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

# with storageBucket we upload images to real-time database.
# Since we run this program to encode the images into EncodeFile.p, we only need this when we add new image to our images.

# Importing the images
folderPath = 'Images'
# getting the list from Images folder by listdir('Images')
pathList = os.listdir(folderPath)
imgList = []
studentIds = []


# in the loop below, we add every image path one by one. Since we can also update the database one by one,
# we can use this loop to update our database.

for path in pathList:
    imgList.append(cv2.imread(os.path.join(folderPath, path)))
    # appending the id's into studentIds array and storing them
    studentIds.append(os.path.splitext(path)[0])
    # os.path.join(folderPath, path) with this line creating a full path (for example Images/321654.png)
    # print(os.path.splitext(path)) -> print(os.path.splitext(path)[0])
    # ('321654', '.png') with the split text, path is splitted into two parts recognized as array elements. Since we're doing a student
    # attendance system, and the image names are the ID numbers, we don't want .png or .jpeg parts therefore we need 0'th element only.
    fileName = f'{folderPath}/{path}'
    # fileName variable holds the path for the image
    bucket = storage.bucket()
    # bucket variable now has access to our database storageBucket.
    blob = bucket.blob(fileName)
    # so in a variable called blob, we will store the binary image. Also the abbreviation for blob is Binary Large Object.
    blob.upload_from_filename(fileName)
    # after storing the bucket into blob, we will upload our file with its path into our storageBucket with upload_from_filename() function.

# print(studentIds)  # ['321654', '852741', '963852']


def findEncodings(imagesList):

    encodeList = []

    for img in imagesList:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        # encoding the faces into encode variable, and then we'll store them into encodeList array.
        # with that array
        # since we're sending only one image at a time, we should choose the 0'th element every time.
        encodeList.append(encode)

    return encodeList


# This part is for encoding the image into encodeListKnown variable
print("Encoding Started...")
encodeListKnown = findEncodings(imgList)
encodeListKnownWithIds = [encodeListKnown, studentIds]
# encodeListKnownWithIds is a double array, i stands for the encode list and j stands for the studentIds
print(encodeListKnown)
print("Encoding Complete")


print("Writing Into File...")
# opening the EncodeFile.p in write mode which means, this file will be deleted and created again if it's not present.
file = open("EncodeFile.p", 'wb')
pickle.dump(encodeListKnownWithIds, file)
# dumping the encodeListKnownWithIds into file
file.close()
# closing the file.
print("File saved")

# After this, now we have the data stored in EncodeFile.p. We know the Id's, and imageEncodings for every image. Now we can use this file in our main.py
# Since this encodings are our reference when we compare, Now in main.py the only thing we need to do is to compare the known encodings with the encodings of the
# webcam image. Thus we can say whether the face matches or not.
