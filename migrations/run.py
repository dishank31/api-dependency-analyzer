import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.utils.db import Base, engine
from src.models import User, Team, TeamMember, Service, Endpoint, Dependency, ApiChange

def run_migrations():
    print("Running migrations...")
    Base.metadata.create_all(bind=engine)
    print("✅ All tables created successfully!")
    for table_name in Base.metadata.tables.keys():
        print(f"  ✅ {table_name}")

if __name__ == "__main__":
    run_migrations()