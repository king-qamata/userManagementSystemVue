<template>
  <el-row :gutter="20">
    <el-col id="addADCol" :span="10" :offset="6">
      <el-form ref="refForm" :model="form" label-width="80px">
        <el-form-item label="广告名称" prop="name">
          <el-input v-model="form.name" />
        </el-form-item>
        <el-form-item label="开始时间" prop="startDate">
          <el-date-picker v-model="form.startDate" type="date" placeholder="选择日期" style="width: 100%;" />
        </el-form-item>
        <el-form-item label="结束时间" prop="endDate">
          <el-date-picker v-model="form.endDate" type="date" placeholder="选择日期" style="width: 100%;" />
        </el-form-item>
        <el-form-item label="图片上传">
          <div id="myUpload">
            <el-upload
              ref="upload"
              class="upload-demo"
              action=""
              :on-preview="handlePreview"
              :on-remove="handleRemove"
              :before-remove="beforeRemove"
              :before-upload="beforeUpload"
              :limit="1"
              :on-exceed="handleExceed"
              :file-list="fileList"
              :accept="acceptFileType"
              :auto-upload="false"
            >
              <el-button size="small" type="primary">点击上传</el-button>
              <div slot="tip" class="el-upload__tip">只能上传jpg/png文件，且不超过500kb</div>
            </el-upload>
          </div>
        </el-form-item>
        <el-form-item label="广告链接" prop="link">
          <el-input v-model="form.link" />
        </el-form-item>
        <el-form-item label="描述信息" prop="desc">
          <el-input v-model="form.desc" type="textarea" />
        </el-form-item>
        <el-form-item>
          <el-button type="primary" @click="onSubmit">提交</el-button>
          <el-button>取消</el-button>
        </el-form-item>
      </el-form>
    </el-col>
  </el-row>

</template>

<script>
import { uploadAD } from '../network/api'
export default {
  data() {
    return {
      form: {
        name: '',
        startDate: '',
        endDate: '',
        link: '',
        desc: ''
      },
      acceptFileType: '.jpg',
      fileList: []
    }
  },
  methods: {
    handleRemove(file, fileList) {
      console.log(file, fileList)
    },
    handlePreview(file) {
      console.log(file)
    },
    handleExceed(files, fileList) {
      this.$message.warning(`您已上传了图片，如要更正请先移除当前图片`)
    },
    beforeRemove(file, fileList) {
      // return this.$confirm(`确定移除 ${file.name}？`)
    },
    onSubmit() {
      this.$refs.upload.submit()
    },
    beforeUpload(file) {
      const fd = new FormData()
      fd.append('file', file)
      // console.log(fd.get('file'))
      // 不能传递对象，将对象拆分
      for (const i in this.form) {
        fd.append(i, this.form[i])
      }

      uploadAD(fd)
        .then(res => {
          if (res.status === 200) {
            this.$message({
              showClose: true,
              message: '提交成功',
              type: 'success'
            })
            // 需要在 el-form-item 上添加 prop 属性
            this.$refs.refForm.resetFields()
            // this.$nextTick(() => { this.$refs.refForm.resetFields() })
            // this.$router.push({ path: '/about' })
          }
        })
        .catch(res => {
          console.log(res)
        })
      return false
    }
  }
}
</script>

<style scoped>
#addADCol {
  margin-top: 20px;
  padding-top: 10px;
  /* border: 1px solid red; */
}
.el-col {
  padding-left: -1px;
}
</style>
