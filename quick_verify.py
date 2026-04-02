import sys
import os
sys.path.insert(0, os.path.abspath(os.path.dirname(__file__)))

from src.utils.db import engine
from sqlalchemy import inspect

inspector = inspect(engine)
tables = inspector.get_table_names()

expected = ["users", "teams", "team_members", "services", "endpoints", "dependencies", "api_changes"]

print(f"Tables found: {tables}\n")
all_good = True
for t in expected:
    if t in tables:
        print(f"  ✅ {t}")
    else:
        print(f"  ❌ {t}  ← MISSING")
        all_good = False

print()
if all_good:
    print("✅ All tables present.")
else:
    print("❌ Some tables missing. Re-run: python -m migrations.run")
    