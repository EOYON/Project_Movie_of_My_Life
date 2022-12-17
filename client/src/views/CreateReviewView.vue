<template>
  <div class="reviewPage">
    <h1>Review</h1>
    <form v-on:submit.prevent="createReview">
      <div>
        <label for="vote_point">점수 : </label>
        <input type="number" id="vote_point" min="0" max="5" step="0.5" v-model="vote_point"><br>
      </div>
      <div>
        <label for="content">내용 : </label>
        <textarea id="content" cols="30" rows="10" v-model="content"></textarea><br>
      </div>
      <div>
        <input type="submit" id="submit">
      </div>
    </form>
  </div>
</template>

<script>
import axios from 'axios'
const API_URL = 'http://127.0.0.1:8000'
export default {
  data() {
    return {
      vote_point: null,
      content: null,
    }
  },
  methods: {
    createReview() {
      const vote_point = this.vote_point
      const content = this.content
      if (!vote_point) {
        alert("평점을 입력해주세요!")
        return 
      }
      axios({
        method: 'post',
        url: `${API_URL}/api/v1/movies/${this.$route.params.id}/reviews/`,
        data: {
          vote_point: vote_point,
          content: content,
        },
        headers: {
          Authorization: `Token ${this.$store.state.TOKEN}`
        }
      })
        .then(() => {
          this.$router.push({name: 'MovieDetail'})
        })
        .catch((err) => {
          console.log(err)
        })
    } 
  }
}
</script>

<style>
.reviewPage > h1 {
  color: #da942c;
}
.reviewPage form{
  padding: 25px;
}
</style>