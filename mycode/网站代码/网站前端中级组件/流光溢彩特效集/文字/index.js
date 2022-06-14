    // 要显示的字符串
    const s = 'Stunning'
    // 获取父元素id
    const main = document.getElementById('main')
    // 裁剪父元素到数组
    const array = s.split('')
    // 计时器
    const ospanAnimationDelay = 0
    // 循环数组
    for (let i in array) {
        // 新建元素span
        const ospan = document.createElement('span');
        // 设置新建元素内容
        ospan.innerText = array[i];
        // 添加动画等待时间以形成循环闪烁效果
        ospan.style.animationDelay = ospanAnimationDelay + 0.25 * i + 's'
        // 添加子元素
        main.appendChild(ospan)
    }
