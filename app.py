from flask import Flask, render_template, request, jsonify
import io
import base64
from utils import min_per_km_to_kmh, kmh_to_min_per_km, compound_interest, create_investment_plot

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert_pace', methods=['POST'])
def convert_pace():
    data = request.json
    value = float(data['value'])
    conversion_type = data['type']
    
    try:
        if conversion_type == 'minPerKmToKmh':
            result = min_per_km_to_kmh(value)
            return jsonify({'result': f'{result:.2f} km/h'})
        else:
            result = kmh_to_min_per_km(value)
            return jsonify({'result': f'{result:.2f} min/km'})
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

@app.route('/calculate_interest', methods=['POST'])
def calculate_interest():
    try:
        data = request.json
        principal = float(data['principal'])
        monthly_contribution = float(data['monthlyContribution'])
        rate = float(data['rate'])
        years = int(data['years'])
        
        final_amount, history = compound_interest(principal, monthly_contribution, rate, years)
        plot_data = create_investment_plot(history, years)
        
        return jsonify({
            'finalAmount': f'{final_amount:.2f}',
            'plotData': plot_data
        })
    except ValueError as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
