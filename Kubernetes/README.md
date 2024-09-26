Course Outline

Basic Concepts of kubernetes or
K8s Architecture
Main K8s Component
kubectl -> which is K8s CLI
K8s YAML configuration File
K8s Namespace -Organizing your Components
K8s ingress
Helm -Package Manager
Volume and persitent Databases
K8s Stafeful Set and Deploying Stateful Apps
K8s Services and use cases

Kubernetes Services Offers
--------------------------
   - High availability or no downtime
   - Scability  or High peformance (Application size can change base on Workloads)
   - Disaster recovery - backup and restore (can restore latest before crsah)

Kubernetes Cluster work on Master-WORKERS Architecture
  - Cluster is a collection of multiple machines

Kubernetes work on the architecture of LEADER-WROKER ARCHITECTURE => One of the VM is designated as Master and the other are designated as NODE
All Worker Nodes has => Container Runtime/Docker  running on them which can be any brand of Container Manager as shown below

===================
kinds in Kubernetes
===================
  - Deployment
  - Secret
  - Service
  - configMap
  - ServiceAccount
  - Ingress
  - PersistentVolumeClaim
  - PersistentVolume -> 
  - StatefulSet
  - clusterRole -> 
  - ClusterRoleBinding ->
  - Role -> #meaning  a user can have access to a particular resource



Scenario 
========
- I have 10,000 customers that will be accessing my application, for proper loaded management and accommodation of my customers,
- I want to deploy 100 containers for my Frontend=>Angular/React
- I want to deploy 100 container for my backend => python/java
- I want to deploy 100 containers for my databases => mysql
While the Master Node receive this request through the Kube - API Sever

MASTER
======
- Kube-ApI Server => Is a gatekeeper through which request routed and validated/authenticated before passing to other process in the cluster.

- ETCD => Is the brain of the cluster. It is a key value pair database that stores all cluster state information and interactions across the 4 prooesses plus kublets on the Node.

NOTE => The etcd does not store the Application data like the database data.

- Scheduler = > The Scheduler is the intelligent hub of the cluster , It determines  which node should a POD before deployed.
    The Scheduler has all details about the nodes. It gives a feedback to the API Server which nodes is what and where the
    PODs should be deployed. these config are passed to kubelet on Node which is reponsible for the spin up of the PODs on th Node.
 
- Controller: Working together with Scheduler and API Server decides how many PODS should be on each Nodes and if there is any failure of PODs on the Node, basically it checks for State, it gathers those informations and send request to the scheduler for re deployment of another PODs.

  How do you interact with the Cluster
  ====================================

  1. How to schedule pods ?
  2. Monitor
  3. Reschedule/restart pod
  4. Join a new NOde

Master Node is responsible for state and Status of thw orker Node and there are atleast 4 processes running on the Master

NODE
====
Kubelet (Container) => It is found on all the NODE this is channel through which the Master NODE communicate with WORKERS NODE
What decision is reached in the MASTER NODE this is passed down to the WORKERS Node via the kubelet.
When the kubelet get request from the Master Node it passes to the Container Runtime/POD , then it spins up all the request as multiple Containers.

Key Componenets of Every Node/Worker

   -  Container Runtime (Docker Engine)
   -  Kubelet is responsible for get instructions from the API server deplying POD taking necessary resources from the Node machine.
   cpus, ram, and storage
   - Kube proxy responsing for forwarding requests from Services to PODS and ensuring optimal route delivery to reduce network overhead.
        Kube proxy always to try to send the request to nearest PODs avioding overheads.


The POD Component
=================
Is the smallest unit of a kubernetes
A pod is an abstraction on a container runtime , just a container is an abstraction on an image runtime

Ideal case only one container application should run in side a POD, but sometimes some helper container may be in a single POD

POD Communication -> Kubernestes offers a virtual network 
  - Every POD has its own IP address which is internal to the cluster and not for public for communication
  - If a container crashes inside a POD for whatever reason , the POD will fail and a new POD is created to replace the old POD with a different IP address

