import plotly.graph_objects as go
from vizblend.create_report import CreateReport

# from reporting import figure_defaults_wrapper, blend_graphs_to_html


# ===========================================================================
bar_options = {"title": "Bar Graph"}
x = ["A", "B", "C"]
y = [3, 1, 2]
bar_fig = go.Figure(go.Bar(x=x, y=y, text=y))


# ===========================================================================
scatter_options = {"title": "Scatter Graph"}
x_scatter = [0, 1, 2, 3, 4]
y_scatter = [0, 1, 4, 9, 16]
scatter_fig = go.Figure(go.Scatter(x=x_scatter, y=y_scatter, mode="lines+markers"))


# ===========================================================================
pie_options = {"title": "Pie Graph"}
labels = ["Apples", "Bananas", "Cherries"]
values = [30, 20, 50]
pie_fig = go.Figure(go.Pie(labels=labels, values=values))


# ===========================================================================
box_options = {"title": "Box Graph"}
data_box = [10, 15, 20, 25, 30, 35, 40]
box_fig = go.Figure(go.Box(y=data_box, boxpoints="all", jitter=0.3))


# ===========================================================================


if __name__ == "__main__":
    report = CreateReport(
        report_title="Example Report", logo_path="Logo_TV_2015.svg.png"
    )
    report.add_figure(bar_fig, bar_options)
    report.add_figure(scatter_fig, scatter_options)
    report.add_figure(pie_fig, pie_options)
    report.add_figure(box_fig, box_options)

    report_generation = report.blend_graphs_to_html()
    print(f"report saved to {report_generation}")
