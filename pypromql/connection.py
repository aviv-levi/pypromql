import json
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from urllib.parse import quote

__all__ = ['PrometheusConnection']


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

    def execute_query(self, query: str, to_url_decode: bool = True):
        """
            Execute a PromQL query by sending an HTTP GET request to Prometheus.

        :param query: to execute promql query.
        :param to_url_decode: enable url encoding?
        :raises: requests.exceptions.RequestException: If an error occurs during
        the HTTP request (e.g., network error, timeout). requests.exceptions.HTTPError: If a non-successful HTTP
        response status code is returned.
        :return: dict or None: The content of the HTTP response if the request is successful,
         or None if an error occurs.
        """
        execute_query_url = f'{self.prometheus_base_url}/api/v1/query?query={query}'
        if to_url_decode:
            execute_query_url = quote(execute_query_url)
        response = self.session.get(execute_query_url)
        response.raise_for_status()
        response_as_dict = json.loads(response.content.decode('utf-8'))
        return response_as_dict
