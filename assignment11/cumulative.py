import sqlite3

import matplotlib.pyplot as plt
import pandas as pd


connection = sqlite3.connect("../db/lesson.db")

query = """
SELECT
    o.order_id,
    SUM(p.price * l.quantity) AS total_price
FROM orders o
JOIN line_items l
    ON o.order_id = l.order_id
JOIN products p
    ON l.product_id = p.product_id
GROUP BY o.order_id
ORDER BY o.order_id;
"""

df = pd.read_sql_query(query, connection)
connection.close()

df["cumulative"] = df["total_price"].cumsum()

print(df)

df.plot(
    kind="line",
    x="order_id",
    y="cumulative",
    color="darkgreen",
    linewidth=2,
    legend=False,
)

plt.title("Cumulative Revenue by Order")
plt.xlabel("Order ID")
plt.ylabel("Cumulative Revenue ($)")
plt.grid(alpha=0.3)
plt.tight_layout()
plt.show()