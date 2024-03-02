import os
import serpapi

from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv('SERPAPI_KEY')       # Llamar a la API key generada en .env

client = serpapi.Client(api_key=api_key)

results = client.search({
    'engine': 'google_maps_reviews',
    'type': 'search',
    'place_id': 'ChIJN1t_tDeuEmsRUsoyG83frY4',
    'sort_by': 'newestFirst',
    'next_page_token': "VALUE_FROM_PREVIOUS_RESPONSE"
})

print(results)