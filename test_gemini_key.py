import google.generativeai as genai

genai.configure(api_key="AIzaSyAKgn0Tm2dSBkuIhZhB6wGt4rTzDx9vYGs")

try:
    models = genai.list_models()
    for m in models:
        print(m.name, m.supported_generation_methods)
except Exception as e:
    print("❗API 金鑰錯誤或未啟用:", e)
