from pathlib import Path
import geopandas as gpd
from sqlalchemy import create_engine

# ---- Paths ----
BASE_PATH = Path("data/raw")
ROAD_FILE = BASE_PATH / "gis_osm_roads_free_1.shp"  # replace with your shapefile name

# ---- Database connection ----
# Change username/password/host/dbname if needed
DB_USER = "postgres"
DB_PASSWORD = "chob2chob"  # your password
DB_HOST = "localhost"
DB_PORT = "5432"
DB_NAME = "spatial_etl"

engine = create_engine(f"postgresql+psycopg2://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}")

# ---- Load and write to PostGIS ----
print("Loading road shapefile...")
gdf = gpd.read_file(ROAD_FILE)

print("Writing to PostGIS...")
gdf.to_postgis("roads", engine, if_exists="replace", index=False)

print("Done! Table 'roads' should now exist in your database.")
