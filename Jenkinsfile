pipeline {
    agent any

    stages {

        // Stage 1 - Build
        stage('Build') {
            steps {
                echo 'Installing all the dependencies required'
                bat 'pip install -r requirements.txt'
            }
        }

        // Stage 2 - Test
        stage('Test') {
            steps {
                echo 'Running tests on the code'
                bat 'pytest test_app.py -v'
            }
        }

        // Stage 3 - Code Quality
        stage('Code Quality') {
            steps {
                echo 'Running the code quality checker'
                bat 'pip install pylint'
                bat 'pylint app.py checker.py --fail-under=5'
            }
        }

        // Stage 4 - Security
        stage('Security') {
            steps {
                echo 'Running the security scan'
                bat 'pip install bandit'
                bat 'bandit -r . --exit-zero'
            }
        }

        // Stage 5 - Deploy
        stage('Deploy') {
            steps {
                echo 'Deploying to the staging environment'
                bat 'docker build -t password-checker .'
                bat 'docker stop password-checker-staging || true'
                bat 'docker rm password-checker-staging || true'
                bat 'docker run -d --name password-checker-staging -p 5000:5000 password-checker'
            }
        }

        // Stage 6 - Release
        stage('Release') {
            steps {
                echo 'Releasing to production environment'
                bat 'docker stop password-checker-prod || true'
                bat 'docker rm password-checker-prod || true'
                bat 'docker run -d --name password-checker-prod -p 5001:5000 password-checker'
            }
        }

        // Stage 7 - Monitoring
        stage('Monitoring') {
            steps {
                echo 'Starting the monitoring phase with Prometheus and Grafana'
                bat 'docker-compose up -d prometheus grafana'
                echo 'Prometheus running at http://localhost:9090'
                echo 'Grafana running at http://localhost:3000'
            }
        }
    }

    post {
        success {
            echo 'Pipeline has completed successfully!'
        }
        failure {
            echo 'Error, Pipeline has failed. Please check the logs.'
        }
    }
}