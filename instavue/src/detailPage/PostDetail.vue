<template>
    <div id="post-content">
        <div class="post-detail">
            <p>게시글 디테일</p>
        </div>
        <div class="re-btn" @click="back">
            <p>돌아가기</p>
        </div>
    </div>
</template>

<script>
  export default {
    methods: {
    back() {
      this.$router.push('/analysis');
    },
  },
  };
</script>

<style>
#post-content {
    display: flex;
    flex-direction: column;
    align-items: center;
}
.post-detail {
    width: 70%;
    border: 1px solid #c2c2c2;
    border-radius: 10px;
    text-align: center;
    margin: 0 auto;
    padding: 70px;
    min-height: 500px;
}
.re-btn {
    display: inline-flex;
    padding: 10px 25px;
    margin-top: 70px;
    background: #0CB2C9;
    border: none;
    font-weight: 500;
    border-radius: 8px;
    transition: 0.2s;
}
.re-btn:hover{
    background: #00a1b7
}
</style>