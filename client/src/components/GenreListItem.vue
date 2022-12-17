<template>
  <div>
    {{ genre.name }}
    <b-icon
      v-on:click="genreFollow(genre)"
      icon="bookmark"
      v-if="!isLike"
      font-scale="1.4"
      class="beat"
      v-bind:style="{ color: isLike ? 'yellow' : 'gray' }"
    ></b-icon>
    <b-icon
      v-on:click="genreFollow(genre)"
      icon="bookmark-star-fill"
      v-if="isLike"
      font-scale="1.4"
      class="beat"
      v-bind:style="{ color: isLike ? 'yellow' : 'gray' }"
    ></b-icon>
  </div>
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  data() {
    return {
      isLike: false,
    };
  },
  props: { genre: Object },
  created() {
    if (
      Object.keys(this.$store.state.recommended_movies).includes(
        this.genre.name
      )
    ) {
      this.isLike = true;
    }
  },
  methods: {
    genreFollow(genre) {
      axios({
        method: "post",
        url: `${API_URL}/api/v1/movies/genres/${genre.id}/follow/`,
        headers: {
          Authorization: `Token ${this.$store.state.TOKEN}`,
        },
      })
        .then(() => {
          this.isLike = !this.isLike;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style>
.beat:hover {
  transform: scale(1.1);
  cursor: pointer;
}
</style>
