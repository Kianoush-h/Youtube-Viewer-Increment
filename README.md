# Youtube Viewer Increment
Increase your viewers with this bot!


This code uses selenium to scrap the Youtube page that you want to increase its viewers count. In the following sections, I will explain how to enter your page URL and how this code increases the viewers.




## Install

### Dependencies

It would help if you had the following dependencies:

- python3
- selenium
- pafy
- youtube-dl



### Install the repo and the requirements

Clone the repository and install 3rd-party libraries.

```bash
$ git clone https://github.com/Kianoush-h/Youtube-Viewer-Increment.git
$ cd Youtube-Viewer-Increment
$ pip3 install -r requirements.txt
```








## Run the code

You can run the code with this:

```
python3 viewer.py
```
After you run the mentioned code in your console, it opens a browser page in the background.

 
 
## CODE

Importing libraries 
 
 ```
from selenium import webdriver 
from time import sleep 
from selenium.webdriver.firefox.options import Options
import pafy
 ```
 
You can enter your page URL here:
 ```
URL = '...........'
 ```

- You need to enter the page URL that contains all the videos.
- For now, this code works perfectly on the videos without Ads.



This code runs in the background, and you won't see the browser page. If you wish to see the browser page, you need to disable the "headless" line from the options section as follows:

 ```
options.headless = True
 ```


In each iteration, the code gets the video length and sleeps for that duration. Then, it plays the next video and waits until it ends.



 
 # Future 
 You can use this project to increase your Youtube video viewers. As my next step, I can modify the code to work on those videos with ADs. 
 
Furthermore, I have a plan to modify this code to create different accounts in order to be able to like the video and subscribe to the channels.
 
 


# Contact Me

Email: haratiank2@gmail.com

YouTube channel: https://www.youtube.com/channel/UCvf9_53f6n3YjNEA4NxAkJA?view_as=subscriber

GitHub: https://github.com/Kianoush-h

LinkedIn: https://www.linkedin.com/in/kianoush-haratiannejadi/















