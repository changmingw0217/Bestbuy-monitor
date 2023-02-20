from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from discord_webhook import DiscordWebhook, DiscordEmbed
import time
# input_url = input("Input Bestbuy url: ")
# input_drive_path = input("Please input your chrome driver path: ")
# input_url = input_url.strip()
# input_drive_path = input_drive_path.strip()
# url = input_url
# driver = webdriver.Chrome(input_drive_path)
# driver.get(url)

def get_title_sku(web_drive):
    add = web_drive.find_element_by_class_name('shop-product-title')
    str1 = add.text
    l1 = str1.split("\n")
    l2 = str1.split()
    index = 0
    for i in range(len(l2)):
        if "SKU" in l2[i]:
            index = i
    SKU = l2[index]
    SKU_number = SKU.split(":")[1]
    return l1[0], SKU_number



url = "https://www.bestbuy.com/site/nintendo-switch-32gb-lite-yellow/6257142.p?skuId=6257142"
driver = webdriver.Chrome('/Users/changmingwang/Downloads/chromedriver')
driver.get(url)

title, SKU = get_title_sku(driver)
# add_to_cart_link = "[__***Click Here***__](Https://api.bestbuy.com/click/-/" + SKU + "/cart/)"
add_to_cart_link = "https://api.bestbuy.com/click/-/" + SKU + "/cart/"

button = driver.find_element_by_class_name('fulfillment-add-to-cart-button')

if button.text == "Add to Cart":
    driver.get(add_to_cart_link)
    time.sleep(3)
    select = driver.find_elements_by_class_name("availability__fulfillment")
    print(len(select))

# while True:
#
#     driver.get(url)
#
#     try:
#         add = driver.find_element_by_class_name('fulfillment-add-to-cart-button')
#         add.find_element_by_class_name("ficon-cart")
#         # webhook = DiscordWebhook(url='https://discordapp.com/api/webhooks/531169449659727875/mtwi_XVPibEdXURLmj_28RNubT_DG3VdIv45ZNHiXeF8nqsd6UNPDE5MiBnXvDS7oMQt')
#         # embed = DiscordEmbed(title=title, url=url)
#         # embed.add_embed_field(name='ATC', value=add_to_cart_link)
#         # webhook.add_embed(embed)
#         # webhook.execute()
#     except:
#         time.sleep(15)




