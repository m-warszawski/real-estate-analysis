import plotly.express as px
import plotly.io as pio

def visualize_data_plotly(data):
    try:
        center_lat = data['latitude'].mean()
        center_lon = data['longitude'].mean()
        fig = px.scatter_mapbox(data, lat="latitude", lon="longitude", color="cena", size="powierzchnia",
                                color_continuous_scale=px.colors.cyclical.IceFire, size_max=15,
                                zoom=10, mapbox_style="carto-positron", title="Map Visualization of Real Estate Data")
        fig.update_layout(mapbox=dict(center=dict(lat=center_lat, lon=center_lon), zoom=10))
        pio.show(fig)
        fig.write_html("../results/map.html")
    except Exception as e:
        raise RuntimeError(f"Błąd podczas wizualizacji danych: {e}")
