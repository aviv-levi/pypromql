from typing import List
from pypromql.query.prometheus_query import Query
from pypromql.result.prometheus_metric import Metric
from pypromql.connection import PrometheusConnection

__all__ = ['PrometheusResult']


class PrometheusResult:
    def __init__(self, prometheus_api_response: dict):
        self.metrics: List[Metric] = []
        self.status = prometheus_api_response['status']
        if self.status == 'success':
            prometheus_api_response_data = prometheus_api_response['data']
            self.result_type = prometheus_api_response_data['resultType']
            result = prometheus_api_response_data['result']
            self._load_metrics_from_api_response(result)
        else:
            pass

    def _load_metrics_from_api_response(self, response_metrics_list: List[dict]):
        for metric in response_metrics_list:
            self.metrics.append(Metric(prometheus_api_metric_response=metric))

    @classmethod
    def from_query(cls, query: Query, prometheus_connection: PrometheusConnection):
        prometheus_api_response = prometheus_connection.execute_query(query=str(query))
        return cls(prometheus_api_response)
