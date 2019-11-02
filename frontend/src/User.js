import React from 'react'
import './User.css'

class User extends React.Component {
    constructor(props) {
        super(props);
        this.handleClick = this.handleClick.bind(this);
    }
    handleClick(page) {
        // event.preventDefault();
        let path = '/user/43/' + page;
        this.props.history.push(path);
    }

    render() {
        return (
            <div>
                <div className="split left-up">
                        <div className="centered">
                            <img src={require('./menthealth.jpg')} onClick = {() => this.handleClick("mentalhealth")}></img>
                            <h2>Mental Health</h2>
                            <p>Some text.</p>
                        </div>
                    </div>
                    <div className="split left-down">
                        <div className="centered">
                            <img src={require('./orgcult.png')} onClick = {() => this.handleClick("organisationalculture")}></img>
                            <h2>Organisational Culture</h2>
                            <p>Some text.</p>
                        </div>
                    </div>


                <div className="split right-up">
                        <div className="centered">
                            <img src={require('./confid.png')} onClick = {() => this.handleClick("workselfconfidence")}></img>
                            <h2>Work Self Confidence</h2>
                            <p>Some text here too.</p>
                        </div>
                </div>
                    <div className="split right-down">
                        <div className="centered">
                            <img src={require('./adjust.png')} onClick = {() => this.handleClick("adjustments")}></img>
                            <h2>Adjustments</h2>
                            <p>Some text here too.</p>
                        </div>
                    </div>
            </div>
            )
    }
}
export default User