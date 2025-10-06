#------------Data Ingestion Config Entity------------------------------------

from pathlib import Path
from dataclasses import dataclass
#step3)update the entity file --->is nothing we r defining the class variable
#which was used in yaml file and futhure taking rtn as function

@dataclass
class DataIngestionConfig():
    #defining class variable along with dtypes
    root_dir_path:Path
    train_test_path: Path
    raw_file_path:Path