Service Component (Load balancer)
==================================

To deal with the headache of dynamic IP address of a POD that keeps changing each time a POD is recreated.

Sevice Component -> Is a static IP address attached to each POD application 
NOTE: The lifecycle of service and POD are seperate , so even if a POD terminate the service and its address will stay.

and also serve as a load balancer for routing request to the available poDs.
                  - Web application PODS will have its own service
                  - Database PODS will have its own service

Types of services 
=================
    - Internal serivces used for internal comm between the PODS
    - External  This is used for external/pubic communication
    - Ingess -> This is the intermediary between the external service and the POD. 
                 It is an API object that manages external access to the services in a cluster, typically HTTP.
                 Ingress may provide load balancing, SSL termination and name-based virtual hosting
                 Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Traffic routing is controlled by rules defined on the Ingress resource.
        Image-> Here is a simple example where an Ingress sends all its traffic to one Service:
           Engineering/Kubernetes/Ingress.png

ConfigMap
===========

- Is an external configuration your application stores in plain text
  Is uses an API object used to store non-confidential data in key-value pairs. Pods can consume ConfigMaps as environment variables, command-line arguments, or as configuration files in a volume.
  You simply connect it to the PODs, and if endpoint changes, you only makes changes in the configMap.

  A ConfigMap allows you to decouple environment-specific configuration from your container images, so that your applications are easily portable.

  Caution: ConfigMap does not provide secrecy or encryption because is plain text.

Secret
=======

This is used to stores all passwords, certificates  encrypted in base64 encoded format.
Just like configMap you can cannect your pods and the PODs can read those credentials


Data Storage Or Volume
=====================

To persist data in K8s for example a database data , use volumes
Attach a local storage or local machine to the POD
Attach a remote storage which can be outside of the Kubernestes cluster(Cloud Storage)

Think of storage as a hard drive that is plug into a kubernestes cluster. K8s does not manage persist any storage.

Deployment vs  Stateful Set(Data)
=================================
Deployment(Stateless)

This is the blueprint for for deployment of a kubernetes pods.
The deployment is a layer on top of the pod , which allow us to deploy kubernetes pods replicas. across different NODES.
You can scale up or scale down number of PODS through replicas.

apiVersion: apps/v1

kind: Deployment
metadata:
  name: nginx-deployment
  labels:
    app: nginx
spec:
  replicas: 3
  selector:
    matchLabels:
      app: nginx
  template:
    metadata:
      labels:
        app: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.14.2
        ports:
        - containerPort: 80


Stateful Set 
=============
For Application that is stateful, statefulset is used to deploy then, it is used to replicate , scale up or down when a persistence data/dabase is involved. And ensure they in sync.
   - Apps like database(mysql, elastic,mongodb )
   Like a Deployment, a StatefulSet manages Pods that are based on an identical container spec. Unlike a Deployment, a StatefulSet maintains a sticky identity for each of its Pods. These pods are created from the same spec, but are not interchangeable: each has a persistent identifier that it maintains across any rescheduling.

  STOPPED @12:28 -> https://www.youtube.com/watch?v=X48VuDVv0do&t=204s

Limitations
===========
The storage for a given Pod must either be provisioned by a PersistentVolume Provisioner based on the requested storage class, or pre-provisioned by an admin.
Deleting and/or scaling a StatefulSet down will not delete the volumes associated with the StatefulSet. This is done to ensure data safety, which is generally more valuable than an automatic purge of all related StatefulSet resources.

Components
============
The example below demonstrates the components of a StatefulSet.

apiVersion: v1
kind: Service
metadata:
  name: nginx
  labels:
    app: nginx
spec:
  ports:
  - port: 80
    name: web
  clusterIP: None
  selector:
    app: nginx
---




