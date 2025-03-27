import google.generativeai as genai

GEMINI_API_KEY = "AIzaSyCETBi_6UT5zVuu6JvjcuQU4l8IiPHCxxM"  # Put your real API key here
genai.configure(api_key=GEMINI_API_KEY)

models = genai.list_models()
for model in models:
    print(model.name)
