from pathlib import Path
import geopandas as gpd
from sqlalchemy import create_engine

BASE_PATH = Path("data/raw")
STATIONS_FILE = BASE_PATH / "nextbike.geojson"
DB_URI = "postgresql+psycopg2://postgres:chob2chob@localhost:5432/spatial_etl"

def extract():
    gdf = gpd.read_file(STATIONS_FILE)
    return gdf

def transform(gdf):
    gdf = gdf.rename(columns={
        "id": "station_id",
        "name": "station_name",
        "lat": "latitude",
        "lng": "longitude"
    })
    if "geometry" not in gdf.columns:
        gdf["geometry"] = gpd.points_from_xy(gdf.longitude, gdf.latitude)
        gdf = gdf.set_geometry("geometry", crs="EPSG:4326")
    return gdf

def load(gdf):
    engine = create_engine(DB_URI)
    gdf.to_postgis("bike_stations", engine, if_exists="replace", index=False)

if __name__ == "__main__":
    gdf = extract()
    gdf = transform(gdf)
    load(gdf)
    print("Bike stations loaded to PostGIS!")

