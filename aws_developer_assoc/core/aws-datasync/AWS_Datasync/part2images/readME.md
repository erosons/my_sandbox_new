Step-by-Step Guide to How to Build and Deploy AWS DataSync in Your On-Premises Computer- Part 2
===============================================================================================

Hi guys !! Welcome back to the final part of the AWS DataSync configuration

So, from the last article, I have shown you, step by step, how to successfully configure AWS DataSync Agent. From this section, let me show you how the syncing really happens between the AWS S3 bucket and the on-prem NFS server.

First things first. We need to configure the NFS server. Because I’m absolutely certain anyone can log into their AWS management console and create a folder, in this case I have already created a S3 bucket called datasync-test123 and inside that bucket, I have created a folder called the samples. So basically, the NFS mount point of my computer (The folder that I have configured to store our files in the NFS) and the my S3 buckets datasync-test123 folder is gonna sync with each other. Meaning that, the agent going to check what are the files at the NFS and S3 and, only upload or download the difference between 2 places. Imagine you have the exact same file in both S3 bucket and your mount folder in NFS. When the sync started, the DataSync agent does not replicate that same file again to either direction. It only downloads or uploads the content that are unique at either end.

For linux users, following articles provides you a complete guide of 

==================
how to implement a NFS server on your machine and give the required permissions for the mount folder, respectively.
==================
AWS DataSync NFS to S3 data transfer

1. sudo apt update -y
2. sudo apt upgrade -y
3. sudo apt install nfs-kernel-server -y
4. sudo mkdir mnt
5. chmod 777 mnt
6. sudo nano /etc/exports
7. /mnt 192.168.1.0/24(rw,sync,no_subtree_check,crossmnt,no_wdelay)
8. sudo exportfs -ar
9. sudo exportfs -v

And you are done. Now let me explain line-by-line.

For the first 3 commands, you basically install a nfs server in your linux (mine’s ubuntu) machine. Then for the fourth command, you need to create a folder in your root directory. You know, the one with /home, /var etc. folders. The following image might gives an idea, if you aren’t familiar.

The reason you need create your mount point for the server at root directory is because, AWS DataSync gives an error saying it won’t support the temporary directories, if you attempt to sync with a folder created, for an example, in your Desktop or in Documents. The task may still says available even after you created it, pointing those temporary folders. But when you execute that task, it will gives the aforementioned error.

Then after creating /mnt directory in the root folder, you need to give it the read and write access. To do so, use the 5th command, which not only gives the read and write, but also exec access as well. (In this case, don’t mind the extra privilege ;). 

Then, you have to open the configuration file for the NFS server you have installed, to change the mount directory, as to that freshly created /mnt folder. .

By executing line 6, you will open the relevant config file in the nano text editor. At the very bottom, insert the 7th line.

In there, the first “/mnt” is the mount folder that is created in the root directory. The IPv4 Address range is your private ip address range which belongs your AWS DataSync agent and the NFS server. (Must be in the same private network).

Then finally, execute the 8th and 9th command and restart your linux instance. (Or you can simply restart the nfs server only, which I’m too lazy to find the command for it). Well done. Now you have successfully created your NFS server on your on-premises computer which supports the AWS DataSync process.

This syncing process consists of 2 main parts.

    Source is the S3 bucket and the Destination is the NFS
    Source is the NFS and the destination is the S3 bucket

The source and destination here stands like this. When the source is S3 and the destination is NFS, the DataSync agent downloads all the content of the s3 bucket (except for the same files in the NFS) to the NFS mount point. And likewise, for the second part, the DataSync agent checks the NFS mount path and upload all the files from that NFS mount folder to the s3 bucket, with the exception of the similar files between both endpoints.

Let’s start with the first one. To start syncing, for either of the 2 parts, we need to create a task and specify the source and the destination. But first, check your agent is available. If not recheck your AWS DataSync agent (VM) status. When you go to the “Agents” tab, it should be displayed as follows. (Sometimes, it tends to display “Online” even if the DataSync agent VM is shutdown. To make sure the agent has a healthy network connectivity, test the network connections on the AWS DataSync agent (VM) from you end)

When the agent is all up and running, go to the “Tasks”. In the “Create Task”, you will be greeted with the following page. Since, for the first task, we gonna download all the files that are on the s3 bucket to the on-prem NFS (except of course the similar files that already exits in the NFS) , following are the configuration for the source as the S3 bucket and the destination as the NFS server. Remember, we are not syncing the entire S3 bucket, but a folder inside it called “samples”, for the sake of simplicity.

The latter part is as follows.

For the IAM role, simply click Autogenerate button and let the AWS create a role for you that only gives access specifically to this task only. (Which is safe :). Then click next.

In here, you will be greeted a similar page as before, but for the destination. Do the selections appropriately . (Select “Create a new location” option at here too). For the “NFS Server” option, insert the ip address of your linux instance. You can easily find it using “ip -a” command execution at the terminal as follows.

As you can see, in here, my ip address is 192.168.1.33, which is highlighted in white. Then for the mount path, simply give /mnt and click next.

Now as displayed above, give an appropriate name and select the Transfer mode as you wish. Here, I went with the default.

As you can see, you can schedule the syncing process too :) I didn’t enable the CloudWatch log entries for this one, but feel free to do so, if you wish.

The finally, you will be greeted with the review page. Check all the configurations are correct. If so, click on Create Task button. My review page configs are as follows.

And you are done !!! Congratulations :) You have made it this far. You can see the link is available or not, just after few minutes of creating. Refresh the page few times until you see that beautiful green message. Initially it would be displayed as Creating.

But few minutes (for me around 45s, depends on your internet speed), you will get the “Task status” as “Available”.

To start the syncing process, click on “Start” button at the top right corner. Then you can go to the task execution page, which is as follows.

Initially, it will displays the “Execution status” as Launching. But friends, this definitely gonna take some time. In here I have got the following error message. Though it says, Transfer and Verification completes, we need to dig into the error message.

So, in my s3 bucket, I have placed 3 different types of files. An image, a word document and a video. I needed to see if they are corrupted when they are synced with the NFS server. Despite the message, they were all fine and there weren’t any corruptions whatsoever. Since I didn’t enable CloudWatch, I couldn’t looked into it. But I can assure you, there weren’t any crashes or corruptions. Still I have no idea why it says some files are skipped due to errors, since all the 3 files are downloaded successfully without any fault. If any of you find-out, please let me know in the comment.

Following is my s3 bucket’s “samples” folder.

And this is my on-prem /mnt folder after the syncing completed.

But this error/warning message only seems to be appear at for the first task only. For the second task, when the source is NFS at on-prem and the destination is the s3 bucket, the execution completes successfully without any error message whatsoever as follows.

First it goes from Launching to Transferring.

After when the Transferring hits 100%, it displayed as “Success”

So my dear readers, that conclude both the tasks that I have promised. For the second task, simply reverse the source and destination details which you have inserted for the first task. Hence, in the “Tasks” tab, now you will be greeted the following 2 tasks.

Thanks for reading guys. I love you all !!!