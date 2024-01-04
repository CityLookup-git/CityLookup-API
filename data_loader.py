import pandas as pd

# Sample data for demonstration
data = {'Column 1': ['This', 'is', 'pandas', 'working!'],
        'Column 2': ['Some', 'sample', 'data', 'here']}

# Create a DataFrame from the sample data
df = pd.DataFrame(data)
    
# Convert the DataFrame to an HTML table
table_html = df.to_html(classes='table table-striped')