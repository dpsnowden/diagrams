from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

# Node, Portal, NDBC, NCEI, NCCF, External
# List the various users of thee hfrnet and try to group them into one diagram
# Is it possible to import things defined in other files?
# Should these be modeled as systems or persons/users?  Leaning toward systems (external)

with Diagram("[User List] HFRNet v2.0", direction="LR", filename="hfrnet-users", outformat = ["png", "svg"], graph_attr=graph_attr):

    hfr_site = System(
        name="HFR Station", 
        description="An HFR Station where a SeaSonde/WERA/LERA unit is installed and operating.",
        external=True
    )
    wms_user = System(
        name="Web Visualization", 
        description = "Web site or GIS application visualizing maps of total vectors via OGC/WMS.",
        external=True
    )
    ncep_decoders = System(
        name="NCEP Data tanks", 
        description="Copies of total vectors created by NCEP decoder team and stored in NCEP data tanks.",
        external=True
    )
    uscg_sarops = System(
        name="USCG SAROPS", 
        description="USCG Search and Rescue Optimal Planning System, accessing total vectors via RPS EDS",
        external=True
    )
    rps_eds = System(
        name="RPS EDS", 
        description = "Environmental Data Server system (Tetratech/RPS), harvests from THREDDS to populate SAROPS.",
        external=True
    )
    oceansmap = System(
        name="Oceansmap",
        description = "RPS developed visualization portal used by RAs, IOOS, CO-OPS.",
        external=True
    )
    rtofs = System(
        name="RTOFS",
        description = "NOAA Real-Time Operational Forecast System (Accesses RTV via NCEP Data Tanks)",
        external=True
    )
    wcofs = System(
        name="WCOFS",
        description = "NOAA/NOS West Coast Operational Forecast System (Accesses RTV via NCEP Data Tanks)",
        external=True
    )
    stps = System(
        name="STPS",
        description = "Short Term Prediction System: UCONN developed statistical forecast (24-48hrs) based on rtv data obtained from THREDDS.",
        external=True
    )
    roms_radial_assimilation = System(
        name="ROMS Radial DA",
        description = "Generic reference to an ocean model asimilating radial data obtained via ERDDAP Servers.",
        external=True
    )
    hfr_erddap = System(
        name="Radials ERDDAP",
        description = "IOOS supported ERDDAP server with real time radial data aggregations for assimilation into models.",
        external=True
    )
    hfr_thredds = System(
        name="RTV THREDDS",
        description = "IOOS supported ERDDAP server with real time radial (and rtv) data aggregations for assimilation into models.",
        external=True
    )
    xarray = System(
        name="ARCO Cloud Data Lake",
        description = "Publicly accessible Analysis Ready Cloud Optimized data lake.",
        external=True
    )
    nwstg = System(
        name="NWS Telecom Gateway",
        description = "Central hub for brokering dissemination to operational systems.",
        external=True
    )
    awips = System(
        name="AWIPS",
        description = "Accesses GRIB files from NWSTG for usage at WFO/RFCs.",
        external=True
    ) 
    ports = System(
        name="CO-OPS PORTS",
        description = "Accesses HFR data from ? for display in PORTS web portal",
        external=True
    )
    goods = System(
        name="GNOME/GOODS",
        description = "General NOAA Operational Modeling Environment (GNOME) Online Oceanographic Data Server (GOODS)",
        external=True
    )


    # Try to finesse the graph
    hfr_site - Relationship("",color="#ffffff") - hfr_thredds - Relationship("",color="#ffffff") - hfr_erddap
    rps_eds - Relationship("",color="#ffffff") - stps - Relationship("",color="#ffffff") - uscg_sarops
    ncep_decoders - Relationship("",color="#ffffff") - wcofs - Relationship("",color="#ffffff") - rtofs
    roms_radial_assimilation - Relationship("",color="#ffffff") - oceansmap - Relationship("",color="#ffffff") - wms_user
    xarray - Relationship("",color="#ffffff") - nwstg - Relationship("",color="#ffffff") - awips
    ports - Relationship("",color="#ffffff") -  goods




