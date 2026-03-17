

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(
     "sqlite+libsql:///embedded.db",
     connect_args={
         "sync_url": "libsql://coll-ef7fa097f692475a949b209099acc03f-mayson.aws-ap-south-1.turso.io",
         "auth_token": "eyJhbGciOiJFZERTQSIsInR5cCI6IkpXVCJ9.eyJpYXQiOjE3NzM2NTY2MjUsInAiOnsicm9hIjp7Im5zIjpbIjAxOWNmNjJjLTQ1MDEtNzkyNi1iZTBlLTE0MTBjZmZhNzE3NyJdfSwicnciOnsibnMiOlsiMDE5Y2Y2MmMtNDUwMS03OTI2LWJlMGUtMTQxMGNmZmE3MTc3Il19fSwicmlkIjoiMzkyMjc4YmYtZWY5Ny00ZDUzLWJiMjItNzZlYzEyYTI1YTE1In0.XKsc060Lo1RhPYaEuRWzAxKu86B-yu--IzNq9usuuLt02JRFNpsrz6FUiuMS5Eb3kF-lYxUwMwyC7iIqvBK7CA",
     },
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)
Base = declarative_base()

