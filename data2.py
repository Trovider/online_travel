from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

def detail_save():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    path = 'C:\\Users\\LG\\Desktop\\chrome\\chromedriver.exe'
    driver = webdriver.Chrome(path, chrome_options=options)

    # 서울특별시
    url1 = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hsqf&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg#ttdm=37.533159_127.036657_12&ttdmf=%252Fm%252F02qpf1'
    driver.get(url1)

    list = []
    for i in range(10):
        print(i)

        choose_path = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            i + 1) + ']/div'
        choose = driver.find_element_by_xpath(choose_path)
        choose.click()

        """
        c=0
        if (i<2):
            c=4
        elif (i<4):
            c=5
        elif (i<6):
            c=7
        elif (i<8):

    
        try:
            con1 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[4]/div/c-wiz/div/div[3]/div[1]/div[2]/div'
            content = driver.find_element_by_xpath(con1)
        except:
            con2 = ""
            content = driver.find_element_by_xpath(con2)
        
        print(content.text)
        """

        b = 0
        if (i < 4):
            b = 4
        elif (i < 7):
            b = 7
        elif (i < 10):
            b = 10
        else:
            b = 0

        time.sleep(2)
        path5 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            b) + ']/div/c-wiz/div/div[1]/div/div[1]/div/div[1]/easy-img/img'

        time.sleep(2)

        path6 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            b) + ']/div/c-wiz/div/div[1]/div/div[1]/div/div[2]/easy-img/img'

        time.sleep(2)
        path7 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            b) + ']/div/c-wiz/div/div[1]/div/div[1]/div/div[3]/easy-img/img'

        time.sleep(2)
        img = driver.find_element_by_xpath(path5).get_attribute('src')
        time.sleep(2)
        img2 = driver.find_element_by_xpath(path6).get_attribute('src')
        time.sleep(2)
        img3 = driver.find_element_by_xpath(path7).get_attribute('src')
        list.append(img)
        list.append(img2)
        list.append(img3)


        print(i, 1, img)
        print(i, 2, img2)
        print(i, 3, img3)


detail_save()
