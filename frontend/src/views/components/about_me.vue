<template>
    <Card style="margin: 0 30px 0 50px">
        <h3 slot="title">About Me</h3>
        <div>
            数据挖掘从业者
        </div>

        <Timeline style="margin-top: 10px;margin-bottom: 0px">
            <TimelineItem>
                <h3 class="time">2017至今</h3>
                <p class="content">阿里巴巴，数据挖掘</p>
            </TimelineItem>
            <TimelineItem>
                <h3 class="time">2015 ~ 2017</h3>
                <p class="content">去哪儿网，数据挖掘</p>
            </TimelineItem>
            <TimelineItem>
                <h3 class="time">2011 ~ 2015</h3>
                <p class="content">哈尔滨工业大学，航天学院</p>
            </TimelineItem>
        </Timeline>
        <div>
            <Icon type="md-mail"/>
            hit-suit@live.hk
        </div>
        <div>
            <Icon type="logo-github"/>
            JensenChik
        </div>
        <div>
            <Icon type="md-pin"/>
            北京
        </div>
        <div>
            <Icon type="md-construct"/>
            <Tag>Hadoop</Tag>
            <Tag>Hive</Tag>
            <Tag>Vue</Tag>
            <Tag>Tensorflow</Tag>
            <Tag>Python</Tag>
            <Tag>Java</Tag>
        </div>

        <div style="text-align: center">
            <!--<img src="https://timgsa.baidu.com/timg?image&amp;quality=80&amp;size=b9999_10000&amp;sec=1544717251942&amp;di=433c78a581f3e6e883123f11c76e6034&amp;imgtype=0&amp;src=http%3A%2F%2Fwww.ccfao.gov.cn%2Fzwgk%2Fxxgkml%2Fdtxx%2F201808%2FW020180801562481131566.jpg"-->
                 <!--style="" width="150">-->
        </div>
    </Card>
</template>

<script>
    export default {
        name: "about_me"
    }
</script>

<style scoped>

</style>