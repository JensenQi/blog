<style scoped>

</style>

<template>
    <div>
        <Col span="4">&nbsp;</Col>
        <Col span="16">
            <Editor ref="editor"/>
        </Col>
    </div>

</template>

<script>
    import Editor from './components/editor';

    export default {
        name: "edit",
        components: {
            Editor
        },
        created() {
            if (this.$route.query.id !== undefined) {
                this.$http.post('/api/article/get', {
                    id: this.$route.query.id
                }).then(response => {
                    if (response.body.status === 'success') {
                        let article = response.body.data;
                        this.$refs['editor'].content = article.content;
                        this.$refs['editor'].title = article.title;
                    } else {
                        this.$Notice.error({
                            title: '获取文章失败',
                            desc: response.body.error
                        })
                    }
                }, err => {
                });
            }
        },
        data() {
            return {}
        }
    }
</script>

