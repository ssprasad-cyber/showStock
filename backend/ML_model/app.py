import yfinance as yf
from datetime import datetime, timedelta
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

def get_start_date(symbol):
    try:
        stock_info = yf.Ticker(symbol)
        hist = stock_info.history(period="max")
        
        # Ensure there's enough historical data for training
        if len(hist) == 0 or hist.index[0].year < (datetime.now().year - 10):
            # If less than 10 years of data available, use a fallback date
            ten_years_ago = datetime.now() - timedelta(days=9 * 365)
            return ten_years_ago.strftime('%Y-%m-%d')
        
        return hist.index[0].strftime('%Y-%m-%d')
    
    except Exception as e:
        raise ValueError(f"Error fetching data for {symbol}: {str(e)}")

def predict_stock_price(symbol):
    try:
        start_date = get_start_date(symbol)
        end_date = datetime.now().strftime('%Y-%m-%d')
        data = yf.download(symbol, start=start_date, end=end_date)

        data['Date'] = data.index
        data['Ordinal Date'] = data['Date'].apply(lambda x: x.toordinal())
        X = np.array(data['Ordinal Date']).reshape(-1, 1)
        y = np.array(data['Close'])

        model = LinearRegression()
        model.fit(X, y)

        # Predict today's price and next day's price
        today = datetime.now().toordinal()
        predict_today = model.predict([[today]])[0]
        
        next_day = datetime.now() + timedelta(days=1)
        next_day_ordinal = next_day.toordinal()
        predicted_price = model.predict([[next_day_ordinal]])[0]

        y_pred = model.predict(X)
        r2 = r2_score(y, y_pred)

        current_price = data['Close'][-1]
        
        # Calculate potential gain or loss
        g_l = "loss" if predicted_price < predict_today else "profit"
        predicted_priced = predicted_price + (current_price - predict_today)

        prediction_data = {
            'Date': datetime.now().strftime('%Y-%m-%d'),
            'Current Price': float(current_price),
            'Predicted Date': next_day.strftime('%Y-%m-%d'),
            'Predicted Price': float(predicted_priced),
            'Predicted Value': g_l,
            'Accuracy': str(round(r2 * 100)) + "%"
        }

        return prediction_data
    
    except Exception as e:
        return {'error': str(e)}

@app.route('/')
def index():
    return render_template('prediction.html')

@app.route('/predict_stock', methods=['GET'])
def predict_stock():
    symbol = request.args.get('symbol')
    if not symbol:
        return jsonify({'error': 'Symbol is required'})

    prediction = predict_stock_price(symbol)
    return jsonify(prediction)

if __name__ == '__main__':
    app.run(debug=True)
