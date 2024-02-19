<template>
  <div>
    <insta-header></insta-header>
    <nav>
      <router-link to="/">홈</router-link>

    </nav>
    <router-view/>
    <insta-content v-bind:propsdata="userList"></insta-content>
    <insta-footer></insta-footer>
    <div id="app1">
      <div>{{ message }}</div>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue';
import Content from './components/Content.vue';
import Footer from './components/Footer.vue';
import axios from 'axios';


let url = 'http://localhost:8000/Profile/'

export default {
  data: () => {
    return {
      userList: []
    };
  },
  components: {
    'insta-header': Header,
    'insta-content': Content,
    'insta-footer': Footer,
  },
  mounted() {
    axios({
      method: "GET",
      url: url
    })
    .then(response => {
      this.userList = response.data;
    })
    .catch(response => {
      console.log("Failed", response);
    });
  },
};
</script>

<style>

</style>