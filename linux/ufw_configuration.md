Step: 1 sudo apt update -y

Step 2: sudo apt install ufw

Step3: systemctl status ufw => to check status

You have to be in the root directory
===================================

Step4: Set the default rule that allows all outgoing traffics
        >>> ufw default allow outgoing
        Output => Default outgoing policy changed to 'allow'
Step 5:  set default rule for incoming for all traffic to DENY
        >>> ufw default deny incoming 
        Output => Default incoming policy changed to 'deny'

Step 6 : Allow ssh
         >>> ufw allow ssh

Step 7 : Before enabling ufw ensure you have the ssh activate, because this 
         could drop all ssh connections
         >>> ufw enable

Step8 : Allow Only my public IPs/internal IPs
        >>> ufw allow from 76.30.189.64 to any port 22 proto tcp 

Step 9: clean unwanted securitysetups or IPs not needed
     >>> ufw status numbered => the numbers
     
    >>> ufw delete 1
    >>> ufw delete 2