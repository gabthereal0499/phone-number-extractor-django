import React, { useState } from "react";
import axios from "axios";
import { FaUpload, FaBolt } from "react-icons/fa";

function Upload({ setNumbers }) {
  const [files, setFiles] = useState([]);
  const [loading, setLoading] = useState(false);

  // Handle file input change
  const handleChange = (e) => {
    setFiles(e.target.files);
  };

  // Handle submit / extract numbers
  const handleSubmit = async () => {
    if (!files.length) {
      alert("Please upload images");
      return;
    }

    const formData = new FormData();
    for (let i = 0; i < files.length; i++) {
      formData.append("files", files[i]);
    }

    try {
      setLoading(true);

      // Call Django API to extract numbers
      const response = await axios.post(
        "http://127.0.0.1:8000/api/upload/",
        formData
      );

      // ✅ Pass numbers to App.js and automatically go to Results page
      setNumbers(response.data.numbers);

    } catch (error) {
      console.error(error);
      alert("Upload failed");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="card">

      <h2 className="upload-title">Upload Images</h2>

      <div className="upload-box">
        <FaUpload className="upload-icon" />
        <p className="upload-text">
          Drag & Drop Images or Click Below
        </p>

        <input
          type="file"
          multiple
          className="file-input"
          onChange={handleChange}
        />

        {files.length > 0 && (
          <p className="file-count">
            {files.length} file(s) selected
          </p>
        )}
      </div>

      <button
        className="extract-btn"
        onClick={handleSubmit}
        disabled={loading}
      >
        {loading ? (
          <>
            <span className="loader"></span>
            Extracting Numbers...
          </>
        ) : (
          <>
            <FaBolt className="bolt-icon"/>
            Extract Numbers
          </>
        )}
      </button>

    </div>
  );
}

export default Upload;