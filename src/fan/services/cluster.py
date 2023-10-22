"""Cluster Service"""

from prometheus_api_client import PrometheusConnect


class ClusterService():
    """Service for Cluster"""

    def __init__(self):
        self.prometheus = PrometheusConnect(
            url         = "http://192.168.8.40:31300",
            disable_ssl = True,
        )

    def get_maximum_temperture(self) -> float:
        """Get node temperture"""

        dataframe = self.prometheus.custom_query(
            query = 'max(node_hwmon_temp_celsius{instance=~".*"}) by (instance)',
        )

        temperture_list = [ float(data["value"][1]) for data in dataframe ]
        return max(temperture_list) 

service = ClusterService()
