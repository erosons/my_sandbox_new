Publishing images to Github ghcr.io Container registry
Setup your container registry using this link
  - https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry
Login 
  - echo $Package_token | docker login ghcr.io -u erosons --password-stdin

push image to github container registry
  - docker push ghcr.io/erosons/python:01

Volume

Anomymous volume
    -v /app
Named Volume
    -v feedback:/app
BindMount Volume
    -v $(pwd):/app  OR   -v /Users/s.eromonsei/my_sandbox/Engineering/Docker/sampleDocker-project4:/app 
Making a bind mount volume read-only for docker container  not to be able to write to external host volumes/folder
    -v $(pwd):/app:ro
Making subfolder writable Even when there is a bind mount in place mapped to folder in the image and set to read-only
    -v /app/temp  =>  Note this takes precedence over the original ro set above