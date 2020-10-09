#*****************************************
#PLOTLY GRAPHS
#*****************************************

import plotly.graph_objects as go

fig = go.Figure()

fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 1, 3, 2, 4, 3, 4, 6, 5]
))


fig.add_trace(go.Scatter(
    x=[0, 1, 2, 3, 4, 5, 6, 7, 8],
    y=[0, 4, 5, 1, 2, 2, 3, 4, 2]
))

fig.add_annotation(
            x=2,
            y=5,
            text="Text")
fig.add_annotation(
            x=4,
            y=4,
            text="Text 2")
fig.update_annotations(dict(
            xref="x",
            yref="y",
            showarrow=True,
            arrowhead=7,
            ax=0,
            ay=-40
))


D=['Alphabet','Antique','Bold','D3','Dark2','Dark24','G10','Light24','Pastel','Pastel1']

Z=[[0, 0],[1, 2],[2, 4],[3, 6],[4, 8],[5, 10],[6, 12],[7, 14],[8, 16],[9, 18]]

for i, m in enumerate(D):
    fig.add_annotation(dict(font=dict(color='rgba(0,0,200,0.8)',size=12),
                                        x=Z[i][0],
                                        y=Z[i][1],
                                        showarrow=False,
                                        text=D[i],
                                        textangle=0,
                                        xanchor='left',
                                        xref="x",
                                        yref="y"))

# fig.update_layout(showlegend=False)

fig.show()