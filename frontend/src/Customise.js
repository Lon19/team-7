import React from 'react'

class Customise extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fontSize: 12,
            colorScheme: ''
        }
        this.handleFontChange = this.handleFontChange.bind(this);
    }

    handleFontChange(event) {
        this.setState({fontSize: event.target.value}, () => {event.target.style.fontSize = event.target.value});
    }

    render() {
        return(
            <div>
                <h2>Customise your experience</h2>
                <div>
                    <label for="fontSize">Font Size</label>
                    <input type="range" class="custom-range" id="fontSize" value={this.state.fontSize} onChange={this.handleFontChange}></input>
                    <p style={{fontSize: this.state.fontSize}}>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</p>
                    <p>{this.state.fontSize}</p>
                </div>
                
            </div>
        )
    }
}

export default Customise