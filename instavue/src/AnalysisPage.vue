<template>
  <div class="content_analysis" :propsdata="userList">
    <div class="user_info1">
      <v-row style="text-align: center">
        <v-col cols="1" md="2" lg="2">
          <h2>@{{ propsdata.name }}</h2>
        </v-col>
        <v-col cols="1" md="2" lg="2">
          <h2>{{ formatNumber(propsdata.followers) }}</h2>
          <a>팔로워</a>
        </v-col>
        <v-col cols="1" md="2" lg="2">
          <h2 v-if="propsdata.following">{{ propsdata.following.toLocaleString() }}</h2>
          <h2 v-else>0</h2>
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
          <h3 v-if="propsdata.introduction">소개 : {{ propsdata.introduction }}</h3>
          <h3 v-if="propsdata.tag_id">태그 아이디 : {{ propsdata.tag_id }}</h3>
          <h3 v-if="propsdata.threads">스레드: {{ propsdata.threads }}</h3>
          <h3 v-if="propsdata.authentication">계정 인증: {{ propsdata.authentication }}</h3>
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
      <h4>게시글 분석</h4>
      <div class="post-analysis">
        <div class="posting-day">
          <h5 style="padding-top: 30px;">게시글 작성이 가장 활발한 요일</h5>
          <div class="mostday">
            {{ findMostActiveDays(calculateDayOfWeekStats(sortedPosts.slice(0, 5))).join(', ') }}
          </div>
          <div class="day">
            <div v-for="(count, day) in calculateDayOfWeekStats(sortedPosts.slice(0, 5))" :key="day">
              {{ day }}: {{ count }}개
            </div>
          </div>
        </div>
        <div class="posting-gap" style="padding-right: 70px;">
          <h5 style="padding-top: 30px;">평균 게시글 업로드 간격</h5>
          <div class="gap">
            {{ calculateAveragePostingGap(sortedPosts).toFixed(2) }}일
          </div>
        </div>
      </div>
    </div> 
    <div class="post">
      <div style="padding: 0px 10px">📍 최근 게시물 10개 중 좋아요가 가장 많이 누적된 5개의 게시글 데이터입니다.</div>
      <v-container style="display: flex; gap: 20px;">
        <v-card v-for="(post, index) in sortedPosts.slice(0, 5)" :key="index" style="height: 300px; width: 30%;" @click="goPost(post)">
          <v-card-text class="scrollable-text">{{ post.content }}</v-card-text>
          <v-card-subtitle>좋아요: {{ post.like ? post.like.toLocaleString() : 'N/A' }}개</v-card-subtitle>
          <v-card-subtitle>작성일: {{ formatWithDayOfWeek(post.date) }}</v-card-subtitle>
        </v-card>
      </v-container>
    </div>
    <div class="analysis">
      <p>릴스 분석</p> 
      <div class="reels-analysis">
        <div class="reels-day">
          <h5 style="padding-top: 30px;">릴스 업로드가 가장 활발한 요일</h5>
          <div class="mostday">
            {{ findMostActiveDaysReels(calculateDayOfWeekStatsReels(sortedReels.slice(0, 5))).join(', ') }}
          </div>
          <div class="day">
            <div v-for="(count, day) in calculateDayOfWeekStatsReels(sortedReels.slice(0, 5))" :key="day">
              {{ day }}: {{ count }}개
            </div>
          </div>
        </div>
        <div class="posting-gap" style="padding-right: 70px;">
          <h5 style="padding-top: 30px;">평균 릴스 업로드 간격</h5>
          <div class="gap">
            {{ calculateAverageReelsGap(sortedReels).toFixed(2) }}일
          </div>
        </div>
      </div>
    </div>
    <div class="reels">
      <div style="padding: 0px 10px">📍 최근 릴스 10개 중 좋아요가 가장 많이 누적된 5개의 릴스 데이터입니다.</div>
      <v-container style="display: flex; gap: 20px;">
        <v-card v-for="(reels, index) in sortedReels.slice(0, 5)" :key="index" style="height: 300px; width: 30%;" @click="goPost(reels)">
          <v-card-text class="scrollable-text">{{ reels.reels_caption }}</v-card-text>
          <v-card-subtitle>좋아요: {{ reels.reels_like ? reels.reels_like.toLocaleString() : 'N/A' }}개</v-card-subtitle>
          <v-card-subtitle>누적 조회수: {{ reels.reels_view.toLocaleString() }}회</v-card-subtitle>
          <v-card-subtitle>업로드: {{ formatWithDayOfWeek(reels.reels_date) }}</v-card-subtitle>
        </v-card>
      </v-container>
    </div>
    <div class="analysis hashtagAnalysis">
      <div style="width: 100%;">
        <h4>해시태그 분석</h4>
      </div>
      <div class="hashtag">
        <h5 style="padding-bottom: 20px; font-size: medium;">가장 많이 사용한 해시태그</h5>  
        <div class="tag">
          <div v-for="(tags, index) in sortedTags" :key="index" style="min-width: 15%; box-sizing: border-box; padding: 5px;">
            {{ Number(index) + 1 }}위. ({{ tags[1] + 1}}개) <span style="color: rgb(63, 114, 155);">{{ tags[0] }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import moment from 'moment';

export default {
  props: ["propsdata"],
  computed: {
  sortedPosts() {
    return [...this.propsdata.post].sort((a, b) => b.like - a.like);
  },
  sortedReels() {
    return [...this.propsdata.reels].sort((a, b) => b.reels_like - a.reels_like);
  },
  sortedTags() {
    // 해시태그를 불러와서 배열에 하나씩 삽입.
      let tagList = [];
      for (let i = 0; i < this.propsdata.post.length; i++) {
        if (this.propsdata.post[i].tags.length > 0) {
          var words = this.propsdata.post[i].tags.split('\n');
          for (let j = 0; j < words.length; j++) {
            tagList.push(words[j])
          }
        }
      }
      
      // 해시태그를 담고있는 배열의 원소를 key값, 해당 key값이 얼마나 있는지 카운트값을 value값으로 딕셔너리 생성.
      let counts = {};
      for (let i = 0; i < tagList.length; i++) {
        if (tagList[i] in counts) {
          counts[tagList[i]]++;
        }
        else {
          counts[tagList[i]] = 0;
        }
      }

      // value값을 기준으로 내림차순 정렬.
      let sortedKeys = Object.entries(counts).sort((a, b) => b[1] - a[1]);
      if (sortedKeys.length > 10) {
        const slicedDictionary = Object.fromEntries(
          Object.entries(sortedKeys).slice(0, 10)
        );
        console.log(slicedDictionary);
        return slicedDictionary;
      }
      else {
        return sortedKeys;
      }
    },
  },
  methods: {
    //팔로워 단위
    formatNumber(number) {
      if (number >= 1000000) {
        const formattedNumber = (number / 1000000).toFixed(2).replace(/\.0$/, '');
        return `${formattedNumber}M`;
      } else if (number >= 1000) {
        const formattedNumber = (number / 1000).toFixed(1).replace(/\.0$/, '');
        return `${formattedNumber}K`;
      }
      return number.toLocaleString();
    },
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
      const stats = { '월요일': 0, '화요일': 0, '수요일': 0, '목요일': 0, '금요일': 0, '토요일': 0, '일요일': 0 };
      
      posts.forEach(post => {
        const dayOfWeek = this.getDayOfWeek(post.date);
        stats[dayOfWeek]++;
      });
      
      return stats;
    },
    getDayOfWeek(date) {
      if (!date) {
        return 'N/A'; 
      }
      
      const dateString = date.toString();
      const dayOfWeekOptions = { weekday: 'long' };
      const fullDayOfWeek = new Date(`${dateString.substr(0, 4)}-${dateString.substr(4, 2)}-${dateString.substr(6, 2)}`).toLocaleDateString('ko-KR', dayOfWeekOptions);
      
      return fullDayOfWeek;
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
    calculateAveragePostingGap(posts) {
      if (!posts || posts.length < 2) {
        return 0; 
      }
      
      const sortedPosts = [...posts].sort((a, b) => a.date - b.date);
      let totalGap = 0;
      
      for (let i = 1; i < sortedPosts.length; i++) {
        const currentDate = moment(sortedPosts[i].date, 'YYYYMMDD'); 
        const previousDate = moment(sortedPosts[i - 1].date, 'YYYYMMDD');  
        
        const gapInDays = currentDate.diff(previousDate, 'days');
        totalGap += gapInDays;
      }
      
      const averageGap = totalGap / (sortedPosts.length - 1);
      return averageGap;
    },
    calculateDayOfWeekStatsReels(reels) {
      const stats = { '월요일': 0, '화요일': 0, '수요일': 0, '목요일': 0, '금요일': 0, '토요일': 0, '일요일': 0 };
      
      reels.forEach(reel => {
        const dayOfWeek = this.getDayOfWeek(reel.reels_date);
        stats[dayOfWeek]++;
      });
      
      return stats;
    },
    
    findMostActiveDaysReels(stats) {
      let maxCount = 0;
      let mostActiveDays = [];
      
      if (Object.keys(stats).length === 0) {
        return [];
      }
      
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
    
    calculateAverageReelsGap(reels) {
      if (!reels || reels.length < 2) {
        return 0; 
      }
      
      const sortedReels = [...reels].sort((a, b) => a.reels_date - b.reels_date);
      let totalGap = 0;
      
      for (let i = 1; i < sortedReels.length; i++) {
        const currentDate = moment(sortedReels[i].reels_date, 'YYYYMMDD'); 
        const previousDate = moment(sortedReels[i - 1].reels_date, 'YYYYMMDD');  
        
        const gapInDays = currentDate.diff(previousDate, 'days');
        totalGap += gapInDays;
      }
      
      const averageGap = totalGap / (sortedReels.length - 1);
      return averageGap;
    },

    // 게시물 클릭 시 해당 게시물로 들어가는 함수
    goPost(post) {
      window.open(post.post_URL, "_blank");
    }
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
  .post-analysis {
    display: flex;
    padding: 15px;
    gap: 100px;
  }
  .reels-analysis {
    display: flex;
    padding: 15px;
    gap: 100px;
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
  .gap {
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
    justify-content: center;
    padding: 40px;
    box-sizing: border-box;
    overflow: hidden;
  }
  .analysis.hashtagAnalysis {
    display: flex;
    flex-wrap: wrap;
  }
  .hashtag {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .tag {
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    width: 80%;
    gap: 10px;
  }
  .scrollable-text {
    height: 230px;
    overflow-y: auto;
  }
</style>