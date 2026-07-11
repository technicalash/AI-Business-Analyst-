import pandas as pd


def _build_statistics(plot, statistics):

    return {
        "title": plot["title"],
        "type": plot["type"],
        "reason": plot.get("reason", ""),
        "statistics": statistics
    }
    

def _apply_value_labels(values, plot):

    if "value_labels" not in plot:
        return values

    mapping = plot["value_labels"]

    labeled = {}

    for key, value in values.items():

        labeled[
            mapping.get(str(key), str(key))
        ] = value

    return labeled


def generate_plot_statistics(
    df: pd.DataFrame,
    visualization_plan: dict
):

    statistics = []

    for plot in visualization_plan["plots"]:

        plot_type = plot["type"]

        if plot_type == "bar":
            statistics.append(_bar_statistics(df, plot))

        elif plot_type == "histogram":
            statistics.append(_histogram_statistics(df, plot))

        elif plot_type == "scatter":
            statistics.append(_scatter_statistics(df, plot))

        elif plot_type == "boxplot":
            statistics.append(_boxplot_statistics(df, plot))

        elif plot_type == "line":
            statistics.append(_line_statistics(df, plot))

        elif plot_type == "pie":
            statistics.append(_pie_statistics(df, plot))

        elif plot_type == "heatmap":
            statistics.append(_heatmap_statistics(df, plot))

    return statistics

def _histogram_statistics(df, plot):

    column = plot["x"]

    data = df[column].dropna()

    statistics = {
    "column": column,
    "count": int(data.count()),
    "mean": round(float(data.mean()),3),
    "median": round(float(data.median()),3),
    "std": round(float(data.std()),3),
    "min": round(float(data.min()),3),
    "max": round(float(data.max()),3)
    }
    return _build_statistics(
    plot,
    statistics 
    )

    
def _bar_statistics(df, plot):

    x = plot["x"]

    aggregation = plot["aggregation"]

    if aggregation == "count":

        stats = (
            df[x]
            .value_counts()
            .to_dict()
        )
        

    else:

        y = plot["y"]

        stats = (
            df.groupby(x)[y]
            .agg(aggregation)
            .to_dict()
        )
    stats = _apply_value_labels(
    stats,
    plot
)

    return _build_statistics(plot, stats)
    
def _scatter_statistics(df, plot):

    x = plot["x"]
    y = plot["y"]

    correlation = df[x].corr(df[y])

    return _build_statistics(
    plot,
    {
        "x": x,
        "y": y,
        "correlation": round(float(correlation), 3)
    }
)
    
def _boxplot_statistics(df, plot):

    y = plot["y"]

    data = df[y].dropna()

    statistics = {
        "count": int(data.count()),
        "min": round(float(data.min()), 3),
        "q1": round(float(data.quantile(0.25)), 3),
        "median": round(float(data.median()), 3),
        "q3": round(float(data.quantile(0.75)), 3),
        "max": round(float(data.max()), 3),
        "iqr": round(float(data.quantile(0.75) - data.quantile(0.25)), 3)
    }

    if "x" in plot:

        x = plot["x"]

        mapping = plot.get("value_labels", {})

        grouped_statistics = {}

        grouped = df.groupby(x)[y]

        for group_name, values in grouped:

            label = mapping.get(str(group_name), str(group_name))

            grouped_statistics[label] = {
                "count": int(values.count()),
                "mean": round(float(values.mean()), 3),
                "median": round(float(values.median()), 3),
                "min": round(float(values.min()), 3),
                "max": round(float(values.max()), 3)
            }

        statistics["group_statistics"] = grouped_statistics

    return _build_statistics(
        plot,
        statistics
    )
    
def _pie_statistics(df, plot):

    x = plot["x"]

    counts = df[x].value_counts()

    percentages = (
        counts / counts.sum() * 100
    ).round(2)

    counts = _apply_value_labels(
    counts.to_dict(),
    plot
    )
    percentages = _apply_value_labels(
    percentages.to_dict(),
    plot
    )
    
    return _build_statistics(
    plot,
    {
        "counts": counts,
        "percentages": percentages
    }
)
    
def _line_statistics(df, plot):

    x = plot["x"]
    y = plot["y"]

    aggregation = plot["aggregation"]

    grouped = (
        df.groupby(x)[y]
        .agg(aggregation)
        .sort_index()
    )

    grouped = grouped.dropna()

    if grouped.empty:
        return _build_statistics(
            plot,
            {
                "message": "No data available."
            }
        )

    start_value = float(grouped.iloc[0])
    end_value = float(grouped.iloc[-1])

    if start_value != 0:
        percent_change = (
            (end_value - start_value)
            / start_value
        ) * 100
    else:
        percent_change = 0

    if percent_change > 5:
        trend = "Increasing"

    elif percent_change < -5:
        trend = "Decreasing"

    else:
        trend = "Stable"

    statistics = {
        "x_axis": x,
        "y_axis": y,
        "count": int(len(grouped)),
        "start_value": round(start_value, 3),
        "end_value": round(end_value, 3),
        "min": round(float(grouped.min()), 3),
        "max": round(float(grouped.max()), 3),
        "mean": round(float(grouped.mean()), 3),
        "median": round(float(grouped.median()), 3),
        "percent_change": round(percent_change, 2),
        "trend": trend
    }

    return _build_statistics(
        plot,
        statistics
    )
    
def _heatmap_statistics(df, plot):

    if "columns" in plot:

        corr = (
            df[plot["columns"]]
            .corr()
        )

    else:

        corr = (
            df.select_dtypes(include="number")
            .corr()
        )

    statistics = {}
    for i, col1 in enumerate(corr.columns):
        for col2 in corr.columns[i + 1:]:
            statistics[f"{col1} vs {col2}"] = round(
                float(corr.loc[col1, col2]),
                3
                )
    return _build_statistics(
        plot,
        statistics
        )