async function checkAllergens() {
    const data = {
        "Food Product": document.getElementById('food_product').value,
        "Main Ingredient": document.getElementById('main_ingredient').value,
        "Sweetener": document.getElementById('sweetener').value,
        "Fat/Oil": document.getElementById('fat_oil').value,
        "Seasoning": document.getElementById('seasoning').value,
        "Allergens": document.getElementById('allergens').value,
    };

    const response = await fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
    });

    const result = await response.json();
    document.getElementById('result').innerText = `Prediction: ${result.prediction}`;
}
