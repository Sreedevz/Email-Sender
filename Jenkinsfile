pipeline {
    agent any

    environment {
        EMAIL_USER = credentials('admin')     // Jenkins credential ID
        EMAIL_PASS = credentials('Sreedevz@123')
    }

    stages {
        stage('Checkout') {
            steps {
                git 'https://github.com/Sreedevz/Email-Sender'   // 🔁 Replace with your Git repo
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'python3 -m venv venv'
                sh '. venv/bin/activate && pip install -r requirements.txt'
            }
        }

        stage('Run Email Test') {
            steps {
                sh '''
                . venv/bin/activate
                export EMAIL_USER=$EMAIL_USER
                export EMAIL_PASS=$EMAIL_PASS
                python manage.py test mailtest.tests.email_test
                '''
            }
        }
    }
}
