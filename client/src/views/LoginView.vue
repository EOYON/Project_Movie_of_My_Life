<template>
  <div>
    <h1>Login</h1>
    <div>
      <div>
        <input type="text" v-model="username" placeholder="아이디를 입력하세요"
 />
      </div>
      <div>
        <input v-on:keyup.enter="login" type="password" v-model="userpassword" placeholder="비밀번호를 입력하세요" />
      </div>
      <button v-on:click="login">로그인</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      username: "",
      userpassword: "",
      URL: "http://localhost:8000/",
    };
  },
  methods: {
    async login() {
      try {
        const response = await axios.post(this.URL + "accounts/login/", {
          username: this.username,
          password: this.userpassword,
        });
        if (response.data) {
          this.$store.dispatch("login", response.data.key);
          this.$store.dispatch("get_username", this.username);
          this.$router.push({ name: "home" });
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
