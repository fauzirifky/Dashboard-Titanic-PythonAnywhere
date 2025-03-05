import dash
from dash import dcc, html
import pandas as pd
import plotly.express as px

# Memuat data Titanic dari URL
url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_df = pd.read_csv(url)

# Hapus kolom 'Cabin'
titanic_df = titanic_df.drop('Cabin', axis=1)

# Isi nilai kosong di 'Age' dengan median
titanic_df['Age'] = titanic_df['Age'].fillna(titanic_df['Age'].median())

# Isi nilai kosong di 'Embarked' dengan modus
titanic_df['Embarked'] = titanic_df['Embarked'].fillna(titanic_df['Embarked'].mode()[0])


# Buat visualisasi
# Histogram distribusi umur
fig_histogram = px.histogram(titanic_df, x='Age', nbins=20,
                             title='Histogram Distribusi Umum Penumpang Titanic',
                             labels={'Age': 'Umur', 'count': 'Jumlah'})
fig_histogram.update_layout(bargap=0.2, yaxis_title='Jumlah')

# Histogram distribusi kelas penumpang berdasarkan kelangsungan hidup dan jenis kelamin
fig_histogram2 = px.histogram(titanic_df,
                              x='Pclass',
                              color='Survived',  # Data kategorik: selamat (1) dan tidak (0)
                              facet_col="Sex",
                              barmode="group",  # Grouping biasa
                              title='Histogram Distribusi Umum Penumpang Titanic',
                              labels={'Pclass': 'Kelas Penumpang', 'Survived': 'Survivor'},
                              color_discrete_map={0: 'red', 1: 'blue'})
fig_histogram2.update_layout(yaxis_title='Jumlah')

# Violin plot distribusi kelas dan usia berdasarkan kelangsungan hidup
fig_violin = px.violin(titanic_df,
                       x='Pclass',
                       y='Age',
                       color='Survived',  # Data kategorik: selamat (1) dan tidak (0)
                       box=True,
                       points='all',
                       title='Distribusi Kelas dan Kelangsungan Hidup Penumpang Titanic',
                       labels={'Pclass': 'Kelas Penumpang', 'Survived': 'Survivor'},
                       color_discrete_map={0: 'red', 1: 'blue'})
fig_violin.update_layout(yaxis_title='Jumlah')

# Inisiasi aplikasi Dash
app = dash.Dash(__name__)

# Definisikan layout aplikasi
app.layout = html.Div(children=[
    html.H1(children='Visualisasi Data'),
    # Tambahkan grafik ke layout
    dcc.Graph(
        id='histogram-pertama',
        figure=fig_histogram
    ),
    dcc.Graph(
        id='histogram-kedua',
        figure=fig_histogram2
    ),
    dcc.Graph(
        id='violin',
        figure=fig_violin
    ),
])

# Bagian ini dikomentari karena akan di-deploy (misalnya di PythonAnywhere)
# Jalankan server secara lokal (hapus komentar jika ingin menjalankan lokal)
# if __name__ == '__main__':
#     app.run_server(debug=True)
