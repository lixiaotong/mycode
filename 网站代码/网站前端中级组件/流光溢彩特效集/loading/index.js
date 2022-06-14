// 获取3个元素
let outer = document.querySelector('.outer')
let inner = document.querySelector('.inner')
let percent = document.querySelector('span')
let count = 0;
// 添加点击事件
inner.addEventListener('click', function() {
  // 添加调用的周期间隔(func, time)
  let loading = setInterval(animate, 200);
  function animate() {
    if(count == 100) {
      // 清除(停止)周期间隔
      clearInterval()
      // 删除、添加类
      outer.classList.remove('active-loader')
      outer.classList.add('active-loader-2')
    }else {
      count = count + 1;
      // 文字更改显示
      percent.textContent = count + '%'
      outer.classList.add('active-loader')
    }
  }
})
