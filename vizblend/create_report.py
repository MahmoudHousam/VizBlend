import os
from vizblend.figure_defaults import figure_defaults
from jinja2 import Environment, FileSystemLoader


class CreateReport:
    def __init__(self, report_title: str):
        self.report_title = report_title
        self.figures = []

    def add_figure(self, fig_or_func, options: dict):
        if callable(fig_or_func):
            fig = fig_or_func(options)
        else:
            fig = fig_or_func

        @figure_defaults()
        def figure_defaults_wrapper(fig, options):
            """Styling a Plotly figure

            Args:
                fig (plotly.core.figure): Plotly chart. The package supports: go.Bar, go.Pie, go.Scatter, go.Histogram, go.Treemap
                options (dict): User options. The dict must contain a least a chart title. Accepts: "groupby", "benchmark", and "calender".
                No need to provide "title" in `fig.update_layout(title)`. Pass the title in options dictionary instead.
            Returns:
                Plotly fig: styled Plotly figure
            """
            return fig

        styled_figure = figure_defaults_wrapper(fig, options)
        self.figures.append(styled_figure)

    def blend_graphs_to_html(self):
        divs = []
        for i, figure in enumerate(self.figures):
            div = figure.to_html(
                full_html=False,
                include_plotlyjs=False,
                config={"displayModeBar": False},
            )
            divs.append(div)

        # Set up the Jinja2 environment
        env = Environment(loader=FileSystemLoader("templates"))
        template = env.get_template("report_template.html")

        # Render the template with the required variables
        html_content = template.render(
            divs=divs,
            total_pages=len(divs) + 1,  # Include the initial report title page
            report_name=self.report_title,
        )
        output_dir = "./"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        output_file = os.path.join(output_dir, f"{self.report_title}.html")
        with open(output_file, "w", encoding="utf-8") as report_file:
            report_file.write(html_content)
        return output_file
