from urllib.request import urlretrieve
from selenium import webdriver

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")

import django
django.setup()

from parsed_data.models import BlogData


def parse_blog(spot):

    path = 'C:\\Users\\LG\\Desktop\\chrome\\chromedriver.exe'
    driver = webdriver.Chrome(path)

    # 서울특별시
    url1 = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hsqf&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg#ttdm=37.533159_127.036657_12&ttdmf=%252Fm%252F02qpf1'

    data = []

    driver.get(url1)
    list = []
    image = []
    img_url = []

    for i in range(8):
        path_name = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            i + 1) + ']/div/div/div[1]/div[2]/div[1]/div'
        name = driver.find_element_by_xpath(path_name)
        list.append(name.text)

        path_name2 = ' /html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            i + 1) + ']/div/div/div[1]/div[1]/easy-img/img'
        img = driver.find_element_by_xpath(path_name2)
        image.append(img.text)
        url = img.get_attribute('src')
        img_url.append(url)

    print(list)
    print(img_url)

# 42-53 까지 이미지 자동 저장 코드임. 지워도 됨!

    import os

    img_folder = './img'

    if not os.path.isdir(img_folder):  # 없으면 새로 생성하는 조건문
        os.mkdir(img_folder)

    for index, link in enumerate(img_url):
        urlretrieve(link, f'./img/{index}.jpg')

    driver.quit()

    data = {}

    for i in range(0, 8):
        data[list[i]] = img_url[i]
    return data


    print(data)
    return data


if __name__=='__main__':
    data = parse_blog()
    for t, l in data.items():
        BlogData(title=t, link=l).save()