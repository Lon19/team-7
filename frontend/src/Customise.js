import React from 'react'
import { Container } from 'react-bootstrap';

class Customise extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fontSize: 12,
            colorScheme: [
                '#B24C5A',
                '#E9B9A5',
                '#9dd5cc',
                '#ebebed',
                '#006174'
            ]
        }
        this.handleFontChange = this.handleFontChange.bind(this);
        this.handleClick = this.handleClick.bind(this);
    }

    handleFontChange(event) {
        this.setState({ fontSize: event.target.value }, () => {
            // document.getElementById('#fontSize').style.fontSize = event.target.value;
        });
    }

    handleClick(event) {
        document.getElementsByClassName('selectTheme')[0].classList.remove("selected");
        document.getElementsByClassName('selectTheme')[1].classList.remove("selected");
        document.getElementsByClassName('selectTheme')[0].classList.remove("shadow");
        document.getElementsByClassName('selectTheme')[1].classList.remove("shadow");
        console.log(event.target);
        event.target.classList.add("shadow");
        event.target.classList.add("selected");
    }

    render() {
        return (
            <div className="text-center">
                <h2 className="text-center">Customise your experience</h2>
                <div className="text-left mt-5 mb-5">
                    <label className="h4" htmlFor="fontSize">Font Size</label>
                    <input type="range" className="custom-range" min="10" max="40" id="fontSize" value={this.state.fontSize} onChange={this.handleFontChange}></input>
                    <p style={{ fontSize: this.state.fontSize + "px" }}>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                </div>

                <div className="text-left mt-5 mb-5">
                    <h4 className="h4">Color Scheme</h4>
                    <p>Select your preferred color scheme</p>
                    <Container className="text-center">
                        <img className="selectTheme selected shadow" src={require('./Capture.PNG')} onClick={this.handleClick} />
                        <img className="selectTheme" src={require('./Capture2.PNG')} onClick={this.handleClick} />
                    </Container>

                </div>
                {/* <button type="button" className="btn btn-lg" style={{ backgroundColor: this.state.colorScheme[0], color: this.state.colorScheme[3] }}>Save</button> */}
            </div>
        )
    }
}

export default Customise