import os
import shutil
from datetime import datetime

def copy_local_csv():
    # Path to the original file on your laptop
    original_file_path = "/Users/abdirahman/Downloads/datasets/Untransformed_Global_retailer.csv"
    
    # Destination directory
    destination_dir = "assets/datasets/Original_file"
    os.makedirs(destination_dir, exist_ok=True)

    # Generate timestamped filename
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    destination_file = f"Untransformed_Global_retailer_{timestamp}.csv"
    destination_path = os.path.join(destination_dir, destination_file)

    # Copy file
    shutil.copy2(original_file_path, destination_path)
    print(f"✅ File copied to: {destination_path}")


if __name__ == "__main__":
    copy_local_csv()