#!/bin/bash
yum update -y
yum install -y httpd
systemctl start httpd
systemctl enable httpd
cd /var/www/html
aws s3 cp s3://etlbucket/index.txt ./
aws s3 cp s3://etlbucket/name.csv ./
EC2NAME="$(curl -s http://169.254.169.254/latest/meta-data/placement/availability-zone)"
sed "s/INSTANCE/$EC2NAME/" index.txt > index.html


#echo “Hello World from $(hostname -f)” > /var/www/html/index.html
