import React, { Component } from "react";
import ParticlesBg from "particles-bg";
import pic from "../infographic1.jpg";
import loading from "../loading.png";

class Home extends Component {
    state = {
        onSelectedFile: null,
        onData: null,
        image: loading
    };

    changeData = (newData) => {
        this.setState({ onData: newData })
    }

    onFileChange = event => {
        this.setState({ onSelectedFile: event.target.files[0] });
        this.setState({ image: loading });
    };


    onFileUpload = () => {
        this.setState({ onData: " " })
        const formData = new FormData();
        formData.append(
            "file",
            this.state.onSelectedFile,
        );
        console.log(formData);

        // Request made to the backend api
        // Send formData object
        fetch("http://localhost:5000/pdf", {
            method: 'POST',
            body: formData,
        }).then((response) => {
            return response.text();
        }).then((data) => {
            this.setState({ onData: data })
            this.setState({ image: pic })
        });
    };

    render() {
        if (!this.props.data) return null;

        const name = this.props.data.name;
        const description = this.props.data.description;

        return (
            <header id="home">
                <ParticlesBg type="circle" bg={true} />
                <div className="row banner">
                    <div className="banner-text">
                        <h1 className="responsive-headline">{name}</h1>
                        <h3>{description}</h3>
                        <hr />
                        <ul className="social">
                            <input type="file" onChange={this.onFileChange} className="button btn project-btn" />
                            <button onClick={this.onFileUpload} className="button btn github-btn">
                                <i className="fa fa-share"></i>Convert
                            </button>
                        </ul>
                    </div>

                    {this.state.onData &&
                        <div className="container">
                            <h3 style={{ color: "white" }}>{this.state.onData}</h3>
                            <img style={{ width: "30%" }} src={this.state.image} />
                        </div>}

                </div>
            </header>
        );
    }
}

export default Home;