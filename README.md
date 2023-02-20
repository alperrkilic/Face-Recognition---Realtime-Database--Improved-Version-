<a name="readme-top"></a>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-">
    <img src="Readme-Images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">Face Recognition with Realtime Database</h3>

  <p align="center">
    A Face Recognition Project
    <br />
    <a href="https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-">View Demo</a>
    ·
    <a href="https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/issues">Report Bug</a>
    ·
    <a href="https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <!-- <li><a href="#usage">Usage</a></li> -->
    <li><a href="#images">Images</a></li>
    <!-- <li><a href="#contributing">Contributing</a></li> -->
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

Welcome to our Face Recognition with Realtime Database project, which aims to provide a seamless attendance-taking experience for educational institutions. With this system, we have created an efficient and reliable method for tracking students' attendance in real-time, using facial recognition technology and a Firebase database.

The system stores data and images of each student in the Firebase database, including their name, ID, major, starting year, last attendance, and total attendance. Each student is categorized according to their unique ID number and is treated as an object in the system. Their images are also stored in the database alongside their ID number.

Using facial recognition, the system matches the image captured by the camera with the images stored in the database. Once a match is found, the corresponding student's information is downloaded from the database and displayed on the user interface.

To prevent duplicate attendance, the system has several modes, including active, marked, already marked, no match, and display mode. When a student is detected, their ID is stored and their information is downloaded from the database. The UI mode is then set to "marked" for a few seconds to indicate that the student has been successfully marked as present. If the same student attempts to check in again, the system will switch to the "already marked" mode to prevent duplicate attendance.

When a student is marked as present, their last attendance and total attendance records are updated in the database. With the elapsed time, the system can control when a student can be marked present again, ensuring accurate attendance records.

Overall, our Face Recognition with Realtime Database project offers a reliable, convenient, and efficient way to take attendance in classrooms. With this system, educational institutions can implement automatic attendance-taking, saving time and improving accuracy.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

Our Face Recognition with Realtime Database project is built with Python, OpenCV, dlib, numpy, and face_recognition libraries. These powerful tools allow us to detect and recognize faces from live video feeds and automatically take attendance. With our system, you can save time and streamline attendance-taking in classrooms and events.

* [![Python][Python]][Python-url]
* [![openCV][openCV]][openCV-url]


<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

Before you can get started with our Face Recognition with Realtime Database project, you need to make sure that you have a few prerequisites in place. Don't worry; these are straightforward to set up, and we'll guide you through the process.

To use our system, you will need to have Python 3.x installed on your computer, along with pip (the Python package manager). You'll also need to create a Firebase account and project, and obtain the necessary credentials to access the Firebase database. Additionally, you'll need a webcam or camera to capture the students' faces for attendance purposes.

Once you have all the prerequisites in place, you can easily install and set up the Face Recognition with Realtime Database project by following a few simple steps. We've provided detailed instructions in the "Installation" section of this README file to help you get started quickly.

### Prerequisites

To install the required files, please enter the following commands into your terminal: 
* pip
  ```sh
  pip install opencv-python 
  ```
  ```sh
  pip install cvzone
  ```
  ```sh
  pip install numpy
  ```
  ```sh
  pip install cmake
  ```
  ```sh
  pip install dlib
  ```
  ```sh
  pip install face-recognition
  ```
  ```sh
  pip install firebase_admin
  ```
  ```sh
  pip install pickle
  ```


  _If you're having trouble installing dlib for our Face Recognition with Realtime Database project, there are a few things to keep in mind. First, note that dlib and face_recognition packages only work with Python 3.7, 3.8, and 3.9. So make sure you're using one of these Python versions_

  _If you're on Windows 11 and having trouble installing dlib, you can refer to this helpful guide by Sacha De'Angeli: https://github.com/sachadee/Dlib. It provides detailed steps to help you install dlib successfully on Windows 11._

  _We hope this note helps you resolve any issues you may encounter during the installation process. If you still have questions or need further assistance, please feel free to reach out to us for support._

### Installation

_Installing the Face Recognition with Realtime Database project is quick and easy. Follow these simple steps to get started in just a few minutes!_

1. Create your virtual environment with Pycharm
2. Clone the repository to your local machine:
   ```sh
   git clone https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-
   ```
3. Install the required dependencies:
   ```sh
   Visual Studio 2019 || Visual Studio 2022
   ```

   _Note: This project is built with Python 3.8, so make sure you have it installed on your machine._
