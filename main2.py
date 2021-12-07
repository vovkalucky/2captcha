# Solve hCaptcha  with Selenium Python Using 2captcha (rucaptcha.com)

#https://rucaptcha.com/software
#result = solver.hcaptcha(sitekey='10000000-ffff-ffff-ffff-000000000001',
                           # url='https://www.site.com/page/',
                           # param1=..., ...)
import sys

from selenium import webdriver
import requests, time
from global_var import API
from twocaptcha import TwoCaptcha

def solver():
    solver = TwoCaptcha(API)
    data_sitekey = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'
    page_url ='https://www.google.com/recaptcha/api2/demo'

    try:
        result = solver.hcaptcha(
            sitekey=data_sitekey,
            url=page_url,
        )

    except Exception as e:
        sys.exit(e)

    else:
        sys.exit('solved: ' + str(result))

if __name__ == '__main__':
    solver()



