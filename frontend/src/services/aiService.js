
import axios from 'axios';

const API_BASE_URL = 'http://localhost:8080/api/ai';

const aiService = {
  getAssistance: async (intent, query, filters = {}) => {
    try {
      const response = await axios.post(`${API_BASE_URL}/assist`, {
        intent,
        query,
        filters,
      });
      return response.data;
    } catch (error) {
      console.error('Error fetching AI assistance:', error);
      throw error;
    }
  },
};

export default aiService;
