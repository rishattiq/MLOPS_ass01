pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                // Checkout the source code from the repository
                git credentialsId: '395e7040-8063-497f-b373-724e49a180e6', url: 'https://github.com/rishattiq/MLOPS_ass01.git'
            }
        }
        
        
        stage('Containerize and Push to Docker Hub') {
            when {
                branch 'master'
            }
            steps {
                // Build and push Docker image to Docker Hub
                sh 'docker build -t mnist . && docker push mnist'
            }
        }
    }
    
    post {
        success {
            // Send email notification on successful build
            emailext(
                to: 'arnishattiq@gmail.com',
                subject: 'Build Success',
                body: 'The build was successful. Docker image has been pushed to Docker Hub.'
            )
        }
        failure {
            // Send email notification on failed build
            emailext(
                to: 'arnishattiq@gmail.com',
                subject: 'Build Failure',
                body: 'The build failed. Please check the Jenkins console output for details.'
            )
        }
    }
}
