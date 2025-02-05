async function convertPace() {
    const value = parseFloat(document.getElementById('paceValue').value);
    const type = document.getElementById('conversionType').value;
    const resultDiv = document.getElementById('paceResult');

    if (!value || value <= 0) {
        resultDiv.innerHTML = '<span class="error">Vänligen ange ett giltigt positivt nummer</span>';
        return;
    }

    try {
        const response = await fetch('/convert_pace', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ value, type })
        });

        const data = await response.json();

        if (response.ok) {
            resultDiv.innerHTML = `Resultat: ${data.result}`;
        } else {
            resultDiv.innerHTML = `<span class="error">${data.error}</span>`;
        }
    } catch (error) {
        resultDiv.innerHTML = '<span class="error">Ett fel uppstod under beräkningen</span>';
    }
}

async function calculateInterest() {
    const principal = parseFloat(document.getElementById('principal').value);
    const monthlyContribution = parseFloat(document.getElementById('monthlyContribution').value);
    const rate = parseFloat(document.getElementById('rate').value);
    const years = parseInt(document.getElementById('years').value);

    const resultDiv = document.getElementById('interestResult');
    const plotContainer = document.getElementById('plotContainer');

    if (!principal || !monthlyContribution || !rate || !years || 
        principal < 0 || monthlyContribution < 0 || rate < 0 || years <= 0) {
        resultDiv.innerHTML = '<span class="error">Vänligen ange giltiga positiva nummer</span>';
        plotContainer.style.display = 'none';
        return;
    }

    try {
        const response = await fetch('/calculate_interest', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                principal,
                monthlyContribution,
                rate,
                years
            })
        });

        const data = await response.json();

        if (response.ok) {
            const formattedAmount = parseInt(data.finalAmount).toString().replace(/\B(?=(\d{3})+(?!\d))/g, " ");
            resultDiv.innerHTML = `Slutbelopp: ${formattedAmount} SEK`;
            document.getElementById('investmentPlot').src = `data:image/png;base64,${data.plotData}`;
            plotContainer.style.display = 'block';
        } else {
            resultDiv.innerHTML = `<span class="error">${data.error}</span>`;
            plotContainer.style.display = 'none';
        }
    } catch (error) {
        resultDiv.innerHTML = '<span class="error">Ett fel uppstod under beräkningen</span>';
        plotContainer.style.display = 'none';
    }
}

// Add input validation on enter key
document.querySelectorAll('input').forEach(input => {
    input.addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            if (this.closest('.card').querySelector('h2').textContent.includes('Tempo')) {
                convertPace();
            } else {
                calculateInterest();
            }
        }
    });
});