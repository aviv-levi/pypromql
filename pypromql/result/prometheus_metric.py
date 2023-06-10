class Metric:
    def __init__(self, prometheus_api_metric_response: dict):
        self.labels = prometheus_api_metric_response['metric']
        self.timestamp = prometheus_api_metric_response['value'][0]
        self.value = prometheus_api_metric_response['value'][1]
