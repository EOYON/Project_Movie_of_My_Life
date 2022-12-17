<template>
  <div id="app">
    <nav>
      <router-link to="/">Home</router-link> |
      <router-link to="/search">Search</router-link>
      <span v-if="$store.state.username === ''">
        | <router-link to="/login">Login</router-link>
        | <router-link to="/signup">Sign Up</router-link>  
      </span>
      <span v-if="$store.state.username !== ''">
        | {{ $store.state.username }}
        | <router-link to="/logout">Logout</router-link>
      </span>
    </nav>
    <router-view />
  </div>
</template>

<script>
import axios from "axios";
export default {
  data() {
    return {
      URL: "http://localhost:8000/",
    };
  },
  props: {
    username: String,
  },
  methods: {
    async logout() {
      try {
        const response = await axios.post(this.URL + "accounts/logout/");
        if (response.data) {
          this.$store.dispatch("logout");
          alert("로그아웃되었습니다.");
          this.$router.push({ name: "home" });
        }
      } catch (error) {
        console.log(error);
      }
    },
  },
  watch: {
    $route(to) {
      if (to.name === "Logout") {
        this.logout();
      }
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #da942c;
}
</style>
