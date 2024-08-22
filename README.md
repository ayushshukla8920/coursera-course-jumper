# Course Jumper
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
  * Now the Path is Set Successfully !!

## How to get cAUTH Cookies ?
* Firstly open Chrome 

## How to use
* A sample config is provided in the repo. For now, cookie auth has been implemented since login requires reCaptcha.
* Add your cookies to example config as key:value pairs (simple python dict). The presence of the "CAUTH" cookie is important. (https://github.com/serv0id/skipera/issues/1)
* Rename `config_example.py` to `config.py`
* `python3 main.py course-slug` where course-slug is present in the Coursera Course URL. Example: "introduction-psychology" (without the quotes) if the URL is https://www.coursera.org/learn/introduction-psychology/home/module/2.
