import React from 'react'
class Researcher extends React.Component {
    render() {
        const { params } = this.props.match
        return (
            <div>
                <h1>Researcher</h1>
                <p>{params.id}</p>
            </div>
        )
    }
}
export default Researcher