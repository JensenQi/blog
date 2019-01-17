<style scoped>
    .layout {
        border: 1px solid #d7dde4;
        background: #f5f7f9;
        position: relative;
        border-radius: 4px;
        overflow: hidden;
    }

    .layout-nav {
        float: right;
    }

    .layout-footer-center {
        text-align: center;
    }

    .layout-logo {
        width: 100px;
        height: 30px;
        background: #5b6270;
        border-radius: 3px;
        float: left;
        position: relative;
        top: 15px;
    }

    a {
        color: white;
    }
</style>
<template>
    <div class="layout">
        <Layout>
            <Header :style="{position: 'fixed', width: '100%', zIndex: 1}">
                <Menu mode="horizontal" theme="dark" active-name="1">
                    <div class="layout-logo">
                        <div style="text-align: center;margin-top: -15%">
                            <router-link :to="{name: 'Home'}">
                                <strong>
                                    Home
                                </strong>
                            </router-link>
                        </div>

                    </div>

                    <div class="layout-nav">
                        <MenuItem name="2">
                            <Input v-model="search_key" placeholder="搜索..." style="width: 300px" :search="true" @on-search="search">
                                <Icon type="md-search" slot="suffix" @click="search"/>
                            </Input>
                        </MenuItem>
                        <Submenu name="3" v-if="is_login">
                            <template slot="title">
                                操作
                            </template>
                            <MenuItem name="3-1">
                                <span @click="$router.push({name: 'Edit'})">
                                    新建文章
                                </span>
                            </MenuItem>
                            <MenuItem name="3-2">
                                <span @click="logout">
                                退出登陆
                                </span>
                            </MenuItem>
                        </Submenu>


                        <MenuItem name="3" v-if="!is_login">
                            <Button @click="login_modal = true" type="text" ghost icon="md-lock">
                                登陆
                                <Modal v-model="login_modal" title="登陆" @on-ok="login">
                                    <Input prefix="md-person"
                                           placeholder="账号"
                                           type="text"
                                           style="width: 300px"
                                           v-model="user_name"></Input>
                                    <Input prefix="md-lock"
                                           placeholder="密码"
                                           type="password"
                                           style="width: 300px;margin-top: 10px"
                                           v-model="password"></Input>
                                </Modal>
                            </Button>
                        </MenuItem>

                    </div>
                </Menu>
            </Header>

            <div :style="{margin: '88px 20px 0', minHeight: '800px'}">
                <router-view/>
            </div>
            <Footer class="layout-footer-center">2015-2020 &copy; cuda.tech</Footer>
        </Layout>
    </div>
</template>
<script>
    export default {
        mounted() {
            this.is_login = this.$session.get('is_login');
        },
        data() {
            return {
                login_modal: false,
                user_name: null,
                password: null,
                is_login: false,
                search_key: null
            }

        },
        methods: {
            login() {
                this.$http.post('/api/user/login', {
                    user_name: this.user_name,
                    passwd: this.password
                }).then(response => {
                    if (response.body.status === 'success') {
                        this.$session.start();
                        this.$session.set('is_login', true);
                        this.is_login = true;
                        this.$router.go(0);
                    } else {
                        this.$Notice.error({
                            title: '登陆失败',
                            desc: response.body.error
                        })
                    }
                }, err => {
                });
            },

            logout() {
                this.$http.post('/api/user/logout', {}).then(response => {
                    if (response.body.status === 'success') {
                        this.$session.set('is_login', false);
                        this.is_login = false;
                        this.$router.go(0);
                    } else {
                        this.$Notice.error({
                            title: '退出登陆失败',
                            desc: response.body.error
                        })
                    }
                }, err => {
                });
            },


            search() {
                this.$router.push({
                    name: 'Home',
                    query: {
                        search: this.search_key
                    }
                });
                this.$router.go(0)
            }
        }
    }
</script>
