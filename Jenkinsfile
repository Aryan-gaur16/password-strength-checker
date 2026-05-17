pipeline {
    agent any

    environment {
        PYTHON = 'C:\\msys64\\mingw64\\bin\\python.exe'
        PIP = 'C:\\msys64\\mingw64\\bin\\pip.exe'
    }

    stages {

        // This is the build stage for my pipeline
        stage('Build') {
            steps {
                echo 'Installing all dependencies required'
                bat '"C:\\msys64\\mingw64\\bin\\pip.exe" install -r requirements.txt'
            }
        }

        //  Test stage
        stage('Test') {
            steps {
                echo 'Running tests on the code'
                bat '"C:\\msys64\\mingw64\\bin\\python.exe" -m pytest test_app.py -v'
            }
        }

        // Code Quality stage
        stage('Code Quality') {
            steps {
                echo 'Running the code quality check '
                bat '"C:\\msys64\\mingw64\\bin\\pip.exe" install pylint'
                bat '"C:\\msys64\\mingw64\\bin\\python.exe" -m pylint app.py checker.py --fail-under=5'
            }
        }

        // This checks the Security
        stage('Security') {
            steps {
                echo 'Running the security scan on your code'
                bat '"C:\\msys64\\mingw64\\bin\\pip.exe" install bandit'
                bat '"C:\\msys64\\mingw64\\bin\\python.exe" -m bandit -r . --exit-zero'
            }
        }

        //  Deployment stage
        stage('Deploy') {
            steps {
                echo 'Deploying to staging environment'
                bat 'docker build -t password-checker .'
                bat 'docker stop password-checker-staging || true'
                bat 'docker rm password-checker-staging || true'
                bat 'docker run -d --name password-checker-staging -p 5000:5000 password-checker'
            }
        }

        //  Release stage
        stage('Release') {
            steps {
                echo 'Releasing to production environment...'
                bat 'docker stop password-checker-prod || true'
                bat 'docker rm password-checker-prod || true'
                bat 'docker run -d --name password-checker-prod -p 5001:5000 password-checker'
            }
        }

        //  Monitoring phase
        stage('Monitoring') {
            steps {
                echo 'Starting monitoring with Prometheus and Grafana...'
                bat 'docker-compose up -d prometheus grafana'
                echo 'Prometheus running at http://localhost:9090'
                echo 'Grafana running at http://localhost:3000'
            }
        }
    }

    post {
        success {
            echo 'The pipeline has completed successfully!'
        }
        failure {
            echo 'Error, Pipeline has failed. Please check the logs.'
        }
    }
}