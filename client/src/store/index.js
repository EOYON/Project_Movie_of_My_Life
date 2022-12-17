import Vue from "vue";
import Vuex from "vuex";
import axios from "axios";
import createPersistedState from "vuex-persistedstate";
Vue.use(Vuex);

const API_URL = "http://127.0.0.1:8000";

export default new Vuex.Store({
  plugins: [
    createPersistedState({
      storage: window.sessionStorage,
    }),
  ],
  state: {
    // userdata: [],
    movies: [],
    popular_movies: [],
    recommended_movies: [],
    username: "",
    TOKEN: "",
  },
  getters: {},
  mutations: {
    GET_MOVIES_DATA(state, movies) {
      state.movies = movies;
    },

    GET_POPULAR_MOVIES_DATA(state, popular_movies) {
      state.popular_movies = popular_movies;
    },

    GET_RECOMMENDED_MOVIES_DATA(state, recommended_movies) {
      state.recommended_movies = recommended_movies;
    },

    LOGIN(state, TOKEN) {
      state.TOKEN = TOKEN;
    },

    GET_USERNAME(state, username) {
      state.username = username;
    },

    LOGOUT(state) {
      state.TOKEN = "";
      state.username = "";
      state.recommended_movies = [];
      state.first_movies = [];
    },
  },
  actions: {
    // 1. 모든 영화 리스트
    getMoviesData(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/`,
      })
        .then((res) => {
          context.commit("GET_MOVIES_DATA", res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // 2. 인기 영화 리스트
    getPopularMoviesData(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/popular/`,
      })
        .then((res) => {
          context.commit("GET_POPULAR_MOVIES_DATA", res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    // 3. 유저별 추천 영화 리스트
    getRecommendedMoviesData(context) {
      axios({
        method: "get",
        url: `${API_URL}/api/v1/movies/recommended/`,
        headers: {
          Authorization: `Token ${context.state.TOKEN}`,
        },
      })
        .then((res) => {
          context.commit("GET_RECOMMENDED_MOVIES_DATA", res.data);
        })
        .catch((error) => {
          console.log(error);
        });
    },

    login(context, TOKEN) {
      context.commit("LOGIN", TOKEN);
    },

    get_username(context, username) {
      context.commit("GET_USERNAME", username);
    },

    logout(context) {
      window.sessionStorage.clear();
      context.commit("LOGOUT");
    },

  },
});
