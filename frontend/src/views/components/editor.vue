<style>

</style>

<template>
    <div>
        <Input v-model="title" clearable placeholder="输入标题" style="margin-bottom: 20px"/>
        <quill-editor v-model="content"
                      ref="quill_editor"
                      :options="editorOption"
                      @blur="onEditorBlur"
                      @focus="onEditorFocus"
                      @ready="onEditorReady">
            <div id="toolbar" slot="toolbar">
                <button class="ql-bold">Bold</button>
                <button class="ql-italic">Italic</button>
                <button class="ql-underline">Underline</button>
                <button class="ql-strike">Strike</button>

                <button class="ql-blockquote">Blockquote</button>
                <button class="ql-code-block">code-block</button>

                <button class="ql-header" value="1">h1</button>
                <button class="ql-header" value="2">h2</button>

                <button class="ql-script" value="sub">Sub</button>
                <button class="ql-script" value="super">Super</button>
                <button class="ql-formula">formula</button>

                <button class="ql-indent" value="-1">i1</button>
                <button class="ql-indent" value="+1">i2</button>


                <select class="ql-size">
                    <option value="small"></option>
                    <option selected></option>
                    <option value="large"></option>
                    <option value="huge"></option>
                </select>


                <select class="ql-header">
                    <option value="1"></option>
                    <option value="2"></option>
                    <option value="3"></option>
                    <option value="4"></option>
                    <option value="5"></option>
                    <option value="6"></option>
                    <option selected="selected"></option>
                </select>

                <select class="ql-color ql-picker ql-color-picker">
                    <option value="#FF0000"></option>
                    <option value="#FFA07A"></option>
                    <option value="#FA8072"></option>
                    <option value="#E9967A"></option>
                    <option value="#F08080"></option>
                    <option value="#CD5C5C"></option>
                    <option value="#DC143C"></option>
                    <option value="#B22222"></option>
                    <option value="#8B0000"></option>
                    <option value="#FFC0CB"></option>
                    <option value="#FFB6C1"></option>
                    <option value="#FF69B4"></option>
                    <option value="#FF1493"></option>
                    <option value="#DB7093"></option>
                    <option value="#C71585"></option>
                    <option value="#FFA500"></option>
                    <option value="#FF8C00"></option>
                    <option value="#FF7F50"></option>
                    <option value="#FF6347"></option>
                    <option value="#FF4500"></option>
                    <option value="#FFFF00"></option>
                    <option value="#FFFFE0"></option>
                    <option value="#FFFACD"></option>
                    <option value="#FAFAD2"></option>
                    <option value="#FFEFD5"></option>
                    <option value="#FFE4B5"></option>
                    <option value="#FFDAB9"></option>
                    <option value="#EEE8AA"></option>
                    <option value="#F0E68C"></option>
                    <option value="#BDB76B"></option>
                    <option value="#FFD700"></option>
                    <option value="#800080"></option>
                    <option value="#E6E6FA"></option>
                    <option value="#D8BFD8"></option>
                    <option value="#DDA0DD"></option>
                    <option value="#EE82EE"></option>
                    <option value="#DA70D6"></option>
                    <option value="#FF00FF"></option>
                    <option value="#FF00FF"></option>
                    <option value="#BA55D3"></option>
                    <option value="#9370DB"></option>
                    <option value="#9966CC"></option>
                    <option value="#8A2BE2"></option>
                    <option value="#9400D3"></option>
                    <option value="#9932CC"></option>
                    <option value="#8B008B"></option>
                    <option value="#7B68EE"></option>
                    <option value="#6A5ACD"></option>
                    <option value="#483D8B"></option>
                    <option value="#4B0082"></option>
                    <option value="#008000"></option>
                    <option value="#98FB98"></option>
                    <option value="#90EE90"></option>
                    <option value="#9ACD32"></option>
                    <option value="#ADFF2F"></option>
                    <option value="#7FFF00"></option>
                    <option value="#7CFC00"></option>
                    <option value="#00FF00"></option>
                    <option value="#32CD32"></option>
                    <option value="#00FA9A"></option>
                    <option value="#00FF7F"></option>
                    <option value="#66CDAA"></option>
                    <option value="#7FFFD4"></option>
                    <option value="#20B2AA"></option>
                    <option value="#3CB371"></option>
                    <option value="#2E8B57"></option>
                    <option value="#8FBC8F"></option>
                    <option value="#228B22"></option>
                    <option value="#006400"></option>
                    <option value="#6B8E23"></option>
                    <option value="#808000"></option>
                    <option value="#556B2F"></option>
                    <option value="#008080"></option>
                    <option value="#0000FF"></option>
                    <option value="#ADD8E6"></option>
                    <option value="#B0E0E6"></option>
                    <option value="#AFEEEE"></option>
                    <option value="#48D1CC"></option>
                    <option value="#40E0D0"></option>
                    <option value="#00CED1"></option>
                    <option value="#E0FFFF"></option>
                    <option value="#00FFFF"></option>
                    <option value="#00FFFF"></option>
                    <option value="#008B8B"></option>
                    <option value="#5F9EA0"></option>
                    <option value="#B0C4DE"></option>
                    <option value="#4682B4"></option>
                    <option value="#87CEFA"></option>
                    <option value="#87CEEB"></option>
                    <option value="#00BFFF"></option>
                    <option value="#1E90FF"></option>
                    <option value="#6495ED"></option>
                    <option value="#4169E1"></option>
                    <option value="#0000CD"></option>
                    <option value="#00008B"></option>
                    <option value="#000080"></option>
                    <option value="#191970"></option>
                    <option value="#A52A2A"></option>
                    <option value="#FFF8DC"></option>
                    <option value="#FFEBCD"></option>
                    <option value="#FFE4C4"></option>
                    <option value="#FFDEAD"></option>
                    <option value="#F5DEB3"></option>
                    <option value="#DEB887"></option>
                    <option value="#D2B48C"></option>
                    <option value="#BC8F8F"></option>
                    <option value="#F4A460"></option>
                    <option value="#DAA520"></option>
                    <option value="#B8860B"></option>
                    <option value="#CD853F"></option>
                    <option value="#D2691E"></option>
                    <option value="#8B4513"></option>
                    <option value="#A0522D"></option>
                    <option value="#800000"></option>
                    <option value="#FFFFFF"></option>
                    <option value="#FFFAFA"></option>
                    <option value="#F0FFF0"></option>
                    <option value="#F5FFFA"></option>
                    <option value="#F0FFFF"></option>
                    <option value="#F0F8FF"></option>
                    <option value="#F8F8FF"></option>
                    <option value="#F5F5F5"></option>
                    <option value="#FFF5EE"></option>
                    <option value="#F5F5DC"></option>
                    <option value="#FDF5E6"></option>
                    <option value="#FFFAF0"></option>
                    <option value="#FFFFF0"></option>
                    <option value="#FAEBD7"></option>
                    <option value="#FAF0E6"></option>
                    <option value="#FFF0F5"></option>
                    <option value="#FFE4E1"></option>
                    <option value="#808080"></option>
                    <option value="#DCDCDC"></option>
                    <option value="#D3D3D3"></option>
                    <option value="#C0C0C0"></option>
                    <option value="#A9A9A9"></option>
                    <option value="#696969"></option>
                    <option value="#778899"></option>
                    <option value="#708090"></option>
                    <option value="#2F4F4F"></option>
                    <option value="#000000"></option>
                </select>

                <select class="ql-background ql-picker ql-color-picker">
                    <option value="#FF0000"></option>
                    <option value="#FFA07A"></option>
                    <option value="#FA8072"></option>
                    <option value="#E9967A"></option>
                    <option value="#F08080"></option>
                    <option value="#CD5C5C"></option>
                    <option value="#DC143C"></option>
                    <option value="#B22222"></option>
                    <option value="#8B0000"></option>
                    <option value="#FFC0CB"></option>
                    <option value="#FFB6C1"></option>
                    <option value="#FF69B4"></option>
                    <option value="#FF1493"></option>
                    <option value="#DB7093"></option>
                    <option value="#C71585"></option>
                    <option value="#FFA500"></option>
                    <option value="#FF8C00"></option>
                    <option value="#FF7F50"></option>
                    <option value="#FF6347"></option>
                    <option value="#FF4500"></option>
                    <option value="#FFFF00"></option>
                    <option value="#FFFFE0"></option>
                    <option value="#FFFACD"></option>
                    <option value="#FAFAD2"></option>
                    <option value="#FFEFD5"></option>
                    <option value="#FFE4B5"></option>
                    <option value="#FFDAB9"></option>
                    <option value="#EEE8AA"></option>
                    <option value="#F0E68C"></option>
                    <option value="#BDB76B"></option>
                    <option value="#FFD700"></option>
                    <option value="#800080"></option>
                    <option value="#E6E6FA"></option>
                    <option value="#D8BFD8"></option>
                    <option value="#DDA0DD"></option>
                    <option value="#EE82EE"></option>
                    <option value="#DA70D6"></option>
                    <option value="#FF00FF"></option>
                    <option value="#FF00FF"></option>
                    <option value="#BA55D3"></option>
                    <option value="#9370DB"></option>
                    <option value="#9966CC"></option>
                    <option value="#8A2BE2"></option>
                    <option value="#9400D3"></option>
                    <option value="#9932CC"></option>
                    <option value="#8B008B"></option>
                    <option value="#7B68EE"></option>
                    <option value="#6A5ACD"></option>
                    <option value="#483D8B"></option>
                    <option value="#4B0082"></option>
                    <option value="#008000"></option>
                    <option value="#98FB98"></option>
                    <option value="#90EE90"></option>
                    <option value="#9ACD32"></option>
                    <option value="#ADFF2F"></option>
                    <option value="#7FFF00"></option>
                    <option value="#7CFC00"></option>
                    <option value="#00FF00"></option>
                    <option value="#32CD32"></option>
                    <option value="#00FA9A"></option>
                    <option value="#00FF7F"></option>
                    <option value="#66CDAA"></option>
                    <option value="#7FFFD4"></option>
                    <option value="#20B2AA"></option>
                    <option value="#3CB371"></option>
                    <option value="#2E8B57"></option>
                    <option value="#8FBC8F"></option>
                    <option value="#228B22"></option>
                    <option value="#006400"></option>
                    <option value="#6B8E23"></option>
                    <option value="#808000"></option>
                    <option value="#556B2F"></option>
                    <option value="#008080"></option>
                    <option value="#0000FF"></option>
                    <option value="#ADD8E6"></option>
                    <option value="#B0E0E6"></option>
                    <option value="#AFEEEE"></option>
                    <option value="#48D1CC"></option>
                    <option value="#40E0D0"></option>
                    <option value="#00CED1"></option>
                    <option value="#E0FFFF"></option>
                    <option value="#00FFFF"></option>
                    <option value="#00FFFF"></option>
                    <option value="#008B8B"></option>
                    <option value="#5F9EA0"></option>
                    <option value="#B0C4DE"></option>
                    <option value="#4682B4"></option>
                    <option value="#87CEFA"></option>
                    <option value="#87CEEB"></option>
                    <option value="#00BFFF"></option>
                    <option value="#1E90FF"></option>
                    <option value="#6495ED"></option>
                    <option value="#4169E1"></option>
                    <option value="#0000CD"></option>
                    <option value="#00008B"></option>
                    <option value="#000080"></option>
                    <option value="#191970"></option>
                    <option value="#A52A2A"></option>
                    <option value="#FFF8DC"></option>
                    <option value="#FFEBCD"></option>
                    <option value="#FFE4C4"></option>
                    <option value="#FFDEAD"></option>
                    <option value="#F5DEB3"></option>
                    <option value="#DEB887"></option>
                    <option value="#D2B48C"></option>
                    <option value="#BC8F8F"></option>
                    <option value="#F4A460"></option>
                    <option value="#DAA520"></option>
                    <option value="#B8860B"></option>
                    <option value="#CD853F"></option>
                    <option value="#D2691E"></option>
                    <option value="#8B4513"></option>
                    <option value="#A0522D"></option>
                    <option value="#800000"></option>
                    <option value="#FFFFFF"></option>
                    <option value="#FFFAFA"></option>
                    <option value="#F0FFF0"></option>
                    <option value="#F5FFFA"></option>
                    <option value="#F0FFFF"></option>
                    <option value="#F0F8FF"></option>
                    <option value="#F8F8FF"></option>
                    <option value="#F5F5F5"></option>
                    <option value="#FFF5EE"></option>
                    <option value="#F5F5DC"></option>
                    <option value="#FDF5E6"></option>
                    <option value="#FFFAF0"></option>
                    <option value="#FFFFF0"></option>
                    <option value="#FAEBD7"></option>
                    <option value="#FAF0E6"></option>
                    <option value="#FFF0F5"></option>
                    <option value="#FFE4E1"></option>
                    <option value="#808080"></option>
                    <option value="#DCDCDC"></option>
                    <option value="#D3D3D3"></option>
                    <option value="#C0C0C0"></option>
                    <option value="#A9A9A9"></option>
                    <option value="#696969"></option>
                    <option value="#778899"></option>
                    <option value="#708090"></option>
                    <option value="#2F4F4F"></option>
                    <option value="#000000"></option>
                </select>

                <select class="ql-align ql-picker ql-icon-picker">
                    <option selected="selected"></option>
                    <option value="center"></option>
                    <option value="right"></option>
                    <option value="justify"></option>
                </select>

                <button class="ql-clean">clean</button>
                <button class="ql-list" value="ordered">order-list</button>
                <button class="ql-list" value="bullet">order-list</button>

                <button class="ql-link">link</button>
                <button class="ql-image">image</button>

                <Button type="text" size="large" icon="md-paper-plane" @click="submit_modal = true"></Button>
            </div>
        </quill-editor>

        <Modal v-model="submit_modal"
               title="确认提交？"
               @on-ok="submit"
               @on-cancel="submit_modal = false">
        </Modal>

        <div v-html="result"></div>
    </div>
