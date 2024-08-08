
from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from fuzzywuzzy import fuzz

app = Flask(__name__)

# Load the dataset
file_path = r'C:\Users\rsv5r\Downloads\phone_data.xlsx'
sheet_name = 'Sheet1'
df = pd.read_excel(file_path, sheet_name=sheet_name)

# Define a function for fuzzy string matching
def fuzzy_match(input_str, options):
    options = [str(option) for option in options if pd.notna(option)]
    return max(options, key=lambda x: fuzz.token_set_ratio(input_str, x.lower()))

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        return redirect(url_for('result',
                                brand=request.form['brand'],
                                model=request.form['model'],
                                color=request.form['color'],
                                storage=request.form['storage']))

    return render_template('index.html')

@app.route('/result')
def result():
    # Get user input from the URL parameters
    brand = request.args.get('brand', '').strip().lower()
    model = request.args.get('model', '').strip().lower()
    color = request.args.get('color', '').strip().lower()
    storage = request.args.get('storage', '').strip().lower()

    # Filter the dataframe based on user input using a case-insensitive search
    filtered_df = df[
        (df["Phone Name"].str.lower().str.contains(brand))
        & (df["Model"].str.lower().str.contains(model))
        & (df["Color"].str.lower().str.contains(color))
        & (df["Storage"].str.lower() == storage)
    ]

    # If no exact match is found, use fuzzy string matching to find the most similar entry
    if filtered_df.empty:
        string_df = df[df["Phone Name"].apply(lambda x: isinstance(x, str))]
        scores = [fuzz.ratio(brand, entry.lower()) for entry in string_df["Phone Name"]]
        best_match_index = scores.index(max(scores))
        filtered_df = df.iloc[[best_match_index]]

    # Initialize prices
    price, flipkart_price, croma_price = None, None, None

    # Extract prices
    if not filtered_df.empty:
        try:
            price = filtered_df['Price'].values[0]
        except IndexError:
            pass

        try:
            flipkart_price = filtered_df['Flipkart1.Price'].values[0]
        except IndexError:
            pass

        try:
            croma_price = filtered_df['croma1.Price'].values[0]
        except (IndexError, KeyError):
            pass

    return render_template('result.html', brand=brand, model=model, color=color, storage=storage, price=price, flipkart_price=flipkart_price, croma_price=croma_price)

if __name__ == '__main__':
    app.run(debug=True)
