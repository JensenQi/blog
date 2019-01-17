const routers = [
    {
        path: '/',
        name: 'Index',
        redirect: {
            name: 'Home'
        },
        component: (resolve) => require(['./views/index.vue'], resolve),
        children: [
            {
                path: '/home',
                name: 'Home',
                component: (resolve) => require(['./views/home.vue'], resolve)
            },
            {
                path: '/edit',
                name: 'Edit',
                component: (resolve) => require(['./views/edit.vue'], resolve)
            },
            {
                path: '/article',
                name: 'Article',
                component: (resolve) => require(['./views/article.vue'], resolve)
            },
        ]
    }
];
export default routers;