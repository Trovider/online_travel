from urllib.request import urlretrieve
from selenium import webdriver
import time
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()
from .models import Spot, Img_url
from multiprocessing import Pool
import time

def parse_blog(country, area):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    path = 'C:\\Users\\LG\\Desktop\\chrome\\chromedriver.exe'
    driver = webdriver.Chrome(path, chrome_options=options)

    url = ''
    if country == 'South Korea':
        if area == "서울":
            url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hsqf&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhsKCC9tLzBoc3FmEg_shJzsmrjtirnrs4Tsi5w#ttdm=37.570160_126.982258_13&ttdmf=%252Fm%252F02qpf1'
        elif area == "전주":
            url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01w961&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhYKCS9tLzAxdzk2MRIJ7KCE7KO87Iuc#ttdm=35.817340_127.068533_11&ttdmf=%25252Fg%25252F11cs5mwv9z'
        elif area == "부산":
            url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hv7l&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhsKCC9tLzBodjdsEg_rtoDsgrDqtJHsl63si5w#ttdm=35.133068_129.140794_11&ttdmf=%25252Fm%25252F0bwss4'
        elif area == "강릉":
            url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01tkyc&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhYKCS9tLzAxdGt5YxIJ6rCV66aJ7Iuc#ttdm=37.776314_128.902919_11&ttdmf=%252Fg%252F1221sdcf'
        elif area == "제주도":
            url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01rffr&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EiIKCS9tLzAxcmZmchIV7KCc7KO87Yq567OE7J6Q7LmY64-E#ttdm=33.343214_126.720928_10&ttdmf=%25252Fm%25252F04cqk6t'
    elif country == 'China':
        if area == "베이징":
            url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01914&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhgKCC9tLzAxOTE0EgzrsqDsnbTsp5Xsi5w#ttdm=40.052562_116.422918_9'
    elif country == 'Japan':
        if area == "도쿄":
            url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F07dfk&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhUKCC9tLzA3ZGZrEgnrj4Tsv4Trj4Q#ttdm=35.642854_139.792202_11'

    driver.get(url)

    data = {}
    spot_img_list=[]

    for i in range(10):
        print(i)
        time.sleep(4)
        path_name = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            i+1) + ']/div/div/div[1]/div[2]/div[1]/div'
        name = driver.find_element_by_xpath(path_name)

        time.sleep(2)
        path_name2 = ' /html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            i+1) + ']/div/div/div[1]/div[1]/easy-img/img'
        img = driver.find_element_by_xpath(path_name2)
        img_url = img.get_attribute('src')

        time.sleep(4)
        try:
            path_name3 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
                i+1) + ']/div/div/div[1]/div[2]/div[3]'
            content = driver.find_element_by_xpath(path_name3)

        except:
            path_name4 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
                i+1) + ']/div/div/div[1]/div[2]/div[2]'
            content = driver.find_element_by_xpath(path_name4)

        time.sleep(4)

        time.sleep(2)
        choose_path = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            i+1) + ']/div'
        
        choose = driver.find_element_by_xpath(choose_path)
        choose.click()
        print("Done")

        b = 0
        if (i < 4):
            b = 4
        elif (i < 7):
            b = 7
        elif (i < 10):
            b = 10

        time.sleep(4)
        print(b)

        path5 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(b) + ']/div/c-wiz/div/div[1]/div/div[1]/div/div[1]/easy-img/img'
        time.sleep(2)
        path6 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(b) + ']/div/c-wiz/div/div[1]/div/div[1]/div/div[2]/easy-img/img'
        time.sleep(2)
        path7 = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(b) + ']/div/c-wiz/div/div[1]/div/div[1]/div/div[3]/easy-img/img'

        spot_img_1 = driver.find_element_by_xpath(path5).get_attribute('src')
        print(spot_img_1)
        spot_img_2 = driver.find_element_by_xpath(path6).get_attribute('src')
        print(spot_img_2)
        spot_img_3 = driver.find_element_by_xpath(path7).get_attribute('src')
        print(spot_img_3)


        btn = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[4]/div/div/button'
        btn1 = driver.find_element_by_xpath(btn).click()

        spot_img_list.extend([spot_img_1, spot_img_2, spot_img_3])

    data[name.text] = [img_url, content.text]
    print(spot_img_list)
    driver.quit()

    for t, l in data.items():
        Spot(spot_name=t, country_name=country, area_name=area, link=l[0], content=l[1]).save()
    """
    for i in spot_img_list:
        Img_url(img_url=i).save()
    """
    return data


if __name__=='__main__':
    start_time = time.time()
    pool = Pool(processes=2)
    pool.map(parse_blog)
    pool.map(parse_blog)

