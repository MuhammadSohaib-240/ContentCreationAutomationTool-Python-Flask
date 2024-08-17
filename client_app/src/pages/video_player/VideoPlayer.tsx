import "./VideoPlayer.scss";

const VideoPlayer = () => {
  return (
    <div className="video-player-container">
      <div className="video-player">
        <video controls>
          <source
            src={"http://localhost:5000/get-video/edited_video.mp4"}
            type="video/mp4"
          />
          Your browser does not support the video tag.
        </video>
      </div>
    </div>
  );
};

export default VideoPlayer;
