import React, { useState } from "react";
import axios from "axios";
import { FaDownload, FaWhatsapp, FaRedo, FaCopy, FaCheck } from "react-icons/fa";

function Result({ numbers = [], reset }) {
  const [search, setSearch] = useState("");
  const [copiedIndex, setCopiedIndex] = useState(null);
  const [downloading, setDownloading] = useState(false);
  const [sending, setSending] = useState(false);

  // Filter numbers based on search input
  const filteredNumbers = numbers.filter((num) =>
    num.toLowerCase().includes(search.toLowerCase())
  );

  // Copy a single phone number to clipboard
  const copyNumber = (num, index) => {
    navigator.clipboard.writeText(num)
      .then(() => setCopiedIndex(index))
      .catch((err) => console.error("Copy failed:", err));

    // Reset copied state after 1.5 seconds
    setTimeout(() => setCopiedIndex(null), 1500);
  };

  // Download Excel file from Django backend
  const handleDownload = async () => {
    try {
      setDownloading(true);
      const response = await axios.get(
        "http://127.0.0.1:8000/api/download/",
        { responseType: "blob" }
      );

      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement("a");
      link.href = url;
      link.download = "phone_numbers.xlsx";
      document.body.appendChild(link);
      link.click();
      link.remove();

    } catch (error) {
      console.error(error);
      alert("Download failed");
    } finally {
      setDownloading(false);
    }
  };

  // Send WhatsApp messages via Django backend
  const handleSendMessages = async () => {
    if (numbers.length === 0) {
      alert("No numbers to send messages to");
      return;
    }

    try {
      setSending(true);

      const formData = new FormData();
      numbers.forEach((num) => formData.append("numbers", num));
      formData.append(
        "message",
        "Hello! This message was sent using the AI Phone Extractor."
      );

      await axios.post(
        "http://127.0.0.1:8000/api/send-messages/",
        formData
      );

      alert("Messages sent successfully");

    } catch (error) {
      console.error(error);
      alert("Message sending failed");
    } finally {
      setSending(false);
    }
  };

  return (
    <div className="card">

      <h3>Extraction Results</h3>

      {/* Stats */}
      <div className="stats">
        <div className="stat-box">
          <h2>{numbers.length}</h2>
          <p>Total Numbers Found</p>
        </div>
      </div>

      {/* Search Input */}
      <input
        className="search"
        type="text"
        placeholder="Search phone number..."
        value={search}
        onChange={(e) => setSearch(e.target.value)}
      />

      {/* Numbers Table */}
      <table>
        <thead>
          <tr>
            <th>#</th>
            <th>Phone Number</th>
            <th>Copy</th>
          </tr>
        </thead>
        <tbody>
          {filteredNumbers.length === 0 ? (
            <tr>
              <td colSpan="3" style={{ textAlign: "center", padding: "20px" }}>
                No numbers found
              </td>
            </tr>
          ) : (
            filteredNumbers.map((num, index) => (
              <tr key={index}>
                <td>{index + 1}</td>
                <td>{num}</td>
                <td>
                  <button
                    className="btn copy-btn"
                    onClick={() => copyNumber(num, index)}
                  >
                    {copiedIndex === index ? (
                      <>
                        <FaCheck /> Copied
                      </>
                    ) : (
                      <>
                        <FaCopy /> Copy
                      </>
                    )}
                  </button>
                </td>
              </tr>
            ))
          )}
        </tbody>
      </table>

      {/* Action Buttons */}
      <div className="actions">

        <button
          className="btn action-btn"
          onClick={handleDownload}
          disabled={downloading}
        >
          <FaDownload />
          {downloading ? " Downloading..." : " Download Excel"}
        </button>

        <button
          className="btn action-btn whatsapp-btn"
          onClick={handleSendMessages}
          disabled={sending}
        >
          <FaWhatsapp />
          {sending ? " Sending..." : " Send WhatsApp"}
        </button>

        <button
          className="btn action-btn reset-btn"
          onClick={reset}
        >
          <FaRedo /> Upload Again
        </button>

      </div>
    </div>
  );
}

export default Result;