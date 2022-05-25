# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

import pandas as pd
import plotly.express as px
from dash import Dash, html, dcc
# from plotly.subplots import make_subplots
# import plotly.graph_objects as go


app = Dash(__name__)

colors = {'background': '#636363', 'text': '#5dfcd7', 'fig_background': '#515151'}
# colors are background:dark grey, and text:turquoise-ish, and fig_background: darker grey

# see https://plotly.com/python/px-arguments/ for more options

achievements = [{'Name': 'HS Graduation', 'Date': '2008-05-01', 'y_axis': 1, 'length': 48, 'involvement': 100},
                {'Name': 'Python Course', 'Date': '2022-03-01', 'y_axis': .75, 'length': 3.75, 'involvement': 100},
                {'Name': 'Begin Learning Code', 'Date': '2020-06-01', 'y_axis': .5, 'length': 2.5, 'involvement': 100},
                {'Name': '1st .py Project', 'Date': '2022-05-14', 'y_axis': .25, 'length': 1.5, 'involvement': 75},
                {'Name': 'UNKNOWN', 'Date': '2016-06-01', 'y_axis': .8, 'length': 7, 'involvement': 100}
                ]
achievement_df = pd.DataFrame(achievements)

skills = [{'name': 'Python', 'Months': 2},
          {'name': 'Data Visualization', 'Months': 1},
          {'name': 'Git', 'Months': 1.75}
          ]
skill_df = pd.DataFrame(skills)
skill_df.sort_values(by='Months', ascending=True, inplace=True)

achievement_fig = px.scatter(
    achievement_df, x='Date', y='y_axis',
    # marginal_x='Date',
    # marginal_y='',
    text='Name',
    title='Achievements and Date of Occurence'
)

achievement_fig.update_traces(
    textposition="bottom center",
    marker={'symbol': 'diamond-cross', 'size': 60,
            'color': '#f5a42a', 'opacity': 1},
    marker_line={'color': 'yellow', 'width': 2}
)
achievement_fig.update_yaxes(visible=False)

achievement_fig.update_layout(
    plot_bgcolor=colors['fig_background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    font_family='Lucida Console')

skill_fig = px.bar(
    skill_df, x='Months', y='name',
    orientation='h',
    title='Skills and Experience')

skill_fig.update_layout(
    plot_bgcolor=colors['fig_background'],
    paper_bgcolor=colors['background'],
    font_color=colors['text'],
    font_family='Lucida Console')

app_components = [
    html.H1(
        children='Taylor McCollom\'s Portfolio',
        style={'color': colors['text'],
               'backgroundColor': colors['background'],
               'textAlign': 'center',
               'font-family': 'Didot',
               'font-size': 36,

               }
    ),

    dcc.Graph(id='skill graph', figure=skill_fig),

    dcc.Graph(id='achievement graph', figure=achievement_fig)
]

app.layout = html.Div(children=app_components, style={'backgroundColor': colors['background']})

if __name__ == '__main__':
    app.run_server(debug=True)
