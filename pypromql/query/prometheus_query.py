from pypromql.query.prometheus_query_builder import QueryBuilder

__all__ = ['Query']


class Query:
    """
        This class represent a promql query.
    """

    @classmethod
    def _get_builder(cls):
        return QueryBuilder()

    @classmethod
    def metric(cls, metric_name: str) -> QueryBuilder:
        """
            Initialize query builder and set metric name.
        :param metric_name: string table name.
        :return: QueryBuilder
        """
        return cls._get_builder().metric(metric_name=metric_name)
