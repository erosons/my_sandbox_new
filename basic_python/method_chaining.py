class SparkDataFrameWriter:
    def __init__(self):
        self.range_value = None
        self.format_value = None
        self.options_value = {}
        self.table_name = None

    def range(self, value):
        self.range_value = value
        return self

    def format(self, fmt):
        self.format_value = fmt
        return self

    def options(self, **kwargs):
        self.options_value.update(kwargs)
        return self

    def option(self, key, value):
        self.options_value[key] = value
        return self

    def save(self):
        # Placeholder for the actual save logic
        print(f"Range: {self.range_value}")
        print(f"Format: {self.format_value}")
        print(f"Options: {self.options_value}")
        print(f"Table: {self.table_name}")
        # Here you would have the actual save logic using Spark

    def to_table(self, table_name):
        self.table_name = table_name
        return self

# Example usage:
writer = SparkDataFrameWriter()
writer.range(5)\
    .format("snowflake")\
    .options(
    sfURL="https://my_snowflake_account.snowflakecomputing.com",
    sfUser="my_user",
    sfPassword="my_password",
    sfDatabase="my_database",
    sfSchema="my_schema",
    sfWarehouse="my_warehouse",
)\
.option("dbtable", "table_name").save()
