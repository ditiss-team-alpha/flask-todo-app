pipeline {
    agent any
    environment {
        DOCKER_HUB_REPO = 'adityak404/flask-todo-app'
        DOCKER_HUB_CREDS = credentials('dockerhub-creds') // <-- Put your Jenkins Docker Hub credentials ID here
        BUILD_TAG = "jenkins-flask-todo-app-42"
    }
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/Aditya-Karbhari/flask-todo-app',
                    credentialsId: 'github-ssh' // <-- Your GitHub SSH credential ID
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                // Remove dir('app') if Dockerfile is in repo root
                sh '''
                    docker build -t flask-todo-app:jenkins-flask-todo-app-42 .
                    docker tag flask-todo-app:jenkins-flask-todo-app-42 flask-todo-app:latest
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running application tests...'
                sh '''
                    docker run --rm flask-todo-app:jenkins-flask-todo-app-42 python -m pytest tests/
                '''
            }
        }
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh '''
                    echo ${DOCKER_HUB_CREDS_PSW} | docker login -u ${DOCKER_HUB_CREDS_USR} --password-stdin
                    docker push flask-todo-app:jenkins-flask-todo-app-42
                    docker push flask-todo-app:latest
                '''
            }
        }
    }
    post {
        success {
            echo ':white_tick: Pipeline completed successfully!'
        }
        failure {
            echo ':x: Pipeline failed!'
        }
        always {
            cleanWs()
        }
    }
}


Pankaj Athe
  2:15 PM
pipeline {
    agent any
    environment {
        DOCKER_HUB_REPO = 'adityak404/flask-todo-app'
        DOCKER_HUB_CREDS = dockerhub-credentials // <-- Put your Jenkins Docker Hub credentials ID here
        BUILD_TAG = "jenkins-flask-todo-app-42"
    }
    stages {
        stage('Checkout Code') {
            steps {
                echo 'Checking out code from GitHub...'
                git branch: 'main',
                    url: 'https://github.com/ditiss-team-aplha/flask-todo-app.git',
                    credentialsId: 'github-ssh' // <-- Your GitHub SSH credential ID
            }
        }
        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                // Remove dir('app') if Dockerfile is in repo root
                sh '''
                    docker build -t flask-todo-app:jenkins-flask-todo-app-42 .
                    docker tag flask-todo-app:jenkins-flask-todo-app-42 flask-todo-app:latest
                '''
            }
        }
        stage('Run Tests') {
            steps {
                echo 'Running application tests...'
                sh '''
                    docker run --rm flask-todo-app:jenkins-flask-todo-app-42 python -m pytest tests/
                '''
            }
        }
        stage('Push to Docker Hub') {
            steps {
                echo 'Pushing image to Docker Hub...'
                sh '''
                    echo ${DOCKER_HUB_CREDS_PSW} | docker login -u ${DOCKER_HUB_CREDS_USR} --password-stdin
                    docker push flask-todo-app:jenkins-flask-todo-app-42
                    docker push flask-todo-app:latest
                '''
            }
        }
    }
    post {
        success {
            echo ':white_tick: Pipeline completed successfully!'
        }
        failure {
            echo ':x: Pipeline failed!'
        }
        always {
            cleanWs()
        }
    }
}

