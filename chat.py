import google.generativeai as genai

GOOGLE_API_KEY='AIzaSyAsYBejM5VCkzq3aov8VJhing5_sNYPtao'
genai.configure(api_key=GOOGLE_API_KEY)

def get_response(msg):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content(msg)
    return response
