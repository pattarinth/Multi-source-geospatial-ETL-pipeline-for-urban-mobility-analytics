import geopandas as gpd
from sqlalchemy import create_engine

# Database connection
engine = create_engine(
    "postgresql://postgres:YOUR_PASSWORD@localhost:5432/city_mobility"
)

# Load shapefile
gdf = gpd.read_file("data/raw/roads.shp")

# Convert to WGS84
gdf = gdf.to_crs(epsg=4326)

# Save to PostGIS
gdf.to_postgis(
    name="roads",
    con=engine,
    if_exists="replace",
    index=False
)

print("Road data loaded successfully.")

