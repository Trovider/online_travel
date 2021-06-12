from urllib.request import urlretrieve
from selenium import webdriver

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import time
from selenium.webdriver.common.keys import Keys

import django
django.setup()

from .models import Spot, Photo
from multiprocessing import Pool
import time

def parse_blog(country, area):
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    options.add_argument('window-size=1920x1080')
    options.add_argument("disable-gpu")

    driver = webdriver.Chrome('C:\\Users\\김나경\\Desktop\\chromedriver.exe', chrome_options=options)

    url = ''

    if area == "서울":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hsqf&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhsKCC9tLzBoc3FmEg_shJzsmrjtirnrs4Tsi5w#ttdm=37.570160_126.982258_13&ttdmf=%252Fm%252F02qpf1'
    if area == "전주":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01w961&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhYKCS9tLzAxdzk2MRIJ7KCE7KO87Iuc#ttdm=35.817340_127.068533_11&ttdmf=%25252Fg%25252F11cs5mwv9z'
    if area == "부산":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hv7l&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhsKCC9tLzBodjdsEg_rtoDsgrDqtJHsl63si5w#ttdm=35.133068_129.140794_11&ttdmf=%25252Fm%25252F0bwss4'
    if area == "강릉":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01tkyc&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhYKCS9tLzAxdGt5YxIJ6rCV66aJ7Iuc#ttdm=37.776314_128.902919_11&ttdmf=%252Fg%252F1221sdcf'
    if area == "제주도":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01rffr&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EiIKCS9tLzAxcmZmchIV7KCc7KO87Yq567OE7J6Q7LmY64-E#ttdm=33.343214_126.720928_10&ttdmf=%25252Fm%25252F04cqk6t'

    if area == "베이징":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01914&dest_state_type=main&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhgKCC9tLzAxOTE0EgzrsqDsnbTsp5Xsi5w#ttdm=40.052562_116.422918_9'
    if area == "상하이":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F06wjf&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhgKCC9tLzA2d2pmEgzsg4HtlZjsnbTsi5w#ttdm=31.162468_121.566700_11&ttdmf=%25252Fm%25252F09s1y8'
    if area == "칭다오":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01l3s0&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhkKCS9tLzAxbDNzMBIM7Lmt64uk7Jik7Iuc#ttdm=36.065663_120.384489_12&ttdmf=%25252Fm%25252F0wrcchk'
    if area == "광저우":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0393g&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhgKCC9tLzAzOTNnEgzqtJHsoIDsmrDsi5w#ttdm=23.079650_113.334877_11&ttdmf=%2525252Fm%2525252F01njfs'
    if area == "톈진":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0df4y&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhUKCC9tLzBkZjR5Egnthojsp4Tsi5w#ttdm=39.071705_117.164462_10&ttdmf=%252Fg%252F11f2m0bkz5'
    if area == "항저우":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F014vm4&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhkKCS9tLzAxNHZtNBIM7ZWt7KCA7Jqw7Iuc#ttdm=30.224922_120.134353_11&ttdmf=%252Fm%252F02677wf'
    if area == '충칭':
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F017236&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhYKCS9tLzAxNzIzNhIJ7Lap7Lmt7Iuc#ttdm=29.081457_106.333656_8&ttdmf=%252Fg%252F1tdfg00s'
    if area == '청두':
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F016v46&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhYKCS9tLzAxNnY0NhIJ7LKt65GQ7Iuc#ttdm=30.647554_104.101712_10&ttdmf=%252Fm%252F04zv3f'
    if area == "홍콩":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F03h64&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhIKCC9tLzAzaDY0EgbtmY3svak#ttdm=22.262070_114.052729_11&ttdmf=%25252Fm%25252F02bl_y'


    if area == "도쿄":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F07dfk&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhUKCC9tLzA3ZGZrEgnrj4Tsv4Trj4Q#ttdm=35.642854_139.792202_11&ttdmf=%252Fm%252F01nf29'
    if area == "후쿠오카":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0gqkd&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhsKCC9tLzBncWtkEg_tm4Tsv6DsmKTsubTsi5w#ttdm=33.562701_130.422216_11&ttdmf=%252Fg%252F1229qltn'
    if area == "오사카":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F018jcq&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhkKCS9tLzAxOGpjcRIM7Jik7IKs7Lm067aA#ttdm=34.664696_135.532335_12&ttdmf=%252Fm%252F0g50xc'
    if area == "교토":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F09d4_&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg&tcfs=EhUKCC9tLzA5ZDRfEgnqtZDthqDsi5w#ttdm=34.956621_135.764876_12&ttdmf=%252Fm%252F02nnhx'
    if area == "요코하마":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0kstw&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhsKCC9tLzBrc3R3Eg_smpTsvZTtlZjrp4jsi5w#ttdm=35.393311_139.629133_11&ttdmf=%25252Fm%25252F03ckcq0'
    if area == "삿포로":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0gp5l6&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhkKCS9tLzBncDVsNhIM7IK_7Y-s66Gc7Iuc#ttdm=43.033152_141.350549_11&ttdmf=%25252Fm%25252F0263ys5'

    if area == "뉴욕":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F02_286&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhMKCS9tLzAyXzI4NhIG64m07JqV#ttdm=40.723123_-74.001735_12&ttdmf=%252Fm%252F0cv4c'
    if area == "라스베이거스":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0cv3w&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=Eh4KCC9tLzBjdjN3EhLrnbzsiqTrsqDsnbTqsbDsiqQ#ttdm=36.089516_-115.286817_10&ttdmf=%252Fm%252F040253'
    if area == "로스앤젤레스":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F030qb3t&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EiAKCi9tLzAzMHFiM3QSEuuhnOyKpOyVpOygpOugiOyKpA#ttdm=33.876700_-118.177319_10&ttdmf=%252Fm%252F01mvl6'
    if area == "샌디에고":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F071vr&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhgKCC9tLzA3MXZyEgzsg4zrlJTsl5Dqs6A#ttdm=32.698892_-117.180428_11&ttdmf=%25252Fm%25252F02pt3vb'
    if area == "시카고":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F01_d4&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhUKCC9tLzAxX2Q0Egnsi5zsubTqs6A#ttdm=41.830595_-87.609490_11'
    if area == "시애틀":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0d9jr&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhUKCC9tLzBkOWpyEgnsi5zslaDti4A#ttdm=47.607843_-122.332652_12&ttdmf=%25252Fm%25252F02kl80'

    if area == "토론토":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0h7h6&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhUKCC9tLzBoN2g2EgnthqDroaDthqA#ttdm=43.638079_-79.384764_13&ttdmf=%252Fm%252F02vylr'
    if area == "오타와":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F05ksh&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhUKCC9tLzA1a3NoEgnsmKTtg4DsmYA#ttdm=45.356949_-75.833326_10&ttdmf=%252Fm%252F042wft'
    if area == "몬트리올":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F052p7&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhgKCC9tLzA1MnA3EgzrqqztirjrpqzsmKw#ttdm=45.489466_-73.573297_12&ttdmf=%25252Fm%25252F0d_pyc'
    if area == "벤쿠버":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F080h2&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhUKCC9tLzA4MGgyEgnrsLTsv6DrsoQ#ttdm=49.282053_-123.179063_11&ttdmf=%252Fm%252F06cx9w'

    if area == "모스크바":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F04swd&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhgKCC9tLzA0c3dkEgzrqqjsiqTtgazrsJQ#ttdm=55.746506_37.619245_13&ttdmf=%25252Fm%25252F05spxg'
    if area == "블라디보스토크":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0fd_x&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EiEKCC9tLzBmZF94EhXruJTrnbzrlJTrs7TsiqTthqDtgaw#ttdm=43.077982_131.995988_11&ttdmf=%252Fg%252F122z_t_n'
    if area == "이르쿠츠크":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0fp2v&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhsKCC9tLzBmcDJ2Eg_snbTrpbTsv6DsuKDtgaw#ttdm=52.274278_104.290905_13&ttdmf=%252Fg%252F122vxxly'
    if area == "상트페테르부르크":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F06pr6&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EiQKCC9tLzA2cHI2Ehjsg4HtirjtjpjthYzrpbTrtoDrpbTtgaw#ttdm=59.798745_30.152125_10&ttdmf=%252Fm%252F055ctk'

    if area == "멜버른":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0chgzm&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhYKCS9tLzBjaGd6bRIJ66mc67KE66W4#ttdm=-37.838014_144.973693_12&ttdmf=%25252Fm%25252F02737h'
    if area == "시드니":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F06y57&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhUKCC9tLzA2eTU3Egnsi5zrk5zri4g#ttdm=-33.881767_151.238792_12&ttdmf=%252Fm%252F05y8df'
    if area == "캔버라":
        url = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C4258168%2C4270442%2C4306835%2C4317915%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4509341%2C4536454%2C4545890%2C4554491%2C4564872%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0dp90&dest_state_type=sattd&dest_src=tsvr&sa=X&ved=2ahUKEwiQ-aSno4_xAhVxw4sBHcI-AscQzTooATAnegQIIRAC&tcfs=EhUKCC9tLzBkcDkwEgnsupTrsoTrnbw#ttdm=-35.303370_149.136622_13&ttdmf=%25252Fm%25252F046cg8'
    driver.get(url)

    data = {}
    image = []

    for i in range(12):
        path_name = '/html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            i + 1) + ']/div/div/div[1]/div[2]/div[1]/div'
        name = driver.find_element_by_xpath(path_name)

        path_name2 = ' /html/body/c-wiz[2]/div/div[2]/div/c-wiz/div/div/div[1]/div[2]/c-wiz/div/div/div/div/div[' + str(
            i + 1) + ']/div/div/div[1]/div[1]/easy-img/img'
        img = driver.find_element_by_xpath(path_name2)
        image.append(img.text)
        img_url = img.get_attribute('src')

        data[name.text] = img_url

    driver.quit()

    for t, l in data.items():
        Spot(spot_name=t, country_name=country, area_name=area, link=l).save()

    return data


