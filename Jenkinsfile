pipeline {
    agent any
    
    environment {
        DOCKER_HUB_REPO = 'adityak404/flask-todo-app'
        DOCKER_HUB_CREDS = credentials('dockerhub-credentials')
        BUILD_TAG = "${env.BUILD_NUMBER}"
    }
    
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub...'
                checkout scm
            }
        }
        
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                script {
                    sh """
                        docker build -t ${DOCKER_HUB_REPO}:${BUILD_TAG} .
                        docker tag ${DOCKER_HUB_REPO}:${BUILD_TAG} ${DOCKER_HUB_REPO}:latest
                    """
                }
            }
        }
        
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                script {
                    sh """
                        echo ${DOCKER_HUB_CREDS_PSW} | docker login -u ${DOCKER_HUB_CREDS_USR} --password-stdin
                        docker push ${DOCKER_HUB_REPO}:${BUILD_TAG}
                        docker push ${DOCKER_HUB_REPO}:latest
                    """
                }
            }
        }
        
        stage('Clean Up') {
            steps {
                echo 'Cleaning up old Docker images...'
                sh """
                    docker rmi ${DOCKER_HUB_REPO}:${BUILD_TAG} || true
                    docker system prune -f
                """
            }
        }
    }
    
    post {
        success {
            echo '✅ Pipeline completed successfully!'
        }
        failure {
            echo '❌ Pipeline failed!'
        }
    }
}
