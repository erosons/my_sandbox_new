Publishing images to Github ghcr.io Container registry
    Setup your container registry using this link
      - https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
- Token creation
     Create a authen token classic if your company uses SSO have enabled for your gothub account or your organization.
- Login 
      - echo $ses_docker_images_token | docker login ghcr.io -u erosons --password-stdin
- push image to github container registry
      - docker push ghcr.io/erosons/python:01

## Volume

  Anomymous volume
    -v /app
  Named Volume
      -v feedback:/app
  BindMount Volume
      -v $(pwd):/app
  Making a bind mount volume read-only for docker container  not to be able to write to external host volumes/folder
    -v $(pwd):/app:ro
  Making subfolder writable when a bind mount folder is read-only
    -v /app/temp   => Note this takes precedence over the original ro set above

## Working with EnvironmentVaraiable

  Add .env to your root directory and pass kwarg
  PORT=80

  on your CLI you can pass --env-file ./.env OR $(pwd)/.env

Working with Build Argument
  ARG in our Dockerfile are like place holders which values can be passed diredtly in the dockerfile or --build-arg during docker build 

Connecting to an IP base services on your localhost machine from a Dockerfile image (e.g  WebApp to a MongoDB installed on your localsystem )
 URL - host.docker.internal:portNumber => This is converted to an IP that is resolved by docker to identify localhost service