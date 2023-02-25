import React, { Component } from "react";
import ParticlesBg from "particles-bg";

class Home extends Component {
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
                <a href={project} className="button btn project-btn">
                  <i className="fa fa-upload"></i>Upload
                </a>
                <a href={github} className="button btn github-btn">
                  <i className="fa fa-share"></i>Convert
                </a>
              </ul>
          </div>
        </div>
      </header>
    );
  }
}

export default Home;
