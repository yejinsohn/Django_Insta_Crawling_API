<template>
    <div>
      <v-container fluid>
        <v-layout column>
          <v-flex xs12>
            <h3 class="subject">what is your plan?</h3>
          </v-flex>
          <v-flex column>
            <v-form v-on:submit="submitForm">
              <v-text-field v-model="title" :counter="64" label="Title" required></v-text-field>
              <v-text-field v-model="content" :counter="255" label="Content" required></v-text-field>
  
              <v-btn @click="create" type="submit" style="background: green">create</v-btn>
              <v-btn @click="clear" type="submit" style="background: red">clear</v-btn>
            </v-form>
          </v-flex>
  
  
          
          <v-flex class="todoList" column>
            <v-card max-width="600" tile>
              <v-list-item v-for="(data, index) in propsdata" v-bind:key="index"> <!-- index python enumurate 와 같이 숫자가 들어가게 됩니다.--> 
                <v-list-item-content>
                  <v-list-item-title>{{ data.name }}</v-list-item-title> <!-- for 문이 돌면서 data.title 출력합니다. -->
                  <v-list-item-subtitle>{{ data.authentication }}</v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
            </v-card>
          </v-flex>
          
          
          
          
        </v-layout>
      </v-container>
    </div>
  </template>
  
  <script>
  export default {
    props: ["propsdata"]
  };
  </script>
  
  <style>
  .subject {
    color: blue;
    font-style: oblique;
    padding: 30px;
    text-align: center;
  }
  .todoList {
    margin: 30px 0px 30px 0px;
  }
  </style>