apiVersion: apps/v1
kind: Deployment
metadata:
  name: web

  # specification for the deployment
=====================================
spec:
  selector:
    matchLabels:
      app: nginx # has to match .spec.template.metadata.labels
  serviceName: "nginx"
  replicas: 1 # by default is 1 
  selector:
      matchLabels:
        app: nginx
  template:
    metadata:
      labels:
        app: nginx # has to match .spec.selector.matchLabels
=====================================================
# specific for the PODs
    spec:
      containers:
      - name: nginx
        image: registry.k8s.io/nginx-slim:0.8
        ports:
        - containerPort: 80
          
NOTE => StatefulSet setup can be very tedious to setup compare to Stateless, so it is common industry practice to host database externally outside of the cluster and provide access deatils in configMap.


Kubectl basic Commands
======================

- Status Pods
  >>> kubectl get nodes

- Status of the services
   >>> kubectl get services

- Status of the pods
   >>> kubectl get pods

Test scenario of Creating a deployment and Nginx PODs 
  - deployment name
  - image for the deployment
 >>> Kubectl create deployment nginx-tescase2 --image=nginx

To confirm/validate the deployment
  >>> kubectl get deployment

To get details about the PODs deployment
 >>> kubectl describe pod <PODNAME>

To delete PODs deployment
 >>> kubectl delete deployment <PodsName> 

ReplicatSet is responsbile for managing th PODs replicas

Layer of Abstraction
=====================
      Deployment >> ReplicaSet >> Pods >> Container

Editing a deployment Files 
==========================
   Note this will automatically genarate a yaml deployment file.
 >>> Kubectl edit deployment nginx-tescase

To check all replicaset deployed for existing PODS and non PODs

 >>> kubectl get replicaset 

Debugging a POD through its logs created by app inside the POD
==============================================================

>>> kubectl logs <PODName>
>>> kubectl exec -it <podName>

=========================================
When deploying an application Kubernetes
=========================================

  - When we just need to provide the configuration file (yaml) that contains all the requirements.

  So basically use the APPLY to deploy the application configuration file

  ========
  CRUD OPS 
  ========
     >>> kubectl apply -f <configFile.yaml>  
     >>> kubectl delete -f <configFile.yaml>  
   This be used for new and modification of an existing deplyment.


Configuration/Manifest File explained
=============================

The configuration file is divded into three parts, The first part contains 
    The Type of API version (Sevrvice/Deployment)
         Deployment -> apiVersion:  apps/v1
                       Kind: Deployment
         Service -> apiVersion:  v1
                       Kind: Service
   - metadata parts -> This part containes the deployment/service name
        - name:
        - labels: (This is used to establish connection  between deployment with service)
   - Specification parts ->This contains the specifications for the deployment/service
       For deployment specifications
            - replicas: 
            - selector:  This is used to select all objects within the labels or match certain patterns
                         Selector allows which pods need to be updated when a new deployment of pod is deployed.
                         Selector allows a service to match a pod.
            - template: => This parts holds the blueprint for the pod and within it we find configuration for the conainer

       For service specifications
             - selector: 
             - ports:
   - Status -> This is desired state of the deployment/service ,if the desired is not the actual state kubernestes will try to fix automatically fix it.
        Scenario: 
        =========
              When a deployment is appplied a status is created to track the state of the deployment and this compared against the desired deployment config.yaml file if there is no match then there is problem
              All this informationare pulled from the etcD database 

Validating your file -> https://www.yamllint.com/


Assuming we want to deploy a sevice and a pod
=============================================

>>> kubectl apply -f '/Users/s.eromonsei/my_sandbox/Engineering/Kubernetes/serviice.yaml'
>>> kubectl apply -f '/Users/s.eromonsei/my_sandbox/Engineering/Kubernetes/serviice.yaml'

To  Validate depoyment (POD,Service) get mode details about the deployment
=========================================

