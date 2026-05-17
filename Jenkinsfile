pipeline {
    agent any

    stages {

        //  Build stage
        stage('Build') {
            steps {
                echo 'Installing all dependencies required'
                bat 'C:\\Users\\Aryan\\Python\\Scripts\\pip.exe install -r requirements.txt'
            }
        }

        //  Test
        stage('Test') {
            steps {
                echo 'Running tests on the code'
                bat 'C:\\Users\\Aryan\\Python\\python.exe -m pytest test_app.py -v'
            }
        }

        //  Code Quality testing
        stage('Code Quality') {
            steps {
                echo 'Running code for quality check'
                bat 'C:\\Users\\Aryan\\Python\\Scripts\\pip.exe install pylint'
                bat 'C:\\Users\\Aryan\\Python\\python.exe -m pylint app.py checker.py --fail-under=5'
            }
        }

        // Security
        stage('Security') {
            steps {
                echo 'Running security scan'
                bat 'C:\\Users\\Aryan\\Python\\Scripts\\pip.exe install bandit'
                bat 'C:\\Users\\Aryan\\Python\\python.exe -m bandit -r . --exit-zero'
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

        // Release stage
        stage('Release') {
            steps {
                echo 'Releasing to the production environment'
                bat 'docker stop password-checker-prod || true'
                bat 'docker rm password-checker-prod || true'
                bat 'docker run -d --name password-checker-prod -p 5001:5000 password-checker'
            }
        }

        // Monitoring stage
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
            echo 'The pipeline has completed successfully!'
        }
        failure {
            echo 'Error, Pipeline has failed. Please check the logs.'
        }
    }
}