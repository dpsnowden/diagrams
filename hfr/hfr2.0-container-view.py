from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

# Existing HFRNet containers
# Node, Portal, NDBC, NCEI, NCCF, External


with Diagram("[Container] HFRNet v1.0", direction="LR", filename="hfrnet-1-container-view", outformat = ["png", "svg"], graph_attr=graph_attr):
    hfr_site = Person(
        name="HFR Station", description="An HFR Station where a SeaSonde/WERA/LERA unit is installed and operating."
    )
    with SystemBoundary("HFRNet 1.0"):
        with SystemBoundary("External to NOAA"):
            portal = Container(
                name="Portal",
                technology="rsync, scripts, Python",
                description="Portal aggregates raw data from observing sites. 6-7 Portals exist.",
            )
#            portal_monitor = Container(
#                name = "Portal Monitor",
#                technology = "Monitor site health and aggregate site configurations."
#            )
        
        with SystemBoundary("NCCF"):
            node = Container(
                name="Node",
                technology="???",
                description="Main internal processing of raw data into products."
            )
#            node_monitor = Container(
#                name="Node Monitor",
#                technology="???tech",
#                description="Monitor and report system health metrics (e.g. 80/80).",
#            )

        with SystemBoundary("NCEI"):
            visualization = Container(
                name="Visualization Service",
                technology="OGC/Image",
                description="Services that provide visualizations via web APIs.",
            )
            dissemination = Container(
                name="Dissemination Service",
                technology = "THREDDS, S3 Buckets, other APIs?",
                description = "Service to organize and publish products to customers."
            )
            archive = Container(name="NCEI Archive", description="NCEI Archive for public dissemination.")

# External Systems
#    archive = System(name="NCEI Archive", description="NCEI Archive for public dissemination.",external=True)
    nwstg = System(
            name="NWS Telecommunications Gateway",
            technology="FS???",
            description="NWS managed gateway to the WMO GTS for international dissemination.",
            external=True
        )

# Relationships and data flow
    hfr_site << Relationship("rsync raw data from many sites") << portal
    portal >> Relationship("Calculate derived products (e.g. Total Vector)") >> node
#    portal_monitor >> Relationship("Monitor data flow, site health, site configuration.") >> portal
#    node_monitor >> Relationship("Monitor data flow and calculate system wide metrics.") >> node
#    visualization >> Relationship("Pull metrics for visualization.") >> node_monitor
    node >> Relationship("Publish files for dissemination.") >> dissemination
    dissemination >> Relationship("Provide files for visualization.") >> visualization
    node >> Relationship("Provide files to archive.") >> archive
    node >> Relationship("Provide files to NWSTG.") >> nwstg


    data_tanks = Database(name="NCEP Data Tank", 
                          technology ="technology",
                          description="Datastore available to the NOAA Operational compute system WCOSS2.", 
                          )
    gts = System(name="WMO GTS", description="WMO Global Telecommunications System provides access to radar data for national weather servies worldwide.  GTS is accessed through the NOAA Telecommunications Gateway",external=True)
    thredds = System(name="THREDDS", description="THREDDS Server providing public web based access to HFR products using OPeNDAP",external=True)
