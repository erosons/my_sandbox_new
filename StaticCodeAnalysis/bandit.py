import subprocess
import xml.etree.ElementTree as ET
import tempfile

def static_Code_analysis(temp_python_file,temp_python_file2):
    
    # Run Bandit on the temporary Python file
    bandit_command = f"bandit -r {temp_python_file} p test  -c {temp_python_file2} -v"
  
    # Write output of the code analysis to the temporary file
    with open("bandit_output.txt", "w") as f:
        subprocess.run(bandit_command, shell=True, stdout=f)


if __name__ == "__main__":
   
   file = "/Users/s.eromonsei/stageGitHub/my_sandbox/Engineering/WpackagesforwebScreping/WebscrapingwithLogin.py"
   file2 = "/Users/s.eromonsei/stageGitHub/my_sandbox/PrivacyPolicy_validator_in_Apps/bandit.yaml"
   static_Code_analysis(file,file2)