import React from 'react';
import { Switch, Route } from  "react-router-dom";
//import Header from './Header';
//import Home from './Home';
//import Reciped from './recip';
import AboutUs from './AboutUs'
import ResPage from "./ResPage"
import DetailRecipe from "./DetailRecipe.js"

import "./css/myAboutUs.css"
import "./css/myResultPage.css"
import "./css/myDetailRecipe.css"



function App() {
  return (
        <div>
            <Switch>
                <Route path="/" exact component={ResPage}/>
                <Route path="/about" component={AboutUs}/>
                <Route path="/detail" component={DetailRecipe}/>
                {/*<Header />
                <Home />*/}
                {/*</Route>
                <Route path="/">
                <Reciped />*/}
            </Switch>
        </div>
  );
}

export default App;
