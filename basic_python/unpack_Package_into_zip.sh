pip download -d ./packages requests
cd packages
mkdir requests_package
pip install -t requests_package requests-*.whl
cd requests_package
zip -r ../requests_package.zip .
cd ..

aws s3 cp requests_package.zip s3://your-bucket/path-to-packages/