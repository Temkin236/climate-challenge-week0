import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import glob
import os
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="African Climate Trends — Week 0",
    page_icon="🌍",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("🌍 African Climate Trends Dashboard (2015–2026)")
st.markdown("""
**COP32 Analysis Tool** — Evidence-backed climate insights for Ethiopia's climate diplomacy.

Data Source: NASA POWER Climate Reanalysis | Analysis Period: January 2015 – March 2026
""")

# Sidebar controls
st.sidebar.header("📊 Dashboard Controls")

DATA_DIR = 'data'
countries_files = {
    'Ethiopia': 'ethiopia_clean.csv',
    'Kenya': 'kenya_clean.csv',
    'Sudan': 'sudan_clean.csv',
    'Tanzania': 'tanzania_clean.csv',
    'Nigeria': 'nigeria_clean.csv'
}

# Multi-select countries
selected_countries = st.sidebar.multiselect(
    'Select Countries:',
    list(countries_files.keys()),
    default=['Ethiopia', 'Kenya']
)

# Year range slider
year_range = st.sidebar.slider(
    'Year Range:',
    min_value=2015, max_value=2026, value=(2015, 2026), step=1
)

# Variable selector
variable = st.sidebar.selectbox(
    'Select Climate Variable:',
    ['T2M (Temperature)', 'PRECTOTCORR (Precipitation)', 'T2M_MAX (Max Temp)', 
     'T2M_MIN (Min Temp)', 'RH2M (Humidity)', 'WS2M (Wind Speed)']
)

# Map display name to column name
var_map = {
    'T2M (Temperature)': 'T2M',
    'PRECTOTCORR (Precipitation)': 'PRECTOTCORR',
    'T2M_MAX (Max Temp)': 'T2M_MAX',
    'T2M_MIN (Min Temp)': 'T2M_MIN',
    'RH2M (Humidity)': 'RH2M',
    'WS2M (Wind Speed)': 'WS2M'
}
var_col = var_map[variable]

# Load data
@st.cache_data
def load_data(countries_list):
    frames = []
    for country in countries_list:
        file = countries_files[country]
        path = os.path.join(DATA_DIR, file)
        try:
            df = pd.read_csv(path)
            df['Country'] = country
            frames.append(df)
        except FileNotFoundError:
            st.warning(f"⚠️  Data file not found: {path}")
    
    if frames:
        return pd.concat(frames, ignore_index=True)
    return None

# Process and display
if selected_countries:
    df = load_data(selected_countries)
    
    if df is not None:
        # Parse dates and filter
        df['DATE'] = pd.to_datetime(df['DATE'])
        df['Year'] = df['DATE'].dt.year
        df['Month'] = df['DATE'].dt.month
        df['YearMonth'] = df['DATE'].dt.to_period('M')
        
        # Filter by year range
        df = df[(df['Year'] >= year_range[0]) & (df['Year'] <= year_range[1])]
        
        # Tab layout
        tab1, tab2, tab3, tab4 = st.tabs(["📈 Time Series", "📦 Distribution", "🔗 Correlations", "📊 Summary Stats"])
        
        with tab1:
            st.subheader(f"Monthly Trend: {variable}")
            monthly_data = df.groupby(['YearMonth', 'Country'])[var_col].mean().reset_index()
            monthly_data['YearMonth'] = monthly_data['YearMonth'].dt.to_timestamp()
            
            fig = px.line(
                monthly_data,
                x='YearMonth',
                y=var_col,
                color='Country',
                title=f"{variable} Trend by Country (2015–2026)",
                markers=True,
                height=500
            )
            fig.update_layout(xaxis_title="Date", yaxis_title=variable, hovermode='x unified')
            st.plotly_chart(fig, use_container_width=True)
        
        with tab2:
            st.subheader(f"Distribution: {variable}")
            
            if variable == 'PRECTOTCORR (Precipitation)':
                # Boxplot for precipitation
                fig = px.box(
                    df,
                    x='Country',
                    y=var_col,
                    title=f"Precipitation Variability by Country",
                    height=500
                )
            else:
                # Violin plot for other variables
                fig = px.violin(
                    df,
                    x='Country',
                    y=var_col,
                    title=f"{variable} Distribution by Country",
                    height=500
                )
            
            st.plotly_chart(fig, use_container_width=True)
        
        with tab3:
            st.subheader("Variable Correlations")
            
            corr_vars = ['T2M', 'PRECTOTCORR', 'RH2M', 'WS2M', 'T2M_RANGE']
            available_vars = [v for v in corr_vars if v in df.columns]
            
            if available_vars:
                corr_matrix = df[available_vars].corr()
                
                fig = px.imshow(
                    corr_matrix,
                    color_continuous_scale='RdBu',
                    zmin=-1, zmax=1,
                    title="Climate Variables — Correlation Matrix",
                    labels=dict(color="Correlation"),
                    height=500
                )
                st.plotly_chart(fig, use_container_width=True)
        
        with tab4:
            st.subheader("Summary Statistics")
            
            summary = df.groupby('Country')[var_col].agg([
                ('Mean', 'mean'),
                ('Median', 'median'),
                ('Std Dev', 'std'),
                ('Min', 'min'),
                ('Max', 'max'),
                ('Count', 'count')
            ]).round(2)
            
            st.dataframe(summary, use_container_width=True)
            
            # Key metrics
            col1, col2, col3 = st.columns(3)
            with col1:
                st.metric("Global Mean", f"{df[var_col].mean():.2f}")
            with col2:
                st.metric("Global Std Dev", f"{df[var_col].std():.2f}")
            with col3:
                st.metric("Total Records", f"{len(df):,}")
else:
    st.info("👈 Select at least one country from the sidebar to begin analysis.")
