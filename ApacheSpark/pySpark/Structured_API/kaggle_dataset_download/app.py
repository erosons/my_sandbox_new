import kagglehub

# Download latest version
path = kagglehub.dataset_download("jefmenegazzo/pvs-passive-vehicular-sensors-datasets")

print("Path to dataset files:", path)