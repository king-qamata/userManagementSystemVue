<template>
  <div class="login-container">
    <div class="text-left">
      <router-link :to="{ name: 'login' }">Already Registered?</router-link>
    </div>
    <h3>Sign Up</h3>
    <el-form ref="signupForm" :model="signupForm" :rules="fieldRules" :status-icon="false" label-width="80px" class="demo-ruleForm">
      <el-form-item label="Username" prop="username">
        <el-input v-model="signupForm.username"> <i slot="prefix" class="fa fa-user fa-lg" /> </el-input>
      </el-form-item>

      <el-form-item label="Password " prop="password" @keyup.enter.native="submitForm('signupForm')">
        <el-input v-model="signupForm.password" :type="passwordType">
          <i slot="prefix" class="fa fa-lock fa-lg" />
          <i slot="suffix" :class="eyeType" @click="showPassword" />
        </el-input>
      </el-form-item>

      <el-form-item label="Email" prop="email">
        <el-input v-model="signupForm.email"> <i slot="prefix" class="fa fa-email fa-lg" /> </el-input>
      </el-form-item>

      <el-form-item class="login-btn">
        <el-button type="primary" @click="submitForm('signupForm')">Register</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
import { Register } from '@/network/api'
import Cookie from 'js-cookie'

export default {
  data() {
    return {
      signupForm: {
        username: '',
        email: '',
        password: ''
      },
      passwordType: 'password',
      eyeType: 'fa fa-eye-slash fa-lg',
      fieldRules: {
        // 'blur' 光标消失时触发
        username: [
          { required: true, message: 'user name', trigger: 'blur' }
        ],
        password: [
          { required: true, message: 'Password ', trigger: 'blur' }
        ],
        email: [
          { required: true, message: 'Email address ', trigger: 'blur' }
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
          const loginInfo = this.signupForm
          Register(loginInfo)
            .then((res) => {
              Cookie.set('token', res.data.token)
              sessionStorage.setItem('user', this.signupForm.username)
              this.$router.push({ path: '/' })
            })
            .catch(res => {
              this.$message({
                type: 'error',
                message: 'Message Alert!' + res,
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
