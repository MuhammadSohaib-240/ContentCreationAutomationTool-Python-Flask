import "./AboutUs.scss";

import img from "../../images/img_white.png";

const AboutUs = () => {
  return (
    <div className="about-us-container">
      <h1>Group Members Details</h1>
      <div className="team-members">
        <div className="team-member-card">
          <img src={img} alt="Team Member 1" />
          <h2>Muhammad Sohaib</h2>
          <p>Roll No: 2021F-BSE-213</p>
          <p>Role: Developer & Data Scientist</p>
        </div>
        <div className="team-member-card">
          <img src={img} alt="Team Member 1" />
          <h2>Maryam Tasneem</h2>
          <p>Roll No: 2021F-BSE-084</p>
          <p>Role: UI/UX Design & Data Analyst</p>
        </div>
        <div className="team-member-card">
          <img src={img} alt="Team Member 1" />
          <h2>Muhammad Owais</h2>
          <p>Roll No: 2021F-BSE-137</p>
          <p>Role: System Design & Documentation</p>
        </div>
        <div className="team-member-card">
          <img src={img} alt="Team Member 1" />
          <h2>Muhammad Mudassir</h2>
          <p>Roll No: 2021F-BSE-199</p>
          <p>Role: Documentation & Testing</p>
        </div>
      </div>
    </div>
  );
};

export default AboutUs;
