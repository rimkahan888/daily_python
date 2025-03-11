import streamlit as st
import dlt
import pandas as pd

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
    
    # Create two columns for the layout
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("Pokemon Data")
        # Add a search box for Pokemon
        search_term = st.text_input("Search Pokemon by name")
        
        if search_term:
            filtered_df = pokemon_df[pokemon_df['name'].str.contains(search_term.lower(), na=False)]
        else:
            filtered_df = pokemon_df
        
        # Display Pokemon data
        st.dataframe(filtered_df)
    
    with col2:
        st.subheader("Abilities Data")
        # Add a search box for abilities
        ability_search = st.text_input("Search abilities")
        
        if ability_search:
            filtered_abilities = ability_df[ability_df['name'].str.contains(ability_search.lower(), na=False)]
        else:
            filtered_abilities = ability_df
        
        # Display abilities data
        st.dataframe(filtered_abilities)
    
    # Add some statistics
    st.subheader("Pokemon Statistics")
    col3, col4, col5 = st.columns(3)
    
    with col3:
        st.metric("Total Pokemon", len(pokemon_df))
    
    with col4:
        st.metric("Total Abilities", len(ability_df))
    
    with col5:
        st.metric("Average Base Experience", int(pokemon_df['base_experience'].mean()))

except Exception as e:
    st.error(f"Error loading data: {str(e)}")
    st.info("Please make sure to run the DLT pipeline (dlttest1.py) first to fetch the data.")