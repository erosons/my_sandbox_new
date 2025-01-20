****INTRODUCTION***
##### https://www.redpanda.com/guides/kafka-tutorial


What is event streaming?


Event streaming is the digital equivalent of the human body's central nervous system. It is the technological foundation for the 'always-on' world where businesses are increasingly software-defined and automated, and where the user of software is more software.

Technically speaking, event streaming is the practice of capturing data in real-time from event sources like databases, sensors, mobile devices, cloud services, and software applications in the form of streams of events; storing these event streams durably for later retrieval; manipulating, processing, and reacting to the event streams in real-time as well as retrospectively; and routing the event streams to different destination technologies as needed. Event streaming thus ensures a continuous flow and interpretation of data so that the right information is at the right place, at the right time.

What can I use event streaming for?
Event streaming is applied to a wide variety of use cases across a plethora of industries and organizations. Its many examples include:

To process payments and financial transactions in real-time, such as in stock exchanges, banks, and insurances.
To track and monitor cars, trucks, fleets, and shipments in real-time, such as in logistics and the automotive industry.
To continuously capture and analyze sensor data from IoT devices or other equipment, such as in factories and wind parks.
To collect and immediately react to customer interactions and orders, such as in retail, the hotel and travel industry, and mobile applications.
To monitor patients in hospital care and predict changes in condition to ensure timely treatment in emergencies.
To connect, store, and make available data produced by different divisions of a company.
To serve as the foundation for data platforms, event-driven architectures, and microservices.

***Apache Kafka® is an event streaming platform. What does that mean?***

Kafka combines three key capabilities so you can implement your use cases for event streaming end-to-end with a single battle-tested solution:

To publish (write) and subscribe to (read) streams of events, including continuous import/export of your data from other systems.
To store streams of events durably and reliably for as long as you want.
To process streams of events as they occur or retrospectively.
And all this functionality is provided in a distributed, highly scalable, elastic, fault-tolerant, and secure manner. Kafka can be deployed on bare-metal hardware, virtual machines, and containers, and on-premises as well as in the cloud. You can choose between self-managing your Kafka environments and using fully managed services offered by a variety of vendors.

***How does Kafka work in a nutshell?***
Kafka is a distributed system consisting of servers and clients that communicate via a **high-performance TCP network protocol**. It can be deployed on bare-metal hardware, virtual machines, and containers in on-premise as well as cloud environments.

Servers: Kafka is run as a cluster of one or more servers that can span multiple datacenters or cloud regions. 
Some of these servers 

  - form the storage layer, called the brokers. 
  - Other servers run Kafka Connect to continuously import and export data as event streams to integrate Kafka with your existing systems such as relational databases as well as other Kafka clusters. 
 
 To let you implement mission-critical use cases, a Kafka cluster is highly scalable and fault-tolerant: if any of its servers fails, the other servers will take over their work to ensure continuous operations without any data loss.

Clients: They allow you to write distributed applications and microservices that read, write, and process streams of events in parallel, at scale, and in a fault-tolerant manner even in the case of network problems or machine failures. Kafka ships with some such clients included, which are augmented by dozens of clients provided by the Kafka community: 

  clients are available for 
      - Java and Scala 
	  - Including the higher-level Kafka Streams library, for Go, Python, C/C++, 
	  - And many other programming languages as well as REST APIs.

Main Concepts and Terminology
An event records the fact that "something happened" in the world or in your business. It is also called record or message in the documentation. When you read or write data to Kafka, you do this in the form of events. 
  Conceptually, an event has a
   - key, 
   - value, 
   - timestamp, 
   - compression type
   - partition offsets
   - and optional metadata headers. Here's an example event:

***Example of Events***
Event key: "Alice"
Event value: "Made a payment of $200 to Bob"
Event timestamp: "Jun. 25, 2020 at 2:06 p.m."

Producers are those client applications that publish (write) events to Kafka, and 
Consumers are those that subscribe to (read and process) these events. 
In Kafka, producers and consumers are fully decoupled and agnostic of each other, which is a key design element to achieve the high scalability that Kafka is known for. For example, producers never need to wait for consumers. Kafka provides various guarantees such as the ability to process events exactly-once.

