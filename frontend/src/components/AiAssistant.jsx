import React, { useState, useRef, useEffect } from 'react';
import aiService from '../services/aiService';
import ReactMarkdown from 'react-markdown';
import './AiAssistant.css';

// SVG Icons
const SendIcon = () => (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" className="icon-send">
        <path d="M22 2L11 13" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
        <path d="M22 2L15 22L11 13L2 9L22 2Z" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" />
    </svg>
);

const AttachIcon = () => (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="#6b7280" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M21.44 11.05l-9.19 9.19a6 6 0 0 1-8.49-8.49l9.19-9.19a4 4 0 0 1 5.66 5.66l-9.2 9.19a2 2 0 0 1-2.83-2.83l8.49-8.48"></path>
    </svg>
);

const BellIcon = () => (
    <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
        <path d="M18 8A6 6 0 0 0 6 8c0 7-3 9-3 9h18s-3-2-3-9"></path>
        <path d="M13.73 21a2 2 0 0 1-3.46 0"></path>
    </svg>
);

const AiAssistant = () => {
    // State: History of messages (Persist context)
    const [messages, setMessages] = useState([
        {
            id: 1,
            type: 'bot',
            text: "Hello! I am your Bajaj Allianz Sales Assistant. How can I help you with policy details, product pitches, or objection handling today?"
        }
    ]);
    const [input, setInput] = useState('');
    const [loading, setLoading] = useState(false);
    const messagesEndRef = useRef(null);
    const inputRef = useRef(null);

    // Mock History Data
    const chatHistory = [
        { id: 1, title: 'Term Insurance Pitch', date: 'Today' },
        { id: 2, title: 'Objection: Too Expensive', date: 'Yesterday' },
        { id: 3, title: 'Competitor Analysis', date: 'Previous 7 Days' },
    ];

    // Auto-scroll to bottom
    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!input.trim()) return;

        // 1. Add User Message
        const userMsg = { id: Date.now(), type: 'user', text: input };
        setMessages(prev => [...prev, userMsg]);
        setInput('');
        setLoading(true);

        try {
            // 2. Call API (mocking 'general_query' intent for chat flow)
            const intent = 'general_query';
            const filters = { product: 'general' };

            const result = await aiService.getAssistance(intent, userMsg.text, filters);

            // 3. Add Bot Response
            const botMsg = {
                id: Date.now() + 1,
                type: 'bot',
                text: result.answer,
                confidence: result.confidence
            };
            setMessages(prev => [...prev, botMsg]);

        } catch (err) {
            const errorMsg = {
                id: Date.now() + 1,
                type: 'bot',
                text: "I apologize, but I'm having trouble connecting to the server. Please try again."
            };
            setMessages(prev => [...prev, errorMsg]);
        } finally {
            setLoading(false);
            // Keep focus for rapid chat
            setTimeout(() => inputRef.current?.focus(), 100);
        }
    };

    return (
        <div className="app-layout">
            {/* 1. Global Header (Top Level) */}
            <header className="app-header">
                <div className="header-content">
                    <div className="logo-area">
                        <img src="/new_logo.png" alt="Bajaj Allianz" className="brand-logo" onError={(e) => {
                            e.target.style.display = 'none';
                            e.target.parentNode.innerHTML = '<span class="brand-fallback">BAJAJ | Allianz</span>';
                        }} />
                    </div>

                    <div className="header-right">
                        <div className="user-profile-header">
                            <div className="user-details">
                                <span className="name">Nikhil Gaikwad</span>
                                <span className="role">Sales Agent</span>
                            </div>
                            <div className="avatar">NG</div>
                        </div>
                    </div>
                </div>
            </header>

            {/* 2. Main Content Wrapper (Sidebar + Chat) */}
            <div className="main-wrapper">

                {/* Sidebar - Below Header */}
                <aside className="sidebar">
                    <div className="sidebar-header">
                        <button className="new-chat-btn">
                            <span style={{ fontSize: '1.2rem' }}>+</span> New Chat
                        </button>
                    </div>
                    <div className="history-list">
                        <div className="history-group">
                            <div className="group-label">Today</div>
                            {chatHistory.filter(h => h.date === 'Today').map(chat => (
                                <div key={chat.id} className="history-item">
                                    {chat.title}
                                </div>
                            ))}
                        </div>
                        <div className="history-group">
                            <div className="group-label">Yesterday</div>
                            {chatHistory.filter(h => h.date === 'Yesterday').map(chat => (
                                <div key={chat.id} className="history-item">
                                    {chat.title}
                                </div>
                            ))}
                        </div>
                        <div className="history-group">
                            <div className="group-label">Previous 7 Days</div>
                            {chatHistory.filter(h => h.date === 'Previous 7 Days').map(chat => (
                                <div key={chat.id} className="history-item">
                                    {chat.title}
                                </div>
                            ))}
                        </div>
                    </div>
                    <div className="sidebar-footer">
                        <div className="user-profile">
                            <div className="avatar small">NG</div>
                            <div className="user-info">
                                <div className="user-name">Nikhil Gaikwad</div>
                                <div className="user-role">Sales Agent</div>
                            </div>
                        </div>
                    </div>
                </aside>

                {/* Main Chat Area */}
                <main className="chat-layout">
                    {/* Chat Container */}
                    <div className="chat-container">
                        <div className="messages-list">
                            {messages.map((msg) => (
                                <div key={msg.id} className={`message-row ${msg.type === 'user' ? 'user-row' : 'bot-row'}`}>
                                    <div className="message-bubble">
                                        {msg.type === 'bot' && <div className="bot-icon">🤖</div>}
                                        <div className="message-content">
                                            {msg.type === 'user' ? (
                                                <div className="text-user">{msg.text}</div>
                                            ) : (
                                                <div className="markdown-body">
                                                    <ReactMarkdown>{msg.text}</ReactMarkdown>
                                                </div>
                                            )}
                                        </div>
                                    </div>
                                </div>
                            ))}

                            {loading && (
                                <div className="message-row bot-row">
                                    <div className="message-bubble">
                                        <div className="bot-icon">🤖</div>
                                        <div className="typing-indicator">
                                            <span></span><span></span><span></span>
                                        </div>
                                    </div>
                                </div>
                            )}
                            <div ref={messagesEndRef} />
                        </div>
                    </div>

                    {/* Fixed Input Area */}
                    <div className="input-area">
                        <div className="input-wrapper">
                            <form onSubmit={handleSubmit} className="chat-input-form">
                                <button type="button" className="attach-btn" title="Attach (Mock)">
                                    <AttachIcon />
                                </button>
                                <input
                                    ref={inputRef}
                                    type="text"
                                    value={input}
                                    onChange={(e) => setInput(e.target.value)}
                                    placeholder="Type a message..."
                                    disabled={loading}
                                />
                                <button type="submit" className="send-btn" disabled={!input.trim() || loading}>
                                    <SendIcon />
                                </button>
                            </form>
                            <div className="footer-note">
                                Bajaj Life Insurance Sales Assistant
                            </div>
                        </div>
                    </div>
                </main>
            </div>
        </div>
    );
};

export default AiAssistant;
