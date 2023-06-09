from typing import List


class PrometheusConnection:
    """
        This class responsible connecting with Prometheus server.
    """
    def __init__(self, prometheus_base_url: str = 'http://localhost:9090/'):
        self.prometheus_base_url = prometheus_base_url
