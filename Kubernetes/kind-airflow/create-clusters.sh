#!/bin/bash

# Set variables for registry name, port, cluster name, network name, registry address, Docker Hub username, and image name
reg_name='registry'
reg_port='5000'
cluster_name='airflow-cluster'
network_name='airflow-network'
reg_address="${reg_name}:${reg_port}"
yaml_config='kind-cluster-config.yaml'
dockerhub_username='iskidet'
image_name='apacheairflow'
image_tag='2.9.3.1'

# Function to log messages
log_message() {
    local message="$1"
    echo "$(date +'%Y-%m-%d %H:%M:%S') - $message"
}
log_message "Delete cluster '$cluster_name' if existexists..."
kind delete cluster --name airflow-cluster
# Ensure Docker network exists
log_message "Ensuring Docker network '$network_name' exists..."
docker network inspect "$network_name" >/dev/null 2>&1
if [ $? -ne 0 ]; then
    docker network create "$network_name"
    log_message "Created Docker network '$network_name'."
else
    log_message "Docker network '$network_name' already exists."
fi

# Check if the registry container is running
log_message "Checking if Docker registry container '$reg_name' is running..."
running=$(docker inspect -f '{{.State.Running}}' "$reg_name" 2>/dev/null)

# Start or create the registry container if not running
if [ "$running" != "true" ]; then
    log_message "Docker registry container '$reg_name' is not running. Attempting to start it..."
    exists=$(docker inspect -f '{{.State.Status}}' "$reg_name" 2>/dev/null)
    
    if [ "$exists" == "exited" ]; then
        log_message "Docker registry container '$reg_name' exists but is stopped. Restarting it..."
        docker start "$reg_name"
    else
        log_message "Creating new Docker registry container '$reg_name' on port $reg_port..."
        docker run -d --restart=always -p "${reg_port}:5000" --name "${reg_name}" --network "${network_name}" registry:2
        
        if [ $? -eq 0 ]; then
            log_message "Docker registry container '$reg_name' started successfully on port $reg_port."
        else
            log_message "Failed to start Docker registry container '$reg_name'."
            exit 1
        fi
    fi
else
    log_message "Docker registry container '$reg_name' is already running."
fi

# Connect the registry to the cluster network
docker network connect "kind" "${reg_name}"

# Create or configure the kind cluster
if [ -f "$yaml_config" ]; then
    log_message "Creating or configuring the kind cluster '$cluster_name' with YAML configuration from $yaml_config..."
    kind create cluster --name "$cluster_name" --config "$yaml_config"
    log_message "Cluster '$cluster_name' created successfully."
else
    log_message "Configuration file $yaml_config not found."
    exit 1
fi

# Annotate all nodes in the cluster to use the local registry
for node in $(kind get nodes --name "$cluster_name"); do
    kubectl annotate node "$node" "kind.x-k8s.io/registry=$reg_address"
    log_message "Annotated $node to use the local Docker registry at $reg_address."
done

# Build and push the Docker image to Docker Hub
log_message "Building Docker image '$dockerhub_username/$image_name:$image_tag'..."
docker build -t "$dockerhub_username/$image_name:$image_tag" .
if [ $? -eq 0 ]; then
    log_message "Image built successfully. Pushing to Docker Hub..."
    docker push "$dockerhub_username/$image_name:$image_tag"
    if [ $? -eq 0 ]; then
        log_message "Image pushed to Docker Hub successfully."
    else
        log_message "Failed to push image to Docker Hub."
    fi
else
    log_message "Failed to build Docker image."
fi

# End of the script
log_message "Script execution completed."
