 {# Inferring schema for Json  #}
  SELECT * FROM
  FROM TABLE(
    infer_schema(
        location => '@mystage',
        files => 'dept.json',
        file_format => 'JSONfileformat'
     ) )


{# Loading JSON string into Table (Not the datatype has to be Variant) #}

Create table abc(v  variant)


SELECT * FROM abc

set json = $$
{
  myobj: {
    PROP1: {
      prop2: {
        name2: { array1: ['a', 'b', 'c'] }
      }
    }
  }
}
$$;

insert into abc select parse_json($json);

SELECT v:myobj:PROP1:prop2:name2:array1[0]::string
from abc