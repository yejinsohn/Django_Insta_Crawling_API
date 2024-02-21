<template>
    <div class="content_analysis" :propsdata="userList">
      <div class="user_info1">
        <v-row style="text-align: center">
          <!-- <v-col cols="1" md="2" lg="2">
            <div></div>
          </v-col> -->
          <v-col cols="1" md="2" lg="2">
            <h2>@{{ propsdata.name }}</h2>
          </v-col>
          <v-col cols="1" md="2" lg="2">
            <h2>{{ propsdata.followers }}</h2>
            <a>팔로워</a>
          </v-col>
          <v-col cols="1" md="2" lg="2">
            <h2>{{ propsdata.following }}</h2>
            <a>팔로잉</a>
          </v-col>
          <v-col cols="1" md="2" lg="2">
            <h2>{{ propsdata.posts }}</h2>
            <a>게시글</a>
          </v-col>
        </v-row>
      </div>
      <div class="user_info2">
        <v-row style="line-height: 70px">
          <v-col cols="12">
            <h3>소개 : {{ propsdata.introduction }}</h3>
            <h3>태그 아이디 : {{ propsdata.tag_id }}</h3>
            <h3>스레드: {{ propsdata.threads }}</h3>
            <h3>계정 인증: {{ propsdata.authentication }}</h3>
          </v-col>
        </v-row>
      </div>        
      <div class="user_info2">
        <v-row style="line-height: 70px">
          <v-col cols="12">
            <h3>하이라이트 그룹: {{ propsdata.highlight_count }}</h3>
            <h3>게시글 평균 좋아요 수: {{ calculateAverageLikes(propsdata.post).toLocaleString() }}개</h3>
            <h3>릴스 평균 좋아요 수: {{ calculateAverageReelsLikes(propsdata.reels).toLocaleString() }}개</h3>
          </v-col>
        </v-row>
      </div>       
      <div class="analysis">
        <span>게시글 분석</span>
      </div> 
      <div class="post">
        <v-container style="display: flex; gap: 20px;">
        <v-card v-for="(post, index) in propsdata.post" :key="index" style="width: 30%" height="300" @click="navigateToPostPage">
          <v-card-subtitle>좋아요: {{ post.like.toLocaleString() }}개</v-card-subtitle>
          <v-card-subtitle>작성일: {{ formatWithDayOfWeek(post.date) }}</v-card-subtitle>
        </v-card>
      </v-container>
      </div>
      <div class="analysis">
        <span>릴스 분석</span>
      </div> 
      <div class="post">
        <v-container style="display: flex; gap: 20px;">
          <v-card v-for="(reels, index) in propsdata.reels" :key="index" style="width: 30%" height="300" @click="navigateToReelsPage">
          <v-card-subtitle>좋아요: {{ reels.reels_like.toLocaleString() }}개</v-card-subtitle>
          <v-card-subtitle>누적 조회수: {{ reels.reels_view.toLocaleString() }}회</v-card-subtitle>
        </v-card>
        </v-container>
      </div>
      <div class="analysis">
        <span>해시태그 분석</span>
      </div> 
    </div>
  </template>
  
  <script>
  export default {
    props: ["propsdata"],
    methods: {
    navigateToPostPage() {
      this.$router.push('/postdetail');
    },
    navigateToReelsPage() {
      this.$router.push('/reelsdetail');
    },
    calculateAverageLikes(posts) {
      if (posts.length === 0) return 0;

      const totalLikes = posts.reduce((sum, post) => sum + post.like, 0);
      return totalLikes / posts.length;
    },
    calculateAverageReelsLikes(reels) {
      if (reels.length === 0) return 0;

      const totalLikes = reels.reduce((sum, reel) => sum + reel.reels_like, 0);
      return totalLikes / reels.length;
    },
    formatWithDayOfWeek(date) {
    const dateString = date.toString();

    const options = { year: 'numeric', month: '2-digit', day: '2-digit' };
    const formattedDate = new Date(`${dateString.substr(0, 4)}-${dateString.substr(4, 2)}-${dateString.substr(6, 2)}`).toLocaleDateString('ko-KR', options);

    const dayOfWeekOptions = { weekday: 'long' };
    const dayOfWeek = new Date(`${dateString.substr(0, 4)}-${dateString.substr(4, 2)}-${dateString.substr(6, 2)}`).toLocaleDateString('ko-KR', dayOfWeekOptions);

    return `${formattedDate} (${dayOfWeek})`;
  },
},
};
  </script>
  
  <style>
    .content_analysis {
      padding: 85px 30px 0 30px;
      display: flex;
      flex-direction: row;
      justify-content: center;
      align-items: center;
      flex-wrap: wrap;
      gap: 30px;
    }
    .user_info1 {
      width: 70%;
      height: auto;
      border: 1px solid #c2c2c2;
      border-radius: 10px;
      display: flex;
      padding: 40px;
      box-sizing: border-box;
      overflow: hidden;
    }
    .user_info2 {
      width: 34%;
      min-height: 360px;
      border: 1px solid #c2c2c2;
      border-radius: 10px;
      display: flex;
      padding: 40px;
      box-sizing: border-box;
      overflow: hidden;
    }
    .v-row {
    display: flex;
    margin: -12px;
    flex-direction: row;
    justify-content: center;
    align-items: center;
    gap : 50px;
    }
    .post {
      width: 70%;
    }
    .analysis {
      width: 70%;
      height: auto;
      border: 1px solid #c2c2c2;
      border-radius: 10px;
      display: flex;
      padding: 40px;
      box-sizing: border-box;
      overflow: hidden;
    }
  </style>