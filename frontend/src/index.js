import 'bootstrap/dist/css/bootstrap.css';

import React from 'react';
import ReactDOM from 'react-dom';
import { Route, Link, BrowserRouter as Router, Switch } from 'react-router-dom'
import { Form, Button, Container, Row, Col, Navbar } from "react-bootstrap";

import './index.css';
import App from './App';
// import * as serviceWorker from './serviceWorker';
import User from './User'
import Researcher from './Researcher'
import BubbleChart from './visualisation/BubbleChart'
import Customise from './Customise'
import Notfound from './Notfound'


const routing = (
    <Router>
        <div>
            <Navbar bg="dark" variant="dark">
                <Navbar.Brand href="#home">
                    <img
                        alt=""
                        src="../public/logo.jpg"
                        width="30"
                        height="30"
                        className="d-inline-block align-top"
                    />{' '}
                    React Bootstrap
                </Navbar.Brand>
            </Navbar>
            <Container>
            <Switch>
                <Route exact path="/" component={App} />
                <Route exact path="/user/:id" component={User} />
                <Route exact path="/researcher" component={Researcher} />
                <Route exact path="/vis" component={BubbleChart} />
                <Route exact path="/user/:id/customise" component={Customise}/>
                <Route component={Notfound} />

            </Switch>
            </Container>
        </div>
    </Router>
)


ReactDOM.render(routing, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
// serviceWorker.unregister();
