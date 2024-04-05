from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

# Existing HFRNet containers
# Node, Portal, NDBC, NCEI, NCCF, External


with Diagram("[Container] HFRNet v1.0", direction="TB", filename="hfrnet-1-container-view", outformat = ["png", "svg"], graph_attr=graph_attr):
    hfr_site = Person(
        name="HFR Station", description="An HFR Station where a SeaSonde/WERA/LERA unit is installed and operating."
    )
    with SystemBoundary("HFRNet 1.0"):
        with SystemBoundary("Academic partners"):
            portal = Container(
                name = "Portal",
                technology = "rsync, Python, Shell Scripts",
                description="Portals aggregate raw data from observing sites. 6-7 Portals exist.",
            )
        
        with SystemBoundary("SIO"):
            portal_monitor = Container(
                name = "Portal Monitor",
                technology = "Monitor site health and aggregate site configurations."
            )
            node = Container(
                name="Node",
                technology="Matlab, Python, Shell Scripts",
                description="Main internal processing of raw data into products."
            )
            node_monitor = Container(
                name="Node Monitor",
                technology="rdbms, html, ",
                description="Monitor and report system health metrics (e.g. 80/80).",
            )
            hfrnet_website = Container(
                name="System status website",
                technology="html, OpenMaps, Javascript.",
                description="Services that provide visualizations via web APIs.",
            )
            thredds_sio = Container(
                name="THREDDS",
                technology = "OPeNDAP, OGC/WMS (ncWMS), other APIs",
                description = "Service to organize and publish products (e.g RTV) to customers."
            )
        with SystemBoundary("NDBC"):
            node_ndbc = Container(
                name="Operational Node",
                technology="Matlab, Python, Shell Scripts",
                description="Main internal processing of raw data into products."
            )
            thredds_ndbc = Container(
                name="THREDDS",
                technology = "OPeNDAP, OGC/WMS (ncWMS), other APIs",
                description = "Service to organize and publish products (e.g RTV) to customers, including NOAA Operations."
            )
            postprocess = Container(
                name = "Postprocess",
                technology = "Python",
                description = "Scripts to reformat files and push to TG and archive."
            )
            


# External Systems
#    archive = System(name="NCEI Archive", description="NCEI Archive for public dissemination.",external=True)
    nwstg = System(
        name="NWS Telecommunications Gateway",
        technology="FS???",
        description="NWS managed gateway to the WMO GTS for international dissemination.",
        external=True
    )
    data_tanks = System(name="NCEP Data Tank", 
        technology ="technology",
        description="Datastore available to the NOAA Operational compute system WCOSS2.", 
        external=True
    )
    archive = System(
        name="NCEI Archive", 
        description="NCEI Archive for public dissemination.",
        external=True
    )
    gts = System(
        name="WMO GTS", 
        description="WMO Global Telecommunications System provides access to radar data for national weather servies worldwide.  GTS is accessed through the NOAA Telecommunications Gateway",
        external=True
        )
    radials_erddap = System(
        name="ERDDAP", 
        description="ERRDAP server providing access to radial data files.",
        external=True
        )

# Relationships and data flow
    hfr_site << Relationship("rsync raw data from many sites") >> portal
    portal >> Relationship("Provides aggregated raw data files.") >> node
    portal >> Relationship("Providess aggregated raw data files.") >> node_ndbc
    portal_monitor >> Relationship("Monitor data flow, site health, site configuration.") >> portal
    node_monitor >> Relationship("Monitor data flow and calculate system wide metrics.") >> node
    hfrnet_website >> Relationship("Pull metrics for visualization.") >> portal_monitor
    hfrnet_website >> Relationship("Pull metrics for visualization.") >> node_monitor
    hfrnet_website >> Relationship("Access OGC/WMS API access to visualize maps.") >> thredds_sio
    node_ndbc >> Relationship("Provide monthly archive package to archive.") >> archive
    node_ndbc >> Relationship("???") >> postprocess
    thredds_ndbc >> Relationship("???") >> postprocess
    postprocess >> Relationship("Provide files to NWSTG.") >> nwstg
    node_ndbc >> Relationship("Provide files to THREDDS.") >> thredds_ndbc
    thredds_ndbc << Relationship("Access OPeNDAP to populate data tanks.") << data_tanks
    nwstg >> Relationship("Provides data to.") >> gts
    node >> Relationship("FTP radials to server") >> radials_erddap

