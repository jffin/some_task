import axios from 'axios'
import settings from './settings'


class TextClient {
  constructor() {
    this.http = axios.create({
      baseURL: settings.WebApiUrl,
    })
  }

  get(url, config) {
    return this.http.get(url, config)
  }

  post(url, data) {
    return this.http.post(url, data);
  }

  async addNewText({text}) {
    const response = this.post('users/', text);
    return response.data;
  }
}

const textClient = new TextClient();
export default textClient;
