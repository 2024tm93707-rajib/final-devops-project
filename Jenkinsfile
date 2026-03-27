pipeline {
    agent any
    stages {
        stage('Clone') {
            steps {
                git 'https://github.com/yourusername/aceest-devops-project.git'
            }
        }
        stage('Install') {
            steps {
                sh 'pip install -r requirements.txt'
            }
        }
        stage('Test') {
            steps {
                sh 'pytest'
            }
        }
        stage('Build') {
            steps {
                sh 'docker build -t aceest-fitness .'
            }
        }
    }
}
