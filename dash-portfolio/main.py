# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Pears", "Apples", "Oranges", "Pears"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")


achievements = [{'name':'HS Graduation', 'date':'2008-05-01'},
                {'name':'Python Course', 'date':'2022-03-01'}]
achievement_df = pd.DataFrame(achievements)
achievement_df['y_axis'] = 1

fig = px.scatter(achievement_df, x='date', y='y_axis', text = 'name')
fig.update_traces(textposition="top center", marker={'symbol':'star', 'size':50, 'color':'gold'})
fig.update_yaxes(visible=False)

app.layout = html.Div(children=[
    html.H1(children='Taylor McCollom Portfolio', style = {'textAlign':'center'}),

    html.Div(children='''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

help()