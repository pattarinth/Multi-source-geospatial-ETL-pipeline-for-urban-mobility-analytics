# Spatial City Mobility Analysis – Berlin

## Project Overview
This project analyzes the relationship between bike-sharing stations, bike-lane infrastructure, traffic sensors, and public transport stops in central Berlin.  
The goal is to identify stations that lack safe bike-lane access and highlight priority areas for infrastructure improvements.

## Objectives
- Integrate multiple urban mobility datasets
- Identify bike stations without nearby bike-lane coverage
- Visualize infrastructure gaps in a professional map
- Generate planning insights from spatial analysis

## Data Sources
- OpenStreetMap (OSM) bike lanes and road network
- Bike-sharing station locations
- Traffic sensor dataset (Berlin)
- GTFS public transport stops

## Methods
1. Load and clean spatial datasets
2. Reproject all layers to a common coordinate system
3. Create a buffer around bike lanes
4. Perform spatial join with bike stations
5. Identify stations outside bike-lane coverage
6. Visualize results in a professional cartographic layout

## Key Metrics
- Total bike stations: 2074
- Stations within bike-lane coverage: 1665
- Stations without lane access: 409
- Coverage rate: 80.28%

## Key Insights
- A significant number of bike stations are outside direct bike-lane coverage.
- Several uncovered stations are located in dense central areas.
- Some uncovered stations are near public transport stops, indicating opportunities for multimodal improvements.

## Tools & Technologies
- Python
- GeoPandas
- Pandas
- Matplotlib
- Contextily
- Shapely

## Project Structure
spatial-city-mobility/
│
├── data/
│   ├── raw/
│   └── processed/
│
├── notebooks/
│   └── spatial_mobility_analysis.ipynb
│
├── outputs/
│   ├── berlin_mitte_portfolio_map.png
│   └── berlin_mitte_portfolio_map.pdf
│
└── README.md

Output

A professional map highlighting:

- Bike lanes

- Bike stations

- Stations without lane access

- Traffic sensors

- Public transport stops

## Data Sources

- OpenStreetMap (bike lanes and road network)  
  https://www.openstreetmap.org/

- Berlin traffic sensor dataset  
  https://daten.berlin.de/datensaetze/verkehrsdetektion-berlin

- GTFS public transport data (Berlin)  
  https://www.vbb.de/


Author

Pattarin Thunyapar
MSc Data Analytics