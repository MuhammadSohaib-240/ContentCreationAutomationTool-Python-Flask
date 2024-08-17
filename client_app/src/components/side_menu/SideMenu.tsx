import "./SideMenu.scss";

import React, { useState } from "react";
import { Link } from "react-router-dom";
import logo from "../../images/SSUET_Logo.png";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import {
  faFileAudio,
  faNewspaper,
  faPhotoVideo,
  faVideoCamera,
} from "@fortawesome/free-solid-svg-icons";

type ActiveLink = string | null;

const SideMenu: React.FC = () => {
  const [activeLink, setActiveLink] = useState<ActiveLink>(null);

  const handleLinkClick = (link: string) => {
    setActiveLink(link);
  };

  return (
    <div className="side-menu">
      <div className="logo">
        <img src={logo} alt="logo" className="logo" />
      </div>
      <ul className="menu-list">
        {/* <li
          className={`menu-item ${
            activeLink === "/content_creator/main_content/your_media"
              ? "active"
              : ""
          }`}
        >
          <Link
            to="/content_creator/main_content/your_media"
            className="link"
            onClick={() =>
              handleLinkClick("/content_creator/main_content/your_media")
            }
          >
            <FontAwesomeIcon className="icon" icon={faFolder} />
            <span>Your Media</span>
          </Link>
        </li> */}
        <li
          className={`menu-item ${
            activeLink === "/content_creator/main_content/record_create"
              ? "active"
              : ""
          }`}
        >
          <Link
            to="/content_creator/main_content/record_create"
            className="link"
            onClick={() =>
              handleLinkClick("/content_creator/main_content/record_create")
            }
          >
            <FontAwesomeIcon className="icon" icon={faVideoCamera} />
            <span>Record & Create</span>
          </Link>
        </li>
        <li
          className={`menu-item ${
            activeLink === "/content_creator/main_content/video_player"
              ? "active"
              : ""
          }`}
        >
          <Link
            to="/content_creator/main_content/video_player"
            className="link"
            onClick={() =>
              handleLinkClick("/content_creator/main_content/video_player")
            }
          >
            <FontAwesomeIcon className="icon" icon={faPhotoVideo} />
            <span>Video Player</span>
          </Link>
        </li>
        <li
          className={`menu-item ${
            activeLink === "/content_creator/main_content/article_generator"
              ? "active"
              : ""
          }`}
        >
          <Link
            to="/content_creator/main_content/article_generator"
            className="link"
            onClick={() =>
              handleLinkClick("/content_creator/main_content/article_generator")
            }
          >
            <FontAwesomeIcon className="icon" icon={faNewspaper} />
            <span>Article Generator</span>
          </Link>
        </li>
        <li
          className={`menu-item ${
            activeLink === "/content_creator/main_content/text_to_speech"
              ? "active"
              : ""
          }`}
        >
          <Link
            to="/content_creator/main_content/text_to_speech"
            className="link"
            onClick={() =>
              handleLinkClick("/content_creator/main_content/text_to_speech")
            }
          >
            <FontAwesomeIcon className="icon" icon={faFileAudio} />
            <span>Text To Speech</span>
          </Link>
        </li>
      </ul>
    </div>
  );
};

export default SideMenu;
