======
Guide:
======= 
https://docs.aws.amazon.com/msk/latest/developerguide/create-cluster.html
create Client Machine : https://docs.aws.amazon.com/msk/latest/developerguide/create-serverless-cluster-client.html
MSK : amazon:https://github.com/aws/aws-msk-iam-sasl-signer-python#get-started
https://github.com/aws/aws-msk-iam-sasl-signer-python/blob/main/docs/installation.rst

SG=> sg-07e8ea0f6398efa2a
subnet-
subnet-006bcedf326abc5e8 
subnet-012d43b35a88edc78 
subnet-02b08a1658804d294 	
vpc-077584d4a4fd61b33
Cluster ARN: arn:aws:kafka:us-east-1:975049886938:cluster/demo-cluster-1/ab5547d8-f8a3-4e2d-bede-29db373831ff-18
Zookeeper string: 
"z-3.democluster1.yj9tlm.c18.kafka.us-east-1.amazonaws.com:2181,
z-1.democluster1.yj9tlm.c18.kafka.us-east-1.amazonaws.com:2181,
z-2.democluster1.yj9tlm.c18.kafka.us-east-1.amazonaws.com:2181"

bootstrap-server:
b-3.democluster1.yj9tlm.c18.kafka.us-east-1.amazonaws.com:9098,
b-1.democluster1.yj9tlm.c18.kafka.us-east-1.amazonaws.com:9098,
b-2.democluster1.yj9tlm.c18.kafka.us-east-1.amazonaws.com:9098

=================================
on your local : describe cluster:
=================================
 aws kafka describe-cluster --region us-east-1 --cluster-arn arn:aws:kafka:us-east-1:975049886938:cluster/demo-cluster-1/ab5547d8-f8a3-4e2d-bede-29db373831ff-18

Command ran on bastian host EC2 instance
wget https://downloads.apache.org/kafka/3.8.0/kafka_2.12-3.8.0.tgz &&
tar -xzf kafka_2.12-3.8.0.tgz &&
cd kafka_2.12-3.8.0 &&
cd bin &&
sudo yum -y install java-11 &&
cd libs &&
wget https://github.com/aws/aws-msk-iam-auth/releases/download/v1.1.1/aws-msk-iam-auth-1.1.1-all.jar &&
cd .. &&
cd bin &&
touch client.properties 

###### All kafka call should include :
        /kafka-topics.sh --list --bootstrap-server "b-3.democluster1.mnz1ow.c18.kafka.us-east-1.amazonaws.com:9098" --command-confi
        g /home/ec2-user/kafka_2.12-3.8.0/bin/client.properties
Ensure your aws credentials config is setup( which translate to a session in the API) 

### GET bootstra server
aws kafka get-bootstrap-broker --region --cluster-arn
==============
Create a topic
==============
>>> bin/kafka-topics.sh --create --bootstrap-server "b-2.democluster1.u65xrz.c18.kafka.us-east-1.amazonaws.com:9098" --command-config /home/ec2-user/kafka_2.12-3.8.0/bin/client.properties  --topic awskafkatopic1 --partitions 1 --replication-factor 2
   

describe cluster:
 aws kafka describe-cluster --region us-east-1 --cluster-arn arn:aws:kafka:us-east-1:975049886938:cluster/demo-cluster-1/ab5547d8-f8a3-4e2d-bede-29db373831ff-18


#### PYTHON KAFKA Package
pip install kafka-python


kafka-acls --bootstrap-server localhost:9092 \
  --command-config adminclient-configs.conf \
  --add \
  --allow-principal User:* \
  --operation All \
  --topic testTopic

#### create topics programmatically

##### config comes from client.properties files
p = KafkaProducer(
        bootstrap_servers=['b-2-public.xxx.c2.kafka.ap-northeast-1.amazonaws.com:9196'],
        security_protocol="SASL_SSL",
        sasl_mechanism="SCRAM-SHA-512",
        sasl_plain_username="t9tXXX",
        sasl_plain_password="2p%wXXX",
)

p.send(topic="my-requests", value=b"test")


***Python implementation***
- https://dev.to/aws-builders/amazon-msk-101-with-python-3g0

Java Connection
===============
import org.apache.kafka.clients.admin.AdminClient;
import org.apache.kafka.clients.admin.AdminClientConfig;

import java.util.Properties;

public class KafkaAdminClientExample {
    public static void main(String[] args) {
        Properties props = new Properties();
        props.put(AdminClientConfig.BOOTSTRAP_SERVERS_CONFIG, "your-msk-bootstrap-servers");
        props.put(AdminClientConfig.SECURITY_PROTOCOL_CONFIG, "SSL");
        props.put("ssl.truststore.location", "/path/to/your/truststore.jks");
        props.put("ssl.truststore.password", "your_truststore_password");

        AdminClient adminClient = AdminClient.create(props);

        // Use the AdminClient to perform administrative tasks

        // Close the AdminClient
        adminClient.close();
    }
}

===============
Python Versions
===============

from confluent_kafka import AdminClient, KafkaException

# Define your configuration
config = {
    'bootstrap.servers': 'your-msk-bootstrap-servers',
    'security.protocol': 'SSL',
    'ssl.truststore.location': '/path/to/your/truststore.jks',
    'ssl.truststore.password': 'your_truststore_password'
}

# Create an AdminClient instance
admin_client = AdminClient(config)

# Example: List existing topics
def list_topics():
    try:
        # List topics
        metadata = admin_client.list_topics(timeout=10)
        print(f"Topics: {metadata.topics.keys()}")
    except KafkaException as e:
        print(f"Failed to list topics: {e}")

# Example: Create a new topic
def create_topic(topic_name):
    try:
        # Define topic creation parameters
        fs = admin_client.create_topics([
            NewTopic(topic_name, num_partitions=1, replication_factor=1)
        ])
        # Wait for topic creation to complete
        fs[topic_name].result()
        print(f"Topic '{topic_name}' created successfully.")
    except KafkaException as e:
        print(f"Failed to create topic: {e}")

# List topics
list_topics()

# Create a topic (example topic name: 'new_topic')
create_topic('new_topic')
