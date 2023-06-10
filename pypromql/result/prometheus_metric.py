__all__ = ['Metric']


class Metric:
    def __init__(self, timestamp: float, value: float, labels: dict):
        self.timestamp = timestamp
        self.value = value
        self.labels = labels

    def __eq__(self, other):
        if isinstance(other, Metric):
            return self.timestamp == other.timestamp and self.value == other.value and self.labels == other.labels
        return False

    @classmethod
    def from_prometheus_api_metric_response(cls, prometheus_api_metric_response: dict):
        labels = prometheus_api_metric_response['metric']
        timestamp = prometheus_api_metric_response['value'][0]
        value = float(prometheus_api_metric_response['value'][1])
        return cls(timestamp=timestamp, value=value, labels=labels)
