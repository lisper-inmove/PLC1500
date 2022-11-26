# format-v1.json

    详情页展示模拟数据:

    format: v1
    column_number: 每一行展示的数据的列数
    device_iamge_url: 设备图片
    name: 设备名称
    title: 页面名称
    values: 所有数据。行数由values.length / column_number决定
        value: 值
        name: 名称

# format-v2.json

    主页展示模拟数据:

    format: v2
    background_image_url: 页面背景图
    title: 主页名称
    column_number: 同format-v1
    values: 同format-v1
        status: 状态
        status_color: 状态图标颜色
        name: 设备名称
        image_url: 设备展示图
        detail_page_url: 详情页地址
