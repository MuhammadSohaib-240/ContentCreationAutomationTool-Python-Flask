import { Route, Routes } from "react-router-dom";
import SideMenu from "../../components/side_menu/SideMenu";
import "./ContentCreator.scss";
import MainContent from "../main_content/MainContent";

const ContentCreator = () => {
  return (
    <div className="content-creator">
      <SideMenu />

      <Routes>
        <Route path="main_content/*" element={<MainContent />} />
      </Routes>
    </div>
  );
};

export default ContentCreator;
