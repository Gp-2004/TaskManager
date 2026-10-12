
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                sh 'python3 -m py_compile taskmanager.py'
            }
        }

        stage('Test') {
            steps {
                sh 'python3 -m unittest -v taskmanager.TaskManagerTests'
            }
        }

        stage('Package') {
            steps {
                sh '''
                    python3 -c "import zipfile; z=zipfile.ZipFile('taskmanager.zip','w'); z.write('taskmanager.py'); z.close()"
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: 'taskmanager.zip',
                                 fingerprint: true
            }
        }
    }

    post {
        success {
            echo 'Task Manager pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check Console Output.'
        }
    }
}
