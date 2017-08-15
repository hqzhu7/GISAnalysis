import arcpy

# Check licenses
arcpy.CheckOutExtension("spatial")

# Local variables (need to be changed according to different computers)
whole_csv = "D:\\gisproject\\data_whole\\whole.csv"
template_lyr = "D:\\gisproject\\template.lyr"
whole_Layer1 = "whole_Layer1"
wholem_lyr = "D:\\gisproject\\wholem.lyr"
pointden = "D:\\gisproject\\pointden"
MakeRas_pointde1 = "MakeRas_pointde1"
pointde_lyr = "D:\\gisproject\\pointde.lyr"

# Process: Make XY Event Layer
arcpy.MakeXYEventLayer_management(whole_csv, "longitude", "latitude", whole_Layer1, "", "")

# Process: Save To Layer File
arcpy.SaveToLayerFile_management(whole_Layer1, wholem_lyr, "ABSOLUTE", "CURRENT")

# Process: Point Density
arcpy.gp.PointDensity_sa(wholem_lyr, "NONE", pointden, ".0016519576", "Circle 1.37663133333334E-02 MAP", "SQUARE_MAP_UNITS")

# Process: Make Raster Layer
arcpy.MakeRasterLayer_management(pointden, MakeRas_pointde1, "", "-74.253530914411 40.498270085589 -73.700125118411 40.912911443189", "")

# Process: Save To Layer File (2)
arcpy.SaveToLayerFile_management(MakeRas_pointde1, pointde_lyr, "ABSOLUTE", "CURRENT")

# Process: Apply Symbology From Layer
arcpy.ApplySymbologyFromLayer_management(pointde_lyr, template_lyr)
