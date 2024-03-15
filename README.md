# SeleniumAutomation

## git clone "http주소"
 git 원격 레포지토리 로컬 저장소로 클론하기 (가져오기)

## git checkout -b first_branch  >   머지 후 메인에 올리고 다시 새로운 branch로 작업 > 반복
 git 로컬 브랜치 생성 후 관리 (first_branch 라는 브랜치 생성하고, 거기로 이동)

## git push origin first_branch
 로컬 first_branch 에서 작업한 내용 원격 레포지토리로 push

## git pull origin main
 풀리퀘스트 승인 후, 머지된 다음 -> 로컬 환경에서 명령어 수행



# 파이썬 가상환경 설정
- 현재 디렉토리로 이동 (여기선 SeleniumAutomation)
- python3 -m venv vevn 입력 (파이썬 가상한경 생성)
- source venv/bin/activate 입력 (파이썬 가상환경 활성화)
- pip3 list 입력 (현재 가상환경에 설치된 라이브러리 조회) (pip만 있어야 정상임)
- 필요한 라이브러리 설치 (selenium, behave ...)"# auto_ws" 
