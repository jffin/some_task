import axios from 'axios'
import settings from './settings'


class TextClient {
  constructor() {
    this.http = axios.create({
      baseURL: settings.WebApiUrl,
    })
  }

  get(url) {
    return this.http.get(url)
  }

  async post(url, data) {
    let response;
    try {
      response = await this.http.post(url, data);
    } catch (err) {
      response = (err.response.data) ? err.response : err;
    }
    return response;
  }

  async addNewText(text) {
    const response = await this.post('texts/', {content: text});
    return response.data;
  }

  async getTexts() {
    const response = await this.get('texts/');
    return response.data;
  }

  async getText(slug) {
    const response = await this.get(`text/${slug}/`);
    return response.data;
  }

  async getSimilarSentences(sentence, slug) {
    const response = await this.post(`text/${slug}/`, {sentence});
    return response.data;
  }
}

const textClient = new TextClient();
export default textClient;
