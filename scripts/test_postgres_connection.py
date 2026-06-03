import pandas as pd
from sqlalchemy import create_engine

# dialect://username:password@host:port/database_name
CONN_URL = "postgresql://root:root@localhost:5432/raw_data"
engine = create_engine(CONN_URL)

try:
    # Ek dummy query chala kar connection test karte hain
    with engine.connect() as conn:
        res = conn.execute("SELECT version();").fetchone()
        print("🎉 Postgres se successfully connect ho gaye!")
        print("Postgres Version:", res[0])
except Exception as e:
    print("❌ Connection failed! Check karein ki container chal raha hai ya nahi.")
    print(e)