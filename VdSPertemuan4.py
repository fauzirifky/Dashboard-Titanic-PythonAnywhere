import jupyter_dash import JupyterDash
from dash import dcc, html


import pandas as pd
import plotly.express as px

url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

titanic_df = pd.read_csv(url)

print(titanic_df.head())

titanic_df['Age'].median()

titanic_df[titanic_df['Age'].isna()]

# Drop semua entri dalam kolom 'Cabin'
titanic_df = titanic_df.drop('Cabin', axis=1)

# Isi nilai kosong dengan nilai tengah data
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].median())

# Isi nilai kosong dengan modus (mode)
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0])

print(titanic_df.head())



fig_histogram = px.histogram(titanic_df, x='Age', nbins=20,
                             title='Histogram Distribusi Umum Penumpang Titanic',
                             labels={'Age': 'Umur', 'count':'Jumlah'})

fig_histogram.update_layout(bargap=0.2, yaxis_title='Jumlah')
fig_histogram.show()

fig_histogram2 = px.histogram(titanic_df,
                              x='Pclass',
                              color='Survived', #data kategorik selamat:1 dan tidak:0
                              facet_col = "Sex",
                              barmode="group", #bukan dari kolom, style grouping biasa
                             title='Histogram Distribusi Umum Penumpang Titanic',
                             labels={'Pclass': 'Kelas Penumpang', 'Survived':'Survivor'},
                              color_discrete_map={0: 'red', 1: 'blue'})

fig_histogram2.update_layout(yaxis_title='Jumlah')
fig_histogram2.show()

fig_violin = px.violin(titanic_df,
                              x='Pclass',
                              y= 'Age',
                              color='Survived', #data kategorik selamat:1 dan tidak:0
                              box=True,
                              points='all',
                             title='Distribusi Kelas dan Kelangsungan HidupPenumpang Titanic',
                             labels={'Pclass': 'Kelas Penumpang', 'Survived':'Survivor'},
                              color_discrete_map={0: 'red', 1: 'blue'})

fig_violin.update_layout(yaxis_title='Jumlah')
fig_violin.show()


# Inisiasi aplikasi
app = dash.Dash(__name__)

# Definisikan layout 
app.layout = html.Div(children=[
    html.H1(children=‘Visualisasi Data’),
    # Jika hendak ada grafik
    dcc.Graph(
        id=‘histogram-pertama',
        figure=fig_histogram
    ),

    dcc.Graph(
        id=‘histogram-kedua',
        figure=fig_histogram2
    ),

    dcc.Graph(
        id=‘violin',
        figure=fig_violin
    ),
   ])

# Jalankan server
if __name__ == '__main__':
    app.run_server(debug=True)
