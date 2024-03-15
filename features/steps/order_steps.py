from pages.OrderPage import OrderPage
from behave import given, when, then


@when('Sign In 버튼 클릭이 가능하다.')
def step_impl(context):
    context.OrderPage.click_Sign_in_button()
    
@when('"id" 및 "password" 입력이 가능하다.')
def step_impl(context):
    context.OrderPage.check_valid_email()
    context.OrderPage.check_valid_password()
    
@when('로그인 페이지에서 로그인 버튼을 클릭이 가능하다.')
def step_impl(context):
    context.OrderPage.click_login_button()
    
@when('메인 페이지 검색입력창에 test qa item을 입력이 가능하다.')
def step_impl(context):
    context.OrderPage.input_qaitem()

@when('test qa item을 검색하면 해당 아이템이 리스트화면에 노출된다.')
def step_impl(context):
    context.OrderPage.search_qaitem()
    
@when('test qa item을 클릭하여 해당 아이템 세부정보로 이동한다.')
def step_impl(context):
    context.OrderPage.click_list_qaitem()
    
@when('Pack 아이템 수량 입력이 가능하다.')
def step_impl(context):
    context.OrderPage.input_qaitem_qty()
    
@when('add shipping bag 버튼을 클릭하여 cart에 아이템이 추가된다.')
def step_impl(context):
    context.OrderPage.click_shipping_bag()
    
@when('장바구니 아이콘을 클릭하여 Cart 페이지로 이동이 가능하다.')
def step_impl(context):
    context.OrderPage.click_cart_icon()

@when('checkout 페이지에서 다음 주문 프로세서 진행이 가능하다.')
def step_impl(context):
    context.OrderPage.click_checkout_button()

@when('Shipped 페이지에서 다음 주문 프로세서 진행이 가능하다.')
def step_impl(context):
    context.OrderPage.click_shipping_continue_button()

@when('Payment Method 페이지에서  다음 주문 프로세서 진행이 가능하다.')
def step_impl(context):
    context.OrderPage.click_payment_continue_button()

@when('Order Review & Confirmation 페이지에서 다음 주문 프로세서 진행이 가능하다.')
def step_impl(context):
    context.OrderPage.click_Submit_order_button()

@then('주문 성공 메시지가 노출되고, 주문이 정상 처리된다.')
def step_impl(context):
    context.OrderPage.verify_order_success()