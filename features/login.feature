Feature: 로그인 기능

Background: 테스트 수행 시 초기화 설정
        Given Chrome 브라우저로 FashionGo 사이트 접속
        And 페이지별 테스트 초기화 실행

Scenario: 로그인 검증
        When Sign In 버튼을 클릭한다
        When 잘못된 아이디를 입력한다
        When 잘못된 비밀번호를 입력한다
        When 로그인 버튼을 클릭한다
        When 사용자는 로그인에 실패하고 오류 메시지가 표시된다
        When 올바른 아이디를 입력한다
        When 올바른 비밀번호를 입력한다
        When 로그인 버튼을 재클릭한다
        Then 로그인 성공하여 메인페이지로 이동한다


