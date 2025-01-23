import random
from datetime import datetime
import plotly.graph_objects as go
from vizblend.create_ppt_report import CreatePowerPoint


def generate_time_series_data(start_date, end_date, categories):
    start_year = start_date.year
    end_year = end_date.year

    years = list(range(start_year, end_year + 1))
    data = {
        category: [random.randint(50, 200) for _ in years] for category in categories
    }
    return years, data


bar_options = {"title": "Bar Chart Example"}
pie_options = {"title": "Pie Chart Example"}
heatmap_options = {"title": "Heatmap Example"}
stacked_bar_options = {"title": "Stacked Bar Chart Example"}
grouped_bar_options = {"title": "Grouped Bar Chart Example"}


def create_bar_chart():
    categories = ["Category A", "Category B", "Category C"]
    values = [10, 20, 30]
    bar_fig = go.Figure(data=[go.Bar(x=categories, y=values, texttemplate="%{y}%")])
    return bar_fig


def create_pie_chart():
    labels = ["Apple", "Banana", "Cherry"]
    values = [300, 450, 250]
    pie_fig = go.Figure(data=[go.Pie(labels=labels, values=values)])
    return pie_fig


def create_heatmap():
    heatmap_fig = go.Figure(
        data=go.Heatmap(
            z=[[1, 20, 30], [20, 1, 60], [30, 60, 1]],
            x=["Monday", "Wednesday", "Friday"],
            y=["Morning", "Afternoon", "Evening"],
        )
    )
    return heatmap_fig


def create_stacked_bar_chart():
    start_date = datetime(2018, 1, 1)
    end_date = datetime(2023, 1, 7)
    categories = ["Product A", "Product B", "Product C"]
    dates, data = generate_time_series_data(start_date, end_date, categories)

    stacked_bar_fig = go.Figure()
    for category in categories:
        stacked_bar_fig.add_trace(
            go.Bar(x=dates, y=data[category], name=category, texttemplate="%{y}%")
        )

    stacked_bar_fig.update_layout(
        barmode="stack",
        xaxis_title="Date",
        yaxis_title="Sales Volume",
    )
    return stacked_bar_fig


def create_grouped_bar_chart():
    start_date = datetime(2018, 1, 1)
    end_date = datetime(2023, 1, 7)
    categories = ["Region X", "Region Y", "Region Z"]
    dates, data = generate_time_series_data(start_date, end_date, categories)

    grouped_bar_fig = go.Figure()
    for category in categories:
        grouped_bar_fig.add_trace(
            go.Bar(x=dates, y=data[category], name=category, texttemplate="%{y}%")
        )

    grouped_bar_fig.update_layout(
        barmode="group",
        xaxis_title="Date",
        yaxis_title="Sales Volume",
    )
    return grouped_bar_fig


if __name__ == "__main__":
    bar_chart = create_bar_chart()
    pie_chart = create_pie_chart()
    heatmap = create_heatmap()
    stacked_bar_chart = create_stacked_bar_chart()
    grouped_bar_chart = create_grouped_bar_chart()
    report = CreatePowerPoint(presentation_title="Example Report 2")
    report.add_figure(bar_chart)
    report.add_figure(pie_chart)
    report.add_figure(heatmap)
    report.add_figure(stacked_bar_chart)
    report.add_figure(grouped_bar_chart)
    report.create_presentation()
