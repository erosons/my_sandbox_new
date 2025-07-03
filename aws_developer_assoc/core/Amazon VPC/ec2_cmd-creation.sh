#!bin/bash

aws ec2 run-instances --image-id ami-0bb84bffd87024d8  --instance-type t2.micro --security-group-ids sg-053744e1695e751cf  --subnet-id subnet-075f358b76d003465 --user-data file://user-data-subnet-id.txt --profile practice_account_main --region us-east-1