4. Open the project in Visual Studio Code or your preferred code editor.
   ```js
   That's it! You're now ready to use the Face Recognition with Realtime Database Project.
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- Images -->
## Images

[![Screen Shots][active-mode]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_This is active mode when there's no face detected through webcam_

[![Screen Shots][loading-screen]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_To account for the time it takes to compare faces, the system displays a loading message until a match is found. Once a match is detected, the corresponding student data is displayed._


[![Screen Shots][product-screenshot]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_If a match is found between the detected face and the faces in our database, the system displays the corresponding user data retrieved from the Firebase server._

[![Screen Shots][already-marked-mode]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_If the face has been matched before, the system will display Already Marked mode._

[![Screen Shots][no-match-mode]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_If there's no match between the face and the student images, system will display No Match mode._

## __How it works ?__ 

<br>


### __EncodeGenerator.py__

[![Screen Shots][encode-img-from-imglist]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)


_The 'findEncodings()' function in the 'EncodeGenerator.py' file accepts an 'imagesList' parameter and encodes the images, storing them into the 'encodeList' array. To read this data from the 'main.py' file, we need to write the encodings to a file._

<br>


[![Screen Shots][saving-encodings]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_This step involves generating the 'EncodeFile.p' that 'main.py' will use._

<br>


[![Screen Shots][uploading-img-to-database]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_To work with a database, we need to upload our images to it. The 'fileName' variable stores the path of the image, which is then uploaded to the database using the 'upload_from_filename()' function with 'fileName' as the parameter._

See the [EncodeGenerator.py](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/blob/master/EncodeGenerator.py) for the detailed explanations on the code.

<br>


### __AddingDataToDatabase.py__

[![Screen Shots][accessing-to-database]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_This step involves accessing to the database with the 'serviceAccountKey.json' file and the URL for the project._

<br>


[![Screen Shots][data-elements]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_Every student's data is stored in a variable called 'data', which holds the students as objects according to their ID numbers. Here is an example of a student._

<br>


[![Screen Shots][adding-data-to-database]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_Finally, to update the data in our Firebase database, we need to set the new values, which are the student objects._


See the [AddingDataToDatabase.py](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/blob/master/AddDataToDatabase.py) for the detailed explanations on the code.


### __main.py__


[![Screen Shots][loading-encoded-file]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_In our 'main.py' file, we will use the 'EncodeFile.p' that we generated with 'EncodeGenerator.py'. To do this, we open the file in read mode and store the values inside 'encodeListKnownWithIds'. Next, we store the encodings and IDs into separate variables so that we can use them later._

<br>


[![Screen Shots][matches-face-dis-loop]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_Within this loop, the variable encodeCurFrame stores the encoded image of the webcam for each frame, while faceCurFrame stores the location of the face in the current frame. The purpose of this loop is to compare the encodings between the current frame and those previously generated by EncodeGenerator.py. If there is a match, the modes of the user interface can be switched accordingly within our system._

<br>

[![Screen Shots][matches-face-dis]](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

_The 'matches' array holds boolean values that indicate whether the face on the webcam matches a face in our database. If the faces match, then the corresponding element in the array is set to true. The 'faceDis' array holds the distances between faces. A lower distance indicates that the faces are more similar._



See the [main.py](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/blob/master/main.py) for the detailed explanations on the code.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
<!-- ## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Bayram Alper KILIÇ - [@alperrkilic](https://www.linkedin.com/in/bayram-alper-kilic/) - alperkilicbusiness@gmail.com

Project Link: [https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-](https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Creating a project like the Face Recognition with Realtime Database requires a lot of research, experimentation, and dedication. I would like to take this opportunity to acknowledge and thank the many individuals, channels, and websites that helped me along the way. Without their guidance and support, this project would not have been possible. In particular, I would like to recommend the following channels and websites for their invaluable resources and contributions to the field of computer vision and image processing.

* [Computer Vision Zone](https://www.computervision.zone/)
* [Murtaza's Workshop - Robotics and AI](https://www.youtube.com/@murtazasworkshop)
* [ChatGPT](https://chat.openai.com/chat)
* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)


<p align="right">(<a href="#readme-top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-.svg?style=for-the-badge
[contributors-url]: https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-.svg?style=for-the-badge
[forks-url]: https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/network/members
[stars-shield]: https://img.shields.io/github/stars/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-.svg?style=for-the-badge
[stars-url]: https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/stargazers
[issues-shield]: https://img.shields.io/github/issues/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-.svg?style=for-the-badge
[issues-url]: https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/issues
[license-shield]: https://img.shields.io/github/license/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-.svg?style=for-the-badge
[license-url]: https://github.com/alperrkilic/Face-Recognition---Realtime-Database--Improved-Version-/blob/master/LICENSE.txt
<!-- Built with and Social Media -->
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/bayram-alper-kilic/
[Python]: https://img.shields.io/badge/python-000000?style=for-the-badge&logo=python&
[Python-url]: https://www.python.org/
[openCV]: https://img.shields.io/badge/opencv-%23white.svg?style=for-the-badge&logo=opencv&logoColor=white
[openCV-url]: https://opencv.org/
<!-- Modes -->
[product-screenshot]: Readme-Images/Modes/displaying-data.png
[active-mode]: Readme-Images/Modes/active-mode.png
[already-marked-mode]: Readme-Images/Modes/already-marked.png
[loading-screen]: Readme-Images/Modes/loading-screen.png
[no-match-mode]: Readme-Images/Modes/no-match.png
<!-- main.py -->
[matches-face-dis]: Readme-Images/main.py/matches-face-dis.png
[matches-face-dis-loop]: Readme-Images/main.py/matches-face-dis-for-loop.png
[loading-encoded-file]: Readme-Images/main.py/loading-encoded-file.png
<!-- EncodeGenerator.py -->
[encode-img-from-imglist]: Readme-Images/EncodeGenerator.py/encode-img-from-imglist.png
[saving-encodings]: Readme-Images/EncodeGenerator.py/saving-encodings-into-EncodeFile.png
[uploading-img-to-database]: Readme-Images/EncodeGenerator.py/uploading-image-into-database.png
<!--  AddingDataToDatabase -->
[accessing-to-database]: Readme-Images/AddingDataToDatabase.py/accessing-to-database.png
[adding-data-to-database]: Readme-Images/AddingDataToDatabase.py/adding-data-to-database.png
[data-elements]: Readme-Images/AddingDataToDatabase.py/data-elements.png
