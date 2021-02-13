#
# FrostyBot v1.1.4
#
import time
from selenium import webdriver
from playsound import playsound
import os
import json
from datetime import datetime
import platform


dirname = os.path.dirname(__file__)

chromeFilePath = os.path.join(dirname, 'chromedriver','chromedriver.exe')
if platform.system() == 'Darwin':
  chromeFilePath = '/usr/local/bin/chromedriver'

alarmMp3 = os.path.join(dirname, 'assets','alarm.mp3')
settingsFilePath = os.path.join(dirname, 'settings.json')

with open(settingsFilePath, 'r') as settingsFile:
    settings = settingsFile.read()

settingsObj = json.loads(settings)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(chromeFilePath, chrome_options=chrome_options)
browser.get(settingsObj['productUrl'])

browser.maximize_window()
buyButton = False
startTime = datetime.now()


def checkStock():
        failed_A = False
        failed_B = False
        try: 
                addToCartBtn = browser.find_element_by_class_name("prd-oos")
        except:
                failed_A = True
        try: 
                addToCartBtn = browser.find_element_by_class_name("oos")
        except:
                failed_B = True

        if (failed_A) and (failed_B):
                raise Exception("InStock")


def addToBasket():
        try: 
                parent_el = browser.find_element_by_xpath("//div[@id='product-actions']/div[@class='channels space-b'][@data-component='channels-panel']/div[@data-component='add-to-basket-button-wrapper']/button[1]")
                parent_el.click()
                print("Item added to basket!")
        except:
                time.sleep(3)
                addToBasket()

def contToBasket():
        try:         
                parent_el2 = browser.find_element_by_xpath("//button[@data-interaction='Continue to basket']")
                parent_el2.click()
                print("Gone to the basket!")
        except:
                print("Can't find the element! Skip to the next step!")
                #time.sleep(3)
                #contToBasket()

def orderSum():
        try:
                parent_el3 = browser.find_element_by_xpath("//div[@data-component='StickyInner']/div[@data-component='OrderSummary']/button[1]")
                parent_el3.click()
                print("Gone to the order details!")
        except:
                time.sleep(3)
                orderSum()

def enterPostcode():
        try:
                searchPostcode = browser.find_element_by_xpath("//input[@placeholder='Enter town or postcode']")
                searchPostcode.send_keys(settingsObj['postcode'])
                print("Postcode entered!")

        except:
                time.sleep(3)
                enterPostcode()

def submitSearch():
        try:
                parent_el4 = browser.find_element_by_xpath("//button[@aria-label='Submit Search']")
                parent_el4.click()      
                print("Postcode submitted!")

        except:
                time.sleep(3)    
                submitSearch()

def delivery():
        try:
                parent_el5 = browser.find_element_by_xpath("//html/body/div[4]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div/div[3]/div[1]/button")
                parent_el5.click()
                print("Delivery confirmed!")
        except:
                time.sleep(1)
                print("Can't find the element! Try new path!")
                parent_el5 = browser.find_element_by_xpath("//html/body/div[4]/div/div[2]/div[2]/div/div/div[2]/div[2]/div[3]/div[2]/div/div[3]/button")
                parent_el5.click()                

def enterEmail():
        try:
                email = browser.find_element_by_xpath("//form[@data-di-form-id='email']/div/div/input[@data-qa='CustomInput_email']")
                email.send_keys(settingsObj['loginEmail'])
                emailSubmit = browser.find_element_by_xpath("//form[@data-di-form-id='email']/button[1]")
                emailSubmit.click()
                print("Email entered and submitted!")

        except:
                time.sleep(3)      
                enterEmail()

def enterPassword():
        try:
                password = browser.find_element_by_xpath("//form[@id='password']/div/input[1]")
                password.send_keys(settingsObj['loginPassword'])
                passwordButton = browser.find_element_by_xpath("//form[@id='password']/div/button[1]")
                passwordButton.click()
                print("Password entered and submitted!")

        except:
                time.sleep(2)    
                enterPassword()

def paypalPaymentM():
        try:
                time.sleep(1)
                paypal = browser.find_element_by_xpath("//div[@data-component='PaymentMethods']/div[@data-element='PaymentMethodsButtons']/div[@data-component='PayPalPayment']/button[1]")
                paypal.click()
                print("Paypal payment button clicked!")

        except:
                time.sleep(2)     
                paypalPaymentM()

def cardlPaymentM():
        try:
                time.sleep(1)
                card = browser.find_element_by_xpath("//div[@data-component='PaymentMethods']/div[@data-element='PaymentMethodsButtons']/div[@data-component='CardPayment']/button[1]")
                card.click()
                print("Card payment button clicked!")

                time.sleep(10)

                cardNumber = browser.find_element_by_id("cardNumber")
                cardNumber.send_keys(settingsObj['cardNumberCC'])

                cardHolderName = browser.find_element_by_id("cardholderName")
                cardHolderName.send_keys(settingsObj['cardHolderNameCC'])

                cardExpiryMonth = browser.find_element_by_id("expiryMonth")
                cardExpiryMonth.send_keys(settingsObj['expiryMonthCC'])

                cardExpiryYear = browser.find_element_by_id("expiryYear")
                cardExpiryYear.send_keys(settingsObj['expiryYearCC'])

                cardCVC = browser.find_element_by_id("securityCode")
                cardCVC.send_keys(settingsObj['cardCvc'])

                if settingsObj['autoPurchase']:
                        submitButton = browser.find_element_by_id("submitButton")
                        submitButton.click()                


        except:
                time.sleep(2)      
                cardlPaymentM()


def getPrice():
        try:
                price = browser.find_element_by_xpath("//meta[@property='og:price:amount']").get_attribute("content")
                return price
        except:
                return ''

while not buyButton:

    try:

        checkStock()
        title = browser.title.replace('Buy', '').replace('| Free Delivery | Currys','')
        print(f"{title} | £{getPrice()} | Out of Stock....")

        time.sleep(settingsObj['refreshTime'])
        browser.refresh()
        endTime = datetime.now()
        print(f"Bot uptime : {endTime - startTime}")

    except:

        if (settingsObj['alarmWhenStockFound']):
                playsound(alarmMp3, block=False) 

        acceptCookies = addButton = browser.find_element_by_id("onetrust-accept-btn-handler")
        acceptCookies.click()
        print("In Stock!")

        addToBasket()
        time.sleep(2)
        contToBasket()
        time.sleep(2)
        orderSum()
        time.sleep(1)
        enterPostcode()
        time.sleep(1)
        submitSearch()
        time.sleep(2)
        delivery()
        time.sleep(1)
        enterEmail()
        time.sleep(2)
        enterPassword()
        if settingsObj['paypalPayment']:
            paypalPaymentM()
        else:
            cardlPaymentM()
        buyButton = True
        playsound(alarmMp3)

