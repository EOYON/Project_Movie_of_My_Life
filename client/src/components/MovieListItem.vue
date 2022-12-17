<template>
  <div class="movieBox" v-on:click="goDetail(movie.id)">
    <img
      class="movieImg"
      v-bind:src="movieImgURL"
      alt="noimage"
    />
    <p class="hoverText">{{ movie.title }} <br> {{ movie.vote_average }}</p>
  </div>
</template>

<script>
export default {
  computed: {
    movieImgURL() {
      return `https://www.themoviedb.org/t/p/w300_and_h450_bestv2${this.movie.poster_path}`;
    },
  },
  props: {
    movie: Object,
  },
  methods: {
    goDetail(id) {
      this.$router.push({ name: "MovieDetail", params: { id } });
    },
  },
};
</script>

<style scoped>
.movieBox,
.movieBox > img {
  /* display: flex; */
  position: relative;
  height: 300px;
  width: 200px;
  cursor: pointer;
}
.movieBox:hover:after,
.movieBox:hover > .hoverText,
.hoverText {
  display: block;
}
.movieBox:after,
.hoverText {
  display: none;
}
.movieBox:after {
  content: '';
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.3);
  z-index: 10;
}
.movieBox {
  overflow: hidden;
}
.movieBox:hover img{
  transform: scale(1.10);
  transition: 1.5s;
}
.hoverText {
  height: 300px;
  width: 200px;
  position: absolute;
  top: 38%;
  left: 0;
  color: #fff;
  z-index: 20;
  font-weight: 600;
  font-size: 18px;
}
</style>
