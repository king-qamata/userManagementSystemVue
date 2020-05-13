<template>
  <section>
    <!-- 显示表单 -->
    <el-table v-loading="tableDataLoading" :data="tableData" style="width: 100%">
      <el-table-column label="Username " width="100">
        <template slot-scope="scope">
          <el-popover trigger="hover" placement="top">
            <p>Full Name: {{ scope.row.first_name }} {{ scope.row.last_name }}</p>
            <div slot="reference" class="name-wrapper">
              <el-tag size="medium">{{ scope.row.username }}</el-tag>
            </div>
          </el-popover>
        </template>
      </el-table-column>

      <el-table-column label="Email" width="180">
        <template slot-scope="scope">
          <i class="el-icon-time" />
          <span>{{ scope.row.email }}</span>
        </template>
      </el-table-column>

      <el-table-column label="Tel" width="180">
        <template slot-scope="scope">
          <span>{{ scope.row.tel }}</span>
        </template>
      </el-table-column>

      <el-table-column label="Address" width="300">
        <template slot-scope="scope">
          <span>{{ scope.row.addr }}</span>
        </template>
      </el-table-column>

      <el-table-column label="Actions">
        <template slot-scope="scope">
          <el-button size="mini" @click="handleEdit(scope.$index, scope.row)">Edit</el-button>
          <el-button size="mini" type="danger" @click="handleDelete(scope.$index, scope.row)">Delete</el-button>
          <el-button size="mini" type="danger" @click="handleSuspend(scope.$index, scope.row)">Suspend</el-button>
        </template>
      </el-table-column>
    </el-table>
    <div class="pagination">
      <el-pagination
        :current-page="curPage.currentPage"
        :page-sizes="[10, 20, 30, 40]"
        :page-size="10"
        layout="total, sizes, prev, pager, next, jumper"
        :total="returnData.length"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
      />
    </div>

    <!-- 编辑 -->
    <el-dialog title="编辑" :visible.sync="dialogVisible" width="50%">
      <el-form ref="editForm" label-width="80px" :model="editForm">
        <el-form-item label="username">
          <el-input v-model="editForm.name" :disabled="true" />
        </el-form-item>

        <el-form-item label="Date">
          <el-input v-model="editForm.date" />
        </el-form-item>

        <el-form-item label="Tel">
          <el-input v-model="editForm.tel" />
        </el-form-item>

        <el-form-item label="Addr">
          <el-input v-model="editForm.addr" />
        </el-form-item>

        <el-form-item label="Description">
          <el-input v-model="editForm.desc" type="textarea" />
        </el-form-item>
      </el-form>
      <span slot="footer" class="dialog-footer">
        <el-button @click="dialogVisible = false">cancel</el-button>
        <el-button type="primary" @click="editSubmit">submit</el-button>
      </span>
    </el-dialog>
  </section>
</template>

<script>
import { getList, removeUser, editUser } from '@/network/api'
export default {
  data() {
    return {
      tableDataLoading: true,
      dialogVisible: false,
      returnData: [],
      // 编辑数据
      editForm: {
        date: '',
        name: '',
        tel: '',
        addr: '',
        disc: ''
      },
      curPage: {
        size: 10,
        currentPage: 1
      }
    }
  },
  computed: {
    tableData() {
      const start = this.curPage.size * (this.curPage.currentPage - 1)
      const end = this.curPage.size * this.curPage.currentPage - 1
      return this.returnData.slice(start, end)
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
      // getList()
      this.$store
        .dispatch('users/fetchUsers')
      //  .then(res => {
        .then(response => {
          this.$store.commit('users/SET_USERS', JSON.stringify(response.data))
          this.loading = false
          // this.returnData = res.data
          this.returnData = response.data
          this.tableDataLoading = false
        })
        .catch((res) => {
          this.$message({
            type: 'error',
            message: res,
            showClose: true
          })
        })
    },
    handleSizeChange(size) {
      this.curPage.size = size
    },
    handleCurrentChange(currentPage) {
      this.curPage.currentPage = currentPage
    }
  }
}
</script>

<style scoped>
.pagination {
  padding-left: 15%;
  margin-top: 25px;
}
</style>
