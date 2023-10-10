
import sys
from pathlib import Path

my_script_folder = Path(__file__).resolve().parent
my_parent_folder = str(my_script_folder.parent)
sys.path.insert(1, my_parent_folder)
