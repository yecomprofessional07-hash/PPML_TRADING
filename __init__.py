import sys
from pathlib import Path

# Configurar paths globalmente
PROJECT_ROOT = Path(__file__).parent
sys.path.insert(0, str(PROJECT_ROOT / 'backend'))