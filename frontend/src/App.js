import React from 'react'
import { Form, Button, Container, FormGroup, FormControl, ControlLabel } from "react-bootstrap";

class App extends React.Component {
    render() {
        return (
            <Container>
                <Form>
                <Form.Group controlId="formBasicEmail">
                    <Form.Label>User ID</Form.Label>
                    <Form.Control type="email" placeholder="Enter user ID" />
                    <Form.Text className="text-muted">
                    </Form.Text>
                </Form.Group>

                {/*<Form.Group controlId="formBasicPassword">*/}
                {/*    <Form.Label>Password</Form.Label>*/}
                {/*    <Form.Control type="password" placeholder="Password" />*/}
                {/*</Form.Group>*/}
                {/*<Form.Group controlId="formBasicCheckbox">*/}
                {/*    <Form.Check type="checkbox" label="Check me out" />*/}
                {/*</Form.Group>*/}
                <Button variant="primary" type="submit">
                    Submit
                </Button>
            </Form>
            </Container>
        )
    }
}
export default App