# Show Stock

## Overview
"Show Stock" is a desktop application for stock market prediction and management. It allows users to paper trade on 500 companies with daily updates on stock prices via an API call. The application features a user-friendly interface and uses machine learning to predict stock prices, helping users make informed trading decisions.

## Features
- **User Management**: Create and manage user accounts.
- **Paper Trading**: Trade with virtual funds on 500 companies.
- **Daily Stock Updates**: Stock prices are updated once a day.
- **Transaction History**: Detailed records of past transactions.
- **Stock Analysis**: Access company details and market data.
- **Price Prediction**: Machine learning model for future stock prices.
- **Intuitive UI**: Built with React and styled with Bulma CSS.

## Technologies Used

### Electron.js
Builds cross-platform desktop applications using JavaScript, HTML, and CSS.

### SQLite3
Manages the local database, ensuring fast and reliable data storage.

### SQL.js
Interfaces SQLite with web applications using WebAssembly.

### React
Builds the user interface, ensuring a seamless user experience.

### Bulma CSS
Styles the application with a modern and responsive design.

### yfinance
Fetches historical stock data for the machine learning model.

### sklearn
Implements the machine learning model for stock price prediction.

### Flask
Creates the web server for the prediction model API.

### Flask-CORS
Handles Cross-Origin Resource Sharing for the API.

## Project Folder Structure
- **main.js**: Entry point for Electron application.
- **preload.js**: Preloads scripts for the application.
- **index.html**: Main HTML file for the application's UI.
- **backend**: Contains API functions and the SQLite database file.

## ER Diagram Attributes

### Users
- **UUID**: Unique user identifier
- **F_NAME**: First name
- **L_NAME**: Last name
- **EMAIL**: Email address
- **PASSWORD**: User password
- **DP_URI**: Display picture URI

### Funds
- **TUID**: Transaction user ID
- **ORDER_TYPE**: Type of order (buy/sell)
- **AMOUNT**: Amount of funds
- **DATE**: Date of transaction

### Transactions
- **TUID**: Transaction user ID
- **CUID**: Company user ID
- **DATE**: Date of transaction
- **QUANTITY**: Quantity of stocks
- **PRICE**: Price of stocks

### US_Companies
- **SYMBOL**: Stock symbol
- **NAME**: Company name
- **TOTAL_OUT_SHARES**: Total outstanding shares
- **DESCRIPTION**: Company description
- **MARKET_CAP**: Market capitalization

### IND_Companies
- **SYMBOL**: Stock symbol
- **CUID**: Company user ID
- **NAME**: Company name
- **TOTAL_OUT_SHARES**: Total outstanding shares
- **DESCRIPTION**: Company description
- **MARKET_CAP**: Market capitalization

### Company Indexes
- **CUID**: Company user ID
- **NAME**: Name of company

## Prediction Model
- **Libraries Used**: yfinance, datetime, sklearn, numpy, pandas, Flask, Flask-CORS
- **Model Type**: Linear Regression
- **Features**: Ordinal Date, Close Price
- **Training Process**: Fetch historical data, convert dates, train model
- **Prediction Process**: Predict today's and next day's prices, calculate potential gain/loss
- **API Endpoints**:
  - **/**: Main HTML page for predictions.
  - **/predict_stock**: Accepts a stock symbol and returns predicted prices and accuracy.

---
