***To switch between different Java versions on macOS****

You can use the "java_home" command-line utility or manage the versions using third-party tools like Homebrew. Here are two methods you can use:

Method 1: Using "java_home" command-line utility (built-in):
==========================================================

Open Terminal, which you can find in the Utilities folder within the Applications folder or by using Spotlight search.

To view the installed Java versions on your system, enter the following command:

This command will display a list of available Java versions.=>
 https://jdk.java.net/archive/,https://www.openlogic.com/openjdk-downloads?field_java_parent_version_target_id=406&field_operating_system_target_id=431&field_architecture_target_id=All&field_java_package_target_id=All
 
  >>> /usr/libexec/java_home -V

To switch to a specific Java version, use the following command:

 >>> export JAVA_HOME=`/usr/libexec/java_home -v <version>`

Replace <version> with the desired version from the list displayed in the previous step. For example, if you want to switch to Java 11, the command would be:

>>> export JAVA_HOME=`/usr/libexec/java_home -v 11`
This command sets the JAVA_HOME environment variable to the specified Java version.

Verify the Java version by running:
>> java -version
It should display the selected Java version.


Method 2: Using Homebrew (with third-party tools):
===================================================

Install Homebrew if you haven't already. Visit the Homebrew website (https://brew.sh/) and follow the installation instructions.

Open Terminal and install the "jenv" tool using Homebrew:

>>> brew install jenv
Add jenv to your shell:

>>> echo 'export PATH="$HOME/.jenv/bin:$PATH"' >> ~/.bash_profile
>>>echo 'eval "$(jenv init -)"' >> ~/.bash_profile
If you're using Zsh, replace ~/.bash_profile with ~/.zshrc.

Close and reopen Terminal, or run the following command to apply the changes:

>>> source ~/.bash_profile
Install the desired Java versions using Homebrew:

****brew tap AdoptOpenJDK/openjdk****
    >>> brew install --cask adoptopenjdk8
    >>> brew install --cask adoptopenjdk11
This example installs Java 8 and Java 11 using AdoptOpenJDK. You can install other versions as needed.

Configure jenv to recognize the installed Java versions:

>>> jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-8.jdk/Contents/Home
>>> jenv add /Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk/Contents/Home

Adjust the paths based on the versions you installed in step 5.

Set the global Java version:

>>> jenv global <version>
Replace <version> with the desired Java version. For example:
jenv global 11.0
Verify the Java version by running:


java -version
It should display the selected Java version.



**LINUX-UBUNTU INSTALLATION ***

install java JDK Version 11 link -> https://docs.aws.amazon.com/corretto/latest/corretto-11-ug/generic-linux-install.html
OR 
sudo apt-get install openjdk-11-jdk

List of Java Versions: update-java-alternatives --list

For more instructions see: https://www.conduktor.io/kafka/how-to-install-apache-kafka-on-linux/#Setup-the-$PATH-environment-variable-5