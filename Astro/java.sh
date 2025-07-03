#!/bin/bash

# Update package lists to ensure you get the latest version
echo "Updating package lists..."
sudo apt-get install software-properties-common
sudo apt-get update

# Install OpenJDK 11
echo "Installing OpenJDK 11..."
sudo apt install -y default-jdk

# Check if the installation was successful
if [ $? -eq 0 ]; then
    echo "OpenJDK 11 installed successfully."
else
    echo "Failed to install OpenJDK 11."
    exit 1
fi

# Setting JAVA_HOME environment variable
JAVA_HOME=$(readlink -f /usr/bin/java | sed "s:/jre/bin/java::" | sed "s:/bin/java::")
echo "Setting JAVA_HOME to $JAVA_HOME"
echo "export JAVA_HOME=$JAVA_HOME" >> ~/.bashrc
echo "export PATH=\$JAVA_HOME/bin:\$PATH" >> ~/.bashrc
source ~/.bashrc

# Verifying Java installation
echo "Verifying Java installation..."
java -version