import React, { useEffect, useState } from "react";
import "./ArticleGenerator.scss";
import img2 from "../../images/hollywood.png";
import img3 from "../../images/real_estate.jpg";
import img4 from "../../images/shopping.jpg";
import ArticleOverlay from "../../components/article_overlay/ArticleOverlay";
import LoadingOverlay from "../../components/loading_overlay/LoadingOverlay";

interface Article {
  index: number;
  category: string;
  title: string;
  paragraphs: string[];
}

const ArticleGenerator: React.FC = () => {
  const [showOverlay, setShowOverlay] = useState(false);
  const [selectedArticle, setSelectedArticle] = useState<Article | null>(null);
  const [filter, setFilter] = useState<string | null>(null);
  const [searchTerm, setSearchTerm] = useState<string>("");
  const [articles, setArticles] = useState<Article[]>([]);

  const [loading, setLoading] = useState(false);

  const fetchLatestUpdates = async () => {
    console.log("Service is called...");
    try {
      setLoading(true);
      const response = await fetch(
        "http://localhost:5000/api/web_scraping/scrape"
      );
      const data = await response.json();
      setArticles(Object.values(data.updates));
      console.log("Data fetched successfully!!!");
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  const fetchCurrentUpdates = async () => {
    console.log("Service is called...");
    try {
      const response = await fetch(
        "http://localhost:5000/api/web_scraping/get-current-updates"
      );
      const data = await response.json();
      setArticles(Object.values(data.updates));
      console.log("Data fetched successfully!!!");
    } catch (error) {
      console.error("Error fetching data:", error);
    }
  };

  useEffect(() => {
    fetchCurrentUpdates();
  }, []);

  const handleButtonClick = () => {
    // Call the fetchData function when the button is clicked
    fetchLatestUpdates();
  };

  const handleCardClick = async (article: Article) => {
    try {
      setLoading(true);
      const response = await fetch(
        "http://localhost:5000/api/web_scraping/generate-article",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/x-www-form-urlencoded",
          },
          body: new URLSearchParams({
            article_index: article.index.toString(),
          }),
        }
      );

      if (!response.ok) {
        throw new Error(`Failed to fetch article: ${response.status}`);
      }

      const data = await response.json();

      // Assuming the response structure is { article: string[] }
      const paragraphs = data.article;

      // Set the selected article with paragraphs
      setSelectedArticle({ ...article, paragraphs });
    } catch (error) {
      console.error("Error fetching article:", error);
    } finally {
      setLoading(false);
      setShowOverlay(true);
    }
  };

  const handleCloseOverlay = () => {
    setSelectedArticle(null);
    setShowOverlay(false);
  };

  return (
    <div className="article-container">
      <div className="filter">
        <div className="search-bar">
          <input
            type="text"
            placeholder="Search..."
            value={searchTerm}
            onChange={(e) => setSearchTerm(e.target.value)}
          />
        </div>
        <div className="filter-tabs">
          <div
            className={`filter-tab ${filter === null ? "active" : ""}`}
            onClick={() => setFilter(null)}
          >
            All
          </div>
          <div
            className={`filter-tab ${filter === "Movie" ? "active" : ""}`}
            onClick={() => setFilter("Movie")}
          >
            Movies
          </div>
          <div
            className={`filter-tab ${filter === "RealEstate" ? "active" : ""}`}
            onClick={() => setFilter("RealEstate")}
          >
            Real Estate
          </div>
          <div
            className={`filter-tab ${filter === "Shopping" ? "active" : ""}`}
            onClick={() => setFilter("Shopping")}
          >
            Shopping
          </div>
          <div className="filter-tab load-button" onClick={handleButtonClick}>
            Fetch Updates
          </div>
        </div>
      </div>
      <div className="article-titles">
        {articles
          .filter(
            (article) =>
              (filter === null || article.category === filter) &&
              article.title.toLowerCase().includes(searchTerm.toLowerCase())
          )
          .map((article) => (
            <div
              className="card"
              key={article.index}
              onClick={() => handleCardClick(article)}
            >
              {article.category === "Movie" && <img src={img2} alt="Movie" />}
              {article.category === "RealEstate" && (
                <img src={img3} alt="RealEstate" />
              )}
              {article.category === "Shopping" && (
                <img src={img4} alt="Shopping" />
              )}
              <h3>{article.category}</h3>
              <h4>{article.title}</h4>
            </div>
          ))}
      </div>

      {showOverlay && (
        <ArticleOverlay
          onClose={handleCloseOverlay}
          article={selectedArticle!}
        />
      )}

      {loading && <LoadingOverlay />}
    </div>
  );
};

export default ArticleGenerator;
