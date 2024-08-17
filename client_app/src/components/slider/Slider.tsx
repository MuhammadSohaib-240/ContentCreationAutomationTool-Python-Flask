// Slider.tsx
import { ChangeEvent, useEffect, useState } from "react";
import "./Slider.scss";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faArrowRight, faArrowLeft } from "@fortawesome/free-solid-svg-icons";

type SliderProps = {
  audioUrls: string[];
};

export const Slider = ({ audioUrls }: SliderProps) => {
  const [audioIndex, setAudioIndex] = useState(0);
  const [imagePreviews, setImagePreviews] = useState<string[]>(
    new Array(audioUrls.length).fill(null)
  );
  const [audioKey, setAudioKey] = useState(0);
  const [loading, setLoading] = useState(false); // New loading state
  const [currentSlide, setCurrentSlide] = useState(audioIndex + 1); // Initial value based on audioIndex

  useEffect(() => {
    const fetchImageUrls = async () => {
      try {
        const response = await fetch(
          "http://localhost:5000/api/record_create/get-image-files"
        );
        if (response.ok) {
          const data = await response.json();
          setImagePreviews(data.imageUrls);
        } else {
          console.error("Failed to fetch image URLs");
        }
      } catch (error) {
        console.error("Error fetching image URLs:", error);
      }
    };

    fetchImageUrls();
  }, []);

  const handleImageUpload = async (event: ChangeEvent<HTMLInputElement>) => {
    const file = event.target.files?.[0];

    if (file) {
      const formData = new FormData();
      formData.append("image", file);
      formData.append("audioIndex", String(audioIndex + 1));

      try {
        setLoading(true);
        const response = await fetch(
          "http://localhost:5000/api/record_create/add-image",
          {
            method: "POST",
            body: formData,
          }
        );

        if (response.ok) {
          console.log("Image uploaded successfully");
        } else {
          console.error("Failed to upload image");
        }
      } catch (error) {
        console.error("Error uploading image:", error);
      } finally {
        setLoading(false);
      }

      const reader = new FileReader();
      reader.onload = function (e) {
        setImagePreviews((prevPreviews) => {
          const newPreviews = [...prevPreviews];
          newPreviews[audioIndex] = e.target?.result as string;
          return newPreviews;
        });
      };
      reader.readAsDataURL(file);
    }
  };

  function showPreviousSlide() {
    setAudioIndex((index) => {
      const newIndex = index === 0 ? audioUrls.length - 1 : index - 1;
      setCurrentSlide(newIndex + 1); // Update slide number
      return newIndex;
    });
    setAudioKey((prevKey) => prevKey + 1);
  }

  function showNextSlide() {
    setAudioIndex((index) => {
      const newIndex = index === audioUrls.length - 1 ? 0 : index + 1;
      setCurrentSlide(newIndex + 1); // Update slide number
      return newIndex;
    });
    setAudioKey((prevKey) => prevKey + 1);
  }

  return (
    <div className="slider">
      <button onClick={showPreviousSlide} className="slider-btn">
        <FontAwesomeIcon className="icon" icon={faArrowLeft} />
      </button>
      <div className="slides">
        <div className="image-uploader">
          <label className="custom-file-upload">
            Custom Upload - Slide # {currentSlide}
            <input type="file" accept="image/*" onChange={handleImageUpload} />
          </label>
          {loading && <div className="loading-overlay">Loading...</div>}
          {imagePreviews[audioIndex] && (
            <img
              src={imagePreviews[audioIndex]}
              alt="Uploaded Image"
              className="slider-img"
            />
          )}
        </div>
        <audio key={audioKey} controls>
          <source src={audioUrls[audioIndex]} type="audio/mp3" />
          Your browser does not support the audio element.
        </audio>
      </div>
      <button onClick={showNextSlide} className="slider-btn">
        <FontAwesomeIcon className="icon" icon={faArrowRight} />
      </button>
    </div>
  );
};
