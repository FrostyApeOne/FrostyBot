# FrostyBot

FrostyBot is a simple Python based bot which allows users to perform an automated checkout on Currys.co.uk website. 

## Supported sites
- Currys.co.uk

## Installation

1. Download and Install Python from the following link

	https://www.microsoft.com/en-gb/p/python-39/9p7qfqmjrfp7?activetab=pivot:overviewtab

2. Open Command Prompt in Windows, type Python and press enter! If it starts Python and shows >>> then you ahve Python installed. Type exit() and press enter then go to step 3 below..
(If after typing Python, Windows takes you to Microsoft Store, that means Python is not installed, please follow the store instructions and install it)

3. Install Selenium and playsound, run the following commands

	```
	python -m pip install selenium
	```
	```
	python -m pip install playsound
	```


## Configuration and settings

1. Rename the **settings-template.json** to **settings.json**
2. Edit and save the file

-----
**productUrl** : direct URL to the item you'd like to check and purchase

**refreshTime** : Refresh interval in seconds to check the page regularly for stock

**postcode** : Your delivery address postcode

**loginEmail** & **loginPassword**  : Your Curry's username and password, make sure this file is only on your computer as it will have your password stored as plain text!

**paypalPayment** : If True, it will open the PayPal page in the last stage of the checkout process! Otherwise it redirects the user to the Credit Card payment!

The Card Payment section allows you to enter your card details and let the bot fill in the WorldPay card payment form for you! Please make sure the project folder and settings file are stored securely on your computer as it will contain your Credit Card and personal details in plain text!

Note: If the **autoPurchase** is set to True, the bot clicks on the pay button and attempts to finalise your purchase!

## Run the bot

To run the bot double click on FrostyBot.bat file in the root of the project folder, alternatively you can run the application by executing the following command
```
	python frostyBot.py
```
Leave the bot running and make sure you computer's audio volume is loud so that you can hear the alarm if the bot find stock and goes to the payment page! Unless the autoPurchase is enabled in the setting the bot will only take the user to the payment gateway and it does not perform the purchase or finalize the order!

## Important 

Please make sure you have already saved a default delivery address in your Curry's account, the postcode needs to match the one you have set in the settings file!

Please make sure the chrome window stays maximized! Do not click on the page or agree with the cookies warning!

Please note, sometimes the Curry's server may respond slower than usual in that case the bot might fail to take you through the checkout! You can check the Chrome window or the console and make sure it is running!

## Test

Test the bot by giving it address of an item which is in stock, you can watch how it works and make sure it hits the last stage and take you to the payment gateway!
Once confirmed that it works as expected please replace the URL with your GPU product URL!





