pipeline{
    agent any

    stages{
        stage("load_data"){
            steps{
                echo "Loading the data is done"
            }
        }
        stage("feature_engineering"){
            steps{
                echo "feature_engineering is done"
            }
        }
        stage("pre_processing"){
            steps{
                echo "pre_processing is done"
            }
        }
        stage("model_selection"){
            steps{
                echo "model_selection is done"
            }
        }
    }
    post{
        always{
            emailext body:"summery", subject: "Pipeline Status", to: 'jayaharisai1212@gmail.com'
        }
    }
}