from selenium import webdriver
from base.BasePage import BasePage
from pages.LoginPage import LoginPage
from pages.OrderPage import OrderPage
import config.config as config
from behave import given
import time
@given('Chrome 브라우저로 FashionGo 사이트 접속')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.get(config.BASE_URL)
    context.driver.maximize_window()
    time.sleep(3)


## 테스트 수행 시 페이지마다 실행 초기화 작업
@given('페이지별 테스트 초기화 실행')
def step_impl(context):
    context.LoginPage = LoginPage(context.driver, context)
    context.OrderPage = OrderPage(context.driver, context)
   



  