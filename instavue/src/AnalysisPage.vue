<template>
    <div class="content_analysis" :propsdata="userList">
      <div class="user_info1">
        <v-row style="text-align: center">
          <v-col v-for="(data, index) in propsdata" :key="index" cols="1" md="2" lg="2">
            <h2>@{{ data.name }}</h2>
          </v-col>
          <v-col v-for="(data, index) in propsdata" :key="index" cols="1" md="2" lg="2">
            <h2>{{ data.followers }}</h2>
            <a>팔로워</a>
          </v-col>
          <v-col v-for="(data, index) in propsdata" :key="index" cols="1" md="2" lg="2">
            <h2>{{ data.following }}</h2>
            <a>팔로잉</a>
          </v-col>
          <v-col v-for="(data, index) in propsdata" :key="index" cols="1" md="2" lg="2">
            <h2>{{ data.posts }}</h2>
            <a>게시글</a>
          </v-col>
        </v-row>
      </div>
      <div class="user_info2">
        <v-row style="line-height: 70px">
          <v-col v-for="(data, index) in propsdata" :key="index" cols="12">
            <h3>소개 : {{ data.introduction }}</h3>
            <h3>스레드: {{ data.threads }}</h3>
            <h3>계정 인증: {{ data.authentication }}</h3>
          </v-col>
        </v-row>
      </div>        
      <div class="user_info2">
        <v-row style="line-height: 70px">
          <v-col v-for="(data, index) in propsdata" :key="index" cols="12">
            <h3>평균 좋아요 수:</h3>
            <h3>평균 댓글 수:</h3>
          </v-col>
        </v-row>
      </div>       
      <div class="analysis">
        <span>게시글 분석</span>
      </div> 
      <div class="post">
        <v-container style="display: flex; gap: 20px;">
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
        </v-container>
      </div>
      <div class="analysis">
        <span>릴스 분석</span>
      </div> 
      <div class="post">
        <v-container style="display: flex; gap: 20px;">
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
          </v-card>
          <v-card style="width: 30%" height="300">
            <v-card-subtitle>좋아요: </v-card-subtitle>
            <v-card-subtitle>댓글:</v-card-subtitle>
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
    props: ["propsdata"]
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
      height: 300px;
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