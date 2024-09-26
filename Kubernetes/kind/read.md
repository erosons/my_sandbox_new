***Spin up a local 3 node kubernetes cluster using kind.

```bash
>>>  kind create cluster --name airflow-cluster --config config.yaml

***To check your existing cluster
  
>>> kind get clusters / kubectl cluster-info --context kind-airflow-cluster

***To delete the cluster

>>> kind delete cluster --name airflow-cluster
```
Add a heml chart repository for test case
```bash
>>> helm repo add airflow https://github.com/marclamberti/airflow-eks-helm-chart
>>>helm repo add apache-airflow https://airflow.apache.org

Update helm repo with
>>>helm repo update
```
Sarch helm chart repo for airflow
```bash
>>> helm chart repo search airflow

Expose airflow helm chart values file

>>> helm show values apache-airflow/airflow > values.yaml

Installing the Helm chart
```bash
>>> helm install  -f values.yaml --kube-context kind-airflow-cluster airflow apache-airflow/airflow
```

# Airflow Webserver:     kubectl port-forward svc/airflow-webserver 8080:8080 --namespace airflow-kind
Default Webserver (Airflow UI) Login credentials:
    username: admin
    password: admin
Default Postgres connection credentials:
    username: postgres
    password: postgres
    port: 5432

You can get Fernet Key value by running the following:
# echo Fernet Key: $(kubectl get secret --namespace airflow-kind airflow-fernet-key -o jsonpath="{.data.fernet-key}" | base64 --decode)