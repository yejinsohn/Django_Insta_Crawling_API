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
            <h2>{{ propsdata.followers.toLocaleString() }}</h2>
            <a>팔로워</a>
          </v-col>
          <v-col cols="1" md="2" lg="2">
            <h2>{{ propsdata.following.toLocaleString() }}</h2>
            <a>팔로잉</a>
          </v-col>
          <v-col cols="1" md="2" lg="2">
            <h2>{{ propsdata.posts }}</h2>
            <a>게시글</a>
          </v-col>
        </v-row>
      </div>
      <div class="user_info2">
        <v-row style="line-height: 50px">
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
            <h3>하이라이트 그룹: {{ propsdata.highlight_count }}개</h3>
            <h3>게시글 평균 좋아요 수: {{ calculateAverageLikes(propsdata.post) !== null ? calculateAverageLikes(propsdata.post).toLocaleString() : 'N/A' }}개</h3>
            <h3>릴스 평균 좋아요 수: {{ calculateAverageReelsLikes(propsdata.reels) !== null ? calculateAverageReelsLikes(propsdata.reels).toLocaleString() : 'N/A' }}개</h3>
          </v-col>
        </v-row>
      </div>       
      <div class="analysis">
        <div class="post-analysis">
          <h4>게시글 분석</h4> 
          <div class="posting-day">
            <h5 style="padding-top: 30px;">게시글 작성이 가장 활발한 요일</h5>
            <div class="mostday">
              {{ findMostActiveDays(calculateDayOfWeekStats(sortedPosts.slice(0, 5))).join(', ') }}요일
            </div>
            <div class="day">
              <div v-for="(count, day) in calculateDayOfWeekStats(sortedPosts.slice(0, 5))" :key="day">
                {{ day }}: {{ count }}개
              </div>
            </div>
          </div>
          <div class="posting-gap">
          </div>
        </div>
      </div> 
      <div class="post">
        <div style="padding: 0px 10px">📍 최근 게시물 10개 중 좋아요가 가장 많이 누적된 5개의 게시글 데이터입니다.</div>
        <v-container style="display: flex; gap: 20px;">
          <v-card v-for="(post, index) in sortedPosts.slice(0, 5)" :key="index" style="height: 300px; width: 30%;">
            <v-card-text class="scrollable-text">{{ post.content }}</v-card-text>
            <v-card-subtitle>좋아요: {{ post.like ? post.like.toLocaleString() : 'N/A' }}개</v-card-subtitle>
            <v-card-subtitle>작성일: {{ formatWithDayOfWeek(post.date) }}</v-card-subtitle>
          </v-card>
        </v-container>
      </div>
      <div class="analysis">
        <div class="reels-analysis">
          <h4>릴스 분석</h4> 
            <div class="reels-day">
            <h5 style="padding-top: 30px;">릴스 업로드가 가장 활발한 요일</h5>
            <div class="mostday">
              {{ findMostActiveDaysReels(calculateDayOfWeekStatsReels(sortedReels.slice(0, 5))).join(', ') }}요일
            </div>
            <div class="day">
              <div v-for="(count, day) in calculateDayOfWeekStatsReels(sortedReels.slice(0, 5))" :key="day">
                {{ day }}: {{ count }}개
              </div>
            </div>
        </div>
      <div class="posting-gap">
      </div>
    </div>
    </div>
      <div class="reels">
        <div style="padding: 0px 10px">📍 최근 릴스 10개 중 좋아요가 가장 많이 누적된 5개의 릴스 데이터입니다.</div>
        <v-container style="display: flex; gap: 20px;">
          <v-card v-for="(reels, index) in sortedReels.slice(0, 5)" :key="index" style="height: 300px; width: 30%;">
            <v-card-text class="scrollable-text">{{ reels.reels_caption }}</v-card-text>
            <v-card-subtitle>좋아요: {{ reels.reels_like ? reels.reels_like.toLocaleString() : 'N/A' }}개</v-card-subtitle>
            <v-card-subtitle>누적 조회수: {{ reels.reels_view.toLocaleString() }}회</v-card-subtitle>
            <v-card-subtitle>업로드: {{ formatWithDayOfWeek(reels.reels_date) }}</v-card-subtitle>
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
    computed: {
    sortedPosts() {
      return [...this.propsdata.post].sort((a, b) => b.like - a.like);
    },
    sortedReels() {
      return [...this.propsdata.reels].sort((a, b) => b.reels_like - a.reels_like);
    },
  },
    methods: {
    // navigateToPostPage() {
    //   this.$router.push('/postdetail');
    // },
    // navigateToReelsPage() {
    //   this.$router.push('/reelsdetail');
    // },
    calculateAverageLikes(posts) {
      if (!posts || posts.length === 0) return 0;

      const totalLikes = posts.reduce((sum, post) => sum + (post.like || 0), 0);
      return totalLikes / posts.length;
    },
    calculateAverageReelsLikes(reels) {
      if (!reels || reels.length === 0) return 0;

      const totalLikes = reels.reduce((sum, reel) => sum + (reel.reels_like || 0), 0);
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
  calculateDayOfWeekStats(posts) {
      const stats = { '일': 0, '월': 0, '화': 0, '수': 0, '목': 0, '금': 0, '토': 0 };

      posts.forEach(post => {
        const dayOfWeek = this.getDayOfWeek(post.date);
        stats[dayOfWeek]++;
      });

      return stats;
    },

  getDayOfWeek(date) {
    const dateString = date.toString();
    const dayOfWeekOptions = { weekday: 'short' };
    return new Date(`${dateString.substr(0, 4)}-${dateString.substr(4, 2)}-${dateString.substr(6, 2)}`).toLocaleDateString('ko-KR', dayOfWeekOptions);
  },
  findMostActiveDays(stats) {
  let maxCount = 0;
  let mostActiveDays = [];

  for (const day in stats) {
    const count = stats[day];

    if (count > maxCount) {
      maxCount = count;
      mostActiveDays = [day];
    } else if (count === maxCount) {
      mostActiveDays.push(day);
    }
  }

  return mostActiveDays;
},
calculateDayOfWeekStatsReels(reels) {
  const stats = { '일': 0, '월': 0, '화': 0, '수': 0, '목': 0, '금': 0, '토': 0 };

  reels.forEach(reel => {
    const dayOfWeek = this.getDayOfWeek(reel.reels_date);
    stats[dayOfWeek]++;
  });

  return stats;
  },
findMostActiveDaysReels(stats) {
  let maxCount = 0;
  let mostActiveDays = [];

  for (const day in stats) {
    const count = stats[day];

    if (count > maxCount) {
      maxCount = count;
      mostActiveDays = [day];
    } else if (count === maxCount) {
      mostActiveDays.push(day);
    }
  }

  return mostActiveDays;
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
    .day {
      display: flex;
      flex-direction: row;
      align-items: center;
      gap: 10px;
      font-size: small;
    }
    .mostday {
      padding: 15px 0px;
    }
    .reels {
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
    .scrollable-text {
      height: 230px;
      overflow-y: auto;
    }
  </style>