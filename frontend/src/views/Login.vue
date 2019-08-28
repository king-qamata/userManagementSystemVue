<template>
  <div class="login-container">
    <h3>登录</h3>
    <el-form ref="ruleForm" status-icon label-width="100px" class="demo-ruleForm">
      <el-form-item label="用户名">
        <el-input v-model="loginData.userData" />
      </el-form-item>
      <el-form-item label="密码">
        <el-input v-model="loginData.passWord" type="password" />
      </el-form-item>

      <el-form-item>
        <el-button id="login-btn" type="primary" @click="submitForm('ruleForm2')">提交</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      loginData: {
        userName: '',
        passWord: ''
      }
    }
  },
  methods: {
    submitForm(formName) {
      this.$refs[formName].validate((valid) => {
        if (valid) {
          alert('submit!')
        } else {
          console.log('error submit!!')
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
#login-btn {
  margin: 0 auto;
}
</style>
