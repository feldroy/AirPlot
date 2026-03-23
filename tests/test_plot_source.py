from airplot import PlotSource


def test_plot_source():
    assert PlotSource().render() == '<script charset="utf-8" src="https://cdn.plot.ly/plotly-3.4.0.min.js"></script>'