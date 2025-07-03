Salesforce also leverage on concept of Primary and Foregin Key is RDBMS

SalesForce has two types of relationship
  ## Lookup 
    This is basically a primary - foreign key relationship , This can either be a 1:1 or 1:many data cardinality
    Record in the Child objects is not lost,even when the Parent key is deleted

  ## MasterDetail
  In masterdetail the records in Parent and child are maintained and as long as the Parent remains.
  And the child get lost once the parent records is deleted.