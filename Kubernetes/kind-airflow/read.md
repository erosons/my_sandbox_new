*** Spin up a local 3 node kubernetes cluster using kind ****
*** Some versions of Linux wll make the install succesul excecpt you use sudo ****

>> install kind -> https://kind.sigs.k8s.io/docs/user/quick-start/#installing-from-source
>> install kubectl -> https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/
>>  docker
>>> install helm -> https://helm.sh/docs/intro/install/
>> docker-compose

## STEP 1 ********
 create step 
>>>  kind create cluster --name airflow-cluster --config kind-cluster-config.yaml

***To check your existing cluster ****
  
>>> kind get clusters / kubectl cluster-info --context kind-airflow-cluster

***To delete the cluster**
`
>>> kind delete cluster --name airflow-cluster

## STEP 2
    Add a helm chart repository
    >>> helm repo add apache-airflow https://airflow.apache.org

    Update helm repo with
    >>>helm repo update

    *** Sarch helm chart repo for airflow ***

    >>> helm search repo airflow

## STEP 3(Good practice to isolate your deployment into a namespace) 
>>> sudo kubectl create namespace airflow

## STEP 4:Deploy the airflow helm chart 
- >>> sudo kubectl create namespace airflow

## Deploy /Installing the Airflow Helm chart
>>> sudo helm install airflow apache-airflow/airflow --namespace airflow --debug --timeout 10m0s

## Deployment Versions
sudo helm ls -n airflow
NAME    NAMESPACE       REVISION        UPDATED                                 STATUS          CHART           APP VERSION
airflow airflow         1               2024-11-24 23:32:36.555182606 -0600 CST deployed        airflow-1.15.0  2.9.3   

## Check logs 
sudo kubectl logs airflow-worker-0 -n airflow

## Expose airflow helm chart values file  and update

>>> helm show values apache-airflow/airflow > values.yaml

# After Deployment should see the folowing airflow , launch the webserver

    Airflow Webserver: kubectl port-forward svc/airflow-webserver 8080:8080 --context kind-airflow-cluster
    Default Webserver (Airflow UI) Login credentials: 
        username: admin
        password: admin
    Default Postgres connection credentials:
        username: postgres
        password: postgres
        port: 5432

    You can get Fernet Key value by running the following:
    # echo Fernet Key: $(kubectl get secret --namespace airflow-kind airflow-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)

# STEP 5: Validate Deployment
sudo(optional)   kubectl get pods --context -kind  

## Deploying Your DAGS Approach 1

     Rebuild a new image from the dockerfile with DAGS and override current image in value.yaml to push the dags to dags folder.

#### NOTE  ###############################################
 Reloading NEW IMAGE INTO KIND cluster after every rebuild
# #########################################################
   # Option One
   >>>sudo  kind load docker-image  apacheairflow:0.0.1 --name airflow-cluster
   After the above operations is loaded then , run the  helm upgrade again 

   # Option two
    - Build the image and push to registry, upgrade your values.yaml files amd 
    - Upgrade to reflect the update version

#### NOTE  ###############################################
To get details about your airflow instance
# #########################################################

get into airflow: ->  kubectl exec --stdin --tty  airflow-webserver-794684d7bb-bxnc2  -n airflow -- /bin/bash
To know all the providers details : ->  kubectl exec --stdin --tty  airflow-webserver-794684d7bb-bxnc2  -n airflow --airflow info
