function calculateProfitLoss() {
    const currentPrice = parseFloat(document.getElementById('currentPrice').value);
    const buyBackPrice = parseFloat(document.getElementById('buyBackPrice').value);

    if (isNaN(currentPrice) || isNaN(buyBackPrice)) {
        document.getElementById('result').textContent = "Please enter valid numbers!";
        return;
    }
    const difference = buyBackPrice - currentPrice;
    const percentage = (difference / currentPrice) * 100;
    if (difference > 0) {
        document.getElementById('result').textContent = `Profit: ${percentage.toFixed(2)}%`;
    } else if (difference < 0) {
        document.getElementById('result').textContent = `Loss: ${Math.abs(percentage).toFixed(2)}%`;
    } else {
        document.getElementById('result').textContent = "No Profit, No Loss.";
    }
}