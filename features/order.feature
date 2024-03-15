Feature: 주문 기능

Background: 테스트 수행 시 초기화 설정
        Given Chrome 브라우저로 FashionGo 사이트 접속
        And 페이지별 테스트 초기화 실행

Scenario: 주문 넣기
        When Sign In 버튼 클릭이 가능하다.
        And "id" 및 "password" 입력이 가능하다.
        And 로그인 페이지에서 로그인 버튼을 클릭이 가능하다.
        And 메인 페이지 검색입력창에 test qa item을 입력이 가능하다.
        And test qa item을 검색하면 해당 아이템이 리스트화면에 노출된다.
        And test qa item을 클릭하여 해당 아이템 세부정보로 이동한다.
        And Pack 아이템 수량 입력이 가능하다.
        And add shipping bag 버튼을 클릭하여 cart에 아이템이 추가된다.
        And 장바구니 아이콘을 클릭하여 Cart 페이지로 이동이 가능하다.
        And checkout 페이지에서 다음 주문 프로세서 진행이 가능하다.
        And Shipped 페이지에서 다음 주문 프로세서 진행이 가능하다.
        And Payment Method 페이지에서  다음 주문 프로세서 진행이 가능하다.
        And Order Review & Confirmation 페이지에서 다음 주문 프로세서 진행이 가능하다.
        Then 주문 성공 메시지가 노출되고, 주문이 정상 처리된다.