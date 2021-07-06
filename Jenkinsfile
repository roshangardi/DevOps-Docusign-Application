pipeline
{
	agent any

	environment
		{
		registry = "public.ecr.aws/x4g8n8v4/docker-images-repo"
		registryCredential = 'dockerhub'
		}



	stages
	{
		stage('Cloning Git') {
	  steps {

	  git credentialsId: 'DocuSign_Git_Repo',
		url: 'git@code.csulb.edu:URD/DocusignDemoApp.git',
		branch: "master"
		}
		}

		stage('Building image') {
		  steps{
			script {
			  docker.build registry
			}
		  }
    }

		 // Uploading Docker images into AWS ECR
		stage('Pushing to ECR') {
		 steps{
			 script {
					sh 'aws ecr-public get-login-password --region us-east-1 | docker login --username AWS --password-stdin public.ecr.aws/x4g8n8v4'
					sh 'docker push public.ecr.aws/x4g8n8v4/docker-images-repo:latest'
			 }
			}
      }

		// Stopping Docker containers for cleaner Docker run
		stage('stop previous containers') {
			 steps {
			 script {
				sh 'docker ps -f name=docusignapp -q | xargs --no-run-if-empty docker container stop'
				sh 'docker container ls -a -fname=docusignapp -q | xargs -r docker container rm'
			 }
		   }
		   }

		stage('Docker Run') {
		 steps{
			 script {
					sh 'docker run -d -p 5000:5000 --rm --name docusignapp public.ecr.aws/x4g8n8v4/docker-images-repo:latest'
				}
		  }
		  }

	  stage('Email Stage') {
		steps {
		  mail bcc: '', body: '''This is a test email.
		This is to notify that the pipeline has reached the last stage.
		''', cc: '', from: '', replyTo: '', subject: 'Test pipeline jenkins email', to: 'roshan.gardi-sa@csulb.edu'
		}
	  }

	}

}
