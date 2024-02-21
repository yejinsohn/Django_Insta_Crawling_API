<template>
  <div>
    <insta-header></insta-header>
    <div id="body-wrapper">
      <div id="body-content">
        <div id="user_search">
          <form>
            <h3>Instagram 사용자 :</h3><input class="input-box" type="text" v-model="username" placeholder="사용자 이름을 입력하세요.">
          </form>
          <button type="submit" class="btn" @click="navigateToAnalysisPage">분석</button>
        </div>
        <div class="guide" v-if="$route.path === '/'">
          사이트 소개 영역
        </div>
        <!-- <router-view :userList="userList" /> -->
        <insta-content v-if="$route.path === '/analysis'" v-bind:propsdata="userList"></insta-content>
      </div>
      <insta-footer></insta-footer>
    </div>
  </div>
</template>


<script>
import Header from './components/Header.vue';
import Content from './AnalysisPage.vue'
import Footer from './components/Footer.vue';
import axios from 'axios';


let url = 'http://localhost:8000/'

export default {
  data: () => {
    return {
      userList: [],
      username: '',
    };
  },
  components: {
    'insta-header': Header,
    'insta-content': Content,
    'insta-footer': Footer,
  },
  methods: {
    navigateToAnalysisPage() {
      if (this.username.trim() !== '') {
        // username에 입력된 값이 있는 경우에만 분석 페이지로 이동
        axios({
          method: "GET",
          url: url + `crawling_method/?input_data=${this.username}`
        })
        .then(response => {
          this.userList = response.data;
          console.log(response);
          this.$router.push({ name: 'analysis', params: { userList: this.userList } });
        })
        .catch(response => {
          console.log("Failed", response);
        });
        this.$router.push('/analysis');
        alert('Instagram 사용자 : ' + this.username);
      } else {
        alert('검색할 사용자 이름을 입력하세요.');
      }
    }
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
form {
  display: flex;
  gap: 10px;
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
    text-align: center;
    padding: 70px;
}

</style>
