{# NOTE always load Json into a variant datatype #}

CREATE temporary TABLE json_holder (v variant)

CREATE FILE FORMAT JSONfileformat
  TYPE = 'JSON'
  {# COMPRESSION = 'GZIP'
  STRIP_OUTER_ARRAY = TRUE
  IGNORE_UTF8_ERRORS = FALSE; #}

{# Load into table  #}
COPY INTO json_holder from @mystage
files = ('dept.json')
file_format = (format_name ='JSONfileformat')
force = true

RETURN => 

{
  "data": [
    {
      "DEPTNO": 10,
      "DNAME": "ACCOUNTING",
      "LOC": "NEW YORK"
    },
    {
      "DEPTNO": 20,
      "DNAME": "RESEARCH",
      "LOC": "DALLAS"
    },
    {
      "DEPTNO": 30,
      "DNAME": "SALES",
      "LOC": "CHICAGO"
    },
    {
      "DEPTNO": 40,
      "DNAME": "OPERATIONS",
      "LOC": "BOSTON"
    }
  ]
}

