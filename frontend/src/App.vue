<template>
  <div id="app">
    <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" router>
      <el-menu-item index="/">用户管理系统</el-menu-item>
      <el-menu-item index="/home">主页</el-menu-item>
      <el-menu-item index="/about">关于我们</el-menu-item>
      <el-menu-item index="/add">添加用户</el-menu-item>
      <el-menu-item index="/addAdvertisement">添加广告</el-menu-item>
      <el-menu-item index="/login" style="float: right">登录</el-menu-item>

    </el-menu>

    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: '2'
    }
  }
}
</script>

<style>
</style>
