from base.BasePage import BasePage
import pages.PageElements as pe


class LoginPage(BasePage):
    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context
     
    ## displayed
     
    def verify_login_success(self):
        BasePage.get_displayed(self, pe.cart_icon_button)
        
    def display_error_wording(self):
        BasePage.get_displayed(self, pe.login_error_text)
    
    ## email / password input box
    
    def check_invalid_email(self):
        BasePage.get_inputbox(self, pe.Email_field, pe.invalid_email_input_text)

    def check_invalid_password(self):
        BasePage.get_inputbox(self, pe.Password_field, pe.invalid_Password_input_text)
    
    def check_valid_email(self):
        BasePage.get_inputbox(self, pe.Email_field, pe.email_input_text)
    
    def check_valid_password(self):
        BasePage.get_inputbox(self, pe.Password_field, pe.Password_input_text)
    
    
    ## 버튼 정의
    
    def check_Sign_in_button(self):
        BasePage.get_click_element(self, pe.Sign_in_button)
    
    
    def check_login_button(self):
        BasePage.get_click_element(self, pe.login_button)
    

    