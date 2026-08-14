const checkButton = document.getElementById("checkButton");

const newsText = document.getElementById("newsText");

const resultBox = document.getElementById("resultBox");

const prediction = document.getElementById("prediction");

const confidence = document.getElementById("confidence");

const errorBox = document.getElementById("errorBox");

const errorMessage = document.getElementById("errorMessage");

const loading = document.getElementById("loading");


checkButton.addEventListener("click", async function () {

    const text = newsText.value.trim();


    // Check empty input

    if (!text) {

        showError("Please enter a news article.");

        return;

    }


    // Hide previous results

    resultBox.classList.add("hidden");

    errorBox.classList.add("hidden");


    // Show loading

    loading.classList.remove("hidden");

    checkButton.disabled = true;


    try {

        // Send request to Flask backend

        const response = await fetch("/predict", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                text: text

            })

        });


        const data = await response.json();


        if (!response.ok) {

            throw new Error(
                data.error || "Something went wrong."
            );

        }


        // Show prediction

        prediction.textContent =
            "Prediction: " + data.prediction;


        // Show confidence

        if (data.confidence !== null) {

            confidence.textContent =
                data.confidence;

        } else {

            confidence.textContent =
                "N/A";

        }


        // Remove old classes

        resultBox.classList.remove(
            "success",
            "fake"
        );


        // Add class according to prediction

        if (data.prediction === "REAL") {

            resultBox.classList.add("success");

        } else {

            resultBox.classList.add("fake");

        }


        resultBox.classList.remove("hidden");


    } catch (error) {

        showError(error.message);

    }


    // Hide loading

    loading.classList.add("hidden");

    checkButton.disabled = false;

});


function showError(message) {

    errorMessage.textContent = message;

    errorBox.classList.remove("hidden");

}