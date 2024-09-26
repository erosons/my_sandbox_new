import glob  #https://www.geeksforgeeks.org/how-to-use-glob-function-to-find-files-recursively-in-python/
import importlib.util
import os
import pytest
from airflow.models import DAG


dag_Path= os.path.join(os.path.dirname(__file__),"..","..","dags/**/*.py")

dag_files=glob.glob(dag_Path,recursive=True)

dag_file='..../dag_cycle.py'

@pytest.mark.parametrize("dag_file",dag_files)
def test_dag_integrity(dagfile):
    module_name,_=os.path.splitext(dagfile)
    module_path= os.path.join(dag_Path,dagfile)
    mod_spec=importlib.util.spec_from_file_location(module_name,module_path)
    module=importlib.util.module_from_spec(mod_spec)
    mod_spec.loader.exec_module(module)

    dag_objects=[var for var in vars(module).values if isinstance(vars , DAG)]

    assert dag_objects

    for dag in dag_objects:
        dag.test_cycle()

