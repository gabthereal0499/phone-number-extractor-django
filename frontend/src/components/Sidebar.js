import React from "react";
import { FaRobot, FaUpload, FaChartBar } from "react-icons/fa";

function Sidebar() {

  return (

    <div className="sidebar">

      <div className="sidebar-logo">
        AI Extractor
      </div>

      <div className="sidebar-menu">

        <div className="menu-item">
          <FaUpload />
          Upload
        </div>

        <div className="menu-item">
          <FaChartBar />
          Results
        </div>

      </div>

    </div>

  );

}

export default Sidebar;