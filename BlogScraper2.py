from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
import time

driver = webdriver.Chrome()
driver.get('https://crisis-diary.net/')

driver.find_element_by_link_text('Blog').click()

post_infos = []
post_locations = {}

post = driver.find_element_by_xpath("//h2[@class='entry-title']/a")
post.click()
post_infos.append(driver.find_element_by_class_name('has-text-align-right').text)
time.sleep(3)

status = True
while(status):
    try:
        driver.find_element_by_class_name('nav-previous').click()
        post_infos.append(driver.find_element_by_class_name('has-text-align-right').text)
        time.sleep(3)
        
    except NoSuchElementException:
        status = False
        
for post_info in post_infos:
    index1 = 0
    index2 = 0
    index3 = 0
    for index, letter in enumerate(post_info):
        if(letter == '|'):
            if(index1 == 0):
                index1 = index
            else:
                index2= index
        if(letter == '&'):
            index3 == index
    if(index3 == 0):
        location = post_info[index1+1:index2]
        if location in post_locations:
            post_locations[location] = post_locations[location] + 1
        else:
            post_locations[location] = 1
    else:
        location1 = post_info[index1+1:index3]
        location2 = post_info[index3+1:len(post_info)-1]
        if location1 in post_locations: 
            post_locations[location1] = post_locations[location1] + 1
        else:
            post_locations[location1] = 1
        if location2 in post_locations:
            post_locations[location2] = post_locations[location2] + 1
        else:
            post_locations[location2] = 1

for location in post_locations:
    print(location + ' : ' + str(post_locations[location]))
        



