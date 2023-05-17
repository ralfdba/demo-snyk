pipeline {
  agent any
  stages {
    stage('Build') {
      agent any
      steps {
        sh 'cd $WORKSPACE/'
        echo 'Dentro de WS'
        sh 'pyraider go'
      }
    }

    stage('Test') {
      steps {
        echo 'In Test'
      }
    }

    stage('Final') {
      steps {
        echo 'Fin'
      }
    }

  }
}