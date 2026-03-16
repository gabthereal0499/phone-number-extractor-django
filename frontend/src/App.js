import React, { useState } from "react";
import Upload from "./components/Upload";
import Results from "./components/Results";
import { FaUpload, FaChartBar } from "react-icons/fa";
import "./App.css";

function App() {
  const [page, setPage] = useState("upload");
  const [numbers, setNumbers] = useState([]);

  // Callback to switch to Results page after extraction
  const handleExtraction = (extractedNumbers) => {
    setNumbers(extractedNumbers);
    setPage("results");
  };

  // Callback to reset and go back to Upload page
  const handleReset = () => {
    setNumbers([]);
    setPage("upload");
  };

  return (
    <div className="dashboard">
      {/* SIDEBAR */}
      <div className="sidebar">
        <div className="sidebar-logo">AI Extractor</div>
        <div className="sidebar-menu">
          <div className="menu-item" onClick={() => setPage("upload")}>
            <FaUpload />
            Upload
          </div>
          <div className="menu-item" onClick={() => setPage("results")}>
            <FaChartBar />
            Results
          </div>
        </div>
      </div>

      {/* MAIN */}
      <div className="main">
        <div className="navbar">
          <h2>{page === "upload" ? "Upload Images" : "Extraction Results"}</h2>
        </div>

        <div className="content">
          {page === "upload" && <Upload setNumbers={handleExtraction} />}
          {page === "results" && <Results numbers={numbers} reset={handleReset} />}
        </div>
      </div>
    </div>
  );
}

export default App;