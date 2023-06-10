from typing import Set
from .prometheus_label import Label

__all__ = ['Query']


class Query:
    """
        This class represent a promql query.
    """

    def __init__(self, metric_name: str):
        """
        :param metric_name:  The name of the metric for the query.
        """
        self.metric_name = metric_name
        self.labels: Set[Label] = set()

    def __str__(self):
        return self.to_promql_query()

    def to_promql_query(self):
        pass
