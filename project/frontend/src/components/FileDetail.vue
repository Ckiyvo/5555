<template>
    <div class="file-detail-container">
      <!-- 路径栏 -->
      <div class="path-bar">
        <router-link :to="{ path: `/project/${projectName}` }"> / {{ projectName }}</router-link>
        / {{ filename }}
    </div>
    <!-- 导航按钮 -->
    <div class="navigation-buttons">
      <button :disabled="isFirstFile" @click="prevFile" class="action-button">上一个</button>
      <button :disabled="isLastFile" @click="nextFile" class="action-button">下一个</button>
    </div>
    <!-- 灰色细线 -->
    <div class="path-bar-divider"></div>

      <h2>{{ filename }} 文件详情</h2>
      <p>这是 {{ filename }} 文件的详细信息页面。</p>
      <!-- 这里可以添加更多文件详情的内容 -->
    </div>
  </template>
  
<script>
import { useRoute } from 'vue-router';
  
export default {
  name: 'FileDetail',
  setup() {
    const route = useRoute();
    const projectName = route.params.projectname;
    const filename = route.params.filename;
  
  return {
      projectName,
      filename
    };
  }
};
</script>
  
<style scoped>
.file-detail-container {
    padding: 0px;
}

/* 路径栏及导航按钮容器样式 */
.path-bar-container {
    margin-bottom:10px;
    width: 100%; /* 确保容器宽度占满 */
}

/* 路径栏样式 */
.path-bar {
    font-size: 14px;
    color: #666;
    display: inline-block;
}

.path-bar a {
    color: #007bff;
    text-decoration: none; /* 取消下划线 */
}

.path-bar a:hover {
    text-decoration: underline; /* 鼠标悬停时显示下划线 */
}

/* 导航按钮样式 */
.navigation-buttons {
    float: right;
    
}

.action-button {
    padding: 5px 10px;
    margin-right: 5px;
    border: none;
    background-color: #007bff;
    color: white;
    border-radius: 3px;
    cursor: pointer;
}

.action-button:hover {
    background-color: #0056b3;
}

/* 清除浮动 */
.clearfix::after {
    content: "";
    display: table;
    clear: both;
}
/* 路径栏分隔线 */
.path-bar-divider {
    border-bottom: 1px solid #ccc;
    margin-bottom: 10px;
    margin-top: 20px;
    width: 100%;
}
</style>