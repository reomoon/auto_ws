from lib.env import BasePage
import lib.PageElements as pe


class OrderPage(BasePage):
    def __init__(self, driver, context):
        super().__init__(driver, context)
        self.driver = driver
        self.context = context
     

    ## displayed 정의
    
    def verify_order_success(self):
        BasePage.get_displayed(self, pe.Order_success_phrases)
   
   
    ## get_enter 정의
    
    def search_qaitem(self):
        BasePage.get_enter(self, pe.search_field)
    
        
    ## get_inputbox 정의
    
    def check_valid_email(self):
        BasePage.get_inputbox(self, pe.Email_field, pe.email_input_text)
    
    def check_valid_password(self):
        BasePage.get_inputbox(self, pe.Password_field, pe.Password_input_text)
    
    def input_qaitem(self):
        BasePage.get_inputbox(self, pe.search_field, pe.qa_item)
        
    def input_qaitem_qty(self):
        BasePage.get_inputbox(self, pe.item_detail_qty, 3)
        BasePage.get_inputbox(self, pe.item_detail_qty2, 2)
    
    
    ## get_click_element
    
    def click_Sign_in_button(self):
        BasePage.get_click_element(self, pe.Sign_in_button)
    
    def click_login_button(self):
        BasePage.get_click_element(self, pe.login_button)
    
    def click_list_qaitem(self):
        BasePage.get_click_element(self, pe.list_qa_item)

    def click_shipping_bag(self):
        BasePage.get_click_element(self, pe.item_detail_ADD_TO_SHOPPING_BAG_button)

    def click_cart_icon(self):
        BasePage.get_click_element(self, pe.cart_icon_button)

    def click_checkout_button(self):
        BasePage.get_click_element(self, pe.Shopping_BAG_Proceed_To_Checkout_button)

    def click_shipping_continue_button(self):
        BasePage.get_click_element(self, pe.Shipping_Save_Continue_button)
        
    def click_payment_continue_button(self):
        BasePage.get_click_element(self, pe.payment_Save_Continue_button)

    def click_Submit_order_button(self):
        BasePage.get_click_element(self, pe.OrderReview_Submit_Order_button)





