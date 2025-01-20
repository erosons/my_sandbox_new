import azure.functions as func
import logging
from snowflake.snowpark import Session
from azure.keyvault.secrets import SecretClient
from azure.identity import ManagedIdentityCredential,DefaultAzureCredential
import os



_ACCOUNT:str = os.environ.get('account')
_USER:str = os.environ.get('user')
_PASSWORD:str = os.environ.get('password')

app = func.FunctionApp(http_auth_level=func.AuthLevel.ANONYMOUS)

@app.route(route="http_trigger_demo")
def http_trigger_demo(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')
    if name =="magic":
        akv_url:str = os.environ.get('akv_url')
        # Getting secrets from the key_vault_url
        key_vault_url = akv_url

        # Use Local login CLI to authenticate in local dev and suse Principal to Authenticate in the cloud env
        credential =  DefaultAzureCredential()
        print(f'printing keyVault,{key_vault_url}')
        # Create a SecretClient to interact with Azure Key Vault
        secret_client = SecretClient(vault_url='', credential=credential)
        print(secret_client)
        snowflake_username = secret_client.get_secret('user').value
        snowflake_pwd = secret_client.get_secret('password').value
        snowflake_account = secret_client.get_secret('account').value

        logging.info('Executing the snowflake connections.')
        new_func(snowflake_account, snowflake_username, snowflake_pwd)
    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
http_trigger_demo(func.HttpRequest) 


def new_func(_ACCOUNT, _USER, _PASSWORD):
    pars ={ 
    'account':_ACCOUNT,
    'user': _USER,
    'password':_PASSWORD,
    'warehouse':'COMPUTE_WH',
    'role':"ACCOUNTADMIN",
}
    sql= """ 
        select dname, sum(sal)
        from SAMPLESUPERSTORE.PUBLIC.emp 
        join SAMPLESUPERSTORE.PUBLIC.dept on emp.deptno = dept.deptno
        where dname <> 'RESEARCH'
        group by dname
        order by dname;
        """
    
    try:
     logging.info('Executing session.')
     session = Session.builder.configs(pars).create()
    except:
        logging.info(f'Error establishing session {sql}')
        return func.HttpResponse("Execept caught attempting to connect to SQL DB", status_code=404)
    
    #     emps = (session.table("EMP").select("DEPTNO", "SAL"))
    #     depts = (session.table("DEPT").select("DEPTNO", "DNAME"))
    #     q = emps.join(depts, emps.deptno == depts.deptno)

    #     q = q.filter(q.dname != 'RESEARCH')
    #     (q.select("DNAME", "SAL")
    #   .group_by("DNAME")
    #   .agg({"SAL": "sum"})
    #   .sort("DNAME")
    #   .show())
    try:
        logging.info(f'Executing {sql}')
        view = session.sql(sql).toPandas()
        return print(view)
    except:
        logging.info(f'Error in executing  {sql}')
        return func.HttpResponse("Execept caught attempting to connect to SQL DB", status_code=500)
