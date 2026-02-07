const submitBtn = document.getElementById('submit-btn');
const inputBox = document.getElementById('input');
const outputBox = document.getElementById('output');


submitBtn.addEventListener('click', () => {
    const url = 'http://localhost:8000/generate'
    const body = {
        input: inputBox.value
    }

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(body)
    })
        .then(response => {
            if (!response.ok) {
                throw new Error(`Network Error: ${response.status}`)
            }
            return response.json()
        })
        .then(data => {
            outputBox.textContent = JSON.stringify(data.output, null, 2)
        })
        .catch(error => {
            console.error('Error: ', error)
        })

});