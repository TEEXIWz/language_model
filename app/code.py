import re
import pickle
language = {0:"Arabic", 1:"Danish", 2:"Dutch", 3:"English",
            4:"French", 5:"German", 6:"Greek", 7:"Hindi",
            8:"Italian", 9:"Kannada", 10:"Malayalam",
            11:"Portugeese", 12:"Russian", 13:"Spanish",
            14:"Sweedish", 15:"Tamil", 16:"Turkish"}
def predict_language(model,cv,text):
    text_1 = re.sub(r'[!@#$%^&*(),:;0-9,\n]',' ',text)
    text_2 = text_1.lower()
    x = cv.transform([text_2])
    lang = model.predict(x)
    return language[lang[0]]