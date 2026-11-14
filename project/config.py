"""
Global configuration file for MindMap project
Provides filesystem paths, channel mapping and other settings.
"""

import numpy as np

from pathlib import Path
from typing import Dict, List, Optional

# ===================================================
# 1. Filesystem paths and directory setup
# ===================================================

PROJECT_DIR: Path = Path(__file__).parent
DATA_DIR: Path = PROJECT_DIR / "data"
NOTEBOOKS_DIR: Path = PROJECT_DIR / "notebooks"
ASSETS_DIR: Path = DATA_DIR / "assets"

def ensure_directories() -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    ASSETS_DIR.mkdir(parents=True, exist_ok=True)

ensure_directories()

# ===================================================
# 2. General reporductibility settings
# ===================================================

RANDOM_SEED: int = 42
ALL_MOBILITIES: bool = True
DEFAULT_LIMIT_SUBJECTS: int = 3

# ===================================================
# 3. MOABB dataset and paradigm settings
# ===================================================

FMIN: float = 8.0
FMAX: float = 32.0

# ===================================================
# 4. Channel definition and mappings
# ===================================================

MED_COLUMNS: List[str] = [
    # 59 EEG Channels                                                              
    'Fpz', 'Fp1', 'Fp2', 'AF3', 'AF4', 'AF7', 'AF8',                                                
    'Fz', 'F1', 'F2', 'F3', 'F4', 'F5', 'F6', 'F7', 'F8',                                           
    'FCz', 'FC1', 'FC2', 'FC3', 'FC4', 'FC5', 'FC6', 'FT7', 'FT8',                                  
    'Cz', 'C1', 'C2', 'C3', 'C4', 'C5', 'C6', 'T7', 'T8',                                           
    'CP1', 'CP2', 'CP3', 'CP4', 'CP5', 'CP6', 'TP7', 'TP8',                                         
    'Pz', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8',                                                       
    'POz', 'PO3', 'PO4', 'PO5', 'PO6', 'PO7', 'PO8',                                                
    'Oz', 'O1', 'O2',             
    
    # 1 ECG Channel
    'ECG',
    
    # 4 EOG Channels                            
    'EOG1', 'EOG2', 'EOG3', 'EOG4' 
]

NUM_CHANNELS: int = len(MED_COLUMNS)
RAW_CHANNEL_NAMES: List[str] = [f'ch_{i}' for i in range(NUM_CHANNELS)]

CHANNEL_MAP: Dict[str, str] = dict(zip(RAW_CHANNEL_NAMES, MED_COLUMNS))

# ===================================================
# 5. Sotrage settings
# ===================================================

PARQUET_ENGINE: str = "pyarrow"
PARQUET_COMPRESSION: str = "snappy"

# ===================================================
# 6. Helper functions
# ===================================================

def get_subject_parquet_path(subject_id: int, limit_subjects: Optional[int] = None) -> Path:
    return DATA_DIR / f"data_sub_{subject_id:02d}.parquet"

def get_subject_npz_path(subject_id: int) -> Path:
    return DATA_DIR / f"data_sub_{subject_id:02d}.npz"

def get_all_parquet_files() -> List[Path]:
    return sorted(list(DATA_DIR.glob("data_sub_*.parquet")))

def get_all_npz_files() -> List[Path]:
    return sorted(list(DATA_DIR.glob("data_sub_*.npz")))

def get_eeg_channel_names() -> List[str]:
    return MED_COLUMNS[:59]