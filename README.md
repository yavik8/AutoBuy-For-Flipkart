# AutoBuy-For-Flipkart

Automated program to buy Flipkart products in flash sale. 
Specifically to buy products which go out of sale in a fraction of seconds and are too difficult to buy manually.

Steps to run this script:
1. Clone or download this repository.
2. Do `cd AutoBuy-For-Flipkart`
3. Run `python3 -m venv appvenv`
`source appvenv/bin/activate`
4. Run `pip install -r requirements.txt`
5. Download the correct [chromedriver](http://chromedriver.chromium.org/downloads) for you operating system (Linux/OSX/Windows), put the chromedriver in this project directory.
6. Set path of  chromedriver in config.ini file.
7. Enter your email and password in config.ini file.
8. Enter flipkart product URL in config.ini file.
7. Run `python FlipkartAutobuy.py`