***Events***
Events are organized and durably stored in topics. Very simplified, a topic is similar to a folder in a filesystem,  and the events are the files in that folder. An example topic name could be "payments". Topics in Kafka are always multi-producer and multi-subscriber: a topic can have zero, one, or many producers that write events to it, as well as zero, one, or many consumers that subscribe to these events. Events in a topic can be read as often as needed—unlike traditional messaging systems, events are not deleted after consumption. 
Instead, you define for how long Kafka should retain your events through a per-topic configuration setting, after which old events will be discarded. Kafka's performance is effectively constant with respect to data size, so storing data for a long time is perfectly fine.

Topics are partitioned, meaning a topic is spread over a number of "buckets" located on different Kafka brokers. This distributed placement of your data is very important for scalability because it allows client applications to both read and write the data from/to many brokers at the same time. When a new event is published to a topic, it is actually appended to one of the topic's partitions. Events with the same event key (e.g., a customer or vehicle ID) are written to the same partition, and Kafka guarantees that any consumer of a given topic-partition will always read that partition's events in exactly the same order as they were written.


Figure: This example topic has four partitions P1–P4. Two different producer clients are publishing, independently from each other, new events to the topic by writing events over the network to the topic's partitions. Events with the same key (denoted by their color in the figure) are written to the same partition. Note that both producers can write to the same partition if appropriate.
To make your data fault-tolerant and highly-available, every topic can be replicated, even across geo-regions or datacenters, so that there are always multiple brokers that have a copy of the data just in case things go wrong, you want to do maintenance on the brokers, and so on. A common production setting is a replication factor of 3, i.e., there will always be three copies of your data. This replication is performed at the level of topic-partitions.

This primer should be sufficient for an introduction. The Design section of the documentation explains Kafka's various concepts in full detail, if you are interested.

***Kafka APIs ***
In addition to command line tooling for management and administration tasks, Kafka has five core APIs for Java and Scala:

The Admin API to manage and inspect topics, brokers, and other Kafka objects.
The Producer API to publish (write) a stream of events to one or more Kafka topics.
The Consumer API to subscribe to (read) one or more topics and to process the stream of events produced to them.
The Kafka Streams API to implement stream processing applications and microservices. It provides higher-level functions to process event streams, including transformations, stateful operations like aggregations and joins, windowing, processing based on event-time, and more. 

Input is read from one or more topics in order to generate output to one or more topics, effectively transforming the input streams to output streams.
The Kafka Connect API to build and run reusable data import/export connectors that consume (read) or produce (write) streams of events from and to external systems and applications so they can integrate with Kafka. 

For example, a connector to a relational database like PostgreSQL might capture every change to a set of tables. However, in practice, you typically don't need to implement your own connectors because the Kafka community already provides hundreds of ready-to-use connectors.
Where to go from here
To get hands-on experience with Kafka, follow the Quickstart.
To understand Kafka in more detail, read the Documentation. You also have your choice of Kafka books and academic papers.
Browse through the Use Cases to learn how other users in our world-wide community are getting value out of Kafka.
Join a local Kafka meetup group and watch talks from Kafka Summit, the main conference of the Kafka community.




***INSTALL KAFKA ON MACOS With bootstrap-server***
https://kafka.apache.org/downloads


	- DownloadJDK 11 (Validate JDK  ) switch if you have a different version
	- Download  Kafka from Apache
	- Extract the tar file
  - Add the bin to the PATH in .bashrc or .zsh-> PATH="$PATH:~/kafka_2.13-3.0.0/bin"

TEST : without the PATH
/kafka-topics.sh

***Start the bootstrap-server followed by Starting Kafka Server****
Please note that the bootstrap-server and Kafka server should be running in different terminals and both are required to run Kafka successfully.

step 1 >>>bootstrap-server-server-start.sh  ~/kafka_2.13-3.1.0/config/bootstrap-server.properties

step 2>>> kafka-server-start.sh ~/kafka_2.13-3.1.0/config/server.properties

***STOP KAFKA and bootstrap-server***

step 1 >> stop Kafka with Crtl +C then 
step 2 stop bootstrap-server with Crtl+C

IF necessary change the storage location on server.properties -> log.dirs and Zookeepr -> dataDir=/tmp/bootstrap-server
 To your storage diectory of choice.



