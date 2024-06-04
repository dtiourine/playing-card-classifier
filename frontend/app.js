function uploadImage() {
    const fileInput = document.getElementById('fileInput');
    const resultText = document.getElementById('resultText');

    if (fileInput.files.length > 0) {
        const file = fileInput.files[0];
        const formData = new FormData();
        formData.append("file", file);

        fetch('http://localhost:8000/predict', {
            method: 'POST',
            body: formData
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error('Network response was not ok: ' + response.statusText);
                }
                return response.json();
            })
            .then(data => {
                // Directly setting the text content to the prediction value
                resultText.textContent = 'Classification: ' + data.prediction;
            })
            .catch(error => {
                // Displaying the error message
                resultText.textContent = 'Error: ' + error.message;
            });
    } else {
        resultText.innerHTML = 'Please select a file to upload.';
    }
}