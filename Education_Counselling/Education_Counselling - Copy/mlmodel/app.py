from flask import Flask, render_template, request, jsonify
import pickle
import numpy as np

app = Flask(__name__, static_url_path='/static')

with open('mlp_model.pkl', 'rb') as f:
    model = pickle.load(f)

def preprocess_input(data):
    categorical_mappings = {
        'self_learning': {'yes': 1, 'no': 0},
        'extra_courses': {'yes': 1, 'no': 0},
        'taken_inputs': {'yes': 1, 'no': 0},
        'management_or_technical': {'man': 0, 'tech': 1},
        'hard_smart_worker': {'hard': 0, 'smart': 1},
        'worked_in_teams': {'yes': 1, 'no': 0},
        'introvert': {'yes': 1, 'no': 0},
        'reading_and_writing_skills': {'poor': 0, 'medium': 1, 'excellent': 2},
        'memory_capability': {'poor': 0, 'medium': 1, 'excellent': 2},
        'interested_subjects': {
            'programming': 9, 'Management': 2, 'data engineering': 5, 'networks': 7, 'Software Engineering': 3,
            'cloud computing': 4, 'parallel computing': 8, 'IOT': 1, 'Computer Architecture': 0, 'hacking': 6
        },
        'interested_career_area': {
            'testing': 5, 'system developer': 4, 'Business process analyst': 0, 'security': 3,
            'developer': 2, 'cloud computing': 1
        },
        'company_type': {
            'BPA': 0, 'Cloud Services': 1, 'product development': 9, 'Testing and Maintainance Services': 7,
            'SAaS services': 4, 'Web Services': 8, 'Finance': 2, 'Sales and Marketing': 5, 'Product based': 3,
            'Service Based': 6
        },
        'interested_books': {
            'Series': 28, 'Autobiographies': 3, 'Travel': 29, 'Guide': 13, 'Health': 14, 'Journals': 17, 'Anthology': 1,
            'Dictionaries': 9, 'Prayer books': 21, 'Art': 2, 'Encyclopedias': 11, 'Religion-Spirituality': 22,
            'Action and Adventure': 0, 'Comics': 6, 'Horror': 16, 'Satire': 24, 'Self help': 27, 'History': 15,
            'Cookbooks': 7, 'Math': 18, 'Biographies': 4, 'Drama': 10, 'Diaries': 8, 'Science fiction': 26,
            'Poetry': 20, 'Romance': 23, 'Science': 25, 'Trilogy': 30, 'Fantasy': 12, 'Childrens': 5, 'Mystery': 19
        },
        'workshops': {
            'cloud computing': 0,
            'data science': 1,
            'database security': 2,
            'game development': 3,
            'hacking': 4,
            'system designing': 5,
            'testing': 6,
            'web technologies': 7,
        },
        'certifications': {
                    
            'app development': 0,
            'distro making': 1,
            'full stack': 2,
            'hadoop': 3,
            'information security': 4,
            'machine learning': 5,
            'python': 6,
            'r programming': 7,
            'shell programming': 8,
        }

    }

    processed_data = []

    processed_data.append(data['logical_quotient'])  
    processed_data.append(data['no_of_hackathons'])  
    processed_data.append(data['coding_skills'])  
    processed_data.append(data['public_speaking'])  

    processed_data.append(categorical_mappings['self_learning'].get(data['self_learning'], 0))  
    processed_data.append(categorical_mappings['extra_courses'].get(data['extra_courses'], 0))  

    # certifications = ['app development', 'distro making', 'full stack', 'hadoop', 'information security', 'machine learning', 'python', 'r programming', 'shell programming']
    # workshops = ['cloud computing', 'data science', 'database security', 'game development', 'hacking', 'system designing', 'testing', 'web technologies']
    
    processed_data.append(categorical_mappings['certifications'].get(data['certifications'], 0))  
    processed_data.append(categorical_mappings['workshops'].get(data['workshops'], 0))  


    processed_data.append(categorical_mappings['reading_and_writing_skills'].get(data['reading_and_writing_skills'], 1))
    processed_data.append(categorical_mappings['memory_capability'].get(data['memory_capability'], 1))

    processed_data.append(categorical_mappings['interested_subjects'].get(data['interested_subjects'], 0))
    processed_data.append(categorical_mappings['interested_career_area'].get(data['interested_career_area'], 0))
    processed_data.append(categorical_mappings['company_type'].get(data['company_type'], 0))
    processed_data.append(categorical_mappings['interested_books'].get(data['interested_books'], 0))

    # if(data['management_or_technical'] == 'yes'):
    processed_data.append(1)
    processed_data.append(0)

    processed_data.append(categorical_mappings['taken_inputs'].get(data['taken_inputs'], 0))

    # if(data['hard_smart_worker'] == 'yes'):
    processed_data.append(1)
    processed_data.append(0)

    processed_data.append(categorical_mappings['worked_in_teams'].get(data['worked_in_teams'], 0))
    processed_data.append(categorical_mappings['introvert'].get(data['introvert'], 0))

    return np.array(processed_data).reshape(1, -1)

@app.route('/')
def index():
    return jsonify({"message": "Hello, World!"})

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json()

        input_features = preprocess_input(data)

        prediction = model.predict(input_features)

        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True,port=5000)