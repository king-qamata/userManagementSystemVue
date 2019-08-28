<template>
  <div id="sss">
    <h2>轮播图</h2>
    <el-row :gutter="0">
      <el-carousel :interval="4000" height="200px">
        <el-carousel-item v-for="item in dataimg" :key="item.id">
          <div class="grid-content">
            <!-- <el-col :md="6" :offset="6"> -->
            <img :src="item.src">
            <!-- </el-col> -->
          </div>
        </el-carousel-item>
      </el-carousel>
    </el-row>
  </div>
</template>

<script>
export default {
  name: 'AboutUs',
  data() {
    return {
      dataimg: [{
        id: 1,
        src: require('../assets/wf1.jpg')
      },
      {
        id: 2,
        src: require('../assets/wf2.jpg')
      },
      {
        id: 3,
        src: require('../assets/wf3.jpg')
      },
      {
        id: 4,
        src: require('../assets/wf4.jpg')
      }
      // {
      //   src: require('../assets/wf4.jpg')
      // }
      ]
    }
  }
}
</script>

<style>
  /* .el-carousel__item h3 {
    color: #475669;
    font-size: 14px;
    opacity: 0.75;
    line-height: 200px;
    margin: 0;
  } */
  /* .el-carousel__item:nth-child(2n) {
    background-color: #99a9bf;
    background-image: url('../assets/wf4.jpg')
  }

  .el-carousel__item:nth-child(2n+1) {
    background-color: #d3dce6;
  } */

  #sss{
    margin: 20px auto;
    width: 500px;
    text-align: center;
    /* background-color: pink; */
  }
</style>
