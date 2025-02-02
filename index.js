import { useState } from "react";

export default function App() {
  const [prompt, setPrompt] = useState("");
  const [response, setResponse] = useState("");
  const [status, setStatus] = useState("");

  const checkAPI = async () => {
    try {
      const res = await fetch("http://localhost:8000/API-check");
      const data = await res.text();
      setStatus(data);
    } catch (error) {
      setStatus("Error connecting to API");
    }
  };

  const generateText = async () => {
    try {
      const res = await fetch(`http://localhost:8000/generate/?prompt=${encodeURIComponent(prompt)}`);
      const data = await res.json();
      setResponse(data.response);
    } catch (error) {
      setResponse("Error generating response");
    }
  };

  return (
    <div className="flex flex-col items-center p-8 bg-gray-100 min-h-screen">
      <h1 className="text-3xl font-bold mb-6">FastAPI + Ollama Frontend</h1>
      
      <button onClick={checkAPI} className="mb-4 p-2 bg-blue-500 text-white rounded-lg">Check API Status</button>
      <pre className="mb-4 p-2 bg-gray-200 rounded w-full max-w-lg">{status}</pre>
      
      <textarea
        className="w-full max-w-lg p-2 border rounded"
        rows="4"
        placeholder="Enter your prompt here..."
        value={prompt}
        onChange={(e) => setPrompt(e.target.value)}
      />
      
      <button onClick={generateText} className="mt-4 p-2 bg-green-500 text-white rounded-lg">Generate</button>
      <pre className="mt-4 p-2 bg-gray-200 rounded w-full max-w-lg">{response}</pre>
    </div>
  );
}
