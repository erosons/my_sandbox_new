import os
from arrowflight import connect_to_dremio_flight_server_endpoint

def query_stage_dremio_by_arrowflight(sql_query):
    hostname = ''
    port = '32010'
    uid  = os.getenv("uid")
    pat = os.getenv("pat")
    df = connect_to_dremio_flight_server_endpoint(hostname, port, uid, pat, sql_query, True, False, True, False, False, False)    
    return df

# Then use the following to query the data
sql_customer_data  = '''SELECT 1 '''
customer_data = query_stage_dremio_by_arrowflight(sql_customer_data)
print(customer_data)