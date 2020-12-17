import Vue from 'vue';
import Vuex from 'vuex';

import textClient from '../text-client'

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    text: [],
    texts: [],
    similarSentences: [],
  },

  getters: {
    texts: state => {
      return state.texts;
    },
    text: state => {
      return state.text;
    },
  },

  mutations: {
    addText(state, newText) {
      state.texts.unshift(newText);
    },
    addTexts(state, texts) {
      state.texts = texts;
    },
    clearTextsAction(state) {
      state.texts = [];
    },
    addTextSentences(state, textSentences) {
      state.text = textSentences;
    },
  },

  actions: {
    async sendText({commit}, newText) {
      const response = await textClient.addNewText(newText);
      console.log(response);
      if (response.text) {
        commit('addText', response.text);
      }
      return (response.msg) ? response.msg : response.message;
    },
    async getTexts({commit, state}) {
      if (!state.texts.length) {
        const response = await textClient.getTexts();
        commit('addTexts', response.results.reverse());
      }
    },
    async getText({commit}, slug) {
      commit('addTextSentences', []);
      const response = await textClient.getText(slug);
      commit('addTextSentences', response.text);
    },
  },

  modules: {},
});
