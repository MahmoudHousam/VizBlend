import os
import pytest
import plotly.graph_objs as go
from bs4 import BeautifulSoup
from vizblend.create_report import CreateReport


@pytest.fixture
def sample_report():
    """Fixture to create a sample report object."""
    return CreateReport(report_title="Test Report")


@pytest.fixture
def sample_figure():
    """Fixture to create a sample Plotly figure."""
    return go.Figure(go.Bar(x=["A", "B", "C"], y=[1, 2, 3]))


def test_add_regular_figure(sample_report, sample_figure):
    """Test adding a regular Plotly figure."""
    options = {"title": "Bar Chart"}
    sample_report.add_figure(sample_figure, options)

    assert len(sample_report.figures) == 1
    assert sample_report.figures[0] == sample_figure


def test_add_figure_from_function(sample_report):
    """Test adding a figure returned by a function."""

    def example_graph(options):
        fig = go.Figure(go.Pie(labels=["A", "B", "C"], values=[30, 20, 50]))
        fig.update_layout(title=options["title"])
        return fig

    options = {"title": "Pie Chart"}
    sample_report.add_figure(example_graph, options)

    assert len(sample_report.figures) == 1
    assert sample_report.figures[0].layout.title.text == "Pie Chart"


def test_blend_graphs_to_html(sample_report, sample_figure, tmpdir):
    """Test blending graphs to an HTML report."""
    options = {"title": "Bar Chart"}
    sample_report.add_figure(sample_figure, options)

    output_file = sample_report.blend_graphs_to_html()
    assert os.path.isfile(output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Bar Chart" in content


def test_html_generation_content(sample_report, tmpdir):
    """Test the generated HTML file for expected content."""
    fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 5, 6]))
    options = {"title": "Scatter Plot"}
    sample_report.add_figure(fig, options)

    output_file = sample_report.blend_graphs_to_html()
    assert os.path.isfile(output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Scatter Plot" in content
        assert "Test Report" in content


def test_empty_figures_list(sample_report, tmpdir):
    """Test blending graphs with no figures added."""
    output_file = sample_report.blend_graphs_to_html()
    assert os.path.isfile(output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Test Report" in content


def test_invalid_add_figure(sample_report):
    """Test adding invalid objects to the report."""
    with pytest.raises(Exception):  # Adjust the exception type if specific
        sample_report.add_figure(123, {"title": "Invalid Figure"})


def test_large_number_of_figures(sample_report, tmpdir):
    """Test blending a large number of figures."""
    for i in range(100):  # Add 100 figures
        fig = go.Figure(go.Bar(x=[i], y=[i]))
        sample_report.add_figure(fig, {"title": f"Figure {i}"})

    output_file = sample_report.blend_graphs_to_html()
    assert os.path.isfile(output_file)

    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
        assert "Figure 99" in content  # Check if the last figure's title exists


def test_valid_html_output(sample_report, sample_figure, tmpdir):
    """Test the validity of the generated HTML."""
    options = {"title": "Valid HTML Test"}
    sample_report.add_figure(sample_figure, options)
    output_file = sample_report.blend_graphs_to_html()

    with open(output_file, "r", encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")

    assert soup.find("div", {"class": "page"}) is not None  # Check for page divs
    assert soup.find("title").text == "Test Report"  # Check the title


def test_integration_user_workflow():
    """Integration test simulating a user workflow of adding figures and generating a report."""
    # Create a report
    report = CreateReport(report_title="Integration Test Report")

    # Add multiple figures
    # Bar chart
    bar_fig = go.Figure(go.Bar(x=["A", "B", "C"], y=[10, 20, 30]))
    report.add_figure(bar_fig, {"title": "Bar Chart"})

    # Scatter plot
    scatter_fig = go.Figure(go.Scatter(x=[1, 2, 3], y=[4, 5, 6], mode="markers"))
    report.add_figure(scatter_fig, {"title": "Scatter Plot"})

    # Pie chart
    pie_fig = go.Figure(
        go.Pie(labels=["Apple", "Banana", "Cherry"], values=[30, 40, 30])
    )
    report.add_figure(pie_fig, {"title": "Pie Chart"})

    # Step 3: Generate the HTML report
    output_file = report.blend_graphs_to_html()
    assert os.path.isfile(output_file), "The report HTML file was not created."

    # Verify the report content
    with open(output_file, "r", encoding="utf-8") as f:
        content = f.read()
        soup = BeautifulSoup(content, "html.parser")

    # Check if all figures' titles are present
    assert "Bar Chart" in content
    assert "Scatter Plot" in content
    assert "Pie Chart" in content

    # Check if all div elements for pages are present
    pages = soup.find_all("div", {"class": "page"})
    assert len(pages) == 5  # 3 figures + 1 title page
