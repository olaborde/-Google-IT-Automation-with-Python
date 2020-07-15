import arrow
import requests
from PIL import Image
import pandas as pd

response = requests.get("http://www.google.com")
len(response.text)
date = arrow.get('2020-01-18', 'YYYY-MM-DD')
date.shift(weeks=+6).format('MMM DD YYYY')
# 'Feb 29 2020'

im = Image.open("roads.png")
# im.rotate(45).show()
print(im.size)
print(im.format)

visitors = [1235, 6424, 9345, 8464, 2345]

errors = [ 23, 45, 33, 45, 76]

df = pd.DataFrame({"Visitors": visitors, "Errors": errors}, index=["Mon", "Tues", "Wed", "Thurs", "Fri"])
print(df)
print(df["Errors"].mean())