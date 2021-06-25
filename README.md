### DevOps Docusign Application

- A Web Application to register for an organizations Docusign PowerForm.
- The application is used by students of California State University Long Beach for Video Production Request by registering on application website.
- The Application bypasses the PowerForm signer Information page and redirects to main Docusign PowerForm.
- Built using Python Flask Framework, Docker and deployed on Azure using CI/CD pipelines.
- The application is Dockerized and hosted on Microsoft Azure.
- The CI/CD pipeline has been created to automate the building and storing of Docker image based on updates and it's deployment as docker containers on Azure instances.

### Application Stack
- Python.
- Docker.
- Microsoft Azure pipelines (CI/CD Pipeline)
- Microsoft Azure App Service

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
