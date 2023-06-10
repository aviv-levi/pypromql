from pypromql.query.prometheus_query_builder import QueryBuilder
from datetime import datetime

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


if __name__ == '__main__':
    print(Query.metric('scrape_duration_seconds')
          .label("instance", "localhost:9090")
          .label("job", "prometheus")
          .between_datetime(datetime(2023, 6, 10, 14, 10, 0), datetime(2023, 6, 10, 14, 12, 0)))
