<template>
    <div class="project-detail-container">
        <!-- 路径栏 -->
        <div class="path-bar">
            <router-link :to="{ path: `/project/${projectName}` }"> / {{ projectName }}</router-link>
        </div>
        <!-- 灰色细线 -->
        <div class="path-bar-divider"></div>
        
        <div v-if="projectFiles.length > 0" class="file-list-container">
            <!-- 表头 -->
            <div class="file-list-header">
                <div class="header-item narrow-item center-item">编号</div>
                <div class="header-item wide-item center-item">名称</div>
                <div class="header-item narrow-item center-item">状态</div>
                <div class="header-item narrow-item center-item">执行时间</div>
                <div class="header-item center-item"></div>
            </div>
            <!-- 文件列表 -->
            <div v-for="(file, index) in projectFiles" :key="file.id" class="file-list-row" :class="{ 'gray-row': index % 2 === 1 }">
                <div class="file-item narrow-item center-item">{{ index + 1 }}</div>
                <div class="file-item wide-item">{{ file.name }}</div>
                <div class="file-item narrow-item center-item">{{ file.status || '待处理' }}</div>
                <div class="file-item narrow-item center-item">{{ file.processed_at || '' }}</div>
                <div class="file-item center-item">
                    <div class="button-container">
                        <button @click="deleteFile(file.id)" class="action-button">删除</button>
                        <button @click="viewFileDetails(file.id, file.name)" class="action-button">查看详情</button>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'ProjectDetail',
    props: ['projectName'],
    data() {
        return {
            projectFiles: []
        };
    },
    mounted() {
        this.getProjectFiles();
    },
    methods: {
        getProjectFiles() {
            axios.get('http://127.0.0.1:8000/api/get_projects/')
                .then((response) => {
                    const projects = response.data.projects;
                    const project = projects.find(p => p.name === this.projectName);
                    if (project) {
                        this.projectFiles = project.files;  // 这里将项目的 file_list 信息保存到 projectFiles 中
                    }
                })
                .catch((error) => {
                    console.error('获取项目文件列表失败:', error);
                });
        },
        deleteFile(fileId) {
            // 这里可以添加删除文件的逻辑，例如发送请求到后端删除文件
            console.log(`删除文件: ${fileId}`);
        },
        viewFileDetails(fileId, filename) {
            const path = `/project/${this.projectName}/${filename}`;
            this.$router.push(path);
        }
    }
};
</script>

<style scoped>
.project-detail-container {
    padding: 0px;
}

.file-list-container {
    width: 100%;
}

.file-list-header {
    display: flex;
    font-weight: bold;
    padding: 10px 0;
    border-bottom: 1px solid #e0e0e0;
}

.file-list-row {
    display: flex;
    align-items: center;
    padding: 10px 0;
}

.header-item,
.file-item {
    flex: 1;
}

/* 窄列样式 */
.narrow-item {
    flex: 0 0 100px;
}

/* 宽列样式 */
.wide-item {
    flex: 2;
}

/* 居中显示 */
.center-item {
    text-align: center;
}

.gray-row {
    background-color: #f5f5f5;
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

/* 按钮容器居中 */
.button-container {
    display: flex;
    justify-content: center;
}

/* 路径栏样式 */
.path-bar {
  margin-bottom: 10px;
  font-size: 14px;
  color: #666;
}

.path-bar a {
  color: #007bff;
  text-decoration: none; /* 取消下划线 */
}

.path-bar a:hover {
  text-decoration: underline; /* 鼠标悬停时显示下划线 */
}

/* 路径栏分隔线 */
.path-bar-divider {
  border-bottom: 1px solid #ccc;
  margin-bottom: 10px;
  width: 100%;
}
</style>