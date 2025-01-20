import json
import re


def TestCase():
   with open('/Users/s.eromonsei/my_sandbox/Engineering/Dremio/RestAPI/jsonfileTestcase.json','r') as fp:
      if fp != '':
         for i in (json.load(fp)['data']):
            if 'sesRepOfRecord' in (i["datasetPath"]) and i["status"]["combinedStatus"]=="CAN_ACCELERATE" and i["status"]["availability"]=="AVAILABLE":
                     result=print(f'everything looks good')
                     break
         else:
            result= print(f'Reflection check was successful')
            raise Exception("Sorry, Reflection not found ")
      else:
         result= print("Test")
         print("Check Connection")

      return result


TestCase()