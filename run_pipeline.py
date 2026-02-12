import subprocess
import sys

def run_script(script_name):
    print(f"Running {script_name}...")
    result = subprocess.run(
        [sys.executable, script_name],
        capture_output=True,
        text=True
    )
    
    if result.returncode != 0:
        print(f"Error in {script_name}")
        print(result.stderr)
    else:
        print(f"{script_name} completed successfully.")
        print(result.stdout)


if __name__ == "__main__":
    run_script("etl_roads.py")
    run_script("etl_bike_stations.py")
