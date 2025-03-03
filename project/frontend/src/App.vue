<template>
  <div id="app">
    <!-- 顶部固定栏 -->
    <div class="top-bar">
      <h1>面向行业大模型的数据治理系统</h1>
    </div>
    <!-- 左侧固定导航栏 -->
    <div class="sidebar">
      <ul>
        <li><router-link to="/">首页</router-link></li>
        <li><router-link to="/project">项目管理</router-link></li>
        <li>
          数据治理
          <ul>
            <li><router-link to="/data-processing">数据处理</router-link></li>
            <li><router-link to="/data-storage">数据存储</router-link></li>
          </ul>
        </li>
        <li>
          系统管理
          <ul>
            <li><router-link to="/user-management">用户管理</router-link></li>
          </ul>
        </li>
      </ul>
    </div>
    <!-- 右侧内容区域 -->
    <div class="content">
      <!-- 添加 key 属性 -->
      <router-view :key="$route.fullPath"></router-view>
      <!-- 显式使用组件 -->
      <HomePage v-if="currentPage === 'HomePage'"></HomePage>
      <ProjectManagement v-if="currentPage === 'ProjectManagement'"></ProjectManagement>
      <DataProcessing v-if="currentPage === 'DataProcessing'"></DataProcessing>
      <DataStorage v-if="currentPage === 'DataStorage'"></DataStorage>
      <UserManagement v-if="currentPage === 'UserManagement'"></UserManagement>
    </div>
  </div>
</template>

<script>
import HomePage from './components/HomePage.vue'
import ProjectManagement from './components/ProjectManagement.vue'
import DataProcessing from './components/DataProcessing.vue'
import DataStorage from './components/DataStorage.vue'
import UserManagement from './components/UserManagement.vue'

export default {
  name: 'App',
  components: {
    HomePage,
    ProjectManagement,
    DataProcessing,
    DataStorage,
    UserManagement
  },
  data() {
    return {
      currentPage: 'HomePage'
    }
  }
}
</script>

<style scoped>
#app {
  display: flex;
  height: 100vh;
  margin: 0;
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

.top-bar {
  position: fixed;
  top: 0;
  left: 0;
  width: 100%;
  height: 50px;
  background-color: #f0f9ff;
  color: #333;
  display: flex;
  align-items: center;
  padding: 0 15px;
  z-index: 1;
  box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
}

.top-bar h1 {
  font-size: 14px;
  margin: 0;
  flex: 1;
  text-align: left;
}

.sidebar {
  width: 220px;
  background-color: #fff;
  position: fixed;
  left: 0;
  top: 50px;
  bottom: 0;
  overflow-y: auto;
  box-shadow: 1px 0 2px rgba(0, 0, 0, 0.1);
}

.sidebar ul {
  list-style-type: none;
  padding: 0;
  margin: 0;
}

/* 一级菜单样式 */
.sidebar > ul > li {
  padding: 15px 20px;
  cursor: pointer;
  color: #333;
  transition: background-color 0.3s ease;
  position: relative;
  font-weight: bold;
  background-color: #f5f5f5;
  border-bottom: 1px solid #e0e0e0;
}

/* 二级菜单样式 */
.sidebar > ul > li > ul > li {
  padding: 10px 30px; /* 增加左内边距，使其有缩进效果 */
  cursor: pointer;
  color: #333;
  transition: background-color 0.3s ease;
  font-weight: normal;

}

/* 二级菜单悬停效果 */
.sidebar > ul > li > ul > li:hover {
  background-color: #e6f7ff;
}

/* 移除一级菜单下展开的子菜单默认高亮 */
.sidebar > ul > li > ul {
  background-color: transparent;
}

/* 隐藏展开收起图标 */
.sidebar li i {
  display: none;
}

.content {
  flex: 1;
  padding: 20px;
  margin-top: 50px;
  margin-left: 220px;
  background-color: #fafafa;
}

/* 引入 Font Awesome 图标库 */
@import url('https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.2/css/all.min.css');
</style>
