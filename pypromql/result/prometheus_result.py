from pypromql.query.prometheus_query import Query
from pypromql.connection import PrometheusConnection

__all__ = ['PrometheusResult']


class PrometheusResult:
    def __init__(self, prometheus_api_response: dict):
        status = prometheus_api_response['status']
        if status == 'success':
            result = prometheus_api_response['data']
        else:
            pass

    @classmethod
    def from_query(cls, query: Query, prometheus_connection: PrometheusConnection):
        prometheus_api_response = prometheus_connection.execute_query(query=str(query))
        return cls(prometheus_api_response)