if __name__=='__main__':
    start_time = time.time()
    pool = Pool(processes=2)
    pool.map(parse_blog)
    pool.map(parse_blog)


def detail_save(spot):
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    path = 'C:\\Users\\김나경\\Desktop\\chromedriver.exe'
    driver = webdriver.Chrome(path, chrome_options=options)

    # 서울특별시
    url1 = 'https://www.google.com/travel/things-to-do/see-all?g2lb=2502548%2C2503780%2C4258168%2C4270442%2C4306835%2C4317915%2C4328159%2C4371334%2C4401769%2C4419364%2C4482438%2C4486153%2C4491350%2C4509341%2C4515403%2C4517258%2C4530346%2C4536454%2C4540819%2C4270859%2C4284970%2C4291517&hl=ko-KR&gl=kr&ssta=1&dest_mid=%2Fm%2F0hsqf&dest_state_type=sattd&dest_src=ts&sa=X&ved=2ahUKEwjK75fwn4XwAhXWdd4KHQjJDYgQuL0BMAB6BAgHEDg#ttdm=37.533159_127.036657_12&ttdmf=%252Fm%252F02qpf1'
    driver.get(url1)

    data = []
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
        data.append(img)
        data.append(img2)
        data.append(img3)


        for l in data:
            Photo(spot_name=spot, image=l).save()

    return data

