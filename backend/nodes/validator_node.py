from ..models import SQLResponse
from ..validator import validate_sql


def validator_node(input: SQLResponse) -> SQLResponse:
    validate_sql(input.sql)
    return input
