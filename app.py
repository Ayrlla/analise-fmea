from flask import Flask, render_template, request
from data import fault_data

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', faults=fault_data.keys())

@app.route('/diagnose', methods=['POST'])
def diagnose():
    fault_effect = request.form.get('fault_effect')
    measurements = list(map(float, request.form.get('measurements').split(',')))
    
    avg_measurement = sum(measurements) / len(measurements) if measurements else 0
    diagnosis, actions = get_diagnosis(fault_effect, avg_measurement)

    return render_template('result.html', 
                           fault_effect=fault_effect,
                           avg_measurement=avg_measurement, 
                           diagnosis=diagnosis, 
                           actions=actions)

def get_diagnosis(fault_effect, avg_measurement):
    # Simplified logic for demo purposes
    fault_info = fault_data.get(fault_effect, {})
    causes = fault_info.get('causes', [])
    diagnosis = "Bom" if avg_measurement > 2 else "Ruim"
    actions = fault_info.get('actions', {})
    return diagnosis, actions

if __name__ == '__main__':
    app.run(debug=True)
