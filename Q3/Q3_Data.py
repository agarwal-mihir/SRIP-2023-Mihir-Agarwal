import matplotlib.pyplot as plt
import seaborn as sns
import openaq

sns.set(style="ticks", font_scale=1.)

api = openaq.OpenAQ()

# grab the data
res = api.measurements(city='Delhi', parameter='pm25', limit=10000, df=True)

# Clean up the data by removing values below 0
res = res.query("value >= 0.0")

res.to_csv('delhi_air_quality_data.csv', index=False)

