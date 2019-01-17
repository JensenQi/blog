<style scoped>

</style>

<template>
    <div>
        <Col span="4">&nbsp;</Col>
        <Col span="16">
            <Card>
                <div style="text-align: center; font-size: 2em">
                    <strong>{{ this.article.title }}</strong>
                </div>
                <Divider>Jensen</Divider>
                <div slot="extra">
                    <ArticleOperation v-if="$session.get('is_login')" :id="$route.query.id"/>
                </div>

                <div style="padding: 30px" v-html="this.article.content"/>
                <div style="float:right; margin-top: -30px;margin-right: 30px">
                    <Icon type="md-time" />{{ this.article.create_time }}
                </div>
            </Card>
        </Col>
    </div>
</template>

<script>
    import ArticleOperation from './components/article_operation';
    export default {
        components:{
            ArticleOperation
        },
        created() {
            this.$http.post('/api/article/get', {
                id: this.$route.query.id
            }).then(response => {
                if (response.body.status === 'success') {
                    this.article = response.body.data;
                } else {
                    this.$Notice.error({
                        title: '获取文章失败',
                        desc: response.body.error
                    })
                }
            }, err => {
            });
        },
        data(){
            return{
                article: null
            }
        }

    }
</script>

