from backend.models import PlotRequest, PlotResult


def generate_visualization(request: PlotRequest) -> PlotResult:
    if request.x_column and request.y_column:
        return PlotResult(
            x_column=request.x_column,
            y_column=request.y_column,
            chart_type="bar"
        )

    return PlotResult(
        x_column="",
        y_column="",
        chart_type="table"
    )
