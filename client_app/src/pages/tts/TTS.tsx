import "./TTS.scss";

import { useState } from "react";
import axios from "axios";

const TTS = () => {
  const [inputText, setInputText] = useState("");
  const [audioKey, setAudioKey] = useState(0);
  const [loading, setLoading] = useState(false); // New loading state
  const [audioSource, setAudioSource] = useState(""); // New state to track audio source

  const convertToSpeech = async () => {
    try {
      setLoading(true);
      clearAudio();
      const response = await axios.post(
        "http://localhost:5000/api/text_to_speech/convert",
        new URLSearchParams({ text: inputText }),
        { headers: { "Content-Type": "application/x-www-form-urlencoded" } }
      );

      const data = response.data;
      if (response.status === 200) {
        console.log("Voice over has successfully been generated:", data);
        setAudioSource("http://localhost:5000/get-audio/output.mp3"); // Set audio source
        setAudioKey((prevKey) => prevKey + 1);
      } else {
        console.error(data.error);
      }
    } catch (error) {
      console.error("Error converting text to speech:", error);
    } finally {
      setLoading(false); // Set loading to false when the conversion process is done
    }
  };

  const clearAudio = () => {
    setAudioSource(""); // Clear audio source
    setAudioKey((prevKey) => prevKey + 1); // Trigger re-render to clear audio
  };

  return (
    <div className="tts">
      <div className="tts-container">
        <div>
          <textarea
            placeholder="Enter article to convert to speech"
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />
        </div>
        <div className="buttons">
          <button onClick={convertToSpeech} disabled={loading}>
            {loading ? "Converting..." : "Convert to Speech"}
          </button>{" "}
        </div>
        <div>
          <audio controls key={audioKey}>
            <source src={audioSource} type="audio/mp3" />
            Your browser does not support the audio tag.
          </audio>
        </div>
      </div>
    </div>
  );
};

export default TTS;
