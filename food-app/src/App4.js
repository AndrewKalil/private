import React, {Component} from 'react'
import axios from 'axios'
import ReactPaginate from 'react-paginate';
import Card from "./components/Card"
import './App4.css'
import "./styles/Card.css"

export default class App extends Component {
    constructor(props) {
        super(props);
        this.state = {
            offset: 0,
            data: [],
            perPage: 10,
            currentPage: 0
        };
        this.handlePageClick = this
            .handlePageClick
            .bind(this);
    }
    receivedData() {
        const APP_ID = "a2799540"
        const APP_KEY = "f7e5e87ff82ab6a8b20afe314169bdde"
        const url = `https://api.edamam.com/search?q=$pizza&app_id=${APP_ID}&app_key=${APP_KEY}&from=${0}&to=${100}`

        axios
            .get(url)
            .then(res => {

                const data = res.data;
                const slice = data.hits.slice(this.state.offset, this.state.offset + this.state.perPage)
                const postData = slice.map(pd => <Card
                    label = {pd.recipe.label}
                />)
                console.log(data)

                this.setState({
                    pageCount: Math.ceil(data.hits.length / this.state.perPage),

                    postData
                })
            });
    }
    handlePageClick = (e) => {
        const selectedPage = e.selected;
        const offset = selectedPage * this.state.perPage;

        this.setState({
            currentPage: selectedPage,
            offset: offset
        }, () => {
            this.receivedData()
        });

    };

    componentDidMount() {
        this.receivedData()
    }

    render() {
        return (
            <div>
                {this.state.postData}
                <ReactPaginate
                    previousLabel={"prev"}
                    nextLabel={"next"}
                    breakLabel={"..."}
                    breakClassName={"break-me"}
                    pageCount={this.state.pageCount}
                    marginPagesDisplayed={2}
                    pageRangeDisplayed={5}
                    onPageChange={this.handlePageClick}
                    containerClassName={"pagination"}
                    subContainerClassName={"pages pagination"}
                    activeClassName={"active"}/>
            </div>

        )
    }
}