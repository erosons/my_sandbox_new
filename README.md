#  CalculatorLibrary

CI-PROJECT- SETTING UP YOUR PYTHON CI (CONTINOUS INTEGRATION) PROJECT

Passthrough: zCX2rXXBbjgmiPB for url :https://realpython.com/lessons/adding-unit-tests/

#  Set remote repo


Step 1: Setup your remote repo. NOTE: add a python gitignore
Step 2 : Clone the repo to your local directory


#  Virtual env setup

Pip Upgrade cmd 

       >>> python -m pip install --upgrade pip

Step 3: Install virtualenv if not available 

       >>> pip3 install virtualenv

Step 4 : Create your venv 

       >>> virtualenv whateverName —system-site-packages

if using conda 

       >>> conda create --name whateverName python=version(optional) --no-default-packages

Step 5 : Activate venv 

      >>> source whateverName/bin/activate

if using conda 
       >>> conda activate whateverName` >>> conda deactivate

To know which virtualenv you are 
       
       >>> which python or where python  

#  Code Quality Test and dependencies update Library

Step 6 : We use Lintinng to look potential errorensure code Quality 

     >>> pip install flake8 with combines error and PEP 8 style checks

To perform unit tests to ensue no test is missed 

       >>> pip install pytest, pytest-cov

To perform and calculates how much of the code is covered by units tests 

       >>> pip install pytest => See implementation

Step 7 :
Because you have added depenencies to your project you will have to save them in a requirements.txt file 

       >>> pip freeze > requirements.txt

This captures all the dependences used in your project in the requirement file
You can then go to another virtualenv to install the requirement.txt 
      
       >>> pip install -r requirements.txt

Just make sure your CWD contains this requirements.txt file
We can modify or customize our requirement file to install update version by changing operator symbol == 3.0.5 or >=3.0.4 , !=3.0.7
Run          
       >>> pip install --upgrade -r requiremnts.txt

To Uninstall a package, run 
 
       >>> pip show packageName to see if any package depends on that package   => check for Required by:

#  Step 10:

As you write you code continously, you want perform quality checks on your code with 

      >>> flake8 - - statistics or flake8 -file.py: This check for error and style issues.(autpep8/black for formatting)

#  Step 11. 

Unit testing :https://docs.python.org/3/library/unittest.html
Create a unit test_calculator.py for Unit testing with pytest.
Note the prefix "test" is very important that how pytest will know/find the file that contain unit test.

# Step 12:

- Run - this shows more details

         >>> pytest -v --cov=calculator 
         >>> pytest test_calculator.py
         >>> pytest --cov=calculator
         >>> pip install coverage for coverage details

- coverage report -m
- coverage html

# CI/CD

- Step 13 : 
       push your changes back to the remote as necessary
- Step 14 : 
       Create a folder extension .circleci for your build automation
- Step 15 : 
       Create a config.yml file inside the folder extension in 
- step 14
       See config.yml for configuration write up
- Step 16 : 
       Commit your update to repo.
- Step 17: 
       Create account with circleci with your git/bitbucket account
- Step 18 : 
       look for your project folder on circleci and setup project.

# NOTE : 

  Git Workflows is specific to Different team within an Organization read more => Git Flow
: Conda or Pipenv for Dependency and environment management
: Testing => Video on getting Start with Test Guide
: Continous Development (CI/CD) => These are deployable artifacts that can used by other users or used in other projects => Benefits

# Testing

i. test Step 2. test Assertion 3. Integration Testing (Testing multiple components of the application together -> parts like classes, functions, modules)

#  Unit Testing

But Unit test checks that a single component operates in the right way. A unit test helps you to isolate what is broken in your application and fix it faster.

Choosing Test Runner

---

- unittest comes as a standard Library with Python
- nose or nose2
- pytest



# ##########
## GITHUB Clean
# ##########

- FOR BRUTAL CLEANUPS,

To remove all commit history in your remote repository and keep only the latest commit, you can follow these steps:

git clone --bare https://github.com/yourusername/your-repo.git
cd your-repo.git
2. Create an Orphan Branch
>>> git checkout --orphan new-branch
Add All Files and Commit

>>> git add -A
>>> git commit -m "Initial commit with latest files"

>>> git push --force origin new-branch:main


- RECALL a WRONG LAST COMMIT
>>> git reset --hard HEAD~N

- TO START FROM a save point
>>>> git rebase -i HEAD~N 