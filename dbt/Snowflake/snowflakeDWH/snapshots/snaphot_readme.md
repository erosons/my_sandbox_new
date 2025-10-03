SCD->0  -> Never Changes
SCD->1 -> Overwrites
SCD->2 -> historical speed issues
SCD->3 -> Additional Attributes, for what is current 

How DBt handles type-2 SCD

# Snaphot Strategies
  - Timestamp strategies: keeping your data at 1st NF and an updated_at field is defined on the source
     the source model. These columns are used for determing changes
  - Check : Any changes in a set of columns will be picked up as an update