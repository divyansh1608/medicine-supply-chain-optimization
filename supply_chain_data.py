import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import random

# Generate a synthetic dataset mimicking Kaggle's Pharma Supply Chain data
np.random.seed(42)
hubs = ['Varanasi North', 'Varanasi South', 'Delhi Central', 'Mumbai East', 'Bangalore Hub']
medicines = ['Amoxicillin', 'Paracetamol', 'Azithromycin', 'Ibuprofen', 'Ciprofloxacin', 'Metformin']

data = []
for _ in range(500):
    hub = random.choice(hubs)
    med = random.choice(medicines)
    # Create some intentional stockouts (0) and normal stock
    stock = np.random.choice([0, random.randint(10, 500)], p=[0.15, 0.85])
    # Create expiration dates ranging from 10 days ago to 200 days in the future
    days_to_expire = random.randint(-10, 200)
    expiry_date = (datetime.now() + timedelta(days=days_to_expire)).strftime('%Y-%m-%d')
    
    data.append([hub, med, stock, expiry_date])

df = pd.DataFrame(data, columns=['Distribution_Hub', 'Medicine_Name', 'Current_Stock', 'Expiry_Date'])

# Save directly to your projects folder
output_path = '/Users/dk/Desktop/projects/pharma_inventory.csv'
df.to_csv(output_path, index=False)
print(f"Dataset ready! Saved to {output_path}")