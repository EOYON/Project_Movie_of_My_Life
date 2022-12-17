<template>
  <div>
    <h1>Sign Up</h1>
    <div>
      <h2>회원가입</h2>
      <div>
        <input
          type="text"
          v-model="signupID"
          placeholder="아이디를 입력하세요"
        />
      </div>
      <div>
        <input
          type="password"
          v-model="signupPW1"
          placeholder="비밀번호를 입력하세요"
        />
      </div>
      <div>
        <input
        v-on:keyup.enter="signup"
          type="password"
          v-model="signupPW2"
          placeholder="비밀번호를 다시 입력하세요"
        />
      </div>
      <button v-on:click="signup">회원가입</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      signupID: "",
      signupPW1: "",
      signupPW2: "",
      URL: "http://localhost:8000/",
    };
  },
  methods: {
    async signup() {
      if (this.signupPW1 !== this.signupPW2) {
        alert("비밀번호가 일치하지 않습니다.");
        return;
      }
      try {
        const response = await axios.post(this.URL + "accounts/signup/", {
          username: this.signupID,
          password1: this.signupPW1,
          password2: this.signupPW2,
        });
        this.$store.dispatch("login", response.data.key);
        this.$store.dispatch("get_username", this.signupID);
        this.$router.push({ name: "home" });
      } catch (error) {
        console.log(error);
      }
    },
  },
};
</script>
