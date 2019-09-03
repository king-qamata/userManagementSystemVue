<template>
  <div class="login-container">
    <h3>登录</h3>
    <el-form ref="loginForm" :model="loginForm" :rules="fieldRules" status-icon label-width="100px" class="demo-ruleForm">
      <el-form-item label="用户名" prop="account">
        <el-input v-model="loginForm.account" />
      </el-form-item>
      <el-form-item label="密码" prop="password">
        <el-input v-model="loginForm.password" type="password" />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" class="login-btn" @click="submitForm('loginForm')">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { Login } from '@/network/api'
import Cookie from 'js-cookie'
export default {
  data() {
    return {
      loginForm: {
        account: '',
        password: ''
      },
      fieldRules: {
        // 'blur' 光标消失时触发
        account: [
          { required: true, message: '请输入账号', trigger: 'blur' }
        ],
        password: [
          { required: true, message: '请输入密码', trigger: 'blur' }
        ]
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        // 表单验证通过执行
        if (valid) {
          console.log('表单验证通过')
          const loginInfo = this.loginForm
          Login(loginInfo)
            .then((res) => {
              Cookie.set('token', res.data.token)
              sessionStorage.setItem('user', this.loginForm.account)
              this.$router.push({ path: '/' })
            })
            .catch(res => {
              this.$message({
                type: 'error',
                message: '返回出错：' + res,
                showClose: true
              })
            })
        } else {
          console.log('表单验证未通过')
          return false
        }
      })
    }
  }
}
</script>

<style scoped>
.login-container {
  width: 500px;
}
h3 {
  text-align: center;
}
login-btn {
  margin: 0 auto;
}
</style>
