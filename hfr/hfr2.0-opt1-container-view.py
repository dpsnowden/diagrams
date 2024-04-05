from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

# Reimagining HFRNet  Option 1 -  External + Internal partners
# HFRNet containers
# Node, Portal, NDBC, NCEI, NCCF, External


with Diagram("[Container] HFRNet v2.0-opt1", direction="TB", filename="hfrnet-2-opt1-container-view", outformat = ["png", "svg"], graph_attr=graph_attr):
    hfr_site = System(
        name="HFR Station", 
        description="An HFR Station where a SeaSonde/WERA/LERA unit is installed and operating.",
        external=True
    )
    with SystemBoundary("HFRNet 2.0"):
        with SystemBoundary("Regional Association/Commercial Partner"):
            portal = Container(
                name = "Portal",
                technology = "rsync, Cloud native ingest tools (lambda, Kafka, IoT)",
                description="Portal aggregates raw data from observing sites, one portal",
            )
            portal_monitor = Container(
                name = "Portal Monitor",
                technology = "Monitor site health and aggregate site configurations."
            )        
        with SystemBoundary("NCCF"):
            node = Container(
                name="Node",
                technology="Python",
                description="Main internal processing of raw data into products."
            )
            node_monitor = Container(
                name="Node Monitor",
                technology="rdbms, html, ",
                description="Monitor and report system health metrics (e.g. 80/80).",
            )

        with SystemBoundary("Dissemination ????"):
            thredds_dis = Container(
                name="THREDDS",
                technology = "OPeNDAP, OGC/WMS (ncWMS), other APIs",
                description = "Service to organize and publish products (e.g RTV) to customers."
            )
            radials_erddap = Container(
                name="ERDDAP", 
                technology = "Java",
                description="ERRDAP server providing access to radial data files.",
                )
            hfrnet_website = Container(
                name="System status website",
                technology="html, OpenMaps, Javascript.",
                description="Services that provide visualizations via web APIs.",
            )

        with SystemBoundary("NDBC"):
            postprocess = Container(
                name = "Postprocess",
                technology = "Python",
                description = "Scripts to reformat files and push to TG."
            )
        
        with SystemBoundary("NCEI"):
            archive = Container(
                name="NCEI Archive", 
                technology = "",
                description="NCEI Archive for public dissemination.",
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
    gts = System(
        name="WMO GTS", 
        description="WMO Global Telecommunications System provides access to radar data for national weather servies worldwide.  GTS is accessed through the NOAA Telecommunications Gateway",
        external=True
        )

# Relationships and data flow
    hfr_site << Relationship("rsync raw data from many sites") >> portal
    portal >> Relationship("Provides aggregated raw data files.") >> node
    portal_monitor >> Relationship("Monitor data flow, site health, site configuration.") >> portal
    node_monitor >> Relationship("Monitor data flow and calculate system wide metrics.") >> node
    hfrnet_website >> Relationship("Pull metrics for visualization.") >> portal_monitor
    hfrnet_website >> Relationship("Pull metrics for visualization.") >> node_monitor
    hfrnet_website >> Relationship("Access OGC/WMS API access to visualize maps.") >> thredds_dis
    node >> Relationship("Provide monthly archive package to archive.") >> archive
    node >> Relationship("Provide files for postprocessing.") >> postprocess
    postprocess >> Relationship("Provide files to NWSTG.") >> nwstg
    node >> Relationship("Provide files to THREDDS.") >> thredds_dis
    thredds_dis << Relationship("Access OPeNDAP to populate data tanks.") << data_tanks
    nwstg >> Relationship("Provides data to.") >> gts
    node >> Relationship("FTP radials to server") >> radials_erddap

