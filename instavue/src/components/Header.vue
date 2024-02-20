<template>
  <div>
    <header>
        <h2 class="title" @click="navigateToMainPage">콘텐츠 분석 서비스</h2>
    </header>
  </div>
</template>
  
  <script>
  export default {
  methods: {
    navigateToMainPage() {
      this.$router.push('/');
    },
  },
};
  </script>
  
  <style>
  header {
    background-color: white;
    width: 100%;
    position: fixed;
    top: 0;
    z-index: 100;
  }
  .title {
    color: black;
    padding: 30px;
    box-shadow: 5px 5px 5px #d8d8d8;
    cursor: pointer;
  }
  </style>