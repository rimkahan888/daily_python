import duckdb

# Store the file path in a Python variable
file_path = "/path/to/data.csv"

# Connect to DuckDB and query the file
con = duckdb.connect()
result = con.execute(f"SELECT * FROM '{file_path}'").fetchall()

# Print the result
print(result)