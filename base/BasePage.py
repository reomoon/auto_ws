# import문 : 외부 모듈에서 필요한 기능을 가져오는데 사용
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time

waitTime = 12
# BasePage : 클래스를 정의하고 Selenium 웹 드라이버를 사용하여 기본 페이지 동작을 수행하는 메서드
class BasePage:

    # 생성자 메서드 : 클래스의 인스턴스가 생성될 때 호출되는 생성자 메서드 'driver' 인자를 받아 인스턴스 변수로 저장
    def __init__(self, driver, context):
        self.driver = driver
        self.context = context

    # Element에 상호작용 했을 때, 빨간색 테두리로 하이라이트 표시하는 함수
    def highlight(self, element, effect_time, color, border):
        driver = element._parent
        def apply_style(s):
            driver.implicitly_wait(waitTime)
            driver.execute_script("arguments[0].setAttribute('style', arguments[1]);", element, s)
        original_style = element.get_attribute('style')
        apply_style(f"border: {border}px solid {color};")
        time.sleep(effect_time)
        apply_style(original_style)
        
    # element가 프론트에 표시되는 지 확인하는 메서드
    def get_displayed(self, locator):
        try:
            # 이 요소가 나타날 때까지 기다림
            element = WebDriverWait(self.driver, waitTime).until(EC.presence_of_element_located((By.XPATH, locator)))
            element.is_displayed()
            self.highlight(element, 1, "#FF0000", 3)
            return True  # is_displayed 대신 True 반환
        except TimeoutException:
            # 대기 시간이 초과될 경우 처리
            print(f"Timeout Exception: Element with locator '{locator}' not found within {waitTime} seconds.")
            assert False

    # 버튼 click 메소드
    def get_click_element(self, locator):
        try:
            # 이 요소가 클릭 가능할 때까지 기다림
            element = WebDriverWait(self.driver, waitTime).until(EC.element_to_be_clickable((By.XPATH, locator)))
            self.highlight(element, 1, "#FF0000", 3)
            element.click()
            return True
        except TimeoutException:
            print(f"Timeout Exception: Failed to click element with locator '{locator}' within {waitTime} seconds.")
            assert False
        except Exception as e:
            print(f"Error : {e}")  # 발생한 모든 예외에 대한 자세한 내용 출력
            assert False  # 클릭 실패 시 False 반환
                
    # 엔터처리 메소드
    def get_enter(self, locator):
        try:
            element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.XPATH, locator)))
            element.send_keys(Keys.RETURN)
            return True
        except TimeoutException:
            print(f"Timeout Exception: Element with locator '{locator}' not found within {waitTime} seconds.")
            assert False
        except Exception as e:
            print(f"Error : {e}")
            assert False  # 엔터 입력 실패 시 False 반환
            
    # element 입력박스 내용 초기화 및 내용 입력 메서드
    def get_inputbox(self, locator, input_text):
        try:
            input_element = WebDriverWait(self.driver, waitTime).until(EC.visibility_of_element_located((By.XPATH, locator)))
            self.highlight(input_element, 1, "#FF0000", 3)
            input_element.clear()  # 입력창 내용 초기화
            input_element.send_keys(input_text)  # 입력창에 텍스트 입력
            return True
        except TimeoutException:
            print(f"Timeout Exception: Element with locator '{locator}' not found within {waitTime} seconds.")
            assert False
        except Exception as e:
            print(f"Error while inputting text: {e}")
            assert False  # 입력 실패 시 False 반환
