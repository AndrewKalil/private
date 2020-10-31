import React from 'react'
import AboutUs from "./RenderComponents/AboutUs"
import Home from "./RenderComponents/Home"
import ResultPage from "./RenderComponents/ResultPage"
import Nav from "./RenderComponents/Nav"
import "./RenderApp.css"
import {BrowserRouter as Router, Switch, Route} from "react-router-dom"

function App() {
    return (
        <Router>
            <div className="App">
                <Nav/>
                <Route path="/" exact component={Home} />
                <Route path="/about" component={AboutUs}/>
                <Route path="/result" component={ResultPage}/>
            </div>
        </Router>
    )
}

export default App