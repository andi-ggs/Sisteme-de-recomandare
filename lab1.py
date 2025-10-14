import csv, re
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import AddItem, SetItemValues, ListItems, DeleteItem

client = RecombeeClient(
    'andiggs-dev',
    '9evxv2Jw8v7w0IgafnKu86B3DOJMym32qZgbDeaAPFRNXksZWNeWiFxEme0mTSVz',
    region=Region.EU_WEST
)

print("Delete all existing items")
items = client.send(ListItems(count=100000))
for item_id in items:
    client.send(DeleteItem(item_id))

with open('tari.csv', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        item_id = re.sub(r'[^a-zA-Z0-9_\-:@\.]', '_', row['country'].lower())

        client.send(AddItem(item_id))
        client.send(SetItemValues(item_id, {
            'countryName': row['country'],
            'capital': row['capital'],
            'area': float(row['area']),
            'continent': row['continent']
        }, cascade_create=True))

print("Data is added to Recombee!")
