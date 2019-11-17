import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go
import pandas as pd

app = dash.Dash(__name__)

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv")

fig = go.Figure()
fig.add_trace(go.Scatter(
                x=df.Date,
                y=df['AAPL.High'],
                name="Team1",
                line_color='red',
                opacity=0.8))

fig.add_trace(go.Scatter(
                x=df.Date,
                y=df['AAPL.Low'],
                name="Team2",
                line_color='blue',
                opacity=0.8))

# Use date string to set xaxis range
fig.update_layout(xaxis_range=['2016-07-01','2016-12-31'],
                  title_text="Team Elo time series")
fig.show()

app.layout = html.Div([
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True)