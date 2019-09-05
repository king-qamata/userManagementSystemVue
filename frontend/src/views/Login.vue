<template>
  <div class="login-container">
    <h3>登 录</h3>
    <el-form ref="loginForm" :model="loginForm" :rules="fieldRules" status-icon label-width="80px" class="demo-ruleForm">
      <el-form-item label="账号" prop="account">
        <el-input v-model="loginForm.account" />
      </el-form-item>
      <el-form-item label="密码" prop="password" @keyup.enter.native="submitForm('loginForm')">
        <el-input v-model="loginForm.password" type="password" />
      </el-form-item>

      <el-form-item class="login-btn">
        <el-button type="primary" @click="submitForm('loginForm')">提 交</el-button>
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
          // console.log('表单验证通过')
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
          return false
        }
      })
    }
  }
}
</script>

<style scoped>
.login-container {
  margin: 180px auto;
  width: 350px;
  border: 1px solid #eaeaea;
  box-shadow: 0 0 25px #cac6c6;
  padding: 35px 35px 15px 0;
}
h3 {
  margin-top: 0;
  padding-left: 40px;
  text-align: center;
  font-size: 30px;
}
.login-btn {
  margin-left: 80px;
}
</style>
