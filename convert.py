import geopandas as gpd

# Cargar shapefiles
gdf = gpd.read_file('./data/PROTECTED_AREAS_V4.shp')
gdf_roads = gpd.read_file('./data/caminos_AP_V4.shp')
gdf_trails = gpd.read_file('./data/senderos_AP.shp')
gdf_water = gpd.read_file('./data/puntos_agua.shp')
gdf_heliports = gpd.read_file('./data/heliports.shp')
gdf_uso_suelo = gpd.read_file('./data/Uso_suelos_AP_V4.shp')

# convertir en GPKG
gdf.to_file('./data/PROTECTED_AREAS_V4.gpkg', driver='GPKG')
gdf_roads.to_file('./data/caminos_AP_V4.gpkg', driver='GPKG')
gdf_trails.to_file('./data/senderos_AP.gpkg', driver='GPKG')
gdf_water.to_file('./data/puntos_agua.gpkg', driver='GPKG')
gdf_heliports.to_file('./data/heliports.gpkg', driver='GPKG')
gdf_uso_suelo.to_file('./data/Uso_suelos_AP_V4.gpkg', driver='GPKG')
