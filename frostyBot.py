#
# FrostyBot v1.1.0 
#
import time
from selenium import webdriver
from playsound import playsound
import os
import json

dirname = os.path.dirname(__file__)

chromeFilePath = os.path.join(dirname, 'chromedriver','chromedriver.exe')
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
        except:
                time.sleep(3)
                addToBasket()

def contToBasket():
        try:         
                parent_el2 = browser.find_element_by_xpath("//button[@data-interaction='Continue to basket']")
                parent_el2.click()
        except:
                time.sleep(3)
                contToBasket()

def orderSum():
        try:
                parent_el3 = browser.find_element_by_xpath("//div[@data-component='StickyInner']/div[@data-component='OrderSummary']/button[1]")
                parent_el3.click()
        except:
                time.sleep(3)
                orderSum()

def enterPostcode():
        try:
                searchPostcode = browser.find_element_by_xpath("//input[@placeholder='Enter town or postcode']")
                searchPostcode.send_keys(settingsObj['postcode'])                
        except:
                time.sleep(3)
                enterPostcode()

def submitSearch():
        try:
                parent_el4 = browser.find_element_by_xpath("//button[@aria-label='Submit Search']")
                parent_el4.click()                    
        except:
                time.sleep(3)    
                submitSearch()

def delivery():
        try:
                parent_el5 = browser.find_element_by_xpath("//div[@data-element='DeliverySlotBlock']/button[1]")
                parent_el5.click()                 
        except:
                time.sleep(3)      
                delivery()

def enterEmail():
        try:
                email = browser.find_element_by_xpath("//form[@data-di-form-id='email']/div/div/input[@data-qa='CustomInput_email']")
                email.send_keys(settingsObj['loginEmail'])
                emailSubmit = browser.find_element_by_xpath("//form[@data-di-form-id='email']/button[1]")
                emailSubmit.click()                
        except:
                time.sleep(3)      
                enterEmail()

def enterPassword():
        try:
                password = browser.find_element_by_xpath("//form[@id='password']/div/input[1]")
                password.send_keys(settingsObj['loginPassword'])
                passwordButton = browser.find_element_by_xpath("//form[@id='password']/div/button[1]")
                passwordButton.click()                 
        except:
                time.sleep(3)    
                enterPassword()

def paypalPaymentM():
        try:
                paypal = browser.find_element_by_xpath("//div[@data-component='PaymentMethods']/div[@data-element='PaymentMethodsButtons']/div[@data-component='PayPalPayment']/button[1]")
                paypal.click()                
        except:
                time.sleep(3)     
                paypalPaymentM()

def cardlPaymentM():
        try:
                time.sleep(1)
                card = browser.find_element_by_xpath("//div[@data-component='PaymentMethods']/div[@data-element='PaymentMethodsButtons']/div[@data-component='CardPayment']/button[1]")
                card.click() 

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
                time.sleep(3)      
                cardlPaymentM()

while not buyButton:

    try:

        checkStock()
        print("Out of Stock........")

        time.sleep(settingsObj['refreshTime'])
        browser.refresh()

    except:

        acceptCookies = addButton = browser.find_element_by_id("onetrust-accept-btn-handler")
        acceptCookies.click()

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
        time.sleep(3)
        enterPassword()
        time.sleep(3)
        if settingsObj['paypalPayment']:
            paypalPaymentM()
        else:
            cardlPaymentM()
        playsound(alarmMp3)        
        buyButton = True
