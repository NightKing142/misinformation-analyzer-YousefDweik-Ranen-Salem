import React, { useState } from 'react';
import './App.css'; // Make sure you have this CSS file

function App() {
    const [text, setText] = useState('');
    const [result, setResult] = useState(null);
    const [isLoading, setIsLoading] = useState(false);

    const handleAnalyzeClick = () => {
        setIsLoading(true);
        setResult(null);

        // FIXED: The URL is now a clean string without extra characters.
        fetch('http://127.0.0.1:5000/api/analyze', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ text: text }),
        })
            .then(response => {
                if (!response.ok) {
                    throw new Error(`Server responded with an error: ${response.status}`);
                }
                return response.json();
            })
            .then(data => {
                setResult(data);
            })
            .catch(error => {
                console.error('Error during analysis:', error);
                setResult({
                    score: 'N/A',
                    summary: `An error occurred. Please check the console for details. (${error.message})`,
                    analysis: { fallacies: [], biases: [] }
                });
            })
            .finally(() => {
                setIsLoading(false);
            });
    };

    // A new component to render the detailed analysis cards
    const AnalysisCard = ({ title, items }) => {
        if (!items || items.length === 0) {
            return null; // Don't render the section if there's nothing to show
        }
        return (
            <div className="analysis-section">
                <h3>{title}</h3>
                {items.map((item, index) => (
                    <div key={index} className="card">
                        <h4>{item.type}</h4>
                        <p>{item.explanation}</p>
                        {item.evidence && item.evidence.length > 0 && (
                            <div className="evidence">
                                <strong>Evidence:</strong>
                                <ul>
                                    {item.evidence.map((quote, qIndex) => (
                                        <li key={qIndex}>"{quote}"</li>
                                    ))}
                                </ul>
                            </div>
                        )}
                    </div>
                ))}
            </div>
        );
    };

    return (
        <div className="App">
            <header className="App-header">
                <h1>Misinformation Analyzer</h1>
                <p className="subtitle">Enter text below to analyze it for logical fallacies and cognitive biases.</p>
                <textarea
                    rows="10"
                    cols="80"
                    placeholder="Paste a news headline, social media post, or any text here..."
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                />
                <br />
                <button onClick={handleAnalyzeClick} disabled={isLoading || !text}>
                    {isLoading ? 'Analyzing...' : 'Analyze Text'}
                </button>
            </header>

            {result && (
                <div className="results">
                    <h2>Analysis Complete</h2>
                    <div className="summary-card">
                        <div className="score">
                            <span>Misleading Score</span>
                            <strong>{result.score}/10</strong>
                        </div>
                        <p><strong>Summary:</strong> {result.summary}</p>
                    </div>

                    {/* Use the new component to display the detailed analysis */}
                    <AnalysisCard title="Logical Fallacies Detected" items={result.analysis?.fallacies} />
                    <AnalysisCard title="Cognitive Biases Detected" items={result.analysis?.biases} />
                </div>
            )}
        </div>
    );
}

export default App;
