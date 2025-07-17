pipeline {
    agent any

    stages {
        stage("Code Clone") {
            steps {
                echo "🔁 Cloning Repository..."
                git url: "https://github.com/tanujsaini123/devops-quote-app.git", branch: "main"
            }
        }

        stage("Build Docker Image") {
            steps {
                echo "🐳 Building Docker image..."
                sh 'docker build -t quote-app .'
            }
        }

        stage("Push To DockerHub") {
            steps {
                echo "📦 Pushing Docker image to DockerHub..."
                withCredentials([usernamePassword(
                    credentialsId: "dockerHubcreds",         // ✅ Must exist in Jenkins credentials
                    usernameVariable: "DOCKER_USER",
                    passwordVariable: "DOCKER_PASS"
                )]) {
                    sh '''
                        echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
                        docker tag quote-app:latest $DOCKER_USER/quote-app:latest
                        docker push $DOCKER_USER/quote-app:latest
                    '''
                }
            }
        }

        stage("Deploy to K8s") {
            steps {
                echo "🚀 Deploying with K8s..."
                sh "kubectl apply -f k8s/"
            }
        }
    }
}
