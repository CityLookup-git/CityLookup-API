from flask import Flask
import pandas as pd

app = Flask(__name__)

# Sample data for demonstration
data = {'Column 1': ['This', 'is', 'pandas', 'working!'],
        'Column 2': ['Some', 'sample', 'data', 'here']}

@app.route('/')
def index():
    # Create a DataFrame from the sample data
    df = pd.DataFrame(data)
    
    # Convert the DataFrame to an HTML table
    table_html = df.to_html(classes='table table-striped')
    
    # Create an HTML page with the table
    html = f"""
    <html>
    <head>
        <title>CityLookup</title>
    </head>
    <body>
        <h1>Pandas Test</h1>
        {table_html}
    </body>
    </html>
    """
    
    return html

if __name__ == '__main__':
    app.run(debug=True)
