<template>
  <div id="app">
    <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" router>
      <el-menu-item index="/">
        用户管理系统
        <!-- <router-link to="/">用户管理系统</router-link> -->
      </el-menu-item>
      <el-menu-item index="/home">
        <!-- <router-link to="/home">主页</router-link> -->
        主页
      </el-menu-item>
      <el-menu-item index="/about">
        关于我们
        <!-- <router-link to="/about">关于我们</router-link> -->
      </el-menu-item>
      <el-menu-item index="/add">
        添加用户
        <!-- <router-link to="/add">添加用户</router-link> -->
      </el-menu-item>
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
