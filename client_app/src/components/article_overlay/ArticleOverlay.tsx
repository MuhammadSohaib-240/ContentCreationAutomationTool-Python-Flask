import React from "react";
import "./ArticleOverlay.scss";

interface ArticleOverlayProps {
  onClose: () => void;
  article: {
    title: string;
    paragraphs: string[];
  };
}

const ArticleOverlay: React.FC<ArticleOverlayProps> = ({
  onClose,
  article,
}) => {
  // Loop through paragraphs and display them with extra line breaks
  const paragraphsContent = article.paragraphs.map((paragraph, index) => (
    <p key={index}>
      {paragraph}
      <br />
      <br />
    </p>
  ));

  return (
    <div className="overlay">
      <div className="overlay-content">
        <h2>{article.title}</h2>
        {paragraphsContent}
        <button onClick={onClose}>Close</button>
      </div>
    </div>
  );
};

export default ArticleOverlay;
