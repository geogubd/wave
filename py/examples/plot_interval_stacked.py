# Plot / Interval / Stacked
# Make a stacked column plot.
# ---
from synth import FakeMultiCategoricalSeries
from h2o_wave import site, data, ui

page = site['/demo']

n = 10
k = 5
f = FakeMultiCategoricalSeries(groups=k)
v = page.add('example', ui.plot_card(
    box='1 1 4 5',
    title='Intervals, stacked',
    data=data('country product price', n * k),
    plot=ui.plot([ui.mark(type='interval', x='=product', y='=price', color='=country', stack='auto', y_min=0)])
))

v.data = [(g, t, x) for x in [f.next() for _ in range(n)] for g, t, x, dx in x]

page.save()
