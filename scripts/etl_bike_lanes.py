from pathlib import Path
import geopandas as gpd
from sqlalchemy import create_engine

# ----- CONFIG -----
BASE_PATH = Path("data/raw")
GEOJSON_PATH = BASE_PATH / "bike_lanes.geojson"

DB_USER = "postgres"
DB_PASS = "chob2chob"  # Use environment variables in production
DB_NAME = "spatial_etl"
DB_HOST = "localhost"
DB_PORT = "5432"

# ----- LOAD -----
print("Loading bike lane data...")
gdf = gpd.read_file(GEOJSON_PATH)
print(f"Loaded {len(gdf)} bike lane features.")

# ----- CLEAN / TRANSFORM -----
# Keep only actual cycleway or path geometries
if "highway" in gdf.columns:
    gdf = gdf[gdf["highway"].isin(["cycleway", "path"])]
    print(f"Filtered {len(gdf)} cycleway features.")
else:
    print("Warning: 'highway' column not found; loading all features.")

# Reproject to WGS84 for PostGIS
gdf = gdf.to_crs(epsg=4326)

# ----- LOAD TO POSTGIS -----
engine = create_engine(f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

print("Writing to PostGIS table 'bike_lanes'...")
gdf.to_postgis("bike_lanes", engine, if_exists="replace", index=False)
print("Bike lane ETL completed successfully.")
