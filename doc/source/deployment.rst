Deployment
===========

Deployment occurs when there is a commit on the master branch. The pipeline is triggered, builds a Docker image, and pushes it to Docker Hub. Once pushed to Docker Hub, a webhook triggers the deployment on Azure.