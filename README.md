# Youtube Viewer Increment
Increse your viewers with this bot !


This code uses selenium to scrap the Youtube page that you want to increase its viewers count. In the following sections I wil explain how to enter your page URL and how this code increases the viewers.




## Install

### Dependencies

You need the following dependencies:

- python3
- selenium
- pyfy
- youtube-dl



### Install the repo and the requirements

Clone the repository and install 3rd-party libraries.

```bash
$ git clone https://github.com/Kianoush-h/Youtube-Viewer-Increment.git
$ cd Youtube-Viewer-Increment
$ pip3 install -r requirements.txt
```








## Run the code

You can run the the code with this:

```
python3 viewer.py
```
After you run the mentioned code in your console, it opens a browser page in the background.

![wifi](./etc/pic2.JPG)

 
 
 
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
url = 'https://www.youtube.com/channel/UC9BJisjDT9Gm4zdH1GZTuPA/videos'
 ```



















