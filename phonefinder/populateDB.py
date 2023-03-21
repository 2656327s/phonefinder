import json
import decimal

from django.conf import settings
import django
from django.db import connection

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'phonefinder.settings')

django.setup()

cursor = connection.cursor()
cursor.execute("""SELECT devices.name, brands.name,SUBSTRING_INDEX(SUBSTRING_INDEX(released_at, ', ', 1), ' ', -1) AS release_year,    CASE 
        WHEN storage LIKE '%TB%' THEN CAST(SUBSTRING_INDEX(storage, ' ', 1) AS UNSIGNED) * 1024
        WHEN storage LIKE '%GB%' THEN CAST(SUBSTRING_INDEX(storage, ' ', 1) AS UNSIGNED)
        WHEN storage LIKE '%MB%' THEN CAST(SUBSTRING_INDEX(storage, ' ', 1) AS UNSIGNED) / 1024
        ELSE 0
    END AS storageGB,
    SUBSTRING_INDEX(display_resolution, ' pixels', 1) AS resolution_value,
        CASE 
        WHEN ram LIKE '%/%' THEN ROUND((CAST(SUBSTRING_INDEX(ram, '/', 1) AS FLOAT) + CAST(SUBSTRING_INDEX(ram, '/', -1) AS FLOAT)) / 2, 1)
        WHEN ram LIKE '%-%' THEN ROUND((CAST(SUBSTRING_INDEX(ram, '-', 1) AS FLOAT) + CAST(SUBSTRING_INDEX(ram, '-', -1) AS FLOAT)) / 2, 1)
        WHEN ram LIKE '%GB%' THEN CAST(SUBSTRING_INDEX(ram, ' ', 1) AS FLOAT)
        ELSE 1
    END AS ramGB, picture
FROM world.devices
INNER JOIN world.brands ON devices.brand_id = brands.id WHERE (cast(substr(released_at,10,4) AS dec)>2018) order by cast(substr(released_at,10,4) AS dec) DESC;""")
data = cursor.fetchall()

with open("phones.json", "w") as fp:
    listObj = []

    for row in data:
        listObj.append({"id": data.index(row)+1, "name": row[0], "brand": row[1], "releaseYear": row[2],
                        "storage": str(row[3]), "resolution": row[4], "ram": str(row[5]), "picture": row[6]})

    json.dump(listObj, fp, indent=4, default=str, ensure_ascii=False)

cursor.close()
