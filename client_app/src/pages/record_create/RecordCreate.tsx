import { Slider } from "../../components/slider/Slider";

import "./RecordCreate.scss";

import { useEffect, useState } from "react";

const RecordCreate = () => {
  const [audioUrls, setAudioUrls] = useState([]);
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const fetchAudioUrls = async () => {
      try {
        const response = await fetch(
          "http://localhost:5000/api/record_create/get-audio-files"
        );

        if (response.ok) {
          const result = await response.json();
          setAudioUrls(result.audioUrls);
        } else {
          console.error("Failed to fetch audio URLs");
        }
      } catch (error) {
        console.error("Error fetching audio URLs:", error);
      }
    };

    fetchAudioUrls();
  }, []);

  const handleEncodeVideo = async () => {
    try {
      setLoading(true);

      const response = await fetch(
        "http://localhost:5000/api/record_create/edit-video",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.ok) {
        // Handle success if needed
        console.log("Video encoding initiated successfully");
      } else {
        console.error("Failed to initiate video encoding");
      }
    } catch (error) {
      console.error("Error initiating video encoding:", error);
    } finally {
      setLoading(false); // Set loading to false when the encoding process is done
    }
  };

  const handleDeleteFiles = async () => {
    try {
      setLoading(true);
      const response = await fetch(
        "http://localhost:5000/api/record_create/delete-all-files",
        {
          method: "DELETE",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );

      if (response.ok) {
        // Handle success if needed
        console.log("All files deleted successfully");
      } else {
        console.error("Failed to delete files");
      }
    } catch (error) {
      console.error("Error initiating deleting files:", error);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="record-create-container">
      <div className="inner-container">
        {audioUrls.length > 0 ? (
          <Slider audioUrls={audioUrls} />
        ) : (
          <p>Loading...</p>
        )}
      </div>

      <div className="edit-btn">
        <button type="button" onClick={handleEncodeVideo} disabled={loading}>
          {loading ? "Encoding..." : "Encode Video"}
        </button>

        <button type="button" onClick={handleDeleteFiles} disabled={loading}>
          {loading ? "Deleting..." : "Delete Files"}
        </button>
      </div>
    </div>
  );
};

export default RecordCreate;
