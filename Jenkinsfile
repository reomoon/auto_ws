pipeline {
    agent any
    triggers { // 추가: 트리거 설정
        githubPush() // GitHub 저장소에 push가 발생할 때 실행
    }
    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/bomjin/SeleniumAutomation.git'
            }
        }
        stage('Install dependencies') {
            steps {
                script {
                    if (fileExists('requirements.txt')) {
                        sh 'pip3 install -r requirements.txt'
                    } else {
                        error 'requirements.txt 파일을 찾을 수 없습니다.'
                    }
                }
            }
        }
        stage('Install Behave') {
            steps {
                script {
                    sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/pip3 install behave'
                }
            }
        }
        stage('Run Behave tests') {
            steps {
                script {
                    sh '/Library/Frameworks/Python.framework/Versions/3.12/bin/behave -f allure_behave.formatter:AllureFormatter -o allure-results'
                }
            }
        }
        stage('Generate Allure Report') {
            steps {
                script {
                    allure([
                        includeProperties: false, 
                        jdk: '', 
                        properties: [], 
                        reportBuildPolicy: 'ALWAYS', 
                        results: [[path: 'allure-results']]
                    ])
                }
            }
        }
        stage('send email') {
            steps {
                script {
                    // 이메일 전송
                    sendEmail()
                }
            }
        }
    }
}

def sendEmail() {
    echo "Sending email..."
    emailext body: 'Please find the attached test results.', // Extended E-mail Notification Plug in 설치 필요
            subject: 'FG Test Results',
            to: 'qjawls12@nhnservice.com',
            mimeType: 'text/html',
            attachmentsPattern: "**/mail/FG_test_results.html"
}
