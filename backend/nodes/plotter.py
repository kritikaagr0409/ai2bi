from ..models import PlotRequest, PlotResult


def plot_node(input: PlotRequest) -> PlotResult:
    return PlotResult(
        x_column=input.x_column,
        y_column=input.y_column,
        chart_type="bar"
    )
