from selenium import webdriver 
from time import sleep 
from selenium.webdriver.firefox.options import Options
import pafy



url = 'https://www.youtube.com/channel/UC9BJisjDT9Gm4zdH1GZTuPA/videos'


options = Options()
options.headless = True
driver = webdriver.Firefox(options=options, executable_path='./geckodriver.exe')

driver.get(url) 

vid_list = []

for i in range(1,100):
    sections = '/html/body/ytd-app/div/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-grid-renderer/div[1]/ytd-grid-video-renderer[1]'
    try:
        a = driver.find_element_by_xpath(sections[:-3]+'['+str(i)+']')
        vid_list = vid_list + [a]
    except:
        pass
        
print('there are ' + str(len(vid_list))+ ' videos')
    




for j in range(1000):
    print('round: ' + str(j))    
    for i in range(len(vid_list)): 
        a = vid_list[i]
        a.click()
        print('playing ... '+ str(i))
        sleep(5)
        # driver.find_element_by_xpath('//*[@id="ytd-player"]').click()
        # sleep(3)
        video = pafy.new(driver.current_url)
        video_length = video.length
        
        print('video length:' + str(video_length))
        # driver.find_element_by_xpath('//*[@id="ytd-player"]').click()
        
        sleep(video_length*0.7)
        
        print('Next ... ')
        driver.back()
        sleep(5)



































