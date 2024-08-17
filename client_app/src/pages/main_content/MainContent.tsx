import "./MainContent.scss";

import { Route, Routes } from "react-router-dom";
import VideoPlayer from "../video_player/VideoPlayer";
import ArticleGenerator from "../article_generator/ArticleGenerator";
import YourMedia from "../your_media/YourMedia";
import RecordCreate from "../record_create/RecordCreate";
import TTS from "../tts/TTS";

const MainContent = () => {
  return (
    <div className="main-content-container">
      <Routes>
        <Route path="video_player" element={<VideoPlayer />} />
        <Route path="article_generator" element={<ArticleGenerator />} />
        <Route path="your_media" element={<YourMedia />} />
        <Route path="record_create" element={<RecordCreate />} />
        <Route path="text_to_speech" element={<TTS />} />
      </Routes>
    </div>
  );
};

export default MainContent;
