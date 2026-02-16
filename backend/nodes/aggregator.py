from ..models import AggregationRequest, AggregationResult

def aggregation_node(input: AggregationRequest) -> AggregationResult:
    total = sum(row[input.column] for row in input.rows)

    return AggregationResult(
        column=input.column,
        sum=total
    )
