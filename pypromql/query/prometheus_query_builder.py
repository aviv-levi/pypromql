from typing import List, Callable
from .prometheus_label import Label

__all__ = ['QueryBuilder']


def builder_instance_retriever(func: Callable) -> Callable:
    def retrieve_result(self, *args, **kwargs):
        func(self, *args, **kwargs)
        return self
    return retrieve_result


class QueryBuilder:
    """
        This class responsible building promql queries using Builder design pattern.
    """

    def __init__(self):
        self.metric_name = ''
        self.labels: List[Label] = []

    @builder_instance_retriever
    def metric(self, metric_name: str):
        self.metric_name = metric_name

    @builder_instance_retriever
    def label(self, label_name: str, label_value: str, match_operator: str = ''):
        self.labels.append(Label(name=label_name,
                                 value=label_value,
                                 match_operator=match_operator))