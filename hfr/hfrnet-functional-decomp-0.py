from diagrams import Cluster, Diagram
from diagrams.programming import flowchart as fc

# THIS ISN'T GOING TO WORK, GO BACK TO C4 FOR STRUCTURE DIAGRAMS

graph_attr = {
    "splines": "spline",
}

# Trying to emulate the functional decomposition diagram using flowcharts with Clusters
# HFR Net
#   External - HFR Sites
#   Aggregate Observations
#   Monitor System

with Diagram("HFRNet System - Functional Decomposition", direction="TB", filename="hfrnet-functional-decomp", graph_attr=graph_attr):
    #
    start = fc.StartEnd("HFRNet 2.0")

    with Cluster("Collect Observations"):
        collect_obs = [fc.Action("Range Series"),
                       fc.Action("Radials")]
        
    with Cluster("Aggregate Observations"):
        aggregate_obs = [fc.Action("Range Series Aggregator"),
                         fc.Action("Radials Aggregator"),
                         fc.Action("Waves Aggregator")]
        
    with Cluster("Monitor System"):
        system_monitor = [fc.Action("one"),
                          fc.Action("two")]
        
    start - collect_obs
    start - aggregate_obs
    start - system_monitor
