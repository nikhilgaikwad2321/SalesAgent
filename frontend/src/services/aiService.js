
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8000/api'; // Direct to Python Backend

const aiService = {
  getAssistance: async (intent, query, filters = {}, response_language = "EN") => {
    try {
      // Endpoint is /llm/generate based on app/api.py router
      const response = await axios.post(`${API_BASE_URL}/llm/generate`, {
        intent,
        query,
        filters,
        response_language
      });
      return response.data;
    } catch (error) {
      console.error('Error fetching AI assistance:', error);
      throw error;
    }
  },
};

export default aiService;
