import bokeh.io
import numpy as np
import pandas as pd

from bokeh.plotting import figure, show
def bruh(string,num):
    # generate some synthetic time series for six different categories
    column = list(string)
    yy = np.random.randn(num)
    g = np.random.choice(column, num)
    for i, l in enumerate(column):
        yy[g == l] += i // 2
    df = pd.DataFrame(dict(score=yy, group=g))
    print(df)
    # find the quartiles and IQR for each category
    groups = df.groupby('group')
    q1 = groups.quantile(q=0.25)
    q2 = groups.quantile(q=0.5)
    q3 = groups.quantile(q=0.75)
    iqr = q3 - q1
    upper = q3 + 1.5*iqr
    lower = q1 - 1.5*iqr

    # find the outliers for each category
    def outliers(group):
        cat = group.name
        return group[(group.score > upper.loc[cat]['score']) | (group.score < lower.loc[cat]['score'])]['score']
    out = groups.apply(outliers).dropna()

    # prepare outlier data for plotting, we need coordinates for every outlier.
    if not out.empty:
        outx = list(out.index.get_level_values(0))
        outy = list(out.values)

    p = figure(tools="", background_fill_color="#efefef", x_range=column, toolbar_location=None)

    # if no outliers, shrink lengths of stems to be no longer than the minimums or maximums
    qmin = groups.quantile(q=0.00)
    qmax = groups.quantile(q=1.00)
    upper.score = [min([x,y]) for (x,y) in zip(list(qmax.loc[:,'score']),upper.score)]
    lower.score = [max([x,y]) for (x,y) in zip(list(qmin.loc[:,'score']),lower.score)]

    # stems
    p.segment(column, upper.score, column, q3.score, line_color="black")
    p.segment(column, lower.score, column, q1.score, line_color="black")

    # boxes
    p.vbar(column, 0.7, q2.score, q3.score, fill_color="#E08E79", line_color="black")
    p.vbar(column, 0.7, q1.score, q2.score, fill_color="#3B8686", line_color="black")

    # whiskers (almost-0 height rects simpler than segments)
    p.rect(column, lower.score, 0.2, 0.01, line_color="black")
    p.rect(column, upper.score, 0.2, 0.01, line_color="black")

    # outliers
    if not out.empty:
        p.circle(outx, outy, size=6, color="#F38630", fill_alpha=0.6)

    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = "white"
    p.grid.grid_line_width = 2
    p.xaxis.major_label_text_font_size="16px"
    return p
list1 = ["bop","beep","bruh","brr","bufu","brurh"]
p = bruh(list1,30)
bokeh.io.show(p)

