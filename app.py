from flask import Flask
from data_loader import table_html

app = Flask(__name__)

@app.route('/')
def index():
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