>>> kubectl describe  deployment
>>> kubectl describe pod  <podName>
>>> kubectl describe service <ServiceName>  # To validate a service is attached to pod

To show IPS mapped to pods
===========================
kubectl get pod -o wide

As stated earlier when a deployment is done, kubernetes automatically create status of that deployment and this retrieved from ectd database

To See details of an existing deployments
=========================================

>>> kubectl get deployment web -o yaml

To show all components in a cluster with respect to a deployment
=================================================================

>>> kubectl  get all | grep mongodb


To watch as the deployment of the pods
======================================

>>> kubetctl get pod --watch

To expose the pod service to externally 
=======================================
Type: Loadbalancer  -> has to be include the service manifest file -> this actually create a Network LoadBalancer at L4 of OSI model.
NodePort: Portnumber -> the Port number that will expose on the Node , be careful not have a port number conflict between the NodePort and the POD

=======================
     NAMESPACE
=======================
Namespace is is more like a vitualized cluster within a cluster , that allows you to logically group similar resources/applications into a separate namespace

By default there are several namespaces created be kubernetes to manage its components

Benefits of creating a namespace
--------------------------------
   - Manages similar logical resources in their own envirnment
   - Blue-Green deployment that share the same resources
   - ACL management
   - Resource control(Resource Quota A), which defines cpu , ram ,disk used by each name space

Note:=> Few characteristeristics
====

If you have a configMap from Project A namespace that refrences Database namespace 
Project B namespace will also have to maintain the same confiMap that references Database namespace 
Similiar secret for a shared service, you will have to be create them separately across the projects namespaces

But can be shared
==================
  - Services can be shared since the project referencing Database service its configMap will only have to the namespace name as a suffix with the service.
  e.g mysql-service.database

Resource that can be shared
============================

- Volumes are available globally across the cluster
- Nodes are available globally across the cluster

Defining if a resources is bound to a namespace or not.

>>> kubectll api-resources --namespaced=false (not bound to a namespace)
>>> kubectll api-resources --namespaced=True  (Bound to a namespace)


Example
=======
 -> Monitoring (Promethus and Grafana)
 -> workflow-manager (Airflow)
 -> data-analyics(Spark)
 -> logging-Manager(Elastic stash )

>>> kubectl get namespace  

>>> kubectl create  nameapace airflow

==================================
Creating components of a namespace
==================================
Specifying where a component should created

>>> kubectl apply -f mysql-configMap  --namespace=mynamespace

OR  specifying the name space in metadata portion of the manifest file
      apiVersion: v1
      kind: ConfigMap
      metadata: 
        name: mongodb-configmap
        namespace: mynamespaceå
      data: 
        database_url: mongodb-service

Free App out there to control namespace out of kubernetes (Optional)
       >>> brew install Kubectx
       >>> kubens (list out all namespaces and the one that currently active)
       >>> kubenes mynamespace (will switch to mynamespace)

==================
KUBERNETES INGRESS 
===================

Ingress allows you to have a secure domain to externally send request to your pod applications.


Ingress network Flow:
=====================
                                    
                                 ------------------------------------   
                                | Act as a  reverse Proxy Server     |
                                |    Ingress controller Pod          |  <-> myrequest.com(request from external)
                                |      (Routing rules are defined)   |     
                                 ------------------------------------        
                                              ||
                                              \/

 ----------------------------      ----------------------------------          ---------------------       ------------------------
