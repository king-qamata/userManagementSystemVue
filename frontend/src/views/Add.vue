<template>
  <el-form ref="form" :model="form" label-width="80px">
    <el-form-item
      label="Username"
      prop="name"
      :rules="[
        {required: true, message: '姓名不能为空', trigger: 'blur'}
      ]"
    >
      <el-input v-model="form.name" />
    </el-form-item>

    <el-form-item label="Date">
      <el-input v-model="form.date" />
    </el-form-item>

    <el-form-item label="Tel">
      <el-input v-model="form.tel" />
    </el-form-item>

    <el-form-item label="Address">
      <el-input v-model="form.addr" />
    </el-form-item>

    <el-form-item label="Description">
      <el-input v-model="form.desc" type="textarea" />
    </el-form-item>
    <el-form-item>
      <el-button type="primary" @click="onSubmit('form')">Submit</el-button>
      <el-button>取消</el-button>
    </el-form-item>
  </el-form>
</template>

<script>
import { addUser } from '@/network/api'
export default {
  data() {
    return {
      // 添加数据
      form: {
        date: '',
        name: '',
        tel: '',
        addr: '',
        desc: ''
      }
    }
  },
  methods: {
    onSubmit(formName) {
      // 表单验证
      this.$refs[formName].validate(valid => {
        //   如果通过
        if (valid) {
          addUser(this.form)
            .then(() => {
              this.$message({
                showClose: true,
                message: '添加成功',
                type: 'success'
              })
              this.$router.push({ path: '/home' })
            })
            .catch((res) => {
              this.$message({
                showClose: true,
                message: `添加失败,${res}`,
                type: 'error'
              })
            })
        } else {
          this.$message({
            showClose: true,
            message: '请正确填写表单',
            type: 'error'
          })
        }
      })
    }
  }
}
</script>

<style scoped>
</style>

