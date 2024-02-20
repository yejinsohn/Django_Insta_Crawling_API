<template>
  <div>
    <insta-header></insta-header>
    <div id="body-wrapper">
      <div id="body-content">
        <div id="user_search">
          <h3>Instagram 사용자 :</h3> <input class="input-box" type="text" name="username" placeholder="사용자 이름을 입력하세요.">
          <button type="submit" class="btn" @click="navigateToAnalysisPage">분석</button>
        </div>
        <div class="guide" v-if="$route.path === '/'">
          인스타그램 사용자를 입력해주세요.
        </div>
        <router-view :userList="userList" />
      </div>
      <insta-footer></insta-footer>
    </div>
  </div>
</template>

<script>
import Header from './components/Header.vue';
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
    'insta-footer': Footer,
  },
  mounted() {
    axios({
      method: "GET",
      url: url
    })
    .then(response => {
      this.userList = response.data;
      console.log(response);
      this.$router.push({ name: 'analysis', params: { userList: this.userList } });
    })
    .catch(response => {
      console.log("Failed", response);
    });
  },
  methods: {
    navigateToAnalysisPage() {
      this.$router.push('/analysis');
    },
  },
};
</script>

<style>
body {
  padding-top: 100px;
}
#body-wrapper {
    min-height: 100%;
    position: relative;
}
#body-content {
    margin-top: 100px;
    padding-bottom: 200px;
}
#user_search {
  display: flex;
  font-size: large;
  font-weight: 500;
  gap: 10px;
  flex-direction: row;
  justify-content: center;
  align-items: center;
}
.input-box {
  width: 300px;
  border: 1px solid rgb(46, 46, 46);
  padding: 5px 10px;
  font-size: initial;
  font-weight: 400;
}
.btn {
    display: inline-flex;
    padding: 5px 25px;
    background: #0CB2C9;
    border: none;
    font-weight: 500;
    border-radius: 8px;
    transition: 0.2s;
}
.btn:hover{
    background: #00a1b7
}
.guide {
  height: 200px;
  padding: 80px;
  text-align: center;
}

</style>
