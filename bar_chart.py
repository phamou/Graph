import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objects as go

app = dash.Dash(__name__)

maps = ["Inferno", "Mirage", "Nuke", "Train", "Overpass", "DustII", "Vertigo"]

fig = go.Figure()
fig.add_trace(go.Bar(x=maps,
             y = [3, 1, 2, 5, 5, 5, 5, 5],
            name = 'team1',
            marker_color='rgb(0, 0, 200)'
        )
    )  
fig.add_trace(go.Bar(x = maps,
            y = [1, 9, 4, 5, 5, 5, 5, 5],
            name = 'team2',
            marker_color='rgb(200, 0, 0)'
        )
    )

fig.update_layout(
        title = 'Team Win Percentage on Each Map',

        xaxis = dict(
            title ='Maps'
        ),
        
        yaxis = dict(
           title = 'Win Percentage (%)' 
        ),

        legend=dict(
        x=0,
        y=1.0,
        bgcolor='rgba(255, 255, 255, 0)',
        bordercolor='rgba(255, 255, 255, 0)'
        ),

        barmode='group',
        bargap=0.15, # gap between bars of adjacent location coordinates.
        bargroupgap=0.1 # gap between bars of the same location coordinate.
)
fig.show()

app.layout = html.Div([
    dcc.Graph(figure=fig)
])


if __name__ == '__main__':
    app.run_server(debug=True)