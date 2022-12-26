travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
new_country={}
new_country["country"] = "Russia"
new_country["visits"] = 2
new_country["cities"] = ['Moscow', 'Saint Petersburg']

travel_log.append(new_country)

print(travel_log)
