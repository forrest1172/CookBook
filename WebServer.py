from flask import Flask , render_template, request
import json
app = Flask(__name__)

commonIngredients = {

  'aromatic veggies':['onions','garlic','carrots','celery','jalapeno'],

  'herbs':['cilantro','parsley','dill','basil'],

  'other veggies':['potatoes','bell peppers','lettuce','tomatoes'],

  'acidity':['lemon','lime','vinegar'],
  'protein':['chicken thighs','ground beef','salomn','eggs'],
  'dariy':['milk','butter','cheddar cheese','yogurt','parmesan cheese'],
  'pantry':['pasta','white rice','canned black beans'],
  'misc':['vanilla extract','flour','sugar','breadcrumbs']
}

@app.route('/')
def index():
    return render_template("./index.html")

@app.route('/', methods=['POST'])
def my_form():
    textData = request.form.getlist('instruct')
    for submittedWord in textData:
            if(isinstance(submittedWord,str) == True):
                print(submittedWord)
                for ingredType, ingred in commonIngredients.items():
                    for word in ingred:
                        #print(word)
                        if(submittedWord == word):
                            print(f'the word {submittedWord} is already in ingred list')
                            continue
                        else:
                            commonIngredients['misc'] = word
                            print(commonIngredients)
            else:
                print("not a string")
    
        

    saveData(textData)
    return render_template("./index.html")


def saveData(data):
    with open('ingredient_data.json', 'a') as f:
        json.dump(data, f)
        return

if __name__ == '__main__':
    print('Running!')
    app.run(debug=True, port=5000, host='192.168.31.179')



