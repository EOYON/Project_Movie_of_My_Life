<template>
  <div>
    <div class="personBox">
      <img
        class="personImg"
        v-if="person.profile_path"
        v-bind:src="url + person.profile_path"
        alt=""
      />
      <img
        class="personImg"
        v-if="!person.profile_path"
        src="http://localhost:8000/static/Unknown_person.jpg"
        alt=""
      />
      <p class="hoverText">
        <span>
          {{ person.name }}
        </span>
        <br />
      </p>
      <span class="heartBtn" v-on:click="creditFollow(person)">
        <b-icon
          icon="heart"
          v-if="!isLike"
          font-scale="1.5"
          class="beat"
          v-bind:style="{ color: isLike ? 'red' : 'gray' }"
        ></b-icon>
        <b-icon
          icon="heart-fill"
          v-if="isLike"
          font-scale="1.5"
          class="beat"
          v-bind:style="{ color: isLike ? 'red' : 'gray' }"
        ></b-icon>
      </span>
    </div>
  </div>
  <!-- <button v-on:click="creditFollow(credit)">팔로우</button> -->
</template>

<script>
import axios from "axios";
const API_URL = "http://127.0.0.1:8000";
export default {
  data() {
    return {
      selected: 0,
      isLike: false,
      url: "https://www.themoviedb.org/t/p/w138_and_h175_face",
    };
  },
  props: {
    person: Object,
  },
  created() {
    if (
      Object.keys(this.$store.state.recommended_movies).includes(
        this.person.name
      )
    ) {
      this.isLike = true;
    }
  },
  methods: {
    creditFollow(person) {
      axios({
        method: "post",
        url: `${API_URL}/api/v1/credits/${person.id}/follow/`,
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

<style scoped>
.personBox,
.personBox > img {
  /* display: flex; */
  position: relative;
  height: 175px;
  width: 138px;
}
.personBox:hover:after,
.personBox:hover > .hoverText,
.hoverText .heartBtn {
  display: block;
}
.personBox:after,
.hoverText {
  display: none;
}
.personBox:after {
  content: "";
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  left: 0;
  background: rgba(0, 0, 0, 0.3);
  z-index: 10;
}
.personBox {
  overflow: hidden;
}
.personBox:hover img {
  transform: scale(1.05);
  transition: 1.5s;
}
.hoverText {
  height: 175px;
  width: 138px;
  position: absolute;
  top: 38%;
  left: 0;
  color: #fff;
  z-index: 20;
  font-weight: 300;
  font-size: 13px;
}
.beat:hover {
  transform: scale(1.1);
  cursor: pointer;
}
.heartBtn {
  z-index: 30;
  position: absolute;
  right: 10px;
  top: 10px;
}
</style>
