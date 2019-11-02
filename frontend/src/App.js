import React from 'react'
import { Form, Button, Container, Row, Col, Navbar } from "react-bootstrap";
import './App.css'

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            userID: ''
        }
        this.handleLogin = this.handleLogin.bind(this);
        this.handleInputChange = this.handleInputChange.bind(this);
        this.handleKeyPress = this.handleKeyPress.bind(this);

    }
    handleLogin() {
        // event.preventDefault();
        let path = '/user/' + this.state.userID  ;
        this.props.history.push(path);
    }
    handleKeyPress = (event) => {
        // console.log(id)
        if(event.key === 'Enter'){
            this.handleLogin();
        }
    }

    handleInputChange(event) {
        this.setState({userID: event.target.value})
    }
    render() {
        return (
            <div>

            <Container className="height-center align-content-center">

                <Form className="text-center wide-button">
                <Form.Group controlId="formBasicEmail">
                    {/*<Form.Label>User ID</Form.Label>*/}
                    <Form.Control type="text" name="userID" placeholder="Enter user ID" value={this.state.userID} onChange={this.handleInputChange.bind(this)} onKeyPress={this.handleKeyPress}/>
                    <Form.Text className="text-muted">
                    </Form.Text>
                </Form.Group>
                <Button className="wide-button" variant="primary" type="button" onClick = {this.handleLogin}>
                    Login
                </Button>

            </Form>
            </Container>
            </div>
        )
    }

}
export default App