<template>
  <div>
    <!-- 头部区域 -->
    <el-row class="container">
      <el-col :span="24" class="header">
        <el-col :span="10" :class="['logo', isCollapse?'collapseWidth':'defaultWidth']">
          {{ isCollapse? ' ': headerName }}
        </el-col>
        <el-col :span="10">
          <i class="fa fa-navicon fa-2x collapseIcon" :class="isCollapse?'rotate':''" @click="isCollapse = !isCollapse" />
        </el-col>
        <!-- 用户头像 用户名 -->
        <div id="account">
          <el-dropdown trigger="click">
            <div>
              <span class="el-dropdown-link">{{ userName }}
              </span>
              <img :src="userImg" alt="头像">
            </div>
            <el-dropdown-menu slot="dropdown">
              <el-dropdown-item @click.native="goHome">首  页</el-dropdown-item>
              <el-dropdown-item @click.native="dialogFormVisible = true">个人信息</el-dropdown-item>
              <el-dropdown-item divided @click.native="logout">退出登录</el-dropdown-item>
            </el-dropdown-menu>
          </el-dropdown>
          <!-- 嵌套表单 显示个人信息 -->
          <el-dialog title="个人信息" :visible.sync="dialogFormVisible" style="text-align: left">
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
        </div>

      </el-col>
    </el-row>
    <div class="flexBox">
      <!-- 菜单栏 -->
      <aside>
        <el-menu :default-active="this.$route.path" class="el-menu-vertical-demo" :collapse="isCollapse" router unique-opened @open="handleOpen" @close="handleClose">
          <el-submenu index="1">
            <template slot="title">
              <i class="fa fa-user-circle-o fa-fw" />
              <span slot="title"> 用户</span>
            </template>
            <el-menu-item-group>
              <span slot="title">分组一</span>
              <el-menu-item index="/customers">用户管理</el-menu-item>
              <el-menu-item index="/add">添加用户</el-menu-item>
            </el-menu-item-group>
            <el-menu-item-group title="分组">
              <el-menu-item index="/home">首页</el-menu-item>
            </el-menu-item-group>
            <el-submenu index="1-4">
              <span slot="title">选项4</span>
              <el-menu-item index="1-4-1">选项1</el-menu-item>
            </el-submenu>
          </el-submenu>

          <el-submenu index="2">
            <template slot="title">
              <i class="el-icon-location" />
              <span slot="title">广告</span>
            </template>
            <el-menu-item-group>
              <!-- <span slot="title">分组一</span> -->
              <el-menu-item index="/addAdvertisement">添加广告</el-menu-item>
              <el-menu-item index="2-2">选项2</el-menu-item>
            </el-menu-item-group>

          </el-submenu>

          <el-menu-item index="/about">
            <i class="fa fa-image fa-fw" />
            <span slot="title"> 轮播图</span>
          </el-menu-item>

        </el-menu>
      </aside>
      <content>
        <router-view />
      </content>
    </div>

  </div>
</template>

<script>
export default {
  data() {
    return {
      headerName: 'USERADMIN',
      isCollapse: false,
      userName: 'admin',
      userImg: require('@/assets/logo.png'),
      dialogFormVisible: false,
      form: {
        name: 'admin'
      }
    }
  },
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath)
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath)
    },
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

<style scoped>
.el-menu-vertical-demo:not(.el-menu--collapse) {
  width: 200px;
  min-height: 400px;
}
.logo {
    text-align: center;
    color: white;
    height: 60px;
    border-right: 1px solid rgba(238, 241, 146, 0.3);
    transition: width 0.3s;
}
.collapseWidth {
    width: 65px;
}
.defaultWidth {
    width: 201px;
}
.collapseIcon {
    color: white;
    cursor: pointer;
    padding-left: 10px;
    padding-top: 4px;
    transition: all 0.5s;
}
.rotate {
    transform: rotate(90deg);
}
.header {
    background-color:#20a0ff;
    line-height: 60px;
}

#account {
  line-height: 60px;
  text-align: right;
  float: right;
  padding-right: 35px;
}
#account img {
  margin-left: 5px;
  vertical-align:middle;
  width: 36px;
  height: 36px;
  border-radius: 18px;
  background-color: white;
}
.el-dropdown-item {
  text-align: center;
}
.flexBox {
  position: absolute;
  display: flex;
  width: 100%;
  height: 90%;
}
content {
  padding: 20px;
  width: 100%;
}
</style>
