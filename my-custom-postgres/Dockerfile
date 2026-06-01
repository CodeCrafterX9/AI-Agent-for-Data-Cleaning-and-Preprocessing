# 1. Official Postgres Image ko base banayein
FROM postgres:15-alpine

# 2. Environment variables set karein (Database defaults)
ENV POSTGRES_USER=root
ENV POSTGRES_PASSWORD=root
ENV POSTGRES_DB=raw_data

# 3. Port expose karein
EXPOSE 5432

# Note: Postgres image ka default behaviour hota hai ki wo 
# container start hote hi database up kar deti hai.
COPY init.sql /docker-entrypoint-initdb.d/