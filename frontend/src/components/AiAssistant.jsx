import React, { useState } from 'react';
import aiService from '../services/aiService';
import './AiAssistant.css';

const intents = [
    { value: 'product_pitch', label: 'Product Pitch' },
    { value: 'objection_handling', label: 'Handle Objection' },
    { value: 'competitor_comparison', label: 'Competitor Comparison' },
    { value: 'general_query', label: 'General Query' },
];

const AiAssistant = () => {
    const [query, setQuery] = useState('');
    const [intent, setIntent] = useState('product_pitch');
    const [response, setResponse] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!query.trim()) return;

        setLoading(true);
        setError(null);
        setResponse(null);

        try {
            // Basic filters - in a real app these might come from UI
            const filters = { product: 'general' };
            const result = await aiService.getAssistance(intent, query, filters);
            setResponse(result);
        } catch (err) {
            setError('Failed to get response from AI assistant. Please try again.');
        } finally {
            setLoading(false);
        }
    };

    return (
        <div className="ai-assistant-container">
            <div className="header">
                <h1>🔍 Sales Agent Assistant</h1>
                <p>Powered by RAG & LLM</p>
            </div>

            <div className="content-grid">
                <div className="input-section card">
                    <form onSubmit={handleSubmit}>
                        <div className="form-group">
                            <label>Intent</label>
                            <select value={intent} onChange={(e) => setIntent(e.target.value)}>
                                {intents.map((opt) => (
                                    <option key={opt.value} value={opt.value}>
                                        {opt.label}
                                    </option>
                                ))}
                            </select>
                        </div>

                        <div className="form-group">
                            <label>Your Query</label>
                            <textarea
                                value={query}
                                onChange={(e) => setQuery(e.target.value)}
                                placeholder="E.g., Explain term insurance benefits..."
                                rows={5}
                                required
                            />
                        </div>

                        <button type="submit" className="submit-btn" disabled={loading}>
                            {loading ? <span className="spinner"></span> : 'Ask AI Assistant'}
                        </button>
                    </form>
                </div>

                <div className="response-section card">
                    {error && <div className="error-message">{error}</div>}

                    {!response && !loading && !error && (
                        <div className="placeholder-state">
                            <p>AI response will appear here...</p>
                        </div>
                    )}

                    {response && (
                        <div className="response-content">
                            <div className="badge success">
                                Confidence: {response.confidence}
                            </div>
                            <h3>AI Suggestion:</h3>
                            <div className="markdown-body">
                                {response.answer}
                            </div>
                        </div>
                    )}
                </div>
            </div>
        </div>
    );
};

export default AiAssistant;
