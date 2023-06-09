import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


class PrometheusConnection:
    """
        This class responsible connecting with Prometheus server.
    """

    def __init__(self, prometheus_base_url: str = 'http://localhost:9090/', connection_retries=5, backoff_factor=0.5):
        """
        :param prometheus_base_url: Prometheus server base URL.
        :param connection_retries: max connection retries.
        :param backoff_factor: The exponential factor for increasing delay between retries.
            Each subsequent retry delay is calculated as backoff_factor * previous_delay.
        """
        self.prometheus_base_url = prometheus_base_url
        self.session = requests.Session()
        self.retry_strategy = Retry(
            total=connection_retries,
            backoff_factor=backoff_factor,
            status_forcelist=[500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=self.retry_strategy)
        self.session.mount('http://', adapter)
        self.session.mount('https://', adapter)
