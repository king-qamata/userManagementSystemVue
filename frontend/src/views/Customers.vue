<template>
  <section>
    <!-- 显示表单 -->
    <el-table v-loading="tableDataLoading" :data="tableData" style="width: 100%">
      <el-table-column label="姓名" width="100">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>描述: {{ scope.row.desc }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.name }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>

      <el-table-column label="出生日期" width="180">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.date }}</span>
        </template>
      </el-table-column>

      <el-table-column label="电话" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.tel }}</span>
        </template>
      </el-table-column>

      <el-table-column label="地址" width="300">
        <template slot-scope="scope">
          <span>{{ scope.row.addr }}</span>
        </template>
      </el-table-column>

      <el-table-column label="操作">
        <template slot-scope="scope">
          <!-- <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button> -->
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 编辑 -->
    <el-dialog title="编辑" :visible.sync="dialogVisible" width="50%">
      <el-form ref="editForm" label-width="80px" :model="editForm">
        <el-form-item label="姓名">
          <el-input v-model="editForm.name" :disabled="true" />
        </el-form-item>

        <el-form-item label="出生日期">
          <el-input v-model="editForm.date" />
        </el-form-item>

        <!-- <el-form-item label="出生日期">
          <el-col :span="11">
            <el-date-picker
              type="date"
              placeholder="选择日期"
              v-model="editForm.date"
              style="width: 100%;"
            ></el-date-picker>
          </el-col>
        </el-form-item> -->

        <el-form-item label="电话">
          <el-input v-model="editForm.tel" />
        </el-form-item>

        <el-form-item label="地址">
          <el-input v-model="editForm.addr" />
        </el-form-item>

        <el-form-item label="个人简介">
          <el-input v-model="editForm.desc" type="textarea" />
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">取 消</el-button>
        <el-button type="primary" @click="editSubmit">确 定</el-button>
      </span>
    </el-dialog>
  </section>
</template>

<script>
import { getList, removeUser, editUser } from '../network/api'
export default {
  data() {
    return {
      tableDataLoading: true,
      dialogVisible: false,
      tableData: [],
      // 编辑数据
      editForm: {
        date: '',
        name: '',
        tel: '',
        addr: '',
        disc: ''
      }
    }
  },
  mounted() {
    this.getData()
  },
  methods: {
    handleEdit(index, row) {
      this.dialogVisible = true
      // console.log(index);
      // 对原对象进行浅拷贝，解决在编辑中更改时，原数据也更改的问题
      this.editForm = Object.assign({}, row)
    },
    handleDelete(index, row) {
      // console.log(index, row.name);
      removeUser({ name: row.name })
        .then(() => {
          this.$message({
            showClose: true,
            message: '删除成功',
            type: 'success'
          })
          this.getData()
        })
        .catch((res) => {
          this.$message({
            showClose: true,
            message: `删除失败，${res}`,
            type: 'error'
          })
        })
    },
    editSubmit() {
      // console.log(this.editForm);
      this.dialogVisible = false
      editUser(this.editForm)
        .then(() => {
          this.$message({
            showClose: true,
            message: '更新成功',
            type: 'success'
          })
          this.getData()
        })
        .catch((res) => {
          this.$message({
            type: 'error',
            message: `更新失败,${res}`,
            showClose: true
          })
        })
    },

    getData() {
      getList()
        .then(res => {
          this.tableData = res.data
          this.tableDataLoading = false
        })
        .catch((res) => {
          this.$message({
            type: 'error',
            message: res,
            showClose: true
          })
        })
    }
  }
}
</script>

