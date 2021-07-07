### DevOps Docusign Application:

- A complete Jenkins CI/CD Pipeline demonstration.
- Automated Jenkins Continuos Integration and Continuos Deployment of Python Application to register for an organizations Docusign PowerForm.
- The application is used by students of California State University Long Beach for Video Production Request by registering on application website.
- The Application bypasses the PowerForm signer Information page and redirects to main Docusign PowerForm.

### Jenkins CI/CD Pipeline Workflow:
- Developers build and push code to Source Code Management system, GitHub.
- A Webhook is associated with Git repository and Jenkins Pipeline.
- Jenkins polls for the changes on GitHub repo and triggers the pipeline/built for every new commit.
- The application repository is cloned and docker image is been created by jenkins pipeline.
- The docker image is pushed to Amazon ECR repository.
- Python Application is ran as docker container on AWS EC2 instance on port 5000 by pulling the latest image from Amazon ECR.
- All of the above stages of Jenkins pipeline are defined in Jenkinsfile and version controlled in GitHub repo.
- The CI/CD pipeline has been created to automate the building and storing of Docker image based on updates and it's deployment as docker containers on AWS instances.

### Jenkins Workflow Results:
- #### CI/CD Pipeline Arcictecture:

![CICD_DevOps_Pipeline](https://github.com/roshangardi/DevOps-Docusign-Application/blob/master/Images/CICD_DevOps_Pipeline.png?raw=true)

- #### Jenkins Pipeline Stages:

![Pipeline_Stages](https://github.com/roshangardi/DevOps-Docusign-Application/blob/master/Images/PipelineJobOverview.png?raw=true)

- #### AWS ECR Repository for docker images:

![AWS_ECR_Repository](https://github.com/roshangardi/DevOps-Docusign-Application/blob/master/Images/AWS_ECR_Image_Repo.png?raw=true)

- #### AWS EC2 instance running python application's docker container:

![AWS_EC2_Docker](https://github.com/roshangardi/DevOps-Docusign-Application/blob/master/Images/Runningdockercontainer.png?raw=true)

- #### Python Application up and running on 5000 port of EC2 instance:

![Python_App_on_Docker](https://github.com/roshangardi/DevOps-Docusign-Application/blob/master/Images/DockerContainerApp.png?raw=true)

### Application Stack:
- Python.
- Docker.
- Jenkins
- AWS Elastic Container Registry.
- AWS EC2.

### Intructions to run the application locally:
- run.py is the entrypoint. Exectue run.py

### Instructions to run the application as a Docker Container:
- Install Docker Desktop client on the host.
- Change directory to the application folder
- Build the docker image from Dockerfile using below command:
`$ docker build -t image_name .`

- Check the list of images using:
`$ docker image ls`

- Create and run a single container from the image built in previous step using:
`$ docker container run -d -p 5000:5000 --name container_name image_name`

- Check if the container is running using:
`$ docker container ls`

- Go to "http://localhost:5000/" on the webrowser of your choice and you'll see your dockerized application running.

### Instructions to run the application on AWS EC2 instance as a Docker Container through Jenkins CI/CD pipline:

- Launch an EC2 instance on AWS.
- Create an AWS role and assign "AmazonEC2ContainerRegistryFullAccess" policy to the role.
- Assign the role to EC2 instance.
- Setup the working environment on instance by installing following applications:
  - Docker
  - Jenkins
  - Git
- Create and configure Jenkins Pipeline to poll from GitHubSCM.
- Fetch Jenkins Pipeline definition from SCM.
- Add Webhooks to the pipeline.
- Manually run the pipeline to test.
- Now for every new code change in SCM, the pipeline will be triggered and python application will be deployed as a docker container on EC2.
