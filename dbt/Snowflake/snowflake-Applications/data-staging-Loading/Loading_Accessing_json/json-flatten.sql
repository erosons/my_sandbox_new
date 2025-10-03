[
  {"employee":'John',
  "managers": [
    {"name": "Bill","years":[2021,2022]},
    {"name": "Linda","years":[2020]}
    ]
  },
  {
   "employee":'Mary',
   "managers": [
    {"name": "Bill","years":[2022,2023]}
    ]
  }
]
--Flatten and Load into a Transient Table
CREATE TRANSIENT TABLE json(name string , v variant)
AS
SELECT 'John',($${"managers": [
    {"name": "Bill","years":[2021,2022]},
    {"name": "Linda","years":[2020]}
    ]
  }$$)
  UNION
  SELECT 'Mary',($${"managers": [
    {"name": "Bill","years":[2022,2023]}
    ]
  }$$);


{# Flatten in SQL #}
select json.name::string
,m.value:name
,y.value::Numeric(5,0)
FROM json ,
Table(flatten(input => json.v, path =>'managers')) m,
Table(flatten(input => m.value, path =>'years')) y;

{# Flatten in SQL #}
select json.name::string
,m.value:name
,y.value::Numeric(5,0)
FROM json ,
lateral latten(input => json.v, path =>'managers',outer=true) m,
lateral flatten(input => m.value, path =>'years',outer=true) y;