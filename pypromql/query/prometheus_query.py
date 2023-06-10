
__all__ = ['Query']


class Query:
    """
        This class represent a promql query.
    """

    @classmethod
    def _get_builder(cls):
        pass

    @classmethod
    def metric(cls, metric_name: str):
        return cls._get_builder()
