<style scoped>
    .article {
        margin-top: 30px;
    }

</style>
<template>
    <div>
        <Col span="6">&nbsp;</Col>
        <Col span="12">
            <Card v-for="(article, idx) in articles" class="article">
                <h2 slot="title">
                    <Tag v-if="!article.release">草稿</Tag>
                    {{ article.title }}
                </h2>
                <div slot="extra">
                    {{ article.create_time }}
                    <ArticleOperation
                            v-if="$session.get('is_login')" :id="article.id"
                            @remove="articles.splice(idx, 1)"
                            @release="articles[idx].release = true"
                    />
                </div>
                <div v-html="article.content"/>
                <div v-if="article.more" style="text-align: right">
                    <router-link :to="{name: 'Article', query:{id: article.id}}">查看更多</router-link>
                </div>
            </Card>
            <Page :total="this.count" show-elevator show-total :page-size="this.page_size"
                  @on-change="this.change_page"
                  style="float:right; margin-top: 30px"/>

        </Col>
        <Col span="6">
            <AboutMe/>
        </Col>
        <BackTop></BackTop>


    </div>

</template>
<script>
    import ArticleOperation from './components/article_operation';
    import AboutMe from './components/about_me';

    export default {
        components: {
            ArticleOperation,
            AboutMe
        },
        mounted() {
            this.search_key = this.$route.query.search;
            this.change_page(1);
        },
        data() {
            return {
                articles: [],
                page_size: 10,
                search_key: null,
                count: 0
            }
        },
        methods: {
            change_page(page) {
                let search_key = this.search_key !== null && this.search_key !== undefined ? this.search_key : '';
                this.$http.post('/api/article/listing', {
                    page: page,
                    page_size: this.page_size,
                    key: search_key
                }).then(response => {
                    if (response.body.status === 'success') {
                        this.articles = response.body.data.articles;
                        this.count = response.body.data.count
                    } else {
                        this.$Notice.error({
                            title: '登陆失败',
                            desc: response.body.error
                        })
                    }
                }, err => {
                });
            }
        },

    }
</script>