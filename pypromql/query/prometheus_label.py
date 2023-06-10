from dataclasses import dataclass


@dataclass
class Label:
    """
        This class represents a label used in metric queries.
    """
    name: str
    value: str
    match_operator: str = "="

    def __str__(self) -> str:
        """
            Generate a string representation of the label in the format ''' name="Aviv" '''
        :return: string representation of the label.
        """
        return f'{self.name}{self.match_operator}"{self.value}"'
