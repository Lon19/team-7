import React from 'react'
import './User.css'

class User extends React.Component {
    constructor(props) {
        super(props)
        this.state = {
            colorTheme: {
                darkred: '#B24C5A',
                pink: '#E9B9A5',
                lightblue: '#9dd5cc',
                grey: '#ebebed',
                darkblue: '#006174'
            }
        }
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
                <div style={{backgroundColor: this.state.colorTheme.darkblue}} className="split left-up">
                        <div className="centered">
                            <img src={require('./menthealth.jpg')} onClick = {() => this.handleClick("mentalhealth")}></img>
                            <h2>Mental Health</h2>
                        </div>
                    </div>
                    <div style={{backgroundColor: this.state.colorTheme.lightblue}} className="split left-down">
                        <div className="centered">
                            <img src={require('./orgcult.png')} onClick = {() => this.handleClick("organisationalculture")}></img>
                            <h2>Organisational Culture</h2>
                        </div>
                    </div>


                <div style={{backgroundColor: this.state.colorTheme.pink}} className="split right-up">
                        <div className="centered">
                            <img src={require('./confid.png')} onClick = {() => this.handleClick("workselfconfidence")}></img>
                            <h2>Work Self Confidence</h2>
                        </div>
                </div>
                    <div style={{backgroundColor: this.state.colorTheme.darkred}} className="split right-down">
                        <div className="centered">
                            <img src={require('./adjust.png')} onClick = {() => this.handleClick("adjustments")}></img>
                            <h2>Adjustments</h2>
                        </div>
                    </div>
            </div>
            )
    }
}
export default User