|                            |    |                                  |        |                    |      |                        | 
|                            | => |        Ingres domain             |  =>    |  Internal Service  |  =>  |      MongoDB POD       |
|                            |    |   (https/http://my-domain.com)   |        |                    |      |                        |      
 ----------------------------      ----------------------------------          --------------------        ------------------------     

# Note

 - The domain myapp.com must be valid 
 - The domain must be mapped to  Nodes's IP address,which is entry point to the cluster/server
 - We need to install an ingress Controller to with the Kind ingress which are pods that runs in the cluster
       - for evaluating and processing Ingress rules.
       - manages redirection to the right service
       - Entry to cluster

- There is a list of third party Implemenatation for ingress controller you can choose from.
     - K8s Nginx Ingress Controller
     - K8s Traefik Ingress Controller
     - K8s HAProxy Ingress Controller
     - K8s Kong Ingress Controller

# Once the ingress controller is installed, we need to create an ingress resource that will define the routing rules for the ingress controller
  #Steps    
      - deploy the Nginx ingress controller
      - The target pod internal-service has to be up an running
      - Then deploy the ingress manifest file that has all the rules or routing rules for the ingress controller

Use Case
=========
  - For my local system I have to add the below to my /etc/hosts file to map mongoexpress.com to my localhost
    127.0.0.1  mongoexpress.com


   >>> kubectl get ingress

Strategy in ingress Host
=========================
  - By Path -> One host with different path
  - By sub domains -> One host with different sub domains(Muliple host)

Scenario 1
  Consider google.com
   # by Path
        - Analytics -> google.com/analytics
        - Search -> google.com/search
Scenario 2
  Consider google.com
 # By sub domains to differentiate the path
    - analytics.google.com
    - search.google.com

Kubernetes TLS configuration
=============================
  TLS -> Transport Layer Security -> Secure connection between client and server
  Ingress can be configured to use TLS to secure the connection between the client and the server
  For testing purpose we can use self signed certificate to test the connection.

  >>> OpenSSL genrsa -out ca.key 2048 -> generate a private key
  >>> OpenSSL req -x509 -new -nodes -key ca.key -sha256 -days 1825 -out ca.crt -subj "/CN=mongoexpress.com -> generate a certificate

  Add the certificate and key  to the tls section of tls-secret.yaml file


DEPLOYMENT CADENCE
==================
   
   secrete.yaml  => deployment.yaml => configMap.yaml => ingress.yaml




HELM CHARTS :
=============

- Helm is a pachage mananger for kubernetes, way packaging and distributing yaml files in public and private registry. 

Thinking of it as a Bundle of YAML Files packaged for particular deployment
You can create your own Helm Chart with Helm
Push to Hel Repository
Download other helm chart

You search with -> Helm search
Helm Hub -> Public or private registry

- Helm Chart -> Is a templateing Engine, that can be used to create a chart blueprint for microservices certain values can be in configuration can be passed as values {{. Values.container.image}}

Where the .Values is picked from values.yaml

Example of A template file

apiVersion: v1
kind:
metadata:
  name: {{.Value.name}}
spec:
  containers:
  - name:{{.Value.container.name}}
    image:{{.Value.container.image}}
    ports:{{.Value.container.ports}}

All the values required in the template files are defined in the values.yaml

name:my-app
container:
 name:my-container
 image:my-image
 ports:9001

- Helm can be used to deploy same application across different environment.

Helm Chart Structure
=====================

Mychart/  -> The name of the chart
  Chart.yaml -> contains meta data about the chart like name , version, dependcies
  values.yaml -> values for the template files , these are default values that can be overide.
  charts/  -> if the charts depends on other charts those dependcies will be stored here.
  Templates/ -> This where are all the template for microsevices that will be filled with values from the values.yaml, these are the manifest files that can be deployed to kubernetes.
  README.md ->
  License

NOTE: That during deployment of Helm CHart the values.yaml file can be overwritten by suplying another values.yaml and the values in these files will be merged into a single template file.

Example -> values.yaml

name:my-app
container:
 name:my-container
 image:my-image
 ports:9001
 version: 1.0

-> my-values.yaml

name:my-app
container:
  version: 2.0

Result -> my-values.yaml + values.yaml

name:my-app
container:
 name:my-container
 image:my-image
 ports:9001
 version: 2.0

 OR   
  >>> helm install --set version=2.0
Difference between Helm Version 2.0 and Version 3.0

Helm Version 2.0 ->use a client server setup the server is call Tiller , which is capable of performing a CRUD operation
 This poses a problem with the server side of the application.

So in Hem 3.0 -> The Tiller is removed from the cluster.

Installation
>>>> brew install helm

AIRFLOW REPOSITORY
====================

>>> helm repo add apache-airflow https://airflow.apache.org
>>> helm repo update
>>> helm search repo airflow

Installation helm from the repository
>>> helm install airflow apache-airflow/airflow --namespace airflow --debug

helm --delete airflow apache-airflow/airflow --namespace airflow --debug

# Port forwarding port for airflow  afer helm chart installation**

>>> kubectl port-forward svc/airflow-webserver 8080:8080 -n airflow

Exec into POD
=============

>>> kubectl exec --stdin --tty  airflow-webserver-794684d7bb-bxnc2 -- /bin/bash
OR
>>> kubectl exec -i -t  airflow-webserver-794684d7bb-bxnc2  --/bin/bash

To see value in your helm chart used by airflow helm chart OR modification of airflow chart

**GET VALUES.YAML**

- Get airflow values into a yaml file
   >>> helm show values apache-airflow/airflow > values.yaml

 INSTALLATION
===============  
**Option 1**
- Reinstall airflow with updated configuration/Values.yaml
   >>> helm upgrade install airflow apache-airflow/airflow \
       --set excelutor=KubernetesExecutor \
       --set dags.gitSync.enabled=True \
       --set dags.persistence.enabled=True \
       --set dags.persistence.existingClaim=airflow-pvc \
       --set dags.persistence.storageClass=standard \
       --set logs.persistence.enabled=True \
       --set logs.persistence.existingClaim=host-pv-logs \
       --set logs.persistence.storageClass=path-storage \
       --namespace airflow
       --f values.yaml  --debug
**Option 2**
helm upgrade --install airflow apache-airflow/airflow \
-f values.yaml \
--namespace airflow --debug

- To list out all the helm deployment in namespace
 >>> helm ls -n airflow

NOTE: You can manage all your Variables from Using a  extraEnvFrom/configMap section in the Values.yaml
=====
extraEnvFrom: |
- configMapRef:
    name: 'airflow-variables'

Syncing Helm Chart with Github Repository
=========================================

Use the gitSync in your values.yaml file to sync your helm chart with github repository

if your git is using ssh key, create  secret.yaml easily with the below command line

  >>>  kubectl create secret generic git-ssh-key-secret --from-file=gitSshKey=/Users/s.eromonsei/.ssh/id_rsa 

Locate the  sshKeySecret in your values.yaml
     sshKeySecret: ssh-key-secret

**GET the logs of the gitSync**
===========================
kubectl logs <scheduler> -c git-sync -n airflow 
kubectl logs airflow-scheduler-859cbf465f-tpqjk -c git-sync -n airflow 
  

VOLUMES
========

Three types way to persist data in kubernetes
1. Persistent Volume -> PV -> Storage that is provisioned by the administrator of the cluster and can be used by any pod in the cluster.
2. Persistent Volume Claim -> PVC -> Is a request for storage by a user, it is a request for a particular storage by a user.
3. Storage Class -> Is a type of storage that can be requested by a user, it is a type of storage that can be requested by a user.

Volumes are are not bounded to a namespace, they are cluster wide resources.
Volume are not namespaced, they are cluster wide resources.

Volumes are created just as any other kubernetes resources, they are created using a yaml file.

Onces Apersistence volume is created
A user can request for a particular storage using a PVC
PVC is then mapped to the same namespace as the pod that is requesting for the storage.

Other Types of Volume/Storage
- CofigMap
- Secrets

# write a volume mounting a configMap
apiVersion: v1
kind: Pod
metadata:
  name: my-configmap-pod
spec:
  containers:
  - name: my-configmap-container
    image: busybox
    command: ['sh', '-c', 'echo $(MY_VAR) && sleep 3600']
    env:
    - name: MY_VAR
      valueFrom:
        configMapKeyRef:
          name: my-configmap
          key: my-var
    volumeMounts:
    - name: config
      mountPath: /etc/config
      readOnly: true
  volumes:
  - name: config
    configMap:
      name: my-configmap

STORAGE CLASS
=============
Storage class is used to dynamically create persistent volume , such administrator would not have maually be 
provision the persistent volume each time its needed.

storae clas is also created using a yaml file.

# Write a storage class yaml filw
apiVersion: storage.k8s.io/v1
kind: StorageClass
metadata:
  name: my-storage-class
provisioner: kubernetes.io/aws-ebs
parameters:
  type: gp2
  zone: us-east-1a

The Flow 
 Pod makes a cliam to PVC => PVC makes a claim  to Storage Class =? Storage Class creates the persistent volume PV that meets the requirements of the Claim.

 Execution FLow 
  - Use the storage class yaml to create the storage provosioner or PersistentVolume
  - Use the PVC yaml to create the PVC, 
     >>> kubectl get pvc  -> status should be Bounded
  - Pod use the claim request use the storage that is created by the PVccs

StatefulSet
===========
StatefulSet is a controller that is used to manage stateful application in kubernetes.
stateful applications are  that requires the last state of the application to be saved before and opeartion can be peformed. EXAMPLE: Database( mysql, postgresql, mongodb,elastic search)
Stateless application are applications that does not require the last state of the application to be saved before an operation can be performed. EXAMPLE: Webserver, Web Application

Things you need to do by your self of StatefulSet Apps
=================================== 
- Configure the cloning  and and data sync between the master and the slave'
- Manaaging and Backups

NOTE:
=====
  >>> kubectl exec -i -t  airflow-webserver-794684d7bb-bxnc2  --/bin/bash
  >>> ps aux   -> To see process that is running inside the code 

USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND
mongodb      1  0.3  0.7 1593996 58204 ?       Ssl  Jun12  10:10 mongod --auth --bind_ip_all
root       170  0.1  0.0  18512  3412 pts/0    Ss   02:05   0:00 /bin/bash
root       182  0.0  0.0  34408  2732 pts/0    R+   02:06   0:00 ps aux

To Kill
=======
   >>> Kill 1


# **CREATING User Access AND Kubernetes Dashboard**
===================================================
      Getting Started
      IMPORTANT: Read the Access Control guide before performing any further steps. The default Dashboard deployment contains a minimal set of RBAC privileges needed to run.

      To deploy Dashboard, execute following command:

      >>> kubectl apply -f https://raw.githubusercontent.com/kubernetes/dashboard/v2.7.0/aio/deploy/recommended.yaml

      Alternatively, you can install Dashboard using Helm as described at https://artifacthub.io/packages/helm/k8s-dashboard/kubernetes-dashboard.

      Access
      -------
      To access Dashboard from your local workstation you must create a secure channel to your Kubernetes cluster. Run the following command:

      >>> kubectl proxy

      Now access Dashboard at:-> http://localhost:8001/api/v1/namespaces/kubernetes-dashboard/services/https:kubernetes-dashboard:/proxy/.

      # Creating sample user
      ======================
      In this guide, we will find out how to create a new user using the Service Account mechanism of Kubernetes, grant this user admin permissions and login to Dashboard using a bearer token tied to this user.

      IMPORTANT: Make sure that you know what you are doing before proceeding. Granting admin privileges to Dashboard's Service Account might be a security risk.

      For each of the following snippets for ServiceAccount and ClusterRoleBinding, you should copy them to new manifest files like dashboard-adminuser.yaml and use kubectl apply -f dashboard-adminuser.yaml to create them.

      Creating a Service Account
      ==========================
      We are creating Service Account with the name admin-user in namespace kubernetes-dashboard first.
      - Creating a ClusterRoleBinding ->
      - Creating a ClusterRoleBinding


      In most cases after provisioning the cluster using kops, kubeadm or any other popular tool, the ClusterRole cluster-admin already exists in the cluster. We can use it and create only a ClusterRoleBinding for our ServiceAccount. If it does not exist then you need to create this role first and grant required privileges manually.

      **Getting a Bearer Token**

      Now we need to find the token we can use to log in. Execute the following command:

      >>> kubectl -n kubernetes-dashboard create token admin-user


**PROMETHESUS INSTALLATION**-> https://artifacthub.io/packages/helm/grafana/grafana
=============================

, a  project, is a systems and service monitoring system. It collects metrics from configured targets at given intervals, evaluates rule expressions, displays the results, and can trigger alerts if some condition is observed to be true.

This chart bootstraps a  deployment on a  cluster using the  package manager.

Prerequisites
Kubernetes 1.16+
Helm 3.7+
Get Repository Info
  >> helm repo add prometheus-community https://prometheus-community.github.io/helm-charts
  >> helm repo update
See  for command documentation.

Install Chart
Start from Version 16.0, Prometheus chart required Helm 3.7+ in order to install successfully. Please check your Helm chart version before installation.

  >>> helm install prometheus prometheus-community/prometheus
  >>> helm upgrade --install prometheus prometheus-community/prometheus -f values.yaml --debug
  >>> helm show values  prometheus-community/prometheus > values.yaml
See  below.

See  for command documentation.

Dependencies
By default this chart installs additional, dependent charts:
  - Alertmanager
  - kube-state-metrics
  - prometheus-node-exporter


To disable the dependency during installation, set alertmanager.enabled, kube-state-metrics.enabled, prometheus-node-exporter.enabled and prometheus-pushgateway.enabled to false.

The Prometheus PushGateway can be accessed via port 9091 on the following DNS name from within your cluster:
- prometheus-prometheus-pushgateway.logging-manager.svc.cluster.local -> The Pushgateway is an intermediary service which allows you to push metrics from jobs which cannot be scraped

Get the PushGateway URL by running these commands in the same shell:
 >>> export POD_NAME=$(kubectl get pods --namespace logging-manager -l "app=prometheus-pushgateway,component=pushgateway" -o jsonpath="{.items[0].metadata.name}")
 >>> kubectl --namespace logging-manager port-forward $POD_NAME 9091

**GRAFANA INSTALLATION** -> https://artifacthub.io/packages/helm/grafana/grafana
========================

Helm must be installed to use the charts. Please refer to Helm's documentation to get started.

Once Helm is set up properly, add the repo as follows:

>>> helm repo add grafana https://grafana.github.io/helm-charts

You can then run helm search repo grafana to see the charts.


  >>> helm --install grafana grafana/grafana --debug
  >>> helm repo update 
  
  INNITIAL INSTALLATION
  =====================
  >>> helm install my-release grafana/grafana --debug

  UPGRADE VALUES FILE
  =======       =====
  >>> helm upgrade --install  my-release grafana/grafana -f values.yaml --debug

  GET VALUES FILE
  ==============
 
  >>> helm show values grafana/grafana > values.yaml

  NOTEs:
  ======
  1. Get your 'admin' user password by running:

   kubectl get secret --namespace logging-manager my-release-grafana -o jsonpath="{.data.admin-password}" | base64 --decode ; echo


  2. The Grafana server can be accessed via port 80 on the following DNS name from within your cluster:

   my-release-grafana.logging-manager.svc.cluster.local

   Get the Grafana URL to visit by running these commands in the same shell:
     export POD_NAME=$(kubectl get pods --namespace logging-manager -l "app.kubernetes.io/name=grafana,app.kubernetes.io/instance=my-release" -o jsonpath="{.items[0].metadata.name}")
     kubectl --namespace logging-manager port-forward $POD_NAME 3000