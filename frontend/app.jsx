import React, { useState } from "react";
import axios from "axios";
import PredictionForm from "./components/PredictionForm";

function App() {
  const [predictions, setPredictions] = useState(null);
  const [error, setError] = useState(null);

  const handlePrediction = async (file) => {
    const formData = new FormData();
    formData.append("file", file);

    try {
      // Replace 'http://127.0.0.1:8000' with your backend URL
      const response = await axios.post("askroda.com/automl/predict", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setPredictions(response.data.predictions);
      setError(null);
    } catch (err) {
      setError("Error making predictions");
      setPredictions(null);
    }
  };

  return (
    <div>
      <h1>RODAAI - AutoML Predictions</h1>
      <PredictionForm onSubmit={handlePrediction} />
      {error && <p style={{ color: "red" }}>{error}</p>}
      {predictions && (
        <div>
          <h2>Predictions:</h2>
          <pre>{JSON.stringify(predictions, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
