import pyecharts.options as opts
from pyecharts.charts import Bar, Line

x_data = [f"E{i}" for i in range(2, 14, 1)]
y1_data = [0.2, 0.49, 0.70, 0.232, 0.256, 0.767, 0.136, 0.1622, 0.326, 0.20, 0.64, 0.33]
y2_data = [0.2, 0.49, 1.20, 0.332, 0.356, 0.767, 1.136, 0.1622, 0.326, 0.20, 0.64, 0.33]


def generate_muti(X=None, Y1_Name="Y1_Name", Y2_Name="Y2_Name", Y1=None, Y2=None):
    if X is None:
        X = x_data
    if Y1 is None:
        Y1 = y1_data
    if Y2 is None:
        Y2 = y2_data
    # X, Y1, Y2 = x_data, y1_data, y2_data
    print(X)
    print(Y1)
    print(Y2)
    print(Y1_Name)
    print(Y2_Name)
    assert len(X) == len(Y1) == len(Y2), "X, Y1, Y2 must have the same length, got {} and {}".format(X, Y1)
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
                min_=min(Y2) - 0.5,
                max_=max(Y2) + 0.05,
                interval=0.1,
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
                min_=min(Y1) - 0.1,
                max_=max(Y1) + 0.35,
                interval=0.1,
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
        .add_xaxis(xaxis_data=X)
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
            xaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(color="white"), min_=min(Y1) - 0.1,
                max_=max(Y1) + 0.1),
            yaxis_opts=opts.AxisOpts(
                splitline_opts=opts.SplitLineOpts(is_show=True),
                axislabel_opts=opts.LabelOpts(color="white"),
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
    return bar
