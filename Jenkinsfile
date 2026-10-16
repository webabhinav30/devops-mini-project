pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
        IMAGE_NAME = "webabhinav30/devops-mini-app"
    }
    stages {
        stage('Checkout') { steps { checkout scm } }
        stage('Build') { steps { sh 'docker build -t $IMAGE_NAME:latest ./app' } }
        stage('Test') { steps { sh 'docker run --rm $IMAGE_NAME:latest python -m pytest test_app.py' } }
        stage('Push') {
            steps {
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
                sh 'docker push $IMAGE_NAME:latest'
            }
        }
        stage('Deploy') {
            steps {
                dir('ansible') { sh 'ansible-playbook -i inventory.ini deploy.yml' }
            }
        }
    }
}