</template>

<script>
    import hljs from 'highlight.js';


    import Quill from 'quill';
    import {quillEditor} from 'vue-quill-editor';
    import ImageResize from 'quill-image-resize-module'

    Quill.register('modules/imageResize', ImageResize);


    export default {
        components: {
            quillEditor
        },
        computed: {},

        data() {
            return {
                title: null,
                content: null,
                editorOption: {
                    placeholder: "懵逼树上懵逼果，懵逼树下你和我",
                    modules: {
                        toolbar: '#toolbar',
                        syntax: {
                            highlight: text => hljs.highlightAuto(text).value,
                        },
                        formula: true,
                        history: {
                            delay: 1000,
                            maxStack: 50,
                            userOnly: false
                        },
                        imageResize: {
                            displayStyles: {
                                backgroundColor: 'black',
                                border: 'none',
                                color: 'white'
                            },
                            modules: ['Resize', 'DisplaySize', 'Toolbar']
                        }
                    },
                },
                source_code_modal: false,
                preview_modal: false,
                submit_modal: false,
                raw_html: null,
                result: null

            }
        },


        methods: {
            onEditorBlur(editor) {
                // alert(editor.root.innerHTML)
                // console.log('editor blur!', editor)
            },
            onEditorFocus(editor) {
                // console.log('editor focus!', editor)
            },
            onEditorReady(editor) {
                // console.log('editor ready!', editor)
            },

            submit() {
                this.result = this.content.replace(/class="ql-syntax"/g, 'class="hljs"');
                let article_id = this.$route.query.id;
                let trim_result = this.$trim_html(this.result, {limit: 500});
                let abstract = trim_result.html;
                let more = trim_result.more;

                if (article_id === undefined) {
                    this.$http.post('/api/article/create', {
                        title: this.title,
                        abstract: abstract,
                        content: this.result,
                        more: more
                    }).then(response => {
                        if (response.body.status === 'success') {
                            this.$Notice.success({
                                title: '创建文章成功'
                            })
                        } else {
                            this.$Notice.error({
                                title: '创建文章失败',
                                desc: response.body.error
                            })
                        }
                    }, err => {
                    });
                } else {
                    this.$http.post('/api/article/update', {
                        id: article_id,
                        title: this.title,
                        abstract: abstract,
                        content: this.result,
                        more: more
                    }).then(response => {
                        if (response.body.status === 'success') {
                            this.$Notice.success({
                                title: '更新文章成功'
                            });
                        } else {
                            this.$Notice.error({
                                title: '更新文章失败',
                                desc: response.body.error
                            })
                        }
                    }, err => {
                    });
                }
            },


        }
    }
</script>


