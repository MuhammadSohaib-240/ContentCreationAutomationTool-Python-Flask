import { Route, Routes } from "react-router-dom";
import "./App.scss";
import ContentCreator from "./pages/content_creator/ContentCreator";
import AboutUs from "./pages/about_us/AboutUs";
import Home from "./pages/home/Home";

function App() {
  return (
    <>
      <div className="app">
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/about_us" element={<AboutUs />} />
          <Route path="content_creator/*" element={<ContentCreator />} />
        </Routes>
      </div>
    </>
  );
}

export default App;
