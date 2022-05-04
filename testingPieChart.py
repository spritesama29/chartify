import chartify

ch = chartify.Chart(blank_labels=True, y_axis_type='density')
x = {
    'United States': 157,
    'United Kingdom': 93,
    'Sean': 89,
    'China': 63,
    'Germany': 44,
    'India': 42,
    'Italy': 40,
    'Australia': 35,
    'Brazil': 32,
    'France': 31,
    'Taiwan': 31,
    'Spain': 29
}

p = ch.plot.pie(x, 'times')
ch.show("preMade", p)

