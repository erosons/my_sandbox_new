### Feature branch workflow  

<img src="https://github.com/erosons/my_sandbox/blob/main/myPythonprojects/DataEngineering1/Gitfeature_Branching_flow/.drawio.png" width="500" >

#### How it works


The Feature Branch Workflow assumes a central repository, and main represents the official project history. 
Instead of committing directly on their local main branch, developers create a new branch every time they start work on a new feature. 

Feature branches should have descriptive names, like animated-menu-items or issue-#1061. The idea is to give a clear, highly-focused purpose to each branch. Git makes no technical distinction between the main branch and feature branches, so developers can edit, stage, and commit changes to a feature branch.
 

In addition, feature branches can (and should) be pushed to the central repository. This makes it possible to share a feature with other developers without touching any official code


####  Resolve feedback
Now teammates comment and approve the pushed commits. Resolve their comments locally, commit, and push the suggested changes to Bitbucket. Your updates appear in the pull request.


### Merge your pull request

Before you merge, you may have to resolve merge conflicts if others have made changes to the repo. When your pull request is approved and conflict-free, you can add your code to the main branch. Merge from the pull request in Bitbucket.



Clone project
==============
git clone git@example.com:project-name.git

Create branch with your feature:
==================================

git checkout -b feature_name

Write code. Commit changes:
===========================

git commit -m "My feature is ready"

Push your branch to GitLab/GitHub:
===================================

git push origin feature_name

#####  Review your code on commits page.


Create  pull request and merge request.
======================================
Your team lead reviews the code and merges it to the main branch.