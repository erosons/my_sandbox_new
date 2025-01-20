#image pull
docker pull localstack/localstack-pro

sudo docker run \
  -- rm -it \
  - p 4566:4566 \
  - p 4510-4559:4510-4559 \
  - e LOCALSTACK_API_KEY=${LOCALSTACK_API_KEY:-} \
  - v localstack:/Users/s.eromonsei/my_sandbox/Engineering/DataEngineering/LocalStack/src/volume\
  localstack/localstack-pro

#Instead of using docker compose to spin a local stack container
#We can use pip install
   >> pip install localstack
   >> localstack --version
#To Start 
   >> localstack start -d
#Check version 
   >> localstack --version

#s3 API commands from the CLI

- List objects
      aws --endpoint-url=http://localhost:4566 s3api list-objects  --bucket "my-bucket"
      aws --endpoint-url=http://localhost:4566 s3api list-buckets    

- Put Objects
       aws --endpoint-url=http://localhost:4566 s3api put-object --bucket my-bucket --body '/Users/s.eromonsei/Downloads/New Microsoft Excel Worksheet.xls' --key 'New Microsoft Excel Worksheet.xls' --region us-east-1