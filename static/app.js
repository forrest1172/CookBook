const instructEl = document.getElementById("instructions");
const ingredientsEl = document.getElementById("ingredients");

let commonIngredients = {

  'aromatic veggies':['onions','garlic','carrots','celery','jalapeno'],

  herbs:['cilantro','parsley','dill','basil'],

  'other veggies':['potatoes','bell peppers','lettuce','tomatoes'],

  acidity:['lemon','lime','vinegar'],
  protein:['chicken thighs','ground beef','salomn','eggs'],
  dariy:['milk','butter','cheddar cheese','yogurt','parmesan cheese'],
  pantry:['pasta','white rice','canned black beans'],
  misc:['vanilla extract','flour','sugar','breadcrumbs']

};



function NewInstruction() {
  const liEl = document.createElement("li");
  const inputEl = document.createElement("input");
  inputEl.setAttribute("type", "text");
  inputEl.setAttribute('name','instruct');
  liEl.appendChild(inputEl);
  instructEl.appendChild(liEl);
}

function DeleteLastStruct() {
  instructEl.lastChild.remove();
}

function NewIngredient() {
  const liEl = document.createElement("li");
  const inputEl = document.createElement("input");
  inputEl.setAttribute("type", "text");
  liEl.appendChild(inputEl);
  ingredientsEl.appendChild(liEl);
}

function DeleteLastIngred() {
  ingredientsEl.lastChild.remove();
}
