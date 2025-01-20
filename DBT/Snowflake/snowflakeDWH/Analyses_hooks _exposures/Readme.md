# if you don't intend to materialize anything but wabt to analyze the did data
>>> Run dbt analayse

# Hooks:
 These are SQL that run are executed at predefined time
 Hooks can be configured on the
    - Projects
    Subfolder
    Model level

# Types:
  - On_run_start   -> Exceuted at the start of dbt(run,speed,snapshpt)
  - on_run_end     -> Executed at the end of dbt ""
  - prehook        -> before they are built
  - post hook      -> They are built after

# Set a post hook in uour dbt.poject,yaml
    In dbt (data build tool), post-hooks are custom SQL statements that are executed after your model has been materialized. Post-hooks are a powerful feature that allow you to perform additional operations such as data cleanup, indexing, permissions setting, or any other database-specific tasks that should be executed after your model is updated.
