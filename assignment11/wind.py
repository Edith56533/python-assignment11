import plotly.data as pldata
import plotly.express as px


df = pldata.wind(return_type="pandas")

print("First 10 rows:")
print(df.head(10))

print("\nLast 10 rows:")
print(df.tail(10))

df["strength"] = (
    df["strength"]
    .str.extract(r"(\d+(?:\.\d+)?)", expand=False)
    .astype(float)
)

print("\nColumn data types after cleaning:")
print(df.dtypes)

fig = px.scatter(
    df,
    x="strength",
    y="frequency",
    color="direction",
    title="Wind Frequency by Strength and Direction",
    labels={
        "strength": "Wind Strength",
        "frequency": "Frequency",
        "direction": "Direction",
    },
)

fig.write_html("wind.html", auto_open=True)