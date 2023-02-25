import React, { Component } from "react";
import ParticlesBg from "particles-bg";
import axios from 'axios';

class Home extends Component {
    state = {
        onSelectedFile: null
    };


    onFileChange = event => {
        this.setState({ onSelectedFile: event.target.files[0] });
        // let selectedFile = event.target.files[0];
        // const fileObj = ['application/pdf'];
        // if (selectedFile) {
        //     if (selectedFile && fileObj.includes(selectedFile.type)) {
        //         this.setState({ onSelectedFile: selectedFile });
        //         // console.log(selectedFile)
        //         // let reader = new FileReader();
        //         // reader.readAsDataURL(selectedFile);
        //         // reader.onloadend = (e) => {
        //         //     // setSelectPdfFile(e.target.result);
        //         //     this.setState({ onSelectedFile: e.target.result });
        //         // }
        //     }
        // }
        // else {
        //     alert('select pdf file');
        // }
    };


    onFileUpload = () => {
        const formData = new FormData();
        formData.append(
            "file",
            this.state.onSelectedFile,
        );
        console.log(formData);

        // Request made to the backend api
        // Send formData object
        // axios.post("http://localhost:5000/pdf", formData,{}).then(res => {console.log(res.data)});
        fetch("http://localhost:5000/pdf", {
            method: 'POST',
            body: formData,
        }).then((response) => {
            console.log(response);
        });
    };

    render() {
        if (!this.props.data) return null;

        const project = this.props.data.project;
        const github = this.props.data.github;
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
                            {/* <button onClick={this.onFileChange} className="button btn project-btn">
                                    <i className="fa fa-upload"></i>Upload
                                </button> */}
                            <button onClick={this.onFileUpload} className="button btn github-btn">
                                <i className="fa fa-share"></i>Convert
                            </button>
                        </ul>
                    </div>
                </div>
            </header>
        );
    }
}

export default Home;