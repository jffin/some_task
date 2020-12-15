import Vue from 'vue';
import Vuex from 'vuex';

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    texts: [],
  },

  getters: {
    texts: state => {
      return state.texts
    },
  },

  mutations: {
    addTextAction(newText) {
      if (this.debug) console.log('addText triggered with', newText);
      this.state.texts.push(newText);
    },
    addTextsAction(texts) {
      if (this.debug) console.log('addTexts triggered with', texts);
      this.state.texts = texts;
    },
    clearTextsAction() {
      if (this.debug) console.log('clearTexts triggered');
      this.state.texts = [];
    },
  },

  actions: {},
  modules: {},
});
