import subprocess

print("Running road ETL...")
subprocess.run(["python", "scripts/etl_roads.py"], check=True)

print("Running bike station ETL...")
subprocess.run(["python", "scripts/etl_bike_stations.py"], check=True)

print("Pipeline completed successfully.")
