from snowflake.snowpark import Session
import os


_ACCOUNT:str = os.environ.get('account')
_USER:str = os.environ.get('user')
_PASSWORD:str = os.environ.get('password')

print(_ACCOUNT)

pars ={ 
    'account':_ACCOUNT,
    'user': _USER,
    'password':_PASSWORD,
    'warehouse':'COMPUTE_WH',
    'role':"ACCOUNTADMIN",
}
session = Session.builder.configs(pars).create()

sql= """ 
  select dname, sum(sal)
  from SAMPLESUPERSTORE.PUBLIC.emp 
  join SAMPLESUPERSTORE.PUBLIC.dept on emp.deptno = dept.deptno
  where dname <> 'RESEARCH'
  group by dname
  order by dname;
"""
# emps = (session.table("EMP").select("DEPTNO", "SAL"))
# depts = (session.table("DEPT").select("DEPTNO", "DNAME"))
# q = emps.join(depts, emps.deptno == depts.deptno)

# q = q.filter(q.dname != 'RESEARCH')
# (q.select("DNAME", "SAL")
#   .group_by("DNAME")
#   .agg({"SAL": "sum"})
#   .sort("DNAME")
#   .show())

view = session.sql(sql).toPandas()
print(view)