import pandas as pd
from sqlalchemy import create_engine,text

# dialect://username:password@host:port/database_name
CONN_URL = "postgresql://root:root@localhost:5432/raw_data"
engine = create_engine(CONN_URL)

try:
    # Ek dummy query chala kar connection test karte hain
    with engine.connect() as conn:
        query = text("SELECT 'version' as column_name;")
        res = conn.execute(query).fetchone()
        print("🎉 Postgres se successfully connect ho gaye!")
        print("Postgres Output:", res)
except Exception as e:
    print("❌ Connection failed! Check karein ki container chal raha hai ya nahi.")
    print(e)