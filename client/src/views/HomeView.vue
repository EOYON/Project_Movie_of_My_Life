<template>
  <div class="home">
    <div>
      <input
        class="search-input"
        v-on:input="searchText = $event.target.value"
        type="text"
        v-on:keyup="searchMovie"
        placeholder="SearchMovie"
      />
    </div>
    <div class="movieList" v-if="this.isSearched">
      <MovieList v-bind:movieList="searchMovies" />
    </div>
    <div v-if="!this.isSearched">
      <p v-if="this.searchText">검색된 결과가 없습니다.</p>
    </div>
  </div>
</template>

<script>
import MovieList from "@/components/MovieList.vue";
export default {
  data() {
    return {
      searchText: "",
      searchMovies: {},
      isSearched: false,
    };
  },
  components: {
    MovieList,
  },
  methods: {
    searchMovie() {
      if (this.searchText.trim()) {
        this.searchMovies = {};
        const movies = [];
        for (const movie of this.$store.state.movies) {
          if (movie.title.includes(this.searchText)) {
            movies.push(movie);
          }
        }
        if (!movies.length) {
          this.isSearched = false;
        } else {
          this.searchMovies["movies"] = movies;
          this.searchMovies["text"] = "검색된 영화";
          this.isSearched = true;
        }
      } else {
        this.isSearched = false;
      }

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
