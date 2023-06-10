from typing import List
from pypromql.query.prometheus_query import Query, QueryBuilder
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
            self.error_type = prometheus_api_response['errorType']
            self.error = prometheus_api_response['error']
        if 'warnings' in prometheus_api_response:
            self.warnings = prometheus_api_response['warnings']

    def _load_metrics_from_api_response(self, response_metrics_list: List[dict]):
        for metric in response_metrics_list:
            self.metrics.append(Metric.from_prometheus_api_metric_response(prometheus_api_metric_response=metric))

    @classmethod
    def from_query_builder(cls, query_builder: QueryBuilder, prometheus_connection: PrometheusConnection):
        prometheus_api_response = prometheus_connection.execute_query(query=query_builder.to_promql())
        return cls(prometheus_api_response)
