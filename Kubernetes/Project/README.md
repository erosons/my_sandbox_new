This project is licensed under to Goopherwood Consulting. All rights reserved.

This project is deploying a web application called Mongo Express and Mongo databases

Scope of this project
=====================

Create a pod for Mongo Express web application that consume and persist data in a  Mongo Database pod.
We will setup a SERVICE deployment for internal communication bewteen the pods
A ConfigMap will be used to store callable parameters like the URL which does contain confidential information
Secret will be used to store confidential information like DB username and password 

Over the internet we will use External Service to communicate with the Node of pod through the NODE IP and pod port Number either through an http/https connection, which in this scenario is mongo web Express.


Process Flow Network:
=====================
 -----------------------------     ----------------------------------         ---------------------         ---------------------------------        -------------
|                            |    |                                  |        |                    |      |                                 |      |              |
| Browser request(http/https)| => | External Service of Mongo Express|  =>    |  Mongo Express POD |  =>  |  Internal Service of MongoDB POD|   => |  MongoDB POD |
|                            |    |                                  |        |                    |      |                                 |      |              |
 ----------------------------      ----------------------------------          --------------------        ---------------------------------        -------------- 



Create the secret yaml file to hold the base64 encoded confidential information (secrets.yaml)

Creating a secrets the values in Base64 encoded for this test project
   >> echo -n 'username' | base64
   >> echo -n 'password' | base64

Order of deployment Matters in Kubernetes
=========================================
The secret and configMap must exists before and pods creation is done

   >>> kubectl apply -f secret.yaml
   >>> kubectl apply -f configMap.yaml

Create manifest file .yaml for each microservices/pods which reference your secret and configMap as shown in manifest file  mongodb.yaml

The pod configuration and service manifest files can live in a single manifest file as shown the manifest file  mongodb.yaml
