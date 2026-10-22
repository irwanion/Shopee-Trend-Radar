import json
import random

# Example Harvester Logic: Replace this array with your custom API calls / PyTrends requests
live_items = [
    {
        "id": 1,
        "name": "Mini Cordless Desk Vacuum",
        "category": "Tools",
        "demandGrowth": round(random.uniform(140.0, 220.0), 1),
        "competitionScore": 88.0,
        "affiliateScore": 92,
        "tabletopFriendly": True,
        "image": "https://images.unsplash.com/photo-1585338107529-13afc5f02586?w=500&auto=format&fit=crop&q=60",
        "shopeeSearch": "Mini+Desk+Vacuum+Cordless"
    },
    {
        "id": 2,
        "name": "Portable Rechargeable Garlic Chopper 250ml",
        "category": "Kitchen",
        "demandGrowth": round(random.uniform(180.0, 310.0), 1),
        "competitionScore": 92.5,
        "affiliateScore": 96,
        "tabletopFriendly": True,
        "image": "https://images.unsplash.com/photo-1584269600464-37b1b58a9fe7?w=500&auto=format&fit=crop&q=60",
        "shopeeSearch": "Chopper+Bumbu+Elektrik+Portable"
    }
]

# Write updated dataset to JSON file
with open('data.json', 'w') as f:
    json.dump(live_items, f, indent=2)

print("Successfully updated daily trend data!")
