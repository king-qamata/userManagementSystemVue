<template>
  <div>
    <el-row>
      <el-col :span="22">
        <el-menu :default-active="$route.path" class="el-menu-demo" mode="horizontal" router>
          <el-menu-item index="/">用户管理系统</el-menu-item>
          <el-menu-item index="/home">主页</el-menu-item>
          <el-menu-item index="/about">轮播图</el-menu-item>
          <el-menu-item index="/add">添加用户</el-menu-item>
          <el-menu-item index="/addAdvertisement">添加广告</el-menu-item>
        </el-menu>
      </el-col>
      <el-col :span="2">
        <div id="account">
          <el-dropdown trigger="click">
            <div>
              <span class="el-dropdown-link">{{ userName }}
                <!-- <i class="el-icon-arrow-down el-icon--right" /> -->
              </span>
              <img :src="userImg" alt="头像">
            </div>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="goHome">首  页</el-dropdown-item>
              <el-dropdown-item @click.native="dialogFormVisible = true">个人信息</el-dropdown-item>
              <el-dropdown-item divided @click.native="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>

        </div>
      </el-col>
    </el-row>
    <!-- 嵌套表单 显示个人信息 -->
    <el-dialog title="个人信息" :visible.sync="dialogFormVisible">
      <el-form :model="form">
        <el-form-item label="用户名">
          <el-input v-model="form.name" auto-complete="off" />
        </el-form-item>

      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="dialogFormVisible = false">确 定</el-button>
      </div>
    </el-dialog>
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      activeIndex: '2',
      userName: 'admin',
      userImg: require('@/assets/logo.png'),
      dialogFormVisible: false,
      form: {
        name: 'admin'
      }
    }
  },
  methods: {
    goHome() {
      this.$router.push({ path: '/home' })
    },
    logout() {
      this.$confirm('确定退出吗？', '提示', { type: 'warning' })
        .then(() => {
          sessionStorage.removeItem('user')
          this.$router.push({ path: '/login' })
        })
        .catch(() => {})
    }
  }
}

</script>

<style>
#account {
  line-height: 59px;
  border-bottom: solid 1px #e6e6e6;
}
#account img {
  margin-left: 5px;
  vertical-align:middle;
  width: 36px;
  height: 36px;
  border-radius: 18px;
  background-color: pink;
}
.el-dropdown-item {
  text-align: center;
}
</style>
