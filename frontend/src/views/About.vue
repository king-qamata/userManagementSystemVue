<template>
  <div id="sss">
    <h2>轮播图</h2>
    <el-row :gutter="0">
      <el-carousel :interval="4000" height="200px">
        <el-carousel-item v-for="(src, index) in dataimg" :key="index">
          <img :src="imgServerHost + src">
          <!-- <img src="http://10.0.5.2:8080/BiasAlphapose/photos/S.jpg" alt=""> -->
        </el-carousel-item>
      </el-carousel>
    </el-row>
  </div>
</template>

<script>
import { getADList } from '@/network/api'
export default {
  name: 'AboutUs',
  data() {
    return {
      imgServerHost: 'http://127.0.0.1:8000/photos/',
      dataimg: []
    }
  },
  created() {
    getADList()
      .then(res => {
        this.dataimg = res.data
      })
      .catch(res => {
        this.$message({
          showClose: true,
          message: `服务器获取图片失败: ${res}`,
          type: 'error'
        })
      })
  }
}
</script>

<style>
  #sss{
    margin: 20px auto;
    width: 500px;
    text-align: center;
    /* background-color: pink; */
  }
</style>
