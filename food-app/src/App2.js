import React, {useEffect, useState} from 'react'
import Card from "./components/Card"
import "./App.css"

const App = () => {
    const [recipes, setRecipes] = useState([])
    const [search, setSearch] = useState("")
    const [query, setQuery] = useState("chicken")

    const APP_ID = "a2799540"
    const APP_KEY = "f7e5e87ff82ab6a8b20afe314169bdde"
    const url = `https://api.edamam.com/search?q=$arroz&app_id=${APP_ID}&app_key=${APP_KEY}`

    useEffect( async () => {
        getRecipes()
    }, [query])

    const getRecipes = async () => {
        const response = await fetch(url)
        const data = await response.json()
        console.log(data);
        setRecipes(data.hits)

        /*fetch(url)
        .then(response => {response.jason()})
        .then(data = response)
        */
    }

    const updateSearch = e => {
        setSearch(e.target.value)
        console.log(search)
    }

    const getSearch = e => {
        e.preventDefault()
        setQuery(search)
    }

    return (
        <div className="App">
            <form
                className="search-form"
                onSubmit={getSearch}>
                <input className="search-bar" type="text" value={search} onChange={updateSearch}/>
                <button
                    className="search-button"
                    type="submit"
                    >Search
                </button>
            </form>
            {recipes.map(recipe => (<Card
                label = {recipe.recipe.label}
                img = {recipe.recipe.image}
                time = {recipe.recipe.totalTime}
            />))}
        </div>
    )
}

export default App