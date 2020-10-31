import React, {useState} from 'react'
import Axios from 'axios'
import { CardDeck, Jumbotron } from "react-bootstrap"
import PopOutCard from "./Components/PopOutCard"
import PassingPage from "./ResPage"
//import {v4 as uuidv4} from "uuid"

function ResultPage () {

    const [query, setQuery] = useState("")
    //const [recipes, setRecipes] = useState([])

    //const APP_ID = "a2799540"
    //const APP_KEY = "f7e5e87ff82ab6a8b20afe314169bdde"
    //const url = `https://api.edamam.com/search?q=${query}&app_id=${APP_ID}&app_key=${APP_KEY}&to=${100}`

    const getData = async () => {
        //const result = await Axios.get(url)
        //return(query)
        //console.log(result)
        setQuery("")
        //setRecipes(result.data.hits)
    }

    const onSubmit = (e) => {
        e.preventDefault()
        getData()
    }

    const onChange = (e) => {
        setQuery(e.target.value)
    }

    return(
        <div className="myRpage">
            <div className="formDiv">
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
            </div>
            <PassingPage
                query={query}
            />
        </div>
    )
}

export default ResultPage