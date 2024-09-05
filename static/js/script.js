// static/js/script.js

// Funcția de validare pentru procentaj
function validatePercentage(input) {
    const validValues = [100.0, 0.0, 50.0, 33.33, 66.66];
    if (!validValues.includes(parseFloat(input.value))) {
        input.setCustomValidity('Please enter a valid percentage: 100.0, 0.0, 50.0, 33.33, or 66.66');
    } else {
        input.setCustomValidity(''); // Resetează mesajul de validare
    }
}


document.getElementById("prediction-form").addEventListener("submit", function(event) {
    event.preventDefault();

    // Colectarea datelor din formular
    let data = {
        "team": document.getElementById("team").value,
        "opponent": document.getElementById("opponent").value,
        "venue": document.getElementById("venue").value,
        "category difference": parseInt(document.getElementById("category-difference").value),
        "win percentage in last 3": parseFloat(document.getElementById("win-percentage").value),
        "draw percentage in last 3": parseFloat(document.getElementById("draw-percentage").value),
        "loss percentage in last 3": parseFloat(document.getElementById("loss-percentage").value),
        "win percentage in last 3 opponent": parseFloat(document.getElementById("win-percentage-opponent").value),
        "draw percentage in last 3 opponent": parseFloat(document.getElementById("draw-percentage-opponent").value),
        "loss percentage in last 3 opponent": parseFloat(document.getElementById("loss-percentage-opponent").value)
    };

    // Trimiterea datelor la serverul Flask
    fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    })
    .then(response => response.json())
    .then(data => {
        // Afișarea rezultatului predicției
        document.getElementById("result").innerText = "Predicted Result: " + data.result;
    })
    .catch(error => console.error("Error:", error));
});
