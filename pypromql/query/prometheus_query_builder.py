from typing import List, Callable, Tuple
from .prometheus_label import Label
from datetime import datetime

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
        # General parameters
        self.metric_name = ''
        self.labels: List[Label] = []
        self.function_name = ''
        # Time parameters
        self.range_vector_selector: Tuple[datetime, datetime] = None
        self.offset_modifier = ''
        self.time_duration = ''

    def __str__(self):
        return self.to_promql()

    def to_promql(self) -> str:
        promql_query = f'{self.metric_name}'
        if len(self.labels):
            labels_section = f'{{{",".join(str(label) for label in self.labels)}}}'
            promql_query += labels_section
        if self.range_vector_selector:
            epoch_start_time = int(self.range_vector_selector[0].timestamp())
            epoch_end_time = int(self.range_vector_selector[1].timestamp())
            promql_query = f'{promql_query}[{epoch_start_time}s:{epoch_end_time}s]'
        elif self.time_duration:
            promql_query = f'{promql_query}[{self.time_duration}]'
        if self.offset_modifier:
            promql_query = f'{promql_query} offset {self.offset_modifier} '
        if self.function_name:
            promql_query = f'{self.function_name}({promql_query})'
        return promql_query

    @builder_instance_retriever
    def offset(self, offset_modifier: str):
        self.offset_modifier = offset_modifier

    @builder_instance_retriever
    def before_time_duration(self, time_duration: str):
        self.time_duration = time_duration

    @builder_instance_retriever
    def between_datetime(self, start_time: datetime, end_time: datetime):
        self.range_vector_selector = (start_time, end_time)

    @builder_instance_retriever
    def function(self, function_name: str):
        self.function_name = function_name

    @builder_instance_retriever
    def metric(self, metric_name: str):
        self.metric_name = metric_name

    @builder_instance_retriever
    def label(self, label_name: str, label_value: str, match_operator: str = '='):
        self.labels.append(Label(name=label_name,
                                 value=label_value,
                                 match_operator=match_operator))
