import React, {useState} from 'react'
import Axios from 'axios'
import "./App.css"
import Card from './components/Card'
//import {v4 as uuidv4} from "uuid"

function App () {

    const [query, setQuery] = useState("")
    const [recipes, setRecipes] = useState([])

    const APP_ID = "a2799540"
    const APP_KEY = "f7e5e87ff82ab6a8b20afe314169bdde"
    const url = `https://api.edamam.com/search?q=${query}&app_id=${APP_ID}&app_key=${APP_KEY}`

    const getData = async () => {
        const result = await Axios.get(url)

        console.log(result)
        setQuery("")
        setRecipes(result.data.hits)
    }

    const onSubmit = (e) => {
        e.preventDefault()
        getData()
    }

    const onChange = (e) => {
        setQuery(e.target.value)
    }

    return (
        <div className="App">
            <h1 onClick={getData}>RecipEat</h1>
            <form
                className="search-form"
                onSubmit={onSubmit}>
                <input
                    type="text"
                    placeholder="Search recipe"
                    autoComplete="off"
                    onChange={onChange}
                    value={query}
                    />
                <input
                    type="submit"
                    value="search"/>
            </form>
            <div>
                {recipes !== [] && recipes.map(recipe =>
                    <Card
                        label = {recipe.recipe.label}
                    />)}
            </div>
        </div>
    )
}

export default App