###############
---Commands----
###############

***CREATE A TOPIC in a single Node Local host***
>>> kafka-topics.sh --bootstrap-server localhost:9092  --create --topic first_topic 

Second Topics with 5 partitions
cluster >>> kafka-topics.sh --command-config playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --create --topic second_topic --partitions 5
>>> kafka-topics.sh --bootstrap-server localhost:9092  --create --topic second_topic  --partitions 5

***REPlICATION FACTOR***
The replication factor is the number of copies of a topic that will be created 
***NOTE*** : The replication factor cannot be greater than the number of brokers in a cluster

cluster >>> kafka-topics.sh --command-config playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --create --topic third_topic --partitions 3 --replication-factor 3
Local   >>> kafka-topics.sh --bootstrap-server localhost:9092  --create --topic third_topic --partitions 3 --replication-factor 1

write a message to list topics
>>> kafka-topics.sh --bootstrap-server localhost:9092  --list

write a message to describe a topic
>>> kafka-topics.sh --bootstrap-server localhost:9092  --describe --topic third_topic
cluster >>> kafka-topics.sh --command-config playground.config --bootstrap-server cluster.playground.cdkt.io:9092 --describe --topic second_topic
=======


 
 ***INSTALL KAFKA ON MACOS IN KRAFT MODE NO bootstrap-server***

Follow the steps above up the PATH

- The first step is to generate a new ID for your cluster
  >>> kafka-storage.sh random-uuid

This will generate a UUID

  - ClusterIDoutput =>  tDPdZgKmTtqdl7zPXGYPIg

***Format the kafka Storage=> using the server.properties file in the kraft folder***
 >> kafka-storage.sh format -t NZrXvXjeQBiLX0ct5m4wIA -c ~/kafka_2.13-3.1.0/config/kraft/server.properties
- Should get : Formatting /tmp/kraft-combined-logs (things are looking good)

***Start Kafka Server using Kraft (Quorom consensus protocol)**
  >>> 'kafka-server-start.sh' ~/kafka_2.13-3.1.0/config/kraft/server.properties'

- if all goes well you see the Broker with its ID.
- IF necessary change the storage location on server.properties -> log.dirs and Zookeepr 


 ***Working WITH KAFKA CLI***
 kafka CRUD  
### Cheat Sheets 
###### https://gist.github.com/sahilsk/d2a6ec384f5f2333e3fef40a581a97e1

 CRUD OPERATIONS IN THE CLI
   - kafka-topics.sh --creates a topic
   - kafka-topics.sh --list all topics
   - kafka-topics.sh --delete a topic
   - kafka-topics.sh --describe a topic
   - kafka-topics.sh --alter a topic

***TOPICS MANAGEMENT***

   - kafka-topics.sh --create --topic first_topic --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092
   - kafka-topics.sh --if-not-exists --create --topic first_topic --partitions 3 --replication-factor 1 --bootstrap-server localhost:9092

   - kafka-topics.sh --list --bootstrap-server localhost:9092
   - kafka-topics.sh --describe --topic mykraft_topic --bootstrap-server localhost:9092
   - kakfa-topics --increase --topic first_topic --partitions 3 --bootstrap-server localhost:9092
   - kafka-topics.sh --alter --topic first_topic --partitions 3 --bootstrap-server localhost:9092
   - kafka-topics.sh --delete --topic first_topic --bootstrap-server localhost:9092

  NOTE: 
  =====
     We will be using bootstrap Option instead of bootstrap-server option in the future
      >> kafka-topics.sh --bootstrap-server localhost:9092 

# ###############
#### PRODUCING
# ###############
WIHOUT Keys

>> kafka-console-producer.sh  --bootstrap-server localhost:9092 --topic mykraft_topic
Prompt you to send streams >  My myname is Samson
                           > I am the afther of Prosper
                           > I live in Houston, TX
to exits crtl C

## Property that ensures all broker and ISR ack they recieved the messags
>> kafka-console-producer.sh  --bootstrap-server localhost:9092 --topic mykraft_topic producer-property acks=all

### Send Message to non exixtsing tpic
 Kafka will use the default settings in the server properties to ceate the topic and start producing to it
 