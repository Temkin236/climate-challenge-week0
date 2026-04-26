import streamlit as st
import pandas as pd
import glob

st.set_page_config(page_title='Climate Trends — Week0', layout='wide')

st.title('Climate Trends — Africa (2015-2026)')

DATA_DIR = 'data'
csvs = glob.glob(f'{DATA_DIR}/*_clean.csv')
countries = [p.split('/')[-1].replace('_clean.csv','').capitalize() for p in csvs]

selected = st.multiselect('Countries', countries, default=countries[:2])
year_range = st.slider('Year range', 2015, 2026, (2015, 2026))
var = st.selectbox('Variable', ['T2M','PRECTOTCORR','T2M_MAX','RH2M'])

if selected:
    frames = []
    for c in selected:
        path = f"{DATA_DIR}/{c.lower()}_clean.csv"
        try:
            df = pd.read_csv(path)
            df['Country'] = c
            frames.append(df)
        except FileNotFoundError:
            st.warning(f"Missing file: {path}")
    if frames:
        data = pd.concat(frames, ignore_index=True)
        data['Year'] = pd.to_datetime(data['DATE']).dt.year
        data = data[(data['Year'] >= year_range[0]) & (data['Year'] <= year_range[1])]
        st.line_chart(data.groupby(['Year','Country'])[var].mean().unstack())
