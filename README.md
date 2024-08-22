# Course Jumper 
* Created by Ayush Shukla
This Module is developed to facilitate skipping Coursera (https://www.coursera.org/) videos.

## Why ?
Course Jumper assists in automatically skip irrelevant MOOC courses which are made mandatory by universities. 
Many of such courses are allotted directly by the university as credit fillers and are not in the interest of the student. The progress of the completion of these courses is tracked by the university and credits are allotted.

## How ?
Course Jumper makes use of the Coursera web API and completes the videos + reading materials.
Surveys are not automatically completed since they are graded, thus needing user interaction to complete.

## Requirements :
* Python 3.1+ must be Installed.
* [Only Windows] - Path set in Environment Variables
  For Setting Path follow these steps =>
  * Open Python File Location and Copy Path

 ![New Project](https://github.com/user-attachments/assets/36597e38-d4f2-4ff2-b8bb-42efc8ed7103)


  * Open Environment Variables > Path > Add the Python and Script folder Path

![New Project-2](https://github.com/user-attachments/assets/fb46398b-f9b2-48d5-8fda-14af2145b185)
<img width="1149" alt="Screenshot 2024-08-23 at 3 33 18 AM" src="https://github.com/user-attachments/assets/092287f2-0960-4cfd-8171-d25521f0ad02">


  * Now the Path is Set Successfully !!

## How to get cAUTH Cookies ?
* Firstly open Chrome and Login to Coursera
* Now Open any Course Video and open Developer Options [ Ctrl+Shift+I OR Cmd+Option+I ]
* Locate infobatch calls to Coursera domain and copy it as cURL(Bash)

![Screenshot 2024-08-22 at 10 39 42 PM](https://github.com/user-attachments/assets/5b269bfc-f3dd-4dfa-a4c0-53f56b6a348f)


* Go to [https://curlconverter.com](https://curlconverter.com) and Paste the copied cURL and then from the result copy only the Cookie content.


![Screenshot 2024-08-22 at 10 47 18 PM](https://github.com/user-attachments/assets/a2a0d4a7-b0ec-4fc2-a0f1-8e79ae6db99d)

* Now this is the cAUTH cookie that you need !!

## How to use
* Download the Latest Release and Extract the ZIP file
* Open the Folder
* Windows Hosts => run.bat
* macOS/Linux => run.commaand



<img width="1440" alt="Screenshot 2024-08-23 at 3 34 37 AM" src="https://github.com/user-attachments/assets/229fdf35-e6b1-4f26-bb36-2aed5642cf2c">


* Now the App will Open. Enter Your Course URL,Email address, Password and cAUTH cookie and hit Start.
* Wait till it Says Completed and Done !!
  

<img width="798" alt="Screenshot 2024-08-23 at 4 35 22 AM" src="https://github.com/user-attachments/assets/0657263b-8dc6-42ec-8b82-7d6ef6283a06">





