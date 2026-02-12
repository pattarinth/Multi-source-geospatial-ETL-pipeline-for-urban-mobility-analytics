import geopandas as gpd
from sqlalchemy import create_engine

# Database connection
engine = create_engine(
    "postgresql://postgres:chob2chob@localhost:5432/city_mobility"
)

# Load bike station data
gdf = gpd.read_file(
    "data/raw/nextbike.geojson"
)

# Ensure correct CRS
gdf = gdf.to_crs(epsg=4326)

# Save to PostGIS
gdf.to_postgis(
    name="bike_stations",
    con=engine,
    if_exists="replace",
    index=False
)

print("Bike station data loaded successfully.")
