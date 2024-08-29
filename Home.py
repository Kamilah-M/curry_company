import streamlit as st
from PIL import Image

st.set_page_config(page_title="Home")

#image_path= 'C:\\Users\\kamil\\OneDrive\\Data_Science\\Repos\\curso_Python\\JupterLab\\'
image = Image.open('analise.png')
st.sidebar.image(image, width=120)

st.sidebar.markdown('# Cury Company')
st.sidebar.markdown('## Faster Delivery in Town')
st.sidebar.markdown("""---""")

st.write ("# Curry Company Growth Dashboard")

st.markdown(
    """
    Growth Dashboard foi construído para acompanhar as métricas de crescimento dos Entregadores e Restaurantes.
    ### Como utilizar esse Growth Dashboard?
    - Visão Empresa:
        - Visão Gerencial: Métricas gerais de comportamento.
        - Visão Tática: Indicadores semainais de crescimento.
        - Visão Geográfica: Insights de geolocalização.
    - Visão Entregador:
        - Acompanhamento dos indicadores semanais de crescimento.
    - Visão Restaurante:
        - Indicadores semanais de crescimento dos restaurantes.

    ### Ask for help
    - Time de Data Scince no Discord
        - @meigarom
    """)

