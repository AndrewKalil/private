import React from "react"
import "../styles/Card.css"
import {Link} from "react-router-dom"

const clock = "https://www.flaticon.com/svg/static/icons/svg/154/154448.svg"

class Card extends React.Component {
    render() {
        return (
            <div className="myRcard">
                <div>
                    <img src={this.props.img} alt="" className="myRcardImg"/>
                </div>
                <div className="myRcardTitleandClock">
                    <div className="myRcardTitle">
                        <p>{this.props.label}</p>
                    </div>
                    <div className="myClock">
                        <div>{this.props.time}</div>
                    </div>
                </div>
                <div className="myRcardText">
                    <p>{this.props.text}</p>
                </div>
                <div className="myRcardButton">
                    <Link to="/">
                        <p>Go!</p>
                    </Link>
                </div>
            </div>
        )
    }
}

export default Card