<template>
  <div>
    <div class="MovieDetail">
      <div class="movieCard">
        <img class="" v-bind:src="movieurl + movie.poster_path" alt="" />
        <div class="movieInfo">
          <p>제목 : {{ movie.title }}</p>
          <p>개봉일 : {{ movie.release_date }}</p>
          <p>평점 : {{ movie.vote_average }}</p>
          <p>{{ movie.overview }}</p>
      <!-- 장르 -->
          <span v-for="genre in movie.genre" v-bind:key="genre.id">
            <GenreListItem v-bind:genre="genre" />
          </span>
        </div>
      </div>


      <!-- 출연진 -->
      <div class="creditList">
        <CreditList v-bind:credit="movie.credit" />
      </div>

      <!-- 리뷰 -->
      <div class="reviewBox">
        <div>
          Reviews |
          <router-link v-bind:to="{ name: 'CreateReview' }">Create</router-link>
        </div>
        <div
          class="userReview"
          v-for="review in movie.reviews"
          v-bind:key="review.id"
          v-bind:class="{ hidden: review.vote_point == -1 }"
        >
          {{ review.user.username }} - 평점 : {{ review.vote_point }} 내용 :
          {{ review.content }}
          <b-icon icon="eraser" font-scale="1.3" class="beat" v-on:click="deleteReview(review)"></b-icon>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import CreditList from "@/components/CreditList.vue";
import GenreListItem from "@/components/GenreListItem.vue";
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  data() {
    return {
      movie: "",
      movieurl: "https://www.themoviedb.org/t/p/w300_and_h450_bestv2",
      isLike: false,
    };
  },
  async created() {
    const movie_id = this.$route.params.id;
    const API_URL = "http://127.0.0.1:8000";
    await axios({
      method: "get",
      url: `${API_URL}/api/v1/movies/${movie_id}`,
      // headers: {
      //   Authorization: `Token ${this.$store.state.TOKEN}`,
      // },
    })
      .then((res) => {
        this.movie = res.data;
      })
      .catch((error) => {
        console.log(error);
      });
  },
  components: { CreditList, GenreListItem },
  methods: {
    deleteReview(review) {
      axios({
        method: "delete",
        url: `${API_URL}/api/v1/movies/reviews/${review.id}/`,
        headers: {
          Authorization: `Token ${this.$store.state.TOKEN}`,
        },
      })
        .then(() => {
          review.vote_point = -1;
        })
        .catch((err) => {
          console.log(err);
        });
    },
  },
};
</script>

<style scoped>
.movieCard {
  margin: auto;
  display: flex;
  width: 690px;
}
.hidden {
  display: none;
}
.creditList {
  display: flex;
  /* position: relative; */
  margin: auto;
  flex-direction: column;
  /* align-items: center; */
}
.movieInfo {
  color: white;
  background-color: rgb(34, 31, 31);
  /* font-weight: bold; */
  padding: 20px;
}
.reviewBox {
  font-weight: bold;
  margin: 30px;
}
.reviewBox a {
  color: #2c3e50;
}
.userReview {
  margin: 10px;
}
.beat:hover {
  transform: scale(1.2);
  cursor: pointer;
}
</style>
