<template>
  <div class="login-container">
    <h3>Log In</h3>
    <el-form ref="loginForm" :model="loginForm" :rules="fieldRules" :status-icon="false" label-width="80px" class="demo-ruleForm">
      <el-form-item label="User " prop="account">
        <el-input v-model="loginForm.account"> <i slot="prefix" class="fa fa-user fa-lg" /> </el-input>
      </el-form-item>

      <el-form-item label="Password " prop="password" @keyup.enter.native="submitForm('loginForm')">
        <el-input v-model="loginForm.password" :type="passwordType">
          <i slot="prefix" class="fa fa-lock fa-lg" />
          <i slot="suffix" :class="eyeType" @click="showPassword" />
        </el-input>
      </el-form-item>

      <el-form-item class="login-btn">
        <el-button type="primary" @click="submitForm('loginForm')">Sign in</el-button>
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
      passwordType: 'password',
      eyeType: 'fa fa-eye-slash fa-lg',
      fieldRules: {
        // 'blur' 光标消失时触发
        account: [
          { required: true, message: 'user name', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Password ', trigger: 'blur' }
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
    },
    showPassword() {
      if (this.passwordType === 'password') {
        this.passwordType = ''
        this.eyeType = 'fa fa-eye fa-lg'
      } else {
        this.passwordType = 'password'
        this.eyeType = 'fa fa-eye-slash fa-lg'
      }
    }
  }
}
</script>

<style scoped>
.el-input i {
  padding-left: 3px;
}
.el-input i:nth-child(1) {
  margin-right: 5px;
}
.el-input__suffix {
  right: 20px;
}
.el-input i:nth-child(1):hover {
  cursor: pointer;
}
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
