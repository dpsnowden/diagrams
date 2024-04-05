# Following the C4 notation (https://c4model.com/), this diagram represents the highest level abstraction of the hfr-dac. 
# It shows the hfr-dac and how it interacts with users and select external systems

from diagrams import Diagram
from diagrams.c4 import Person, Container, Database, System, SystemBoundary, Relationship

graph_attr = {
    "splines": "spline",
}

with Diagram("[System Context] HFRNet 2.0", direction="TB", filename="hfr-dac-system-context", graph_attr=graph_attr):
    hfr_site = System(
        name="HFR Station", 
        description="An HFR Station where a SeaSonde/WERA/LERA unit is installed and operating.",
        external=True
    )
    hfr_dac = System(
        name="HFRNet",
        technology="TBD Technology summary",
        description="The complete system that aggregates raw data from many sites, and creates national products for dissemination.",
    )
    users = System(
        name = "Users or Consumers",
        description = "Any system that uses the data products created by HFRNet 2.0.",
        external = True
    )
    hfr_site >> Relationship("Provides raw data.") >> hfr_dac
    hfr_dac >> Relationship("Provides derived prodicts to.") >> users

