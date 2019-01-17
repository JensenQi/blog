const Mock = require('mockjs');
const Random = Mock.Random;
Mock.mock('/api/login', 'post', function (req) {
    if (req.body["user_name"] === "test" && req.body["password"] === "test") {
        return {
            success: true
        }
    } else {
        return {
            success: false
        }
    }
});
