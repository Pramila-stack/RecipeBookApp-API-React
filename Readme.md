# import React, { useEffect, useState } from "react";
👉 You are importing React tools:
React → core library (needed to build UI)
useState → stores data (like variables in React)
useEffect → runs code automatically when page loads

# import axios from "axios";
👉 Axios is used to talk to your backend API
GET data from Django
POST data to Django

# function App() {
👉 This creates your main React component
Everything inside App() = your website page

# const [recipes, setRecipes] = useState([]);
👉 This stores recipes from backend
recipes = current data
setRecipes = function to update it
[] = initial empty list

#   const[form, setForm] = useState({
form	current state (data)
setForm	function to update form

<!-- recipes	shows backend data
form	stores user input -->


#   useEffect(() => {
    fetchRecipes();
  },[]);

1. What is useEffect?
👉 useEffect is a React Hook used to run code after the component renders.
Think of it like:
“Do something when the page loads or when something changes”

2. Breaking the structure
useEffect(() => {
  // code here
}, []);

It has two parts:

Part	Meaning
function () => {}	what to run
[]	when to run it

3. What is happening in your code?
fetchRecipes();
👉 This function is called when the page loads.
So it:
sends GET request to Django
fetches recipes
displays them


# // GET Recipes
const fetchRecipes = async() => {
  try{
    const res = await axios.get("http://127.0.0.1:8000/api/v1/recipes/");
    setRecipes(res.data.results || res.data);
  }catch (error) {
    console.log(error);
  }
};

1. What is this function?
👉 This is an async function that fetches data from your Django API
In simple words:
“Go to Django, get recipes, and store them in React state”

2. Line-by-line breakdown
# 🔸 const fetchRecipes = async () =>
Meaning:
You are creating a function
async means:
👉 “this function will wait for API response”
🔸 try { ... }
try {
Meaning:
👉 “Try to run API call safely”
If something fails (server down, error), it goes to catch.

🔸 API call (VERY IMPORTANT)
# const res = await axios.get("http://127.0.0.1:8000/api/v1/recipes/");
Breaking it:
Part	   ->   Meaning
axios.get	send GET request
URL	Django API endpoint
await	wait for response
res	response from backend
What Django sends back:

Example:

[
  {
    "id": 1,
    "name": "Pizza",
    "category": "Italian"
  }
]
# 🔸 setRecipes(...)
setRecipes(res.data.results || res.data);
Meaning:
👉 Save API data into React state

# Why results || data?

Because Django can return:
Case 1 (pagination ON):
{
  "count": 10,
  "results": [...]
}
Case 2 (no pagination):
[
  {...},
  {...}
]

So this line handles both cases safely.

🔸 catch (error)
catch (error) {
  console.log(error);


# // handle input change
const handleChange = (e) => {
  setForm({
    ...form,
    [e.target.name]: e.target.value,
  });
};

1. What is this function?
👉 This function runs every time you type in an input field
So when you type:
"Pizza" → name field
"Italian" → category field
React updates the state automatically.

# 2. Breaking it line by line
🔸 const handleChange = (e) =>
const handleChange = (e) => {
Meaning:
You are creating a function
e = event object
👉 This event comes from the input field

# 🔸 setForm({ ... })
setForm({
👉 You are updating React state (form object)

🔸 ...form
...form,
Meaning:
👉 “Keep old values”

Example before typing:

{
  name: "",
  category: "",
  ingredients: "",
  steps: ""
}
If you type only name, you DON’T want to erase others.
So spread operator keeps everything.

# 🔸 [e.target.name]
[e.target.name] means VERY IMPORTANT
This means:
👉 “Which input is being changed?”


# // POST RECIPE.
  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      await axios.post("http://127.0.0.1:8000/api/v1/recipes/", form);

      // clear form
      setForm({
        name: "",
        category: "",
        ingredients: "",
        steps: "",
      });

      // refresh list
      fetchRecipes();
    } catch (error) {
      console.log(error);
    }
  };

# 1. What is this function?
👉 This function sends form data from React → Django API
In simple terms:
# “User fills form → click submit → data goes to backend → UI updates”

2. Line-by-line breakdown
# 🔸 const handleSubmit = async (e) =>
Meaning:
Function runs when form is submitted
async → because API call takes time

# e → event object

# 🔸 e.preventDefault();
e.preventDefault();
VERY IMPORTANT
👉 Stops page reload
Without this:
Page refreshes
Data disappears
React state resets
So this keeps app like a real SPA (Single Page App)

# 🔸 API call (CREATE)
await axios.post("http://127.0.0.1:8000/api/v1/recipes/", form);

# What Django receives:
{
  "name": "Pizza",
  "category": "Italian",
  "ingredients": "...",
  "steps": "..."
}
# 🔸 Clear form
setForm({
  name: "",
  category: "",
  ingredients: "",
  steps: "",
});
Meaning:
👉 Reset input fields after successful submission
So user sees empty form again

# 🔸 Refresh data
# fetchRecipes();
Meaning:
👉 After adding new recipe:
call API again
get updated list
show new recipe instantly
🔸 Error handling
catch (error) {
  console.log(error);
}

3. Full flow (VERY IMPORTANT)
When user clicks submit:
Step 1 ---> User fills form
Step 2 ----> Clicks "Add Recipe"
Step 3 ----> React runs:handleSubmit()
Step 4----->Stops reload = e.preventDefault()
Step 5 ---> Sends data:axios.post(...)
Step 6----->Django saves data
Step 7--->React clears form
Step 8--->React reloads recipes list

