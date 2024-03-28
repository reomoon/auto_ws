from pages.LoginPage import LoginPage
from behave import when, then


@when('Sign In 버튼을 클릭한다')
def step_impl(context):
    context.LoginPage.check_Sign_in_button()

@when('올바른 아이디를 입력한다')
def setp_impl(context):
    context.LoginPage.check_valid_email()

@when('올바른 비밀번호를 입력한다') 
def setp_impl(context):
    context.LoginPage.check_valid_password()

@when('로그인 버튼을 재클릭한다')
def setp_impl(context):
    context.LoginPage.check_login_button()
    
@then('로그인 성공하여 메인페이지로 이동한다')
def setp_impl(context):
    context.LoginPage.verify_login_success()


# @when('잘못된 아이디를 입력한다')
# def setp_impl(context):
#     context.LoginPage.check_invalid_email()
    
# @when('잘못된 비밀번호를 입력한다')
# def setp_impl(context):
#     context.LoginPage.check_invalid_password()
    
# @when('로그인 버튼을 클릭한다')
# def setp_impl(context):
#     context.LoginPage.check_login_button()
    
# @when('사용자는 로그인에 실패하고 오류 메시지가 표시된다')
# def setp_impl(context):
#     context.LoginPage.display_error_wording()
 

