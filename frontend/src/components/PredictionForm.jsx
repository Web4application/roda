import React, { useState } from "react";

function PredictionForm({ onSubmit }) {
  const [file, setFile] = useState(null);

  const handleFileChange = (e) => {
    const uploadedFile = e.target.files[0];
    if (uploadedFile) {
      setFile(uploadedFile);
    }
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    if (file) {
      onSubmit(file);  // Pass the file to the parent component's handler
    } else {
      alert("Please select a file.");
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <label htmlFor="file-upload">Upload CSV file for prediction:</label>
        <input
          type="file"
          id="file-upload"
          accept=".csv"
          onChange={handleFileChange}
        />
        <button type="submit">Predict</button>
      </form>
    </div>
  );
}

export default PredictionForm;
