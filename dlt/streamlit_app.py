import streamlit as st
import dlt
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# Set up the page configuration
st.set_page_config(page_title="Pokemon Data Explorer", layout="wide")

# Add title and description
st.title("Pokemon Data Explorer")
st.write("Explore Pokemon data fetched from PokeAPI using DLT pipeline")

# Initialize DLT pipeline
@st.cache_data
def load_pokemon_data():
    pipeline = dlt.pipeline(
        pipeline_name="pokeapi_example",
        destination="duckdb",
        dataset_name="pokeapi_data"
    )
    
    # Get the data from the pipeline
    pokemon_df = pipeline.dataset().pokemon.df()
    ability_df = pipeline.dataset().ability.df()
    
    return pokemon_df, ability_df

# Load the data
try:
    pokemon_df, ability_df = load_pokemon_data()
    
    # Create tabs for different views
    tab1, tab2, tab3 = st.tabs(["Pokemon List", "Statistics & Visualizations", "Abilities"])
    
    with tab1:
        st.subheader("Pokemon Data")
        # Add a search box for Pokemon
        search_term = st.text_input("Search Pokemon by name")
        
        if search_term:
            filtered_df = pokemon_df[pokemon_df['name'].str.contains(search_term.lower(), na=False)]
        else:
            filtered_df = pokemon_df
        
        # Display Pokemon data
        st.dataframe(filtered_df)
    
    with tab2:
        st.subheader("Pokemon Statistics & Visualizations")
        
        # Basic statistics
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Total Pokemon", len(pokemon_df))
        with col2:
            st.metric("Total Abilities", len(ability_df))
        with col3:
            st.metric("Average Base Experience", int(pokemon_df['base_experience'].mean()))
        
        # Stats correlation scatter plot
        st.subheader("Stats Correlation")
        stat_x = st.selectbox("Select X-axis stat", ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed'])
        stat_y = st.selectbox("Select Y-axis stat", ['hp', 'attack', 'defense', 'special-attack', 'special-defense', 'speed'], index=1)
        
        fig_scatter = px.scatter(
            pokemon_df,
            x=f"stats.{stat_x}",
            y=f"stats.{stat_y}",
            hover_data=['name'],
            title=f"{stat_x.title()} vs {stat_y.title()}"
        )
        st.plotly_chart(fig_scatter)
        
        # Pokemon types distribution
        st.subheader("Pokemon Types Distribution")
        type_counts = pd.Series([t['type']['name'] for types in pokemon_df['types'] for t in types]).value_counts()
        fig_types = px.bar(
            x=type_counts.index,
            y=type_counts.values,
            title="Pokemon Types Distribution",
            labels={'x': 'Type', 'y': 'Count'}
        )
        st.plotly_chart(fig_types)
        
        # Individual Pokemon Stats Radar Chart
        st.subheader("Pokemon Stats Comparison")
        selected_pokemon = st.selectbox("Select a Pokemon", pokemon_df['name'].tolist())
        if selected_pokemon:
            pokemon_stats = pokemon_df[pokemon_df['name'] == selected_pokemon].iloc[0]['stats']
            stats_values = [stat['base_stat'] for stat in pokemon_stats]
            stats_names = [stat['stat']['name'] for stat in pokemon_stats]
            
            fig_radar = go.Figure()
            fig_radar.add_trace(go.Scatterpolar(
                r=stats_values,
                theta=stats_names,
                fill='toself',
                name=selected_pokemon
            ))
            fig_radar.update_layout(
                polar=dict(radialaxis=dict(visible=True, range=[0, 150])),
                showlegend=True,
                title=f"{selected_pokemon.title()} Stats"
            )
            st.plotly_chart(fig_radar)
    
    with tab3:
        st.subheader("Abilities Data")
        # Add a search box for abilities
        ability_search = st.text_input("Search abilities")
        
        if ability_search:
            filtered_abilities = ability_df[ability_df['name'].str.contains(ability_search.lower(), na=False)]
        else:
            filtered_abilities = ability_df
        
        # Display abilities data
        st.dataframe(filtered_abilities)

except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.info("Please make sure to run the DLT pipeline (dlttest1.py) first to fetch the data.")