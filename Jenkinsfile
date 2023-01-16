node('inbound') {   
    stage('Prepare') {
        echo "1.Prepare Stage"
        pwd
        script {
            build_tag = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
            }
    }
    stage('Test') {
        echo "2.Test Stage"
        echo "${BRANCH_NAME}"
        echo "${build_tag}"
    }
}