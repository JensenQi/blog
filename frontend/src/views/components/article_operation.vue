<style scoped>

</style>

<template>
    <Dropdown trigger="click" @on-click="process">
        <Icon type="ios-arrow-down"></Icon>
        <DropdownMenu slot="list">
            <DropdownItem name="edit">编辑</DropdownItem>
            <DropdownItem name="release">发布</DropdownItem>
            <DropdownItem :disabled="true" name="push">推送</DropdownItem>
            <DropdownItem name="remove">删除</DropdownItem>
        </DropdownMenu>
    </Dropdown>
</template>

<script>
    export default {
        name: "id",
        props: ['id'],
        data() {
            return {}
        },
        methods: {
            process(op) {
                if (op === 'edit') {
                    this.$router.push({
                        name: 'Edit',
                        query: {
                            id: this.id
                        }
                    })
                } else if (op === 'remove') {
                    this.$Modal.error({title: '确认删除？', onOk: this.remove});
                } else if (op === 'release') {
                    this.$Modal.confirm({title: '确认发布？', onOk: this.release});
                } else if (op === 'push') {
                    this.$Modal.confirm({title: '确认推送？', onOk: this.push});
                }
            },

            remove() {
                this.$http.post('/api/article/remove', {
                    id: this.id,
                }).then(response => {
                    if (response.body.status === 'success') {
                        this.$emit('remove');
                    } else {
                        this.$Notice.error({
                            title: '删除文章失败',
                            desc: response.body.error
                        })
                    }
                }, err => {
                });
            },
            release() {
                this.$http.post('/api/article/release', {
                    id: this.id,
                }).then(response => {
                    if (response.body.status === 'success') {
                        this.$emit('release');
                    } else {
                        this.$Notice.error({
                            title: '发布文章失败',
                            desc: response.body.error
                        })
                    }
                }, err => {
                });
            },
            push() {
                alert('推送')
            }
        }
    }
</script>

