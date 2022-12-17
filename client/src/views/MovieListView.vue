<template>
  <div>
    <div
      class="movieList"
      v-for="(movieList, index) in recommended_movies"
      v-bind:key="index"
    >
      <MovieList v-bind:movieList="movieList" />
    </div>
    <div
      class="movieList"
      v-for="(movieList, index) in popular_movies"
      v-bind:key="index"
    >
      <MovieList v-bind:movieList="movieList" />
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
export default {
  data() {
    return {};
  },
  components: {
    MovieList,
  },
  created() {
    this.getMoviesData();
  },
  methods: {
    getMoviesData() {
      this.$store.dispatch("getMoviesData");
      this.$store.dispatch("getPopularMoviesData");
      if (this.$store.state.TOKEN) {
        this.$store.dispatch("getRecommendedMoviesData");
      }
    },
  },
  computed: {
    popular_movies() {
      return this.$store.state.popular_movies;
    },
    recommended_movies() {
      return this.$store.state.recommended_movies
    },
  },
};
</script>

<style>
.movieList {
  display: flex;
  /* position: relative; */
  margin: auto;
  flex-direction: column;
  /* align-items: center; */
}
</style>
