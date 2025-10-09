import json
with open("sample-data.json") as f:
   data = json.load(f)
print("Interface Status")
print("=" * 80)
print("{:<50} {:<20} {:<7} {:<7}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)
for item in data["imdata"]:
   attributes = item["l1PhysIf"]["attributes"]
   print("{:<50} {:<20} {:<7} {:<7}".format(
       attributes["dn"], attributes["descr"], attributes["speed"], attributes["mtu"]
   ))
 