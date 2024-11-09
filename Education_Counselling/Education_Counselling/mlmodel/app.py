import streamlit as st
import pickle
import numpy as np

# Load the model
with open('mlp_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Define the preprocessing function
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
    processed_data.append(categorical_mappings['certifications'].get(data['certifications'], 0))
    processed_data.append(categorical_mappings['workshops'].get(data['workshops'], 0))
    processed_data.append(categorical_mappings['reading_and_writing_skills'].get(data['reading_and_writing_skills'], 1))
    processed_data.append(categorical_mappings['memory_capability'].get(data['memory_capability'], 1))

    processed_data.append(categorical_mappings['interested_subjects'].get(data['interested_subjects'], 0))
    processed_data.append(categorical_mappings['interested_career_area'].get(data['interested_career_area'], 0))
    processed_data.append(categorical_mappings['company_type'].get(data['company_type'], 0))
    processed_data.append(categorical_mappings['interested_books'].get(data['interested_books'], 0))

    processed_data.append(1)  # management_or_technical (always 1 as per code)
    processed_data.append(0)  # management_or_technical (always 0 as per code)

    processed_data.append(categorical_mappings['taken_inputs'].get(data['taken_inputs'], 0))

    processed_data.append(1)  # hard_smart_worker (always 1 as per code)
    processed_data.append(0)  # hard_smart_worker (always 0 as per code)

    processed_data.append(categorical_mappings['worked_in_teams'].get(data['worked_in_teams'], 0))
    processed_data.append(categorical_mappings['introvert'].get(data['introvert'], 0))

    return np.array(processed_data).reshape(1, -1)

# Streamlit UI
st.title("Prediction Model")

# Input form
logical_quotient = st.number_input("Logical Quotient", min_value=0)
no_of_hackathons = st.number_input("Number of Hackathons", min_value=0)
coding_skills = st.number_input("Coding Skills", min_value=0)
public_speaking = st.number_input("Public Speaking", min_value=0)

self_learning = st.selectbox("Self Learning", ['yes', 'no'])
extra_courses = st.selectbox("Extra Courses", ['yes', 'no'])
certifications = st.selectbox("Certifications", ['app development', 'distro making', 'full stack', 'hadoop', 'information security', 'machine learning', 'python', 'r programming', 'shell programming'])
workshops = st.selectbox("Workshops", ['cloud computing', 'data science', 'database security', 'game development', 'hacking', 'system designing', 'testing', 'web technologies'])
reading_and_writing_skills = st.selectbox("Reading and Writing Skills", ['poor', 'medium', 'excellent'])
memory_capability = st.selectbox("Memory Capability", ['poor', 'medium', 'excellent'])
interested_subjects = st.selectbox("Interested Subjects", ['programming', 'Management', 'data engineering', 'networks', 'Software Engineering', 'cloud computing', 'parallel computing', 'IOT', 'Computer Architecture', 'hacking'])
interested_career_area = st.selectbox("Interested Career Area", ['testing', 'system developer', 'Business process analyst', 'security', 'developer', 'cloud computing'])
company_type = st.selectbox("Company Type", ['BPA', 'Cloud Services', 'product development', 'Testing and Maintainance Services', 'SAaS services', 'Web Services', 'Finance', 'Sales and Marketing', 'Product based', 'Service Based'])
interested_books = st.selectbox("Interested Books", ['Series', 'Autobiographies', 'Travel', 'Guide', 'Health', 'Journals', 'Anthology', 'Dictionaries', 'Prayer books', 'Art', 'Encyclopedias', 'Religion-Spirituality', 'Action and Adventure', 'Comics', 'Horror', 'Satire', 'Self help', 'History', 'Cookbooks', 'Math', 'Biographies', 'Drama', 'Diaries', 'Science fiction', 'Poetry', 'Romance', 'Science', 'Trilogy', 'Fantasy', 'Childrens', 'Mystery'])
management_or_technical = 'tech'  # Assuming 'tech' for simplicity
taken_inputs = st.selectbox("Taken Inputs", ['yes', 'no'])
worked_in_teams = st.selectbox("Worked in Teams", ['yes', 'no'])
introvert = st.selectbox("Introvert", ['yes', 'no'])

# Prepare data
data = {
    'logical_quotient': logical_quotient,
    'no_of_hackathons': no_of_hackathons,
    'coding_skills': coding_skills,
    'public_speaking': public_speaking,
    'self_learning': self_learning,
    'extra_courses': extra_courses,
    'certifications': certifications,
    'workshops': workshops,
    'reading_and_writing_skills': reading_and_writing_skills,
    'memory_capability': memory_capability,
    'interested_subjects': interested_subjects,
    'interested_career_area': interested_career_area,
    'company_type': company_type,
    'interested_books': interested_books,
    'management_or_technical': management_or_technical,
    'taken_inputs': taken_inputs,
    'worked_in_teams': worked_in_teams,
    'introvert': introvert,
}

# Predict when user clicks 'Submit'
if st.button('Submit'):
    preprocessed_data = preprocess_input(data)
    prediction = model.predict(preprocessed_data)
    st.write(f"Prediction: {prediction[0]}")
    # Button with anchor tag (open link in a new tab)
    var = "https://education-counselling-steel.vercel.app/kaushan_detail.html"
    if(prediction[0]=="CRM Technical Developer"):
        var = "https://education-counselling-steel.vercel.app/techdev.html"
    elif(prediction[0]=="Database Developer"):
        var = "https://education-counselling-steel.vercel.app/database.html"

    elif(prediction[0]=="Mobile Applications Developer"):
        var = "https://education-counselling-steel.vercel.app/mobapp.html"

    elif(prediction[0]=="Network Security Engineer"):
        var = "https://education-counselling-steel.vercel.app/network.html"

    elif(prediction[0]=="Software Developer"):
        var = "https://education-counselling-steel.vercel.app/software.html"

    elif(prediction[0]=="Software Engineer"):
        var = "https://education-counselling-steel.vercel.app/network.html"

    elif(prediction[0]=="Software Quality Assurance (QA) / Testing"):
        var = "https://education-counselling-steel.vercel.app/database.html"
    elif(prediction[0]=="Systems Security Administrator"):
        var = "https://education-counselling-steel.vercel.app/techdev.html"

    elif(prediction[0]=="Technical Support"):
        var = "https://education-counselling-steel.vercel.app/database.html"

    elif(prediction[0]=="UX Designer"):
        var = "https://education-counselling-steel.vercel.app/software.html"

    elif(prediction[0]=="Web Developer"):
        var = "https://education-counselling-steel.vercel.app/database.html"

    else:
        var = "https://education-counselling-steel.vercel.app/software.html"
    st.markdown(
        f"<a href={var} target='_blank'><button style='background-color: #4CAF50; color: white; padding: 10px; border: none; cursor: pointer;'>Go to Link</button></a>",
        unsafe_allow_html=True
    )   
# , CRM Technical Developer, Database Developer, Mobile Applications Developer, Network Security Engineer, Software Developer, Software Engineer, Software Quality Assurance (QA) / Testing, Systems Security Administrator, Technical Support, UX Designer, Web Developer