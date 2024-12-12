from bs4 import BeautifulSoup
import os
import csv
import re

def process_lake_data(input_folder, output_csv):
    """
    Process all HTML files in the input folder and create a CSV with lake data.
    
    Args:
        input_folder (str): Path to folder containing HTML files
        output_csv (str): Path where the output CSV file should be saved
    """
    # List to store all data
    data_rows = []
    
    # Process each HTML file in the folder
    for filename in os.listdir(input_folder):
        if filename.endswith('.html'):
            file_path = os.path.join(input_folder, filename)
            
            # Extract ID from filename (remove 'a' prefix and .html extension)
            file_id = filename.replace('a', '').replace('.html', '')
            
            with open(file_path, 'r', encoding='utf-8') as file:
                soup = BeautifulSoup(file.read(), 'html.parser')
                
                # Extract volume (remove negative sign)
                volume_text = soup.find(text=re.compile(r'Volume:'))
                volume = float(volume_text.split(':')[1].strip().split()[0])
                volume = abs(volume)  # Remove negative sign
                
                # Extract area
                area_text = soup.find(text=re.compile(r'Area:'))
                area = float(area_text.split(':')[1].strip().split()[0])
                
                # Add to data rows
                data_rows.append([file_id, f"{volume:.2f}", area])
    
    # Sort by file_id
    data_rows.sort(key=lambda x: float(x[0]))
    
    # Write to CSV
    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File ID', 'Volume', 'Area (m²)'])
        writer.writerows(data_rows)

# Example usage:
if __name__ == "__main__":
    # Use relative paths from the workspace root
    current_dir = os.path.dirname(os.path.abspath(__file__))
    input_folder = os.path.join(current_dir, "html_files")  # Assuming HTML files are in a folder named 'html_files'
    output_csv = os.path.join(current_dir, "lake_data.csv")  # CSV will be created in the same directory as the script
    
    # Create input folder if it doesn't exist
    os.makedirs(input_folder, exist_ok=True)
    
    process_lake_data(input_folder, output_csv)