// Home.tsx
import React from "react";
import "./Home.scss";
import logo from "../../images/SSUET_Logo.png";
import { Link } from "react-router-dom";

const Home: React.FC = () => {
  return (
    <div className="landing-page">
      <header className="header">
        <div className="logo-container">
          <img src={logo} alt="Logo" className="logo" />
        </div>
        <div className="nav-links-container">
          <Link className="link" to="/about_us">
            Go to About Us
          </Link>
        </div>
      </header>
      <div className="content">
        <div className="text-container">
          <h1>Content Creation Automation</h1>
          <p>
            In the realm of innovation, we present to you "Content Creation
            Automation" – a dynamic solution that transforms your ideas into
            captivating content effortlessly. Stay updated with live information
            fetched from the internet, curate your preferred updates, and
            witness the magic unfold. Choose a title, and watch as our platform
            generates a well-crafted article for you. Take your narrative a step
            further with our seamless voice-over feature, where audio gracefully
            dances through segments. Elevate your content by adding images,
            creating a visual symphony that resonates with your audience.
            Experience the future of content creation – streamlined, efficient,
            and boundlessly creative. Ready to transform your ideas into
            engaging content?
          </p>
          <Link
            className="link"
            to="content_creator/main_content/text_to_speech"
          >
            Try Now
          </Link>
        </div>
        <div className="video-container">
          <img src={logo} alt="" />
          <h2>Sir Syed University of Engineering & Technology</h2>
          <h3>2024 DSA & AI Project Exhibition</h3>
        </div>
      </div>
    </div>
  );
};

export default Home;
