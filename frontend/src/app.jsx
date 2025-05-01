import React, { useState } from "react";
import axios from "axios";

function App() {
  const [text, setText] = useState("");
  const [predictions, setPredictions] = useState(null);

  const handleSubmit = async () => {
    try {
      const response = await axios.post("http://127.0.0.1:8000/automl/predict", {
        text,
      });
      setPredictions(response.data.predictions);
    } catch (error) {
      console.error("Error making predictions", error);
    }
  };

  return (
    <div>
      <h1>RODAAI Prediction</h1>
      <textarea
        value={text}
        onChange={(e) => setText(e.target.value)}
      ></textarea>
      <button onClick={handleSubmit}>Make Prediction</button>
      {predictions && <pre>{JSON.stringify(predictions, null, 2)}</pre>}
    </div>
  );
}

export default App;
