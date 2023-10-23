"""Cluster Service"""

from prometheus_api_client import PrometheusConnect

# Configurations
TARGET_TEMPERTURE  = 40     # [C] Target temperture 


class ClusterService():
    """Service for Cluster"""

    def __init__(self):
        self.prometheus = PrometheusConnect(
            url         = "http://192.168.8.40:31300",
            disable_ssl = True,
        )

        self.target_temperture = TARGET_TEMPERTURE


    async def get_target_temperture(self):
        """Returns the target temperture"""
        return self.target_temperture


    async def set_target_temperture(self, temperture: float):
        """Sets the target temperture"""
        self.target_temperture = temperture
        return { "target_temperture": self.target_temperture }


    def prometheus_maximum_temperture(self) -> float:
        """Get node temperture"""

        dataframe = self.prometheus.custom_query(
            query = 'max(node_hwmon_temp_celsius{instance=~".*"}) by (instance)',
        )

        temperture_list = [ float(data["value"][1]) for data in dataframe ]
        return max(temperture_list) 


    async def get_maximum_temperture(self) -> float:
        """Get node temperture"""

        max_temp = self.prometheus_maximum_temperture()
        print(f"Maximum temperture: {max_temp}")
        return max_temp 

service = ClusterService()
