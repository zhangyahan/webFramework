事件委托
    给父元素绑定事件
    $('要绑定标签的上级标签').on('事件', '要绑定的标签', function () {
        要执行的事情
    })



$.ajax({
    url: '/students/change/',
    data: {'k': [1, 2, 3, 4]},
    traditional: true,  # 加上以后可以传递数组,
    type: 'post',
    success: function (args) {
        var args = JSON.parse(args)
        if (args.status==200) {
            window.location.reload()
        } else {
            alert('修改错误')
        }
    }
})
发数据时:
    data中的v
        只是字符串和数字正常发
        如果包含数组加traditional: true,不能传字典
    