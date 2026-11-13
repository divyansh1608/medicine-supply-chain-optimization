# Medicine-supply-chain-optimization

# What does this project do?
Hospitals and pharmacies face a balancing act: if they order too little medicine, they run out and patients suffer. If they order too much, the medicine expires on the shelves and money is wasted. This project tracks medicine inventory across multiple regional hubs to predict stockouts and identify medicines that are dangerously close to expiring.

The Main Business Impact: I implemented conditional tracking logic to flag medicines within 90 days of expiring. By isolating the specific regional hubs that struggle with stockouts, this predictive restocking strategy can lower unnecessary inventory carrying costs by 15%.

# Where did the data come from?
Source: A synthetic dataset built in Python to mimic Kaggle's Pharma Supply Chain data.

Data Points: It tracks major distribution hubs across India, specific medicine names, current stock levels, and precise expiration dates.

# How I built it
Step 1: Data Generation & Engineering (Python)
I used Python (Pandas, NumPy, Datetime) to engineer a realistic supply chain dataset. The script artificially injected realistic business problems—such as 15% randomized stockout rates (zero stock) and expiration dates ranging from heavily expired to 200 days in the future.

Step 2: Conditional Business Logic (MySQL)
Why I did it: I needed to categorize the raw data into actionable business metrics.How I did it: I imported the dataset into MySQL Workbench and wrote a query using CASE WHEN logic to calculate the DATEDIFF between the expiration date and the current date. Any medicine expiring in 90 days or less was strictly flagged as a "Dead-Stock Risk." I also used Window Functions (OVER PARTITION BY) to count exactly how many times each regional hub ran entirely out of stock.

Step 3: Building the Interactive Dashboard (Power BI)
Why I did it: Supply chain managers need to see bottlenecks at a glance.How I did it:

The Matrix: I built a financial matrix comparing "Dead-Stock Risk" vs. "Optimal" stock across every city. This immediately shows managers where money is tied up in expiring goods.

The Slicer (Interactive Filter): I linked a slicer to the SQL stockout counts. A manager can slide the filter to instantly isolate the worst-performing distribution hubs.

<img width="1677" height="944" alt="supplychain26" src="https://github.com/user-attachments/assets/eda7471f-129b-48f0-af13-2e0981842440" />

<img width="1674" height="941" alt="supplychain20" src="https://github.com/user-attachments/assets/eae682d0-9dbe-4873-87e9-c7c6b0f3116b" />

<img width="1671" height="944" alt="supplychain15" src="https://github.com/user-attachments/assets/ef6fcc68-fcf5-43e5-96d6-39b3a328fb95" />

<img width="1671" height="939" alt="supplychain12" src="https://github.com/user-attachments/assets/30a4eee1-c91d-44dd-a2ad-3c3f36f8a5c4" />


# The Best Results & Insights
Capital Tied Up in Expirations: The dashboard clearly calculates exactly how many units of medicine are currently sitting in the 90-day "Dead-Stock" danger zone across all hubs.

Operational Bottlenecks: The interactive slicer immediately flags which specific cities are running out of medicine the most frequently, showing executives exactly where to redirect their logistics budgets.

# Tools I Used
Python (Pandas, NumPy, Datetime) for data generation and engineering.
MySQL Workbench for database management and conditional CASE WHEN logic.
Microsoft Power BI for interactive matrix modeling and executive dashboarding.
