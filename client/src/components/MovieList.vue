<template>
  <div>
    <h1 class="themeText">{{ movieList.text }}</h1>
    <!-- <div> -->
    <div class="movieList">
      <span v-bind:class="{ hidden: selected == 1 }">
        <b-icon
          icon="arrow-left-circle-fill"
          font-scale="3"
          class="left"
          v-on:click="pre"
        ></b-icon>
      </span>
      <div
        class="imgList"
        v-bind:style="{
          transform: 'translate(-' + (selected - 1) * 1400 + 'px, 0px)',
        }"
      >
        <MovieListItem
          v-for="(movie, index) in movieList.movies"
          v-bind:key="index"
          v-bind:movie="movie"
        />
      </div>
      <span v-bind:class="{ hidden: selected == page }">
        <b-icon
          icon="arrow-right-circle-fill"
          font-scale="3"
          class="right"
          v-on:click="next"
        ></b-icon>
      </span>
    </div>
  </div>
</template>

<script>
import MovieListItem from "@/components/MovieListItem.vue";
export default {
  data() {
    return {
      page: "",
      selected: 1,
    };
  },
  props: {
    movieList: Object,
  },
  components: {
    MovieListItem,
  },
  created() {
    if (this.movieList.movies.length) {
      this.page = parseInt((this.movieList.movies.length - 1) / 7) + 1;
    }
  },
  methods: {
    next() {
      if (this.selected == this.page) {
        this.selected == 1;
      } else {
        this.selected = this.selected + 1;
      }
    },
    pre() {
      if (this.selected == 1) {
        this.selected == this.page;
      } else {
        this.selected = this.selected - 1;
      }
    },
  },
};
</script>

<style scoped>
.movieList {
  position: relative;
  height: 300px;
  width: 1400px;
  overflow: hidden;
  flex-direction: row;
  /* 좌우 보이게 만들고 싶으면 뺄것*/
}
.imgList {
  display: flex;
  /* overflow: hidden; */
  transition: 1s;
}
.hidden {
  visibility: hidden;
}
.right {
  position: absolute;
  right: 5px;
  top: 45%;
  z-index: 30;
  cursor: pointer;
  color: white;
}
.left {
  position: absolute;
  left: 5px;
  top: 45%;
  z-index: 30;
  cursor: pointer;
  color: white;
}
/* .themeText {
  display: inline-block;
} */
</style>
