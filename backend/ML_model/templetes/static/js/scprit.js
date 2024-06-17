function predictStockPrice() {
    const symbol = document.getElementById('symbolInput').value;
    if (!symbol) {
        alert('Please enter a stock symbol');
        return;
    }

    fetch(`http://127.0.0.1:5000/predict_stock?symbol=${symbol}`)
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById('result').innerHTML = `<p>${data.error}</p>`;
            } else {
                document.getElementById('result').innerHTML = `
                    <p>Current Price: $${data['Current Price'].toFixed(2)}</p>
                    <p>Predicted Price on ${data['Predicted Date']}: $${data['Predicted Price'].toFixed(2)}</p>
                    <p>Prediction: ${data['Predicted Value']}</p>
                    <p>Accuracy: ${data['Accuracy']}</p>
                `;
            }
        })
        .catch(error => {
            console.error('Error:', error);
        });
}
