import dlt
from dlt.sources.rest_api import rest_api_source

# Define the REST API source for PokéAPI
source = rest_api_source({
    "client": {
        "base_url": "https://pokeapi.co/api/v2/",
        "paginator": {
            "type": "json_link",
            "next_url_path": "next",  # PokéAPI uses 'next' for pagination
        },
    },
    "resources": [
        {
            "name": "pokemon",
            "endpoint": "pokemon"
        },
        {
            "name": "ability",
            "endpoint": "ability"
        },
    ],
})

# Define the pipeline
pipeline = dlt.pipeline(
    pipeline_name="pokeapi_example",
    destination="duckdb",
    dataset_name="pokeapi_data",
)

# Run the pipeline
load_info = pipeline.run(source)

# Print load info
print(load_info)

# Print the first few rows of the Pokémon table
print(pipeline.dataset().pokemon.df().head())

# Print the first few rows of the Ability table
print(pipeline.dataset().ability.df().head())