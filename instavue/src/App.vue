<template>
  <div>
    <todo-header></todo-header>
    <nav>
      <router-link to="/">홈</router-link>

    </nav>
    <router-view/>
    <todo-content></todo-content>
    <todo-footer></todo-footer>
  </div>
</template>

<script>
import TodoHeader from './components/Header.vue';
import TodoContent from './components/Content.vue';
import TodoFooter from './components/Footer.vue';
import axios from 'axios';


let url = 'http://localhost:8000/Profile/'
axios.get(url)
.then(function(response){
  console.log(response);
  
})
.catch(function(response){
  console.log(response);
})

export default {
  data: function() {
    return {
      name: 'home',
      imageUrl: null,
    }    
  },
  components: {
    'todo-header': TodoHeader,
    'todo-content': TodoContent,
    'todo-footer': TodoFooter,
  },
  methods: {
    getCats() {
      axios({
        url: 'https://dog.ceo/dog-api/breads-list',
        method: 'get'
      })
      .then((res) => {
        this.imageUrl = res.data[0].url
      })
    }
  },
}
</script>

<style>

</style>