import pyecharts.options as opts
from pyecharts.charts import Bar, Line

x_data = [f"E{i}" for i in range(2, 14, 1)]
y1_data = [2.0, 4.9, 7.0, 23.2, 25.6, 76.7, 135.6, 162.2, 32.6, 20.0, 6.4, 3.3]
y2_data = [2.0, 2.2, 3.3, 4.5, 6.3, 10.2, 20.3, 23.4, 23.0, 16.5, 12.0, 6.2]


def generate_muti(X=None, Y1_Name="Y1_Name", Y2_Name="Y2_Name", Y1=None, Y2=None):
    if X is None:
        X = x_data
    if Y1 is None:
        Y1 = y1_data
    if Y2 is None:
        Y2 = y2_data
    assert len(X) == len(Y1) == len(Y2), "X, Y1, Y2 must have the same length"
    bar = (
        Bar(init_opts=opts.InitOpts(width="80vh", height="40vh"))
        .add_xaxis(xaxis_data=X)
        .add_yaxis(
            series_name=Y1_Name,
            y_axis=Y1,
            label_opts=opts.LabelOpts(is_show=False),
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                name=Y2_Name,
                type_="value",
                min_=0,
                max_=25,
                interval=5,
                axislabel_opts=opts.LabelOpts(formatter="{value}", color='white'),
                is_show=False
            )
        )
        .set_global_opts(
            tooltip_opts=opts.TooltipOpts(
                is_show=True,
                trigger="axis",
                axis_pointer_type="cross"
            ),
            xaxis_opts=opts.AxisOpts(
                type_="category",
                axispointer_opts=opts.AxisPointerOpts(is_show=True, type_="shadow"),
                axislabel_opts=opts.LabelOpts(color="white")
            ),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                min_=0,
                max_=250,
                interval=50,
                axislabel_opts=opts.LabelOpts(formatter="{value}", color='white'),
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
            legend_opts=opts.LegendOpts(
                is_show=True,
                orient='horizontal',
                align='right',
                pos_right='10%',
                textstyle_opts=opts.TextStyleOpts(color="white")
            )
        )
    )

    line = (
        Line()
        .add_xaxis(xaxis_data=x_data)
        .add_yaxis(
            series_name=Y2_Name,
            yaxis_index=1,
            y_axis=Y2,
            label_opts=opts.LabelOpts(is_show=False, color='white'),
        )
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),
                                     axislabel_opts=opts.LabelOpts(color="white")),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),
                                     axislabel_opts=opts.LabelOpts(color="white")),
        )
    )

    bar.overlap(line)
    return bar


def generate_muti_reverse(X_data=None, Y1=None, Y2=None, Y1_name="Y1_name", Y2_name="Y2_name"):
    if X_data is None:
        X_data = x_data
    if Y1 is None:
        Y1 = y1_data
    if Y2 is None:
        Y2 = y2_data

    assert len(X_data) == len(Y1) == len(Y2), "X, Y1, Y2 must have the same length"

    bar = (
        Bar(init_opts=opts.InitOpts(width="80vh", height="40vh"))
        .add_xaxis(X_data)
        .add_yaxis(Y1_name, Y1)
        .add_yaxis(Y2_name, Y2)
        .reversal_axis()
        .set_series_opts(label_opts=opts.LabelOpts(position="right"))
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),
                                     axislabel_opts=opts.LabelOpts(color="white")),
            yaxis_opts=opts.AxisOpts(splitline_opts=opts.SplitLineOpts(is_show=True),
                                     axislabel_opts=opts.LabelOpts(color="white")),
            legend_opts=opts.LegendOpts(
                is_show=True,
                orient='horizontal',
                align='right',
                pos_right='10%',
                textstyle_opts=opts.TextStyleOpts(color="white")
            )
        )
    )
    return bar
