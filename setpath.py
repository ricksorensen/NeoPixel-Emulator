from pathlib import Path
import sys

sys.path.append(str(Path(__file__).resolve().parent))
print("new sys.path\n", sys.path)
