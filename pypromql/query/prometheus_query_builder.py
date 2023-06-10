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
        self.function_name = ''

    def __str__(self):
        return self.to_promql()

    def to_promql(self) -> str:
        promql_query = f'{self.metric_name}'
        if len(self.labels):
            labels_section = f'{{{",".join(str(label) for label in self.labels)}}}'
            promql_query += labels_section
        if self.function_name:
            promql_query = f'{self.function_name}({promql_query})'
        return promql_query

    @builder_instance_retriever
    def function(self, function_name: str):
        self.function_name = function_name

    @builder_instance_retriever
    def metric(self, metric_name: str):
        self.metric_name = metric_name

    @builder_instance_retriever
    def label(self, label_name: str, label_value: str, match_operator: str = ''):
        self.labels.append(Label(name=label_name,
                                 value=label_value,
                                 match_operator=match_operator))
