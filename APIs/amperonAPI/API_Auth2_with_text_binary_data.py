import requests
import pandas as pd
import os
from io import StringIO, BytesIO
from datetime import datetime
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from timeit import timeit
import zipfile
from Tools.database.s3_loader import s3_loder
import os
from Tools.utils import logz
from airflow.models import Variable
from Tools.utils import logz

localPath="/tmp"
logger = logz.create_logger()
root_bucketName='e'

class AmpAPI:
    client_secret=Variable.get("''")
    client_id=Variable.get("''")

    current_datetime_now=datetime.now()
    # Get the current date and time
    current_datetime = datetime.now().date()
    
    # Add 15 days to the current date and time
    currentday_now=current_datetime.strftime("%Y-%m-%d")
    startdate15days = current_datetime + timedelta(days=14)
    startdate = startdate15days.strftime("%Y-%m-%d")
    fileformat=current_datetime.strftime("%Y%m%d")

    # Add 14 days to the current date and time
    future14day = current_datetime + timedelta(days=14)
    future14day= future14day.strftime("%Y-%m-%d")

    futureDate = current_datetime +relativedelta(years=5)
    futureDate = futureDate.strftime("%Y-%m-%d")

    # Create a session
    session = requests.Session()

    # Set up basic authentication
    session.auth = (client_id, client_secret)


    @classmethod    
    def get_dataAmperon_APICall(cls,**kwargs):
        
        # Get the reqiured parameters
        datasorce,apiNumber=kwargs['datasorce'],kwargs['apiNumber']
        params=kwargs['params']
        api_url=kwargs['api_url'].format(apiNumber)
        bucketKey=kwargs['bucketKey']
            
        headers = {'content-type':'text/csv'}
        logger.info("Now making {} request callout ".format(datasorce))

        # Make a GET request to the API endpoint
        response = cls.session.get(api_url,params=params,verify=False,headers=headers)

        # Check if the request was successful
        logger.info("******* Making the API CALL*********")
        if response.status_code == 200:  
                    try:
                        print(response.status_code)
                        response_text=response.text
                        df = pd.read_csv(StringIO(response_text))
                        df['Pulled At']= cls.current_datetime_now
                        result="Ops successfully"  
                        print(df.head(5))

                        logger.info("**********Creating directory**********")
                        if apiNumber =='519':
                            bucketPrefix="http://"

                            filename=str(cls.fileformat) +'.parquet'
                            file_path_name = os.path.join(localPath , bucketPrefix , bucketKey,filename)
                            os.makedirs(os.path.dirname(file_path_name), exist_ok=True)
                            logger.info(file_path_name)
                            df.to_parquet(path=file_path_name, index=False,compression='snappy')
                        else:
                            bucketPrefix='"http://'
                            datasorce='Pulse'

                            filename=str(cls.fileformat) +'.parquet'
                            file_path_name = os.path.join(localPath , bucketPrefix , bucketKey,filename)
                            os.makedirs(os.path.dirname(file_path_name), exist_ok=True)
                            logger.info(file_path_name)
                            df.to_parquet(path=file_path_name, index=False,compression='snappy')

                        logger.info("**********Loading S3 bucket**********")
                        file_name=file_path_name
                        Bucket=root_bucketName
                        key = bucketPrefix+ '/'+ bucketKey + str(cls.fileformat) + '.parquet'
                        logger.info(file_name,Bucket,key)
                        s3_loder(file_name,Bucket,key)
                        logger.info("Blobs successful")
                    except pd.errors.EmptyDataError:
                        print("Empty CSV data")
                    except pd.errors.ParserError:
                        print("Error parsing CSV data")
          
        else:
                print("Error:", response.status_code)
                print("Response:", response.text)

                                
    @classmethod
    def get_dataAmperon_PerMeter(cls,**kwargs):
        
        # Get the reqiured parameters
        datasorce,apiNumber=kwargs['datasorce'],kwargs['apiNumber']
        params=kwargs['params']
        api_url=kwargs['api_url'].format(apiNumber)
        bucketKey=kwargs['bucketKey']

        
        print("Now making {} request callout ".format(datasorce))     
        headers = {'content-type':'json'}

        # Make a GET request to the API endpoint
        logger.info("******* Making the API CALL*********")
        response = cls.session.get(api_url,params=params,verify=False,headers=headers)

        # Check if the request was successful
        if response.status_code == 200:  
            try:
                        data=response.json()['data']
                        #print(data[0])
                        filename= data[0]['name'].replace('.zip','.xlsx')
                        url=(data[0]['download_url'])
                        #print(url)
                        response = cls.session.get(url)
                        response.content
                        read_out_binaryfile = BytesIO(response.content)
                        with zipfile.ZipFile(read_out_binaryfile, 'r') as z:
                            for line in z.namelist():
                                  print(line)
                            with z.open(filename) as f:
                                df = pd.read_excel(f)
                                df.head()
                                df['Pulled At']= cls.current_datetime_now
                                result="Ops successfully"  
                                print(df.head(5))
                        
                        logger.info("**********Creating directory**********")
                        
                        if apiNumber =='519':
                            bucketPrefix='".'
                            filename=str(cls.fileformat) +'.parquet'
                            file_path_name = os.path.join(localPath , bucketPrefix , bucketKey,filename)
                            os.makedirs(os.path.dirname(file_path_name), exist_ok=True)
                            logger.info(file_path_name)
                            df.to_parquet(path=file_path_name, index=False,compression='snappy')
                        else:
                            bucketPrefix=', '
                            datasorce='Pulse'
                            bucketKey='Pulse_PerMeterLTF'
                            filename=str(cls.fileformat) +'.parquet'
                            file_path_name = os.path.join(localPath , bucketPrefix , bucketKey,filename)
                            os.makedirs(os.path.dirname(file_path_name), exist_ok=True)
                            logger.info(file_path_name)
                            df.to_parquet(path=file_path_name, index=False,compression='snappy')
                        # This has to be mapped to s3 bucket

                        logger.info("**********Loading S3 bucket**********")
                        
                        file_name=file_path_name
                        Bucket=root_bucketName
                        key=bucketPrefix+ '/'+ bucketKey + str(cls.fileformat) + '.parquet'
                        logger.info(file_name,Bucket,key)
                        s3_loder(file_name,Bucket,key)
                        logger.info("Blobs successful")
            except pd.errors.EmptyDataError:
                        print("Empty CSV data")
            except pd.errors.ParserError:
                    print("Error parsing CSV data")

        else:
          print("Error:", response.status_code)
          print("Response:", response.text)



amperonAPI=amperonAPI()

def LT_Weather_Neutral():
     for apiNumber in ['519','60700']:
         amperonAPI.get_dataAmperon_APICall(datasorce='SEAR',
                                apiNumber=apiNumber,
                                bucketKey='L/',
                                api_url="www",
                                params={
                                  "startDate":amperonAPI.startdate15days,
                                  "endDate": amperonAPI.futureDate,
                                  "resolution": "X",
                                  "forecastType": "past_obligation",
                                  "metric": "mwh",
                                  "analysisBreakdown": "mixes",
                                  "obligationDuration": 0
                                              }
                                )


# execution_time = timeit(ApiCaller, number=1)

# # Format the execution time
# formatted_time = str(timedelta(seconds=execution_time))

# print(f"Execution time: {formatted